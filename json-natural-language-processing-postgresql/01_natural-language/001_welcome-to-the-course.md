# Welcome to the Course!

- **Course:** Json Natural Language Processing Postgresql
- **Module 1:** Natural Language
- **Lecture #:** 1
- **URL:** https://www.coursera.org/learn/json-natural-language-processing-postgresql/lecture/wNENW/welcome-to-the-course
- **Extracted:** 2026-06-22 20:32:41

---

Welcome to Course 3 of Postgres for Everybody. In this course, we're really going to focus on two topics, and that is text and JSON. Computers do numbers really well and that, for example, is why we use numbers for foreign keys because 64-bit integers are something computers store efficiently, move around efficiently, compare efficiently, etc. But the large fraction of the work of the data that's being stored are strings, names, comments, blog posts.

What good are numbers? I mean, we use them for like average weather temperature or something, and so it's useful. I mean, zip codes, they're not even numbers. They're like strings.

Phone numbers are strings. So text is important and natural language is important. Texts of conversations and search engines, etc. And JSON is really the biggest thing to happen to relational databases in 20, 25 years.

And I've been talking about it kind of all throughout the course about how important it is that databases do a good job with JSON. JSON allows for applications to evolve so that the structure, I mean, we did data modeling. We talked about every column matters, a 64-character width column versus a 2 million-character column matters. We want that for efficiency for maximum packing.

But at some point, that sort of prearranged contract of you know exactly what columns they're going to be and exactly what size they're going to be is great, but it's also limiting for some applications. Sometimes you just want to throw a little bit of data in, not something you're going to sort on or put in a WHERE clause or whatever. Although you will see that with JSON you can index pieces of JSON that make it so that it works great in WHERE clauses. And so the flexibility that JSON gives us is really an improvement to relational databases.

But then what we don't want to do is we don't want to give up all of the amazing performance that we get by a carefully constructed schema where we agree with the database system in advance how we're going to use it. And so this section is going to talk a lot about how unstructured data can be treated like structured data. So I hope you enjoy it.
