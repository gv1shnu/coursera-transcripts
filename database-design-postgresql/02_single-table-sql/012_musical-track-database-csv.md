# Musical Track Database (CSV)

- **Course:** Database Design Postgresql
- **Module 2:** Single Table SQL
- **Lecture #:** 12
- **URL:** https://www.coursera.org/learn/database-design-postgresql/lecture/SP05X/musical-track-database-csv
- **Extracted:** 2026-06-22 20:19:16

---

Hello and welcome to another walkthrough for Postgres for Everybody. In this walkthrough, we're going to do a simple musical track database. We're going to explore the copy command. The idea is we're going to take a comma-separated value, and it depends on how you're doing this.

I'm going to use PythonAnywhere, given that a lot of what we're doing is on PythonAnywhere. So here I am in Linux. I'm in my home directory, I got no files other than that README.txt. So I'm going to run the Postgres, pgsql, or psql command here, but I have to get this file onto this same computer that's running my client so that it can read it.

And so there's a command in Linux and and sometimes in Linux you use wget or curl minus o. In this case they do the same thing. They grab data from a URL and they copy it to a file on your hard drive. So you'll see that this makes a connection like a browser to a URL.

And now I've got a file, it's got about 20,000 characters on it. And if I edit it with my happy little vi library.csv, you see that this is a comma-separated value that's got artist and title and album and my rating and the number of views and the length of this thing. And so it's comma-separated value, the kind of thing that spreadsheets produce. And our goal is to load this into a database, this track_raw that's going to have.

There's six columns in my CSV file. There are six columns in track_raw. And so I've got to run the Postgres command. And so here's all my Postgres details.

But because I do this way too many times, I also make it so that you don't have to construct that. That's the psql command that I've got to type. I'm going to copy my password and paste that over. And now of course I'm not talking to a Linux anymore, I'm talking to the psql command and so I've got this prompt, hello world.

What? And so it's expecting me to type something and I'm not typing what it wants and you'll notice that this little arrow is telling me something and it's telling me that I'm in the middle of a communication. And that's because it expects that semicolon is what's going to happen to end a potentially multiline SQL statement. So in this case, it was expecting me to type SQL, and I didn't.

But it was in a continuation and so that's why it messed up. I can take a look at my tables with \dt. Now \dt is not structured query language. That is part of what it is we do inside psql.

So this is a feature of psql and you might use a different database client and you will have a different way to list all of the tables. But you can also type SQL as well. So going back to our assignment, the thing we've got to do is to run a bit of SQL. Now you'll notice that this is three lines of text ending in a semicolon.

So I'm going to copy that, I'm going to paste it. You'll see it's telling me that it's in a continuation. The second continuation says it's not only a continuation, but it's in a parentheses. But then if I hit Enter, that means that the semicolon is going to cause that statement to execute.

And if I say \dt, it's going to show that I've got another table, those other three tables, pg4e debug, meta, and result, they're from previous assignments that I was doing. So I now have library.csv on my local hard drive and I've got a table called track_raw. The only thing I need to do is to run and copy this all in. Now, later we'll learn all kinds of ways using Python and other things to put data in.

But I'm going to actually use a feature built into psql. Now, if you're using a different database client, this \copy is not necessarily going to work. You might be using a full-screen client, but this is how we do it in psql. For this assignment you might be best off just using psql.

So \copy is a psql command, not an SQL command, a psql command. Going into this table with these columns, read this file and split it with commas and do CSV. And so that's all built in. We're just going to run it.

And it is going to have selected. That means it's going to have inserted SELECT count star track_raw type it correct, Chuck. That's not good. What went wrong?

I only got one. SELECT star FROM, oh I think I needed to say FROM track_raw. Yeah, that's going to make it a little better. SELECT count star is what I wanted to say.

There's supposed to be more than one track in there and there is, there's 296. [LAUGHTER] So I just SELECT count star track_raw was not a syntax error. I don't know quite what it was doing, but it was doing something. And that's why I was confused when I saw only one, but really there's 296, which makes a lot more sense.

And doing the assignment, it says, hey run this SELECT statement just to see if you got the right data. And I will run it and here's the data. The Legend of Johnny Cash, Computing Conversation, Natural Wonders. And there we go.

And at this point, I can submit my assignment because my assignment was to get this table created. And then the autograder is going to make a database connection to this same database and run a SELECT command. So let's have it do that. And so it got a good answer and away you go.

And so I hope this has been a useful walkthrough of one of these early assignments. Again, this one you might want to use psql for because of the use of the copy command there. You can figure it out in other database clients, it might be an import button or something like that. But for this one, it might just be easier to go ahead and use PythonAnywhere.

Let me quit out of this and get out with \q. It might be easier to use PythonAnywhere for this particular one. So hope you found this useful. Cheers.
