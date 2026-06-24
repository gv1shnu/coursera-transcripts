# Julia's Bank

- **Course:** Data Structures
- **Module 4:** Hash Tables
- **Lecture #:** 45
- **URL:** https://www.coursera.org/learn/data-structures/lecture/tvH8H/julias-bank
- **Extracted:** 2026-06-20 21:41:50

---

Hi, in the previous video, I started telling you the story of Julia's Diary, and then in this video, we're going to continue with the story of Julia's Bank. Seeing the success of her diary and keeping everything recorded, Julia actually had an idea that if she could lend money to her friends and then resolve the disputes by showing them records in the diary. Then she could probably not only lend money to friends but lend money to other people, and then resolve the disputes using records of her diary, and it worked. The bank gave credits to lenders and Julia used her diary to keep track of outstanding debts and if someone had some confusion about how much money here she borrowed.

She could show him the corresponding page of her diary with the moment and the amount of money borrowed and all the payments made after that. Julia bank grew very fast because everybody trusted it because she was very diligent and she never requested any money back if there wasn't a corresponding record in her diary that there was an outstanding debt. One night, a desperate lender hired a squad, broke into Julia's room, and forged the record about his debt and all the following records. Knowing that the system made him to forge not only the record about his debt but also all the following records.

It was hard, but with the squad it was doable. This way he didn't have to repay his debt. Julia remembered very vividly giving this day or this credit very few days ago. However, according to her own strict rules, she couldn't demand it back because there was no record whatsoever in her diary about giving this credit.

She wanted to make forgery even harder and to make it even harder and economically non-viable even with hiring a squad she came up with a new idea. She decided to add a special number called (nonce) to the end of each text record in such a way that the hash column value always will end with three zeros. Basically, that the hash value is always divisible by 1,000. How does it work?

Here is the beginning of the same diary. It starts with a special line with the hash column of 0000 and she tries to find such a number, in this case, it turned out to be 263, to write this number right after the text, ("Had breakfast.") Get some hash value for example 125 and concatenate this hash value with a hash value column of the previous line and get 1,250,000 such that after she takes hash value again it ends with three zeros. In this case, it ends with three zeros because it's 2,000, and for the next line, she added a nonce of 352 and it turned out that the intermediate hash value is 9876 and the concatenation is 98762000, and the hash of this string is in turn 7,000 again, ends with three zeros. Of course, to come up with the right nonce, Julia just has to try them all one by one, or in some random order.

The remainder of the resulting hash value modulo 1,000 will be any number between 0 and 999 with approximately the same probability. Because the hash function is so good that it distributes numbers modulo 1,000 almost evenly. It would take her on average around 500 steps until she finds a nonce resulting in remainder 0 modulo 1,000 if she tries them randomly. This in turn makes forgery 500 times harder.

It is unknown how to find a string with a given hash value faster than by trying all possible strings, either in random order or in some strict order. On average, anyone who wants to forge a record would need to find a nonce for 500 steps for every record signed from this record and up to the end of the diary, and this all makes forgery 500 times harder. Julia can control the tradeoff between her effort to keep the diary and the effort needed to forge it. Because in this example, it became 500 times harder to keep the diary but also 500 times harder to forge the diary.

But instead of taking everything modulo 1,000 and requiring three zeros in the end. She could require, for example, nine zeros in the end. Then it will become even harder to both keep the diary and to forge it. In the next video, you'll learn how actually blockchain grows from all these ideas.
