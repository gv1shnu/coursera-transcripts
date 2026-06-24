# Using PythonAnywhere to Run SQL

- **Course:** Database Design Postgresql
- **Module 1:** Introduction to SQL
- **Lecture #:** 5
- **URL:** https://www.coursera.org/learn/database-design-postgresql/lecture/llPUo/using-pythonanywhere-to-run-sql
- **Extracted:** 2026-06-22 20:17:01

---

Hello, and welcome to another recording for PostgreSQL for Everyone. Perhaps the first recording you're watching. So today I'm going to show you how you can do all of the homework using the psql command on a Linux shell that we get for free from PythonAnywhere. First, I want to introduce you to the PythonAnywhere crew.

I have been to London a couple of times and met with and had coffee with the great folks at PythonAnywhere. They are very good. You're going to use a free account and it's going to stay free. It expires after three months if you don't use it, but if you keep using it, it stays free.

And you can upgrade for a more advanced account, but for this class, you just need the completely free account and nothing more. And they don't spam you and they don't try to get your money. They just give it to you for free. So I really like working with them.

Once you sign in and you start doing your homework, you're going to be seeing things like these assignments, Initial Database Setup. And when you go in there, pg4e.com is going to give you a database. And these are the connection. The host, the port, the database, and the user, and the password are what you need to make the database connection for Postgres from any client.

And you can use any client you want but I'm going to focus on the command-line client. And it just also gives you the exact psql command to type if you have a command-line client. So there's some documentation on how to do what I'm talking about that's available and it's linked right from the lesson. And so you can go through that documentation, but my video is going to show you.

So now I have got PythonAnywhere and this is a free account. My username is pg4e. I got it because I got there first. And so there's a number of cool things that you can do here.

And the thing we're going to do most, and I tend to open a lot of things in new tabs. So I'm going to open the Consoles screen in a new tab, and I'm going to start a Bash console. So here I am. I've got a Bash console and it's Linux.

There's a number of pwd I can see my current working directory. I can say ls to see files. I already made this file lesson1.sql cat it. cat lesson1.sql.

That shows the contents of the text file. Cat README.txt. Oh by the way, I just said cat R-E tab. You can do tab completion when you're typing a filename on a Linux command, which is super cool.

The other thing you can do is cursor back through your previous commands. I'm just pressing the up arrow. And so I can do that. I can type cd folder to be in a folder.

cd fold tab, that'll work. There's no files in here. I can say cd dot dot, to go up a folder. I can go back into my folder, cd folder tab, and then I say cd tilde.

If I say cd squiggle or tilde that goes back to your home folder no matter where you're at. And so you'll see a lot of my commands tell you to do cd tilde and then cd into a subfolder. And everyone has a home directory, like in most commands where there's a folder that you can write to and it's based on the name of your account. And then let's see.

We can do a clear command. OK. So let's run Postgres. That's just Linux.

Let's run Postgres. Let me show you one more thing before we go running Postgres. I'm going to go open up another tab of Files. This is super cool.

And so here is the text editor. One of the things you might want to do is type some of your SQL into files. This is the text editor. You see we're in our home folder.

You see a lot of files with dots. You see the folder that I made. You see a lot of files with dots. So I go into folder.

You see that, right? So we see I'm in the folder. I can go back up to my home folder. These dots are like configuration files and folders.

Virtual environments if you're doing Python. These are all files. Generally, leave these dot files around and you can see the README.txt that was placed there by them, by PythonAnywhere, when I got first set up. And then lesson1.sql, which is a file that, and I can edit the file and I can save it, okay?

And so I'm not going to do that. I'm just going to cancel it and leave. Yeah, I'll leave the page because I don't want to change it. So you can edit these files.

You can also edit the files in, oops, come back. Go away. You can use editors like nano or vi. I'm a vi person.

And so there we go. So you can edit these files, etc. Let's remember what's inside lesson1.sql because sometimes you might want to do your homework by editing a text file and putting your SQL into it, because you've got to do it over and over again. You make a little tiny mistake.

Sometimes I just like cut and paste from my desktop tool into the command line. But here we are. We're in Linux and now we're going to connect to Postgres. So I give you in pretty much every assignment I give you the Postgres command.

And so we'll just type it. That's got my account and my database. They're the same thing. You get exactly one account and one database and it's very limited.

And then you've got to type the password, but there is this convenient copy button which puts the password in a paste buffer. And I am now logged in. So there I am. Now I'm talking to Postgres.

I am running on a, this Postgres client is running in England and it's talking to a server that is in Amazon somewhere owned by the University of Michigan. Okay? So the commands you can type here depend on psql, that is the Postgres command-line client. Some of the commands are that start with a slash, for example, like the dt command.

That shows all the tables that you have. That's a psql command. If you're in a different client, you can't always type the dt command. But you can also type SELECT SQL commands, right?

SELECT star FROM, I always like to make my pg4e_debug. So it's going to give me all the rows from the table. Now, this is SQL. You end it with a semicolon and it's SQL.

And you're going to learn a lot SQL in this class because that's what this class is about. And there you go. And you see that SQL. You'll see later what the purpose of that is.

If you want to run from that file, you type slash i lesson1.sql. And you can run that. That says go run that SQL command or commands from lesson1.sql. And you can also press up arrow here as well and rerun the previous command.

And again, I'm not going to do the whole class here. I just wanted to show you how to get in. And now I'm going to show you how to get out. Backslash q.

Again, this i, this backslash i, the things that start with a backslash, those are psql commands. They are not SQL commands. This SELECT statement, no matter what client you're using, there'll be a way to send SQL. These are talking to the local client, okay?

And if you use some kind of a command line or a full screen, you will see that. So I type backslash q and then I am out of psql and back into Linux. Now, if I go back to Consoles, just leave here, I go back to Consoles, you'll see that I've got this console, so I'm not really logged out. And in the free account, you only get two consoles.

So you can come back and you will see when I come back to this console, I'm back where I started. If I want to actually exit out of the console, you can go back to Consoles and you can say get rid of it or from within the console you can type control D or you can type exit. And then it's logged out, so now it's gone. And if you come back here to Consoles, you will see you don't have any consoles.

So you'd start another one with Bash. And so again, thanks to the great folks at PythonAnywhere for giving us such a cool way to play with Linux and SQL for this class. And I hope you found this video useful. Cheers.
