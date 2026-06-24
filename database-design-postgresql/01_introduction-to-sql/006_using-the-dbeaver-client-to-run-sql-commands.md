# Using the DBeaver Client to Run SQL Commands

- **Course:** Database Design Postgresql
- **Module 1:** Introduction to SQL
- **Lecture #:** 6
- **URL:** https://www.coursera.org/learn/database-design-postgresql/lecture/gx009/using-the-dbeaver-client-to-run-sql-commands
- **Extracted:** 2026-06-22 20:17:12

---

Hello and welcome to another Postgres for Everybody walkthrough. In this walkthrough, we're going to use instead of PythonAnywhere or a Jupyter Notebook or even the terminal on your own computer and using psql, I'm just going to show you a way to use a sort of high desktop application to work with your SQL database. So I've already installed this DBeaver. And it's free, it's open source, it's quite amazing, and it works pretty well.

Not all of these kinds of desktop applications work well with Postgres databases. There is pgAdmin that doesn't work well because your database doesn't have enough power, but DBeaver seems to work out okay. So the way these navigators work is they have what are called connections. And this can do not just Postgres, but as you'll see, a whole bunch of things.

You go, you find your way into your assignment, and we're going to do this very first assignment. And I could do this, use this in the database, but psql is a client. We're not going to use that. Our client is going to be DBeaver.

So what we're going to do is we're going to go into DBeaver, and we're going to say add another connection and it already knows about Postgres. Now, if you first install it, it may have to install some drivers. Don't worry about it, seems that works just peachy fine, and away you go. You're going to go back now to the data that you've got, and the data that you've got, I'll show that to you in a second, is at pg.pg4e.com.

That's the name of the host. The database name, we're going to have to copy and paste that back and forth. Database and the user are the same. So we'll do that and that.

So that came from your assignment. Now we can copy our password and come over here, and put our password in, and that's literally all you need to do. And again, we're creating a client through which we can send SQL commands. And so here we go, we've got this.

It says this is a database connection, and within that you could have more than one database, but right now we only have one database. And if you keep opening this up, you see that the schemas, these two, the pg_catalog, this has got stuff that Postgres needs and sometimes we'll actually select from that. But don't hurt it. And the information schema, that's like its own internal stuff, leave that alone.

The place that you work here is in this public and we're going to be making tables, which currently we have none. And so we want to run some SQL, and so if you have a bunch of these over here on the left-hand side, You want to have this one selected. And then you click on this thing that basically says make a new SQL script. And so this is a script and the destination of the SQL commands is that database.

And so if we go back to our assignment now and we look, this CREATE TABLE is the first thing that we're supposed to do. I'll say CREATE TABLE, and then I am going to hit the Go button. That's what this little execute SQL statement is. And look at that.

It told us that it worked and now if we pop this open, there's supposed to be a table here. I need to refresh it or something, I'll refresh the connection. Somehow I lost my connection. Refresh the connection.

So I refreshed the connection, and then we see the pg4e_debug. So now I'm going to go and do another script. This script is right here. I'll close my little public window there, and I'll go to the next thing I'm supposed to do.

I'm going to run another CREATE TABLE pg4e_result and I type that in here and then I run it. Then I go over here and I do a refresh and I see that one. It wouldn't hurt if it auto refreshed. But away we go, we're only going to do a few of these.

So then what we're going to do is we've created these two tables and we're going to do Check Answer, which is going to check to see if our tables are created because my autograder is now connecting to that database connection. And at this point, if we do another refresh, you see that this meta table showed up just like it said it was going to do, and so you've now created this. And so there's things you can do and can't do, and import and export are little bit different. And so most of the assignments you will be able to do in this class using either DBeaver, or another client, or psql.

I tend to focus on psql because sometimes you're working on a server and you're logged into that server and you've got to type the commands in command line. So there's nothing wrong with knowing how to use command line, but there's also nothing wrong with knowing how to use a more advanced client. Okay. So that was just a really quick walkthrough on how you might use DBeaver as your client sometimes as a substitute for psql or a compliment to psql.

Cheers.
