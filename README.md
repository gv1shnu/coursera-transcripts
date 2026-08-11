# Coursera Transcripts

A small Python automation project that walks a Coursera course, discovers lecture links, and exports transcript text into neatly organized Markdown notes.

This project uses Playwright with a dedicated Brave profile so you can authenticate once and then let the script handle the rest automatically.

## Overview

The main script is:

- `coursera_transcripts.py`

It performs two main phases:

1. Discover the course outline and cache every lecture link.
2. Open each lecture, reveal the transcript, and write a Markdown file.

It also supports resume state, optional timestamped transcript output, and a discovery-only mode for checking the course outline before extraction begins.

## Features

- Discovers lecture URLs from the Coursera course outline
- Caches discovered lectures in `coursera_outline.json`
- Automatically resumes from the last processed lecture
- Writes notes under `transcripts/<course-slug>/`
- Generates an index file for each course
- Supports `--discover-only` for previewing the outline
- Supports `--timestamps` for timestamped transcript blocks
- Can attach to an existing running browser with CDP or use a dedicated Brave profile

## Requirements

- macOS
- Python 3.9+
- Brave Browser installed at `/Applications/Brave Browser.app/Contents/MacOS/Brave Browser`
- A valid Coursera account with access to the course
- Internet access

## Quick Start

### 1) Create a virtual environment

```bash
cd /Users/vishnu/Dev/coursera-transcripts
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies

```bash
pip install playwright tqdm
python -m playwright install
```

### 3) Run the script

```bash
python3 coursera_transcripts.py --course-url "https://www.coursera.org/learn/<course-slug>/home/week/1"
```

When the script detects that you are not signed in to Coursera, it opens a Brave window and pauses so you can log in manually. After login, it continues automatically.

## Common Commands

### Discover course outline only

```bash
python3 coursera_transcripts.py --course-url "https://www.coursera.org/learn/<course-slug>/home/week/1" --discover-only
```

This is useful for checking whether the script can find lecture items before extracting all transcripts.

### Restart from the beginning

```bash
python3 coursera_transcripts.py --course-url "https://www.coursera.org/learn/<course-slug>/home/week/1" --restart
```

### Process only a few lectures for testing

```bash
python3 coursera_transcripts.py --course-url "https://www.coursera.org/learn/<course-slug>/home/week/1" --limit 5
```

### Include timestamps in exported transcripts

```bash
python3 coursera_transcripts.py --course-url "https://www.coursera.org/learn/<course-slug>/home/week/1" --timestamps
```

### Use an already-running browser

```bash
python3 coursera_transcripts.py --course-url "https://www.coursera.org/learn/<course-slug>/home/week/1" --cdp-url "http://127.0.0.1:9222"
```

This attaches to an active browser session via Chrome DevTools Protocol instead of launching a dedicated Brave profile.

## Example Usage

A complete, real invocation. Any course URL works — `/home/welcome`, `/home/week/1`, or a lecture page — because the script only needs the `/learn/<course-slug>/` part and walks the modules itself.

```bash
python3 coursera_transcripts.py \
  --course-url "https://www.coursera.org/learn/packt-bug-bounty-from-scratch/home/welcome" \
  --timestamps
```

On the first run for a course, the script opens Brave and pauses for you to log in to Coursera; after that the session persists in the dedicated profile and later runs skip straight to discovery.

Typical console summary at the end of a run:

```text
============================================================
Course           : Introduction To Mongodb
Total lectures   : 59
Extracted        : 59
No transcript    : 0  (-> coursera_manual_items.txt)
Failed           : 0  (-> coursera_failed_items.txt)
Output           : transcripts/introduction-to-mongodb
Log file         : coursera_transcripts.log
```

Preview the outline first (no transcript extraction), then do a small test run before the full pull:

```bash
# 1) See what lectures would be discovered
python3 coursera_transcripts.py --course-url "https://www.coursera.org/learn/packt-bug-bounty-from-scratch/home/welcome" --discover-only

# 2) Pull just the first 3 transcripts to sanity-check output
python3 coursera_transcripts.py --course-url "https://www.coursera.org/learn/packt-bug-bounty-from-scratch/home/welcome" --limit 3 --timestamps

# 3) Run the whole course
python3 coursera_transcripts.py --course-url "https://www.coursera.org/learn/packt-bug-bounty-from-scratch/home/welcome" --timestamps
```

## Output Structure

The script writes output to the project folder and a course-specific transcript directory.

### Root files

- `coursera_outline.json` — cached lecture outline for the current course
- `coursera_last_completed.txt` — last successfully processed lecture URL
- `coursera_last_processed.txt` — most recent lecture URL processed or attempted
- `coursera_failed_items.txt` — lectures that failed extraction
- `coursera_manual_items.txt` — lectures without usable transcript text
- `coursera_transcripts.log` — script logs and diagnostics
- `coursera_screenshots/` — screenshots captured for failed/interesting pages

### Transcript files

Example output layout:

```text
transcripts/
└── <course-slug>/
    ├── 00_index.md
    ├── 01_module-one/
    │   ├── 001_lecture-one.md
    │   └── 002_lecture-two.md
    └── 02_module-two/
        └── 003_lecture-three.md
```

Each exported Markdown file includes:

- course name
- module title
- lecture number
- lecture URL
- extraction timestamp
- transcript text

## Browser and Login Behavior

The script defaults to a dedicated Brave profile stored under:

```text
~/.brave-coursera-transcripts
```

This uses a writable home-level directory instead of a protected macOS system path, which avoids the profile-lock issue seen with some Library locations. If you are not already logged in, the script opens Brave and waits for manual sign-in before continuing.

## Troubleshooting

### No lecture links were found

This often means the site structure changed or the selectors need adjustment. Check:

- `coursera_transcripts.log`
- `coursera_screenshots/`
- `coursera_outline.json`

### Transcript output is empty

A lecture may not have transcript text available, or the page layout may not match the script’s selectors. Such lectures are recorded in `coursera_manual_items.txt`.

### Extraction fails for one lecture

Use `--limit` to test a smaller subset and inspect the error screenshots/log output for that lecture.

## Notes

- This project is intended for personal study and local note-taking.
- Coursera may change page structure over time, so selectors may require updates.
- Please respect Coursera’s terms of use and the licensing of the content you access.

## Full Example Workflow

```bash
cd /Users/vishnu/Dev/coursera-transcripts
python3 -m venv .venv
source .venv/bin/activate
pip install playwright tqdm
python -m playwright install

python3 coursera_transcripts.py --course-url "https://www.coursera.org/learn/<course-slug>/home/week/1" --discover-only
python3 coursera_transcripts.py --course-url "https://www.coursera.org/learn/<course-slug>/home/week/1"
```

## Script Behavior Summary

The script is intentionally straightforward:

- parse arguments
- discover the course outline
- save outline metadata
- write the course index
- traverse lectures
- export transcript Markdown files
- resume cleanly on future runs

This gives you a simple, repeatable workflow for turning Coursera lectures into searchable local notes.
