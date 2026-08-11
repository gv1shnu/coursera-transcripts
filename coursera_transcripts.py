from __future__ import annotations

"""
Fetch all video-lecture transcripts from a Coursera course, navigating the
course one item at a time, and write them as organized Markdown for personal
notes.

Same operating model as review_coding.py / review_mcqs.py in this folder:
  * Playwright drives a DEDICATED Brave profile (separate user_data_dir) so it
    never touches your main browser. You log in to Coursera ONCE in the window
    that opens; the session persists across runs.
  * Resume/bookkeeping files, file+stdout logging, error screenshots, tqdm.

Two phases:
  1. DISCOVER  - walk the course outline and build an ordered list of every
                 lecture (video) item, grouped by week/module. Cached to
                 coursera_outline.json so re-runs don't re-crawl.
  2. EXTRACT   - open each lecture, reveal its Transcript, and write
                 transcripts/<course-slug>/<NN_module>/<NN_lecture>.md

Typical use:
    python3 coursera_transcripts.py --course-url "https://www.coursera.org/learn/<slug>/home/week/1"
    python3 coursera_transcripts.py --course-url "<url>" --discover-only   # just build the outline to eyeball it
    python3 coursera_transcripts.py --course-url "<url>" --restart          # ignore resume cursor

Selectors are best-known Coursera structures with text/JS fallbacks; the first
real run is used to confirm/tune them against the live site (the same way the
admin-panel scripts in this folder were confirmed).
"""

import argparse
import json
import logging
import re
import sys
import tempfile
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from urllib.parse import urlparse

from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright
from tqdm import tqdm


# --- browser / profile (dedicated, mirrors the other scripts here) ---
BRAVE_PATH = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
AUTOMATION_USER_DATA_DIR = Path(tempfile.gettempdir()) / "brave-coursera-transcripts"

HEADLESS = False
DEFAULT_TIMEOUT_MS = 30_000
NAVIGATION_TIMEOUT_MS = 60_000
MANUAL_LOGIN_TIMEOUT_SECONDS = 600
MAX_RETRIES = 3
MIN_DELAY_BETWEEN_ITEMS_SECONDS = 2.0
PAGE_SETTLE_SECONDS = 1.5
TRANSCRIPT_WAIT_MS = 12_000

# --- output / bookkeeping files ---
OUTLINE_FILE = Path("coursera_outline.json")
LAST_COMPLETED_FILE = Path("coursera_last_completed.txt")
LAST_PROCESSED_FILE = Path("coursera_last_processed.txt")
FAILED_FILE = Path("coursera_failed_items.txt")
MANUAL_FILE = Path("coursera_manual_items.txt")
LOG_FILE = Path("coursera_transcripts.log")
SCREENSHOT_DIR = Path("coursera_screenshots")
OUTPUT_ROOT = Path("transcripts")

# --- candidate selectors (confirmed/tuned on first live run) ---
# A "lecture" item links to /learn/<slug>/lecture/<id>/<item-slug>.
LECTURE_HREF_RE = re.compile(r"/learn/[^/]+/lecture/[^/?#]+")
# Course-outline item rows in the left rail / week pages.
OUTLINE_LINK_SELECTOR = "a[href*='/lecture/']"
# Buttons that expand collapsed week/module sections on the outline.
EXPAND_BUTTON_SELECTORS = [
    "button[aria-expanded='false'][data-track-component*='week']",
    "button[aria-expanded='false']",
]
# The "Transcript" tab/toggle on a lecture page.
TRANSCRIPT_TAB_SELECTORS = [
    "button:has-text('Transcript')",
    "div[role='tab']:has-text('Transcript')",
    "a:has-text('Transcript')",
]
# Where transcript text lives once revealed.
TRANSCRIPT_CONTAINER_SELECTORS = [
    "div.rc-Transcript",
    "[data-testid='transcript']",
    "[data-track-component='transcript_text']",
    "div.rc-Phrases",
]
# Individual cue/phrase nodes inside the container (for timestamped mode).
TRANSCRIPT_PHRASE_SELECTORS = [
    "div.phrase",
    "span.phrase",
    "[data-testid='cue']",
    "div.rc-Phrase",
]

LOGGER = logging.getLogger("coursera")


# ----------------------------- data model -------------------------------

@dataclass
class Lecture:
    order: int            # global 1-based order across the whole course
    module_index: int     # 1-based week/module number
    module_title: str
    title: str
    url: str
    item_slug: str

    def safe_module_dir(self) -> str:
        return f"{self.module_index:02d}_{slugify(self.module_title)}"

    def safe_filename(self) -> str:
        return f"{self.order:03d}_{slugify(self.title or self.item_slug)}.md"


# ------------------------------- helpers ---------------------------------

def configure_logging() -> None:
    SCREENSHOT_DIR.mkdir(exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )


def slugify(text: str) -> str:
    text = (text or "").strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text).strip("-")
    return text[:80] or "untitled"


_ITEM_TYPE_RE = re.compile(
    r"\s+(Video|Reading|Quiz|Lab|Discussion(?:\s+Prompt)?|Practice\s+Assignment|"
    r"Graded\s+\w+|Ungraded\s+\w+|Programming\s+Assignment|Peer-graded\s+\w+)$",
    re.IGNORECASE,
)
_MODULE_STATUS_RE = re.compile(
    r"\s*(Complete|\d+\s+(?:graded\s+)?(?:assessments?|assignments?|items?)\s+left)\s*$",
    re.IGNORECASE,
)


def clean_lecture_title(raw: str) -> str:
    """Sidebar anchor text looks like
    'Probability Video• . Duration: 9 minutes 9 min  Resume . Click to resume'.
    Keep just the lecture name."""
    text = re.sub(r"\s+", " ", raw or "").strip()
    text = text.split("•")[0].strip()              # drop type bullet + duration tail
    text = re.sub(r"\s*Resume\b.*$", "", text, flags=re.IGNORECASE).strip()
    text = re.sub(r"\s*Duration:.*$", "", text, flags=re.IGNORECASE).strip()
    text = _ITEM_TYPE_RE.sub("", text).strip()     # drop trailing 'Video'/'Reading'/...
    return text


def clean_module_title(raw: str, module_index: int) -> str:
    text = re.sub(r"\s+", " ", raw or "").strip()
    text = _MODULE_STATUS_RE.sub("", text).strip()
    return text or f"Module {module_index}"


def course_slug_from_url(url: str) -> str:
    m = re.search(r"/learn/([^/?#]+)", url)
    if not m:
        raise ValueError(f"Could not find a /learn/<slug> in: {url}")
    return m.group(1)


def polite_sleep(seconds: float, reason: str) -> None:
    if seconds > 0:
        LOGGER.debug("Sleeping %.1fs (%s)", seconds, reason)
        time.sleep(seconds)


def wait_ready(page) -> None:
    try:
        page.wait_for_load_state("domcontentloaded", timeout=NAVIGATION_TIMEOUT_MS)
    except PlaywrightTimeoutError:
        LOGGER.debug("domcontentloaded wait timed out; continuing.")


def save_screenshot(page, filename: str) -> Path:
    SCREENSHOT_DIR.mkdir(exist_ok=True)
    path = SCREENSHOT_DIR / filename
    page.screenshot(path=str(path), full_page=True)
    return path


def safe_save_screenshot(page, filename: str) -> None:
    try:
        save_screenshot(page, filename)
    except Exception:
        LOGGER.debug("Could not save screenshot %s", filename, exc_info=True)


def find_first_optional(page, selectors, timeout_ms: int = 3_000):
    for selector in selectors:
        locator = page.locator(selector).first
        try:
            locator.wait_for(state="visible", timeout=timeout_ms)
            return locator
        except PlaywrightTimeoutError:
            continue
    return None


# --------------------------- login handling ------------------------------

def is_logged_in(page) -> bool:
    """Heuristic: the lecture/outline page renders course content only when
    authenticated; the login wall lives on /authentication or shows a login form."""
    url = (page.url or "").lower()
    if "authentication" in url or "/login" in url or "accounts.google.com" in url:
        return False
    # The video/transcript region or the course rail only exists when logged in.
    if page.locator(OUTLINE_LINK_SELECTOR).count() > 0:
        return True
    if find_first_optional(page, TRANSCRIPT_TAB_SELECTORS, timeout_ms=1_500) is not None:
        return True
    # Negative signals: an on-page login/create-account wall. Coursera's wall is
    # email-first, so there may be no password field yet — also look for the
    # email field, the social-login buttons, and the heading text.
    login_wall_selectors = [
        "input[type='password']",
        "input[type='email']",
        "input[name='email']",
        "button:has-text('Continue with Google')",
        "text=Log in or create account",
    ]
    for sel in login_wall_selectors:
        try:
            if page.locator(sel).count() > 0:
                return False
        except Exception:
            continue
    # Fall back to absence of an obvious login form.
    return page.locator("input[type='password']").count() == 0


def pause_for_login_if_needed(page, target_url: str) -> None:
    if is_logged_in(page):
        return
    LOGGER.warning("Coursera session not detected. Manual login is needed.")
    print(
        "\nLog in to Coursera in the Brave window that just opened."
        "\nThis script continues automatically once your course content is visible."
        f"\nIf the browser is not on the course page after login, paste this URL there:\n{target_url}\n"
    )
    deadline = time.monotonic() + MANUAL_LOGIN_TIMEOUT_SECONDS
    last_logged = None
    while time.monotonic() < deadline:
        try:
            page.bring_to_front()
            if is_logged_in(page):
                LOGGER.info("Authenticated Coursera session detected.")
                polite_sleep(PAGE_SETTLE_SECONDS, "post-login settle")
                return
            if page.url != last_logged:
                LOGGER.info("Waiting for login. Current page: %s", page.url)
                last_logged = page.url
        except Exception:
            LOGGER.debug("Login polling check failed.", exc_info=True)
        time.sleep(3)
    safe_save_screenshot(page, "login_check_failed.png")
    raise RuntimeError("Timed out waiting for Coursera login.")


# --------------------------- phase 1: discover ---------------------------

def expand_all_sections(page) -> None:
    """Best-effort: click expanders so every week's lecture links are in the DOM."""
    for selector in EXPAND_BUTTON_SELECTORS:
        try:
            buttons = page.locator(selector)
            count = buttons.count()
        except PlaywrightError:
            continue
        for i in range(count):
            try:
                btn = buttons.nth(i)
                if btn.is_visible():
                    btn.click(timeout=2_000)
                    page.wait_for_timeout(150)
            except Exception:
                continue


def harvest_lectures_on_page(page):
    """Return ordered, de-duplicated [(url, title)] for lecture links on the page."""
    js = """
    () => {
      const seen = new Set();
      const out = [];
      for (const a of document.querySelectorAll("a[href*='/lecture/']")) {
        const href = a.href.split('?')[0].split('#')[0];
        if (!/\\/learn\\/[^/]+\\/lecture\\//.test(href)) continue;
        if (seen.has(href)) continue;
        seen.add(href);
        const title = (a.innerText || a.textContent || '').trim().replace(/\\s+/g,' ');
        out.push([href, title]);
      }
      return out;
    }
    """
    try:
        return page.evaluate(js)
    except PlaywrightError:
        return []


def page_module_title(page, module_index: int) -> str:
    for sel in ["main h1", "main h2", "h1", "h2"]:
        try:
            loc = page.locator(sel).first
            if loc.count() > 0:
                txt = (loc.inner_text(timeout=1_500) or "").strip()
                if txt:
                    return clean_module_title(txt, module_index)
        except Exception:
            continue
    return f"Module {module_index}"


def discover_outline(page, course_url: str, slug: str, max_modules: int = 30):
    """Walk module/week pages 1..N, harvesting lecture links in order.

    Stops once a module page yields no new lectures (two empties in a row) to
    avoid guessing the exact week count.
    """
    base = f"https://www.coursera.org/learn/{slug}"
    lectures: list[Lecture] = []
    seen_urls: set[str] = set()
    order = 0
    empty_streak = 0

    if not is_logged_in(page):
        LOGGER.info("Waiting for Coursera login before discovering the outline.")
        pause_for_login_if_needed(page, course_url)

    for module_index in range(1, max_modules + 1):
        found_new = False
        for path in (f"/home/module/{module_index}", f"/home/week/{module_index}"):
            if not is_logged_in(page):
                LOGGER.info("Login lost while discovering the outline; waiting again.")
                pause_for_login_if_needed(page, base + path)
            target = base + path
            # Some (often older) courses use /week/ not /module/, and hitting the
            # non-existent variant can abort (ERR_ABORTED) rather than 404 cleanly.
            # Retry once, then fall through to the other path variant.
            loaded = False
            for attempt in range(2):
                try:
                    page.goto(target, wait_until="domcontentloaded", timeout=NAVIGATION_TIMEOUT_MS)
                    loaded = True
                    break
                except PlaywrightError as exc:
                    LOGGER.warning("Could not load %s (attempt %s): %s", target, attempt + 1, exc)
                    polite_sleep(1.5, "retry after navigation error")
            if not loaded:
                continue
            wait_ready(page)
            polite_sleep(PAGE_SETTLE_SECONDS, "outline settle")
            expand_all_sections(page)
            module_title = page_module_title(page, module_index)
            for url, title in harvest_lectures_on_page(page):
                if url in seen_urls:
                    continue
                seen_urls.add(url)
                order += 1
                item_slug = url.rstrip("/").split("/")[-1]
                lectures.append(Lecture(
                    order=order,
                    module_index=module_index,
                    module_title=module_title,
                    title=clean_lecture_title(title),
                    url=url,
                    item_slug=item_slug,
                ))
                found_new = True
            if found_new:
                break  # don't also crawl the /week/ variant for this index

        if found_new:
            empty_streak = 0
            LOGGER.info("Module %s: %s lectures so far (total %s).",
                        module_index, order, len(lectures))
        else:
            empty_streak += 1
            LOGGER.info("Module %s: no new lectures (empty streak %s).",
                        module_index, empty_streak)
            if empty_streak >= 2:
                break

    return lectures


# --------------------------- phase 2: extract ----------------------------

def reveal_transcript(page) -> None:
    tab = find_first_optional(page, TRANSCRIPT_TAB_SELECTORS, timeout_ms=4_000)
    if tab is not None:
        try:
            tab.click(timeout=3_000)
            page.wait_for_timeout(800)
        except Exception:
            LOGGER.debug("Transcript tab click failed; may already be open.", exc_info=True)


def extract_transcript(page, with_timestamps: bool):
    """Return (plain_text, timestamped_lines). Tries structured phrases first,
    then falls back to the transcript container's innerText, then a JS scan."""
    container = find_first_optional(page, TRANSCRIPT_CONTAINER_SELECTORS,
                                    timeout_ms=TRANSCRIPT_WAIT_MS)

    # Structured phrases (gives clean cue boundaries + any timestamps).
    if container is not None:
        for sel in TRANSCRIPT_PHRASE_SELECTORS:
            phrases = container.locator(sel)
            try:
                n = phrases.count()
            except PlaywrightError:
                n = 0
            if n >= 3:
                cues = []
                for i in range(n):
                    try:
                        txt = (phrases.nth(i).inner_text(timeout=1_000) or "").strip()
                    except Exception:
                        txt = ""
                    if txt:
                        cues.append(re.sub(r"\s+", " ", txt))
                if cues:
                    return cues_to_outputs(cues)

    # Fallback: whole-container innerText.
    if container is not None:
        try:
            raw = container.inner_text(timeout=3_000)
            if raw and raw.strip():
                return raw_to_outputs(raw)
        except Exception:
            LOGGER.debug("Container innerText failed.", exc_info=True)

    # Last-ditch JS scan for a transcript-looking region.
    raw = page.evaluate(
        """
        () => {
          const cands = document.querySelectorAll(
            "div.rc-Transcript, [data-testid='transcript'], [class*='ranscript']"
          );
          let best = '';
          for (const el of cands) {
            const t = el.innerText || '';
            if (t.length > best.length) best = t;
          }
          return best;
        }
        """
    )
    if raw and raw.strip():
        return raw_to_outputs(raw)
    return "", []


TIMESTAMP_RE = re.compile(r"^\(?\d{1,2}:\d{2}(?::\d{2})?\)?$")

# Coursera injects the player's accessibility label into transcript text, e.g.
# "Play video starting at :1:24 and follow transcript". Strip it everywhere.
PLAY_LABEL_RE = re.compile(
    r"Play video starting at[\s:]*[\d:]*\s*and follow transcript", re.IGNORECASE)
# Zero-width / BOM characters Coursera sprinkles between words; NBSP -> space.
_CHAR_FIXES = {0x200b: None, 0x200c: None, 0x200d: None, 0xfeff: None, 0x00a0: ord(' ')}


def sanitize_transcript(text: str) -> str:
    text = (text or "").translate(_CHAR_FIXES)
    text = PLAY_LABEL_RE.sub(" ", text)
    return re.sub(r"[ \t]+", " ", text)


def cues_to_outputs(cues):
    """cues may interleave timestamps and text, or carry both. Build a clean
    paragraph form and a timestamped form."""
    timestamped = []
    text_only = []
    pending_ts = None
    for c in cues:
        c = sanitize_transcript(c).strip()
        if not c:
            continue
        if TIMESTAMP_RE.match(c):
            pending_ts = c.strip("()")
            continue
        if pending_ts:
            timestamped.append(f"[{pending_ts}] {c}")
            pending_ts = None
        else:
            timestamped.append(c)
        text_only.append(c)
    plain = paragraphize(" ".join(text_only))
    return plain, timestamped


def raw_to_outputs(raw: str):
    raw = sanitize_transcript(raw)
    lines = [re.sub(r"\s+", " ", ln).strip() for ln in raw.splitlines()]
    lines = [ln for ln in lines if ln and not TIMESTAMP_RE.match(ln)]
    plain = paragraphize(" ".join(lines))
    return plain, lines


def paragraphize(text: str) -> str:
    """Group sentences into readable paragraphs (~4 sentences each)."""
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return ""
    sentences = re.split(r"(?<=[.!?])\s+", text)
    paragraphs, buf = [], []
    for s in sentences:
        buf.append(s)
        if len(buf) >= 4:
            paragraphs.append(" ".join(buf))
            buf = []
    if buf:
        paragraphs.append(" ".join(buf))
    return "\n\n".join(paragraphs)


def write_lecture_markdown(course_title: str, slug: str, lec: Lecture,
                           plain: str, timestamped, with_timestamps: bool) -> Path:
    out_dir = OUTPUT_ROOT / slug / lec.safe_module_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / lec.safe_filename()
    body = plain if plain else "_(No transcript text could be extracted for this lecture.)_"
    lines = [
        f"# {lec.title or lec.item_slug}",
        "",
        f"- **Course:** {course_title}",
        f"- **Module {lec.module_index}:** {lec.module_title}",
        f"- **Lecture #:** {lec.order}",
        f"- **URL:** {lec.url}",
        f"- **Extracted:** {time.strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "---",
        "",
        body,
        "",
    ]
    if with_timestamps and timestamped:
        lines += ["", "<details><summary>Timestamped transcript</summary>", "", "```"]
        lines += list(timestamped)
        lines += ["```", "", "</details>", ""]
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def write_course_index(course_title: str, slug: str, lectures) -> Path:
    out_dir = OUTPUT_ROOT / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "00_index.md"
    lines = [
        f"# {course_title}",
        "",
        f"- **Course slug:** {slug}",
        f"- **Lectures:** {len(lectures)}",
        f"- **Generated:** {time.strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "---",
        "",
    ]
    current_module = None
    for lec in lectures:
        if lec.module_index != current_module:
            current_module = lec.module_index
            lines += ["", f"## Module {lec.module_index}: {lec.module_title}", ""]
        rel = f"{lec.safe_module_dir()}/{lec.safe_filename()}"
        lines.append(f"{lec.order}. [{lec.title or lec.item_slug}]({rel})")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


# ----------------------------- bookkeeping -------------------------------

def read_lines(path: Path):
    if not path.exists():
        return []
    return [ln.strip() for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()]


def append_unique(path: Path, value: str) -> None:
    existing = set(read_lines(path))
    if value not in existing:
        with path.open("a", encoding="utf-8") as fh:
            fh.write(value + "\n")


def get_resume_order(lectures) -> int:
    resume_file = LAST_PROCESSED_FILE if LAST_PROCESSED_FILE.exists() else LAST_COMPLETED_FILE
    if not resume_file.exists():
        return 0
    last = resume_file.read_text(encoding="utf-8").strip()
    for lec in lectures:
        if lec.url == last:
            return lec.order
    return 0


# ------------------------------- outline IO ------------------------------

def save_outline(course_title: str, slug: str, lectures) -> None:
    OUTLINE_FILE.write_text(json.dumps({
        "course_title": course_title,
        "slug": slug,
        "lectures": [asdict(l) for l in lectures],
    }, indent=2), encoding="utf-8")


def load_outline(slug: str):
    if not OUTLINE_FILE.exists():
        return None
    data = json.loads(OUTLINE_FILE.read_text(encoding="utf-8"))
    if data.get("slug") != slug:
        return None
    lectures = [Lecture(**l) for l in data["lectures"]]
    return data.get("course_title", slug), lectures


def prettify_slug(slug: str) -> str:
    s = re.sub(r"^packt-", "", slug)               # vendor prefix
    s = re.sub(r"-[a-z0-9]{4,6}$", "", s)          # trailing random id (e.g. -bmddx)
    s = s.replace("-", " ").strip()
    return s.title() if s else slug


def get_course_title(page, slug: str) -> str:
    # The document title on a lecture page is the lecture name, not the course,
    # so prefer an explicit course-name node, then fall back to the slug.
    for sel in ["a[data-click-key*='course_home'] h1",
                "nav a[href*='/home/'] span",
                "[data-test='course-name']"]:
        try:
            loc = page.locator(sel).first
            if loc.count() > 0:
                txt = (loc.inner_text(timeout=1_000) or "").strip()
                if txt and len(txt) > 3:
                    return re.sub(r"\s+", " ", txt)
        except Exception:
            continue
    return prettify_slug(slug)


# --------------------------------- main ----------------------------------

def build_fallback_profile_dir(base_profile_dir: str | Path) -> Path:
    base = Path(base_profile_dir)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    fallback = base.parent / f"{base.name}-{timestamp}"
    return fallback


def launch_brave_profile(playwright, profile_dir: str | Path):
    launch_args = [
        "--no-first-run",
        "--no-default-browser-check",
        "--disable-features=Translate",
    ]
    try:
        return playwright.chromium.launch_persistent_context(
            user_data_dir=str(profile_dir),
            executable_path=BRAVE_PATH,
            headless=HEADLESS,
            accept_downloads=False,
            args=launch_args,
        )
    except Exception as exc:
        message = str(exc).lower()
        if "processsingleton" not in message and "profile is already in use" not in message and "already in use" not in message:
            raise

        fallback_dir = build_fallback_profile_dir(profile_dir)
        LOGGER.warning(
            "Brave profile %s is already in use or locked. Falling back to a fresh profile: %s",
            profile_dir,
            fallback_dir,
        )
        return playwright.chromium.launch_persistent_context(
            user_data_dir=str(fallback_dir),
            executable_path=BRAVE_PATH,
            headless=HEADLESS,
            accept_downloads=False,
            args=launch_args,
        )


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Fetch and organize Coursera course transcripts.")
    p.add_argument("--course-url", required=True,
                   help="Any URL of the target course (home/week/lecture page).")
    p.add_argument("--cdp-url", default="",
                   help="Optional CDP URL for an already-running Brave/Chrome started with "
                        "--remote-debugging-port. Leave blank to use the dedicated Brave profile.")
    p.add_argument("--profile-dir", default=str(AUTOMATION_USER_DATA_DIR),
                   help="Dedicated Brave profile dir, used when --cdp-url is not provided.")
    p.add_argument("--discover-only", action="store_true",
                   help="Only build/refresh the outline; don't extract transcripts.")
    p.add_argument("--refresh-outline", action="store_true",
                   help="Re-crawl the outline even if a cache exists.")
    p.add_argument("--timestamps", action="store_true",
                   help="Also embed a timestamped transcript block in each file.")
    p.add_argument("--restart", action="store_true",
                   help="Ignore the resume cursor and process from the first lecture.")
    p.add_argument("--limit", type=int, default=0,
                   help="Process at most N lectures this run (0 = all). Useful for testing.")
    p.add_argument("--max-modules", type=int, default=30)
    p.add_argument("--retries", type=int, default=MAX_RETRIES)
    p.add_argument("--pause-before-exit", action="store_true")
    return p.parse_args()


def main() -> None:
    configure_logging()
    args = parse_args()
    slug = course_slug_from_url(args.course_url)
    LOGGER.info("Course slug: %s", slug)

    with sync_playwright() as playwright:
        browser = None
        cdp_mode = False
        if args.cdp_url:
            LOGGER.info("Attempting to attach to running browser via CDP: %s", args.cdp_url)
            try:
                browser = playwright.chromium.connect_over_cdp(args.cdp_url)
                context = browser.contexts[0] if browser.contexts else browser.new_context()
                cdp_mode = True
            except Exception as exc:
                LOGGER.warning(
                    "CDP attach failed for %s: %s. Falling back to a dedicated Brave profile.",
                    args.cdp_url,
                    exc,
                )
                browser = None
                context = playwright.chromium.launch_persistent_context(
                    user_data_dir=args.profile_dir,
                    executable_path=BRAVE_PATH,
                    headless=HEADLESS,
                    accept_downloads=False,
                    args=["--no-first-run", "--no-default-browser-check",
                          "--disable-features=Translate"],
                )
        else:
            LOGGER.info("Launching dedicated Brave profile: %s", args.profile_dir)
            context = launch_brave_profile(playwright, args.profile_dir)
        context.set_default_timeout(DEFAULT_TIMEOUT_MS)
        context.set_default_navigation_timeout(NAVIGATION_TIMEOUT_MS)
        # In CDP mode open our own working tab (login is shared at the profile
        # level) so we never hijack a tab you're using.
        if cdp_mode:
            page = context.new_page()
        else:
            page = context.pages[0] if context.pages else context.new_page()
        page.bring_to_front()

        try:
            # ---- outline (cached unless refreshing) ----
            cached = None if args.refresh_outline else load_outline(slug)
            if cached:
                course_title, lectures = cached
                LOGGER.info("Loaded cached outline: %s lectures.", len(lectures))
            else:
                page.goto(args.course_url, wait_until="domcontentloaded",
                          timeout=NAVIGATION_TIMEOUT_MS)
                wait_ready(page)
                pause_for_login_if_needed(page, args.course_url)
                course_title = get_course_title(page, slug)
                LOGGER.info("Course title: %s", course_title)
                lectures = discover_outline(page, args.course_url, slug, args.max_modules)
                if not lectures:
                    safe_save_screenshot(page, "no_lectures_found.png")
                    raise RuntimeError("No lecture items discovered. Selectors may need tuning "
                                       "(see coursera_screenshots/no_lectures_found.png).")
                save_outline(course_title, slug, lectures)

            index_path = write_course_index(course_title, slug, lectures)
            LOGGER.info("Wrote course index: %s", index_path)
            LOGGER.info("Total lectures: %s", len(lectures))

            if args.discover_only:
                print(f"\nDiscovered {len(lectures)} lectures. Outline: {OUTLINE_FILE}")
                print(f"Index: {index_path}")
                return

            # ---- extract transcripts ----
            start_order = 0 if args.restart else get_resume_order(lectures)
            remaining = [l for l in lectures if l.order > start_order]
            if args.limit and args.limit > 0:
                remaining = remaining[:args.limit]
            LOGGER.info("Resuming after order %s; remaining: %s", start_order, len(remaining))

            done = failed = empty = 0
            for lec in tqdm(remaining, desc="Transcripts", unit="lec"):
                polite_sleep(MIN_DELAY_BETWEEN_ITEMS_SECONDS, "between lectures")
                LAST_PROCESSED_FILE.write_text(lec.url, encoding="utf-8")
                ok = False
                for attempt in range(1, args.retries + 1):
                    try:
                        page.goto(lec.url, wait_until="domcontentloaded",
                                  timeout=NAVIGATION_TIMEOUT_MS)
                        wait_ready(page)
                        if attempt == 1:
                            pause_for_login_if_needed(page, lec.url)
                        polite_sleep(PAGE_SETTLE_SECONDS, "lecture settle")
                        reveal_transcript(page)
                        plain, ts = extract_transcript(page, args.timestamps)
                        path = write_lecture_markdown(course_title, slug, lec,
                                                      plain, ts, args.timestamps)
                        if plain:
                            LOGGER.info("[%s/%s] %s -> %s",
                                        lec.order, len(lectures), lec.title or lec.item_slug, path)
                            done += 1
                        else:
                            LOGGER.warning("[%s] No transcript text: %s",
                                           lec.order, lec.url)
                            append_unique(MANUAL_FILE, lec.url)
                            empty += 1
                        ok = True
                        break
                    except Exception as exc:
                        LOGGER.warning("[%s] attempt %s/%s failed: %s",
                                       lec.order, attempt, args.retries, exc)
                        safe_save_screenshot(page, f"error_{lec.order:03d}_attempt{attempt}.png")
                        time.sleep(3 * attempt)
                if ok:
                    LAST_COMPLETED_FILE.write_text(lec.url, encoding="utf-8")
                else:
                    append_unique(FAILED_FILE, lec.url)
                    failed += 1

            print("\n" + "=" * 60)
            print(f"Course           : {course_title}")
            print(f"Total lectures   : {len(lectures)}")
            print(f"Extracted        : {done}")
            print(f"No transcript    : {empty}  (-> {MANUAL_FILE})")
            print(f"Failed           : {failed}  (-> {FAILED_FILE})")
            print(f"Output           : {OUTPUT_ROOT / slug}")
            print(f"Log file         : {LOG_FILE}")
        finally:
            if args.pause_before_exit:
                print("\nInspect the browser if needed.")
                input("Press ENTER to finish...")
            if browser is not None:
                # Attached via CDP: leave the user's Brave and tabs intact,
                # just detach our own working tab and the connection.
                try:
                    if page is not None and not page.is_closed() and len(context.pages) > 1:
                        page.close()
                except Exception:
                    LOGGER.debug("Could not close working tab.", exc_info=True)
                browser.close()
            else:
                context.close()


if __name__ == "__main__":
    main()
