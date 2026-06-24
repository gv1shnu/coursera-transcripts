# Altering Table Schema

- **Course:** Intermediate Postgresql
- **Module 1:** SQL Techniques
- **Lecture #:** 2
- **URL:** https://www.coursera.org/learn/intermediate-postgresql/lecture/MVa7Y/altering-table-schema
- **Extracted:** 2026-06-22 20:24:23

---

So the first topic I want to talk about is what we do after a CREATE TABLE. And so up till now I keep talking about like, oh, the CREATE TABLE and you've got to get it right and if you get the columns too short, then you're in bad shape. That's not exactly true, right? You can absolutely make mistakes.

Like in this one, the content, I'm making some blog posts, and the content I make is 1,000 characters and you might make a database table and think, well, my little paragraphs are going to be 1,000 characters and about that much text fits nicely into 1,000 characters. But then someone types more, and you're like, "Oh crap, 1,000 characters is not enough." And you're like, "Oh, now what do I do?" Well, it turns out that this ALTER TABLE capability in most competent databases is amazing. Meaning that you can change the schema and it will auto convert all of the data to the new schema all while the application is running. And even though we're doing data mining, so you're not always working with a live database, literally if you are building an online system, because you might actually be talking to a database where there is a front end to it, but you're like talking to the back end, it can do an ALTER TABLE while it's live.

Now, you've got to be careful because if you're like taking a column out or adding a column in, then if the application starts sending data to a column that you just removed, then that part will blow up. But in this case, I made my content a VARCHAR 1024, and it's like, no, that's not right, but I could easily fix that with an ALTER TABLE Another kind of thing that you might do is you wouldn't name your column oops, but you might be copying and pasting. And I do this all the time. You might be copying and pasting your CREATE statements, and then you leave something in, like in the favorites.

And so the comments, there's a text area and the favorites is a number, but I copied and pasted. I was in too much of a hurry and so I left the text thing in, but I forgot to add a number and I'm like, "Am I doomed?" And actually the application has already started and it's actually started to load data and you've got to fix it. Well, the good news is that's the ALTER TABLE. We make a mistake in a schema or the schema is going to evolve, and so we create it.

And even though these two look like they happen one right after another, I mean, ALTER TABLE DROP COLUMN oops could happen days or weeks or months later. And once the database starts altering it and doing that work, it's fine. And again, if nothing is looking for or storing stuff into this column oops, then we're good. And so again, you can do this on live databases.

And so the little mistakes I made is I added a column so you can drop a column. I had a column called content that was VARCHAR 1024 and it really needs to be TEXT so it could be unlimited length, and I forgot to set the column fav, which is how much you like something, and it's an integer. So you can add a column, you can drop a column, you can change a column. And it doesn't all have to be columns.

If you have like a foreign key relationship and you got it wrong, or uniqueness constraints. Sometimes you make a uniqueness constraint and you need to have two of your columns unique instead of one column and you just, like, change it. And you've got to like drop the constraints sometimes and then add a new constraint. But go talk to StackOverflow and say, "How do I change a constraint in a Postgres database?" And they will be like, Alter Table or sometimes drop constraint or whatever.

And like I said, I love the fact that it can run on a live database. Another technique that we're going to use is the basic notion of reading SQL statements from a file. And so I can hand you, and I do hand you, some of these files. Usually when I'm giving you the main file for the lecture, I kind of want you to cut and paste and see what each thing does.

But what if I'm going to load 1,000 records? Well, I'll just give you the insert statements in a text file with 1,000 insert statements or an insert statement with 1,000 values. And you're like, I want to run this file and so you just say \i, and then you give the file name. In this case, you would have downloaded it into the same folder as you are running your psql command.

Okay, so that's changing the schema and running scripts. And up next we're going to talk about how we handle dates. Dates are a real important part of databases.
