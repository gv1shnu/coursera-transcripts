# Demonstration: Creating and Loading a Database

- **Course:** Intermediate Postgresql
- **Module 2:** Using SQL Techniques
- **Lecture #:** 16
- **URL:** https://www.coursera.org/learn/intermediate-postgresql/lecture/iXJJI/demonstration-creating-and-loading-a-database
- **Extracted:** 2026-06-22 20:26:52

---

Hello and welcome to another walkthrough of our Postgres. This is a simple three table many-to-many situation. We're going to have users and posts and comments. And the comment is effectively a many-to-many join table, except it has very important information that's stored at that connection in content.

created_at the content, there's all kinds of stuff there. A post belongs to a user, so we have a foreign key account_id. And so away we go. So let's go ahead and build these tables, just copy them all, comments and all, and post them into, there we go.

Good thing I've got no typographical errors. If you see some of my slides that say TIMESTAMPZ, that was a common typo that I made. So you might want to anytime you see TIMESTAMPZ, turn it into TIMESTAMPTZ. Sorry about that mistake.

So now we have this all set up. Now, let's make this favorites also. Now I want to talk a little bit about the ALTER TABLE. So one of the cool things about the database, and usually it's not right after you create it where you notice you've made a mistake, but we're going to fix a couple of mistakes.

So if you look at the post table, you see that I made a content of VARCHAR 1024. I'm in a meeting and someone says, whoa, we're going to have to have posts that are more than 1000 characters. So I'm like, oh, I'd better fix that. ALTER TABLE post ALTER COLUMN content TYPE TEXT.

So what we're doing is we're changing a table, the table post, we're altering a column, alter column. The name of the column is content. And the new type is text. Now, the key is this is also going to convert live during the database if there's already data.

So ALTER TABLE is a very powerful thing. So you can get rid of a column. ALTER TABLE fav DROP COLUMN oops. So that gets rid of a column.

And we can add another column, add a column. ALTER TABLE fav ADD COLUMN howmuch INTEGER. And so that adds a column. So we're able to play with the schema of these tables.

The schema is very constraining on purpose. That's just how databases work. But we get to change the schema. And automatic conversion.

You can convert something from an integer to a string, or a string to an integer. If you do an ALTER TABLE that converts from a string to an integer, it's going to try to convert it and it will have trouble if there's strings in there that aren't legitimate integers. But you'd be surprised at how much you can do, and you can do it while the database is running and while actually transactions are happening, as long as you don't break the software. So if you drop a column the software is looking for, then all the SELECT statements will just like blow up in the next moment.

But you can alter these tables, so that's pretty cool. So the next thing I want to do is I want to load a bit of data. And so you can put, you can make SQL commands living in you see me just copying and pasting this stuff, but you can also do this by putting it all in a file and then running the file. So if I look at this file, 03-Techniques-Load.sql The one thing I'm doing is I'm DELETE FROM account, that's remember how a DELETE statement works is delete all records.

And this ALTER SEQUENCE, this basically restarts this serial number so I clear them all out. This you wouldn't do in a live running database, I'm just doing this so I can do it over and over and over again. And then I'm going to do some INSERT statements, fill some stuff up, just sort of to save it. Now, you need to figure out how to get this in here.

And so what I'm going to do is I'm going to make myself a terminal. And I am in that same, same directory. I could download that file, and I could upload that file. But the easiest thing to do is do what's called a wget.

So wget actually retrieves a file using HTTP and then stores it in the local directory. And I am going to grab this. Actually, that's not quite going to work because I don't I don't have the I don't have it up on its ultimate final. This domain name is not final yet, so it's going to have to come from here.

So if I do an ls minus l, you see that I have this file here, and if I do a nano 03-Techniques-Load.sql, there we go. And Control X gets me out of that. So I've got that file loaded. So that means that I can go back here in this same place, and I can simply say, read this file.

So anything that says backslash, backslash i, and we'll have other things like backslash d plus, those are commands to the Postgres client, the psql client that we're using. They're not actual SQL. And so if you're using MySQL or Oracle, there's like like d plus fav. There's a whole different name for that.

And so those are non-standard across databases. ALTER TABLE is pretty standard across databases, certainly CREATE TABLE is pretty standard with a few. SELECT is pretty standard. But I'm going to use this backslash i, and that is going to load a file on from this shell that I'm working at inside of my Jupyter notebook and I copy that file there, and it's going to load it, and it ran all of those commands.

See how cool that is? So now I can say SELECT star FROM post, and there they are. And so all those things were loaded up quite nicely and that just saves me some time. Okay.

So I'm going to stop now and I'll pick this up a bit later in with the same database.
