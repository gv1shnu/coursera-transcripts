# Code Walkthrough: Installing KVAdmin.py Client and Server on Deno Deploy

- **Course:** Database Architecture Scale Nosql Elasticsearch Postgresql
- **Module 3:** DenoKV
- **Lecture #:** 18
- **URL:** https://www.coursera.org/learn/database-architecture-scale-nosql-elasticsearch-postgresql/lecture/Ojz78/code-walkthrough-installing-kvadmin-py-client-and-server-on-deno-deploy
- **Extracted:** 2026-06-22 20:49:21

---

Hello, and welcome to a code walkthrough for PostgreSQL everybody. Code walkthrough that I'm going to be doing right now is really the install process for setting up the deno-kv-admin. This is really two parts. As described in the lectures, this kv-admin is going to be a Python application that uses web services to talk to JavaScript application running on Deno Deploy.

I'm going to give you the JavaScript application. You don't have to learn too much JavaScript. You have to look at it and read it and understand it and have a really short lecture on how to do JavaScript. The first thing you need to do is you need to make a Deno Deploy account.

It's 100% free. Don't worry about it. Just go to dash.deno.com. Now I'm already logged in.

I'm set up, but this is just a free account. I'm just using a free account both for my reference implementation of a couple of things that I've got going. I don't think I'll have to pay for it. The things you're going to do to this shouldn't overwhelm my traffic.

I've got this setup, and so we'll start following instructions. We're going to go to the Deploy dashboard. In the overview section, we're going to do New Playground, and it's going to create a playground for us. What's a playground?

Playground is just a really tiny deployment. You're going to get a URL. This one is called lazy-wolf-17. This is a new URL.

At this point, I now have a global web page called lazy-wolf-17.deno.dev. I could do all cool stuff with this. But well, what I want you to do, is I want you to install code that I am giving you. I just select it all.

I'm going to copy this code in the main.ts in this same GitHub repo, the main.ts is just one file. This is all JavaScript. We'll cover this later. The things that you need to work on are the things at the end.

There's a cron job that I use in mine because this is also my reference implementation. If you change this cron string as described, it means that it'll clear the data only once a month rather than once every hour. Cron is a Unix concept that's also there in Deno. The other thing is this checkToken.

Most of the rest of this, you're not going to have to change. Now we're going to save it and deploy. This is going to take 15 seconds or so, and it just put it out on 32 Deno servers around the world. Now, this is the new version.

I just upgraded this. You'll notice that that lazy-wolf.deno.dev doesn't say hello world anymore. It says 404 Not Found. But if you say /dump, which is one of the URLs this application handles, it dumps all the request data.

We now have a running server at lazy-wolf-17. We just did that, except ours is called lazy-wolf-17, and we got a 404 Not Found. We did a dump, and it's like, "There we go." We could look for data with kv/list/books to see if there's anything in data, kv/list/books? token.

We know what the token is. It's 42, and there are no records in there. You could verify this same thing by quickly going into the KV viewer and looking at data. By the time you're doing this, this UA may be changed.

I don't quite understand why they don't have a way to insert the data, but all they can do is browse the data. We'll come back to this in a second. Let's go back to our lazy-wolf playground. There's our lazy-wolf playground.

This is where we edit it. We're not going to do much to edit it right now. We verified that. Now we're going to do another thing.

We're going to install some code on our laptop. I'm going to open this in a new tab, and open this in a new tab. These are just flat files. I'm going to save this file, Save Page As.

I'm going to have this in a csev desktop code folder. Save that. Then this hidden-dist.py. I'm going to save that.

Except I'm also going to rename it because kv-admin wants this to be called hidden.py. I'm going to close these tabs because I've got these down there. Let's go into here. If I look and I do a pwd print working directory, ls, I got two files.

It told us to download these. Then it says copy hidden-dist.py, and then edit this hidden file. I'm going to edit the hidden file. There's a Deno section to it.

Instead of using my reference implementation, let's put your URL, which is without the slash, it's lazy-wolf-17.deno.dev. That's the instruction to copy it. Now we're going to talk to deno-kv. I don't really need that tab anymore.

We'll get out of here. I'm going to say python3. I'm going to Macintosh. You could say Python kvadmin.py.

The first thing it does is, it checks to see if it can ping using that dump. The dump doesn't take a token, so it can always check to see if the server's name is right, and it does. If it complains, you'll see it with a message like this. It will say, "Unable to communicate with Deno.

Sometimes it takes a while to start the Deno instance after it's been idle. You might want to access the URL in a browser, wait 30 seconds, and then restart kvadmin." You just go to your terminal, and you can go to this URL, which we already did, and it wakes it up. Right now because we're in the playground, it's alive and it's running. But sometimes if you left it for a while, it takes a while for it to come back.

That's called cold starting. Now we are talking to your lazy-wolf-17. Remember, this kvadmin is like phpMyAdmin or PSQL. It's a command line way to talk to these systems.

I'll just type help to see what we've got. There's a number of things. There's some samples. This works with JSON documents.

Here's just some JSON documents based on some books that we've been playing within this course. Set and get are the store. Set /books/Hamlet. Then we can just grab some JSON.

Don't grab it all. That's just one of them. This worked. That means that we posted.

We sent it with a token. We did all that stuff. Let's really go quickly here. Let's go back to lazy-wolf-17 and look at the KV and look at the data in the KV, and boom.

Now, the lecture talks about this. The real key in KV, there's no tables, but we tend to use that first key as a books table, as it were, but it's really just a first key in a hierarchical key. The real key is JavaScript array. I just happened for my own craziness.

I treat this books/Hamlet because I got to put it on a URL, and then parse it and turn it back into a JavaScript array. Will cover all that stuff later. You see that we've stored something, and you have all these commands like I can do a list of/books, which is almost like select star from books, and so there were records that had books. That's pretty much all I wanted to cover in this little video, and that is how to install a bit of code, and I'll walkthrough all this code, and I will walkthrough all the KV admin code in separate videos.

I hope that this helps you get things started because you probably want to install this stuff before you watch my walkthrough videos so that you can actually look at the code that you're really running. Hope this helps. Cheers.
