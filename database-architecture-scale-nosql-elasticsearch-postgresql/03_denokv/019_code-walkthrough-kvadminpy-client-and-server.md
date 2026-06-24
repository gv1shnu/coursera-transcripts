# Code Walkthrough - KVAdmin.py Client and Server

- **Course:** Database Architecture Scale Nosql Elasticsearch Postgresql
- **Module 3:** DenoKV
- **Lecture #:** 19
- **URL:** https://www.coursera.org/learn/database-architecture-scale-nosql-elasticsearch-postgresql/lecture/VvrCP/code-walkthrough-kvadmin-py-client-and-server
- **Extracted:** 2026-06-22 20:49:32

---

Hello, and welcome to another code walk through for Postgres for everybody. In this code, we're going to walk through both the client and the server code for my KV Admin tool that I have you install as part of your activity in this course. This is in github.com/csev/deno-kv-admin. Let me go to the ReadMe here.

The ReadMe in this repo is All Instructions. I've done this already in another video, so you should watch that video first. It tells you how to install both the server side of the admin and the client side of the admin. What I want to do here, let me go into the command line, is I want to build a tool that's like the PSQL or the MySQL client, where you can connect to a database and then type commands into that database.

There's a database here and we don't have a protocol. There is a KV protocol, but it's just easier for me to build a little web service endpoint so I can show it all to you. I will point out right away that KV is in absolute beta right now. By the time you're watching this, it could be beyond beta and in way better shape, but for now, it's fun to play with it at the beginning, and it gives me the opportunity to build this little PG admin tool and explore the underlying thing.

There's been a couple of open source admin, like phpMyAdmin. Thanks for KV, but the vector of the code is moving so rapidly that those things go out of date too fast. That's why we just have to build one. When you're done with that install process, in Deno dashboard you should have an instance.

That instance will have all that code, and you can see the logs, you can see the KV data. I would hope that one of these days, they're going to build a complete admin tool to set, delete, query everything. I don't understand why there's not an admin tool here already, but there isn't. That gives us an excuse to write one.

Here's the admin tool that I wrote, it's called kvadmin.py. You download that, you download this hidden.py file and you put your information in here, and then this KV admin talks to yours. When it first starts up, it verifies the connection, and if it doesn't, it tells you how to start it up or maybe you misconfigured it, but it's working. I just made a series of commands.

These are insert, select, delete, update. This is a command line interface via web services to a KV data store. Let's just take a look at the KV data store on Lazy Wolf, and I'm going to say set/hello/there is the key, and then I'm going to put in a little bit of JavaScript, a JavaScript object. Let's do it on two lines.

Then I can say, name, pg4e. You can send any JSON to this thing so long as it's valid. Let's see if I got it valid. There it goes.

Now, at some point, we can look in this and there is a new key. Hello there. I put that in. Now, let's trace that all the way through.

I'll go through all these things. The sampled command, if you type samples, it will give you some sampled JSON because it's hard to type it. Set and get are the primitives, like insert and select. I wish they called set put because I'm a Python person, and I'm, oh, it's got to be a put.

In most key values, in most languages, it's put and get, not set and get, but I get why they say set and get. I just ran a set. Now, what happens in this Python code, let's take a look at what happens in the kvadmin.py. Here's the code.

Let's look at set. There we go. This is the code for set, and it's pretty simple. It has broken the line into two lines.

It's using blanks, and so sometimes I can put stuff there. If I say set /second/thing, if I can type my JSON with no spaces, x:y, it will see that second parameter. Can't be any spaces here. That's my thing.

You can fix it if you want, but I made it so that just split that on spaces. That's going to send the JSON document second thing, x:y. If you look at the code for kv.admin, it splits that command into two pieces. If there's greater than equal to two pieces, and the first one is set, then what it does is it takes the second piece, which is /kv, here we go, /books/Hamlet.

That is pieces sub one. It's going to have the URL, which is not supposed to have a trailing space. /kv/set, that's going to make a URL, then book/hamlet, and then it just adds the token. It's fiddling around.

Now it's prompting for the JSON unless the JSON was on the command line. Text equals pieces sub zero or text equals readjson. Then we're going to parse it to make sure it's valid. If it doesn't parse right, readjson has a bunch of error checking, so that's cool.

But if data is none, we're going to continue, and then we're going to dump it just for debugging. If we're going to set the content type because we're going to post this, we print the URL out, and then we do a post request, just the headers and that JSON body. We give ourselves 30 seconds. Part of the 30 seconds is because it can take time to cold start the server.

Then we get the status, and we print it out. If things go wrong we get all kinds of tracebacks and stuff. You could clean this code up a lot, but I wanted to keep it simple so it could all be on one page to read. You can see that for the set, it went and constructed that URL lazy-wolf-17.deno.dev/kv/set/hello/there?token=42, and then the actual JSON is in the post body.

Let's take a look at what happens in the server. If we take a look at our code, this is the code running, it was installed from GitHub in the previous video. This is using a framework called Hono, and Hono is one of the many frameworks. Deno is really JavaScript, and then you still have to have a web serving, just like Python is a language.

Python anywhere runs Python online, and Django is a framework, so you got to decide, I'm going to run Django inside Python anywhere, and se're going to run a Hono inside Deno Deploy. This line here, const kv = await Deno.openKv(), that line is the coolest line of all because if you've done this in Postgres, you know that you need a URL on ID and a password. The key thing is this is running in the context of the app lazy-wolf-17, which means there's a database in the context of lazy-wolf-17. Here we are looking at the KV database in lazy-wolf-17.

Why would you even need a password? You're already in the application. Now, you can put parameters on here, but in this case, it's just, open the database that is associated with this running application, and the basic database connection here in JavaScript is in the variable KV, and we're going to use it. Now let's take a look at the server side code.

It's coming in /set. Actually, that's really /kv/set. I got to fix that. I'll fix that in the source code after this video, but that documentation is wrong because the real URL is /kv/set, and then the key is the next parameters but that's okay.

It's right here in the code. It's just not right in that comment. Which I'll fix that. You can go back and see that later.

We grab the key, and this says app post, and you'll see that there's a whole series of these are K statement, and there's a router eventually. Deno.serve is a router that picks based on the URL to run this code sequence and request data comes in in the variable c. We're saying we route to us paths that start with /kv/set/, and then this:key says, give me the rest of the path, whatever it is, like set/books/Hamlet, give that to me in the parameter key. First, we check the token, and that's a little bit of code that checks to see if whatever this number is right, and it throws exception and sends a 401 back if the token's not right.

It just continues on if the token is right. We grab the key off of the URL. I got a console log. Let's go find the console log.

Let's take a look at the logs. Come on, log. What? How come the log's not right?

Let's go to this URL and see if we can't wake the logs up. I don't quite understand why the logs are not there. Logs here. Wait, I know what I did.

I have not yet deployed this. Come back, or have I deployed this? Console.log path key. It's been deployed.

I see, here's the log right here. Let's run it again and make sure the log is working. Let's just re-run this second thing one here. Did the log come out?

Dang it. I just closed it. There we go. I'll open the KV store up again.

You can see, finally, I get this console log. The first console log is path is the key is second/thing. That is parsing the URL and it's parsing the key, which I've serialized this with a slash because it's just a little easier, but the real key is an array. It's a hierarchical array, second thing.

If we go look at the documentation, it's probably time to start talking to the documentation here. We're doing this kv.set code. This is at docs.deno.com/deploy/kv/manual/. You see in this little set section that we're opening the KV, we're creating prefs as a object with keys and values, and then we're going to do a kv.set with an array that has two strings in it, preferences and ada.

Now, again, these are hierarchical, and then with the second parameter is the JSON object in this case, the JavaScript object, and that's what's being stored. That's the code that we are basically running here. I'm showing the key, undo, I'm showing the key, then I am splitting the key, and I'm showing the array and then passing in the array and the body, and that is it. Then we get a result back.

If you look at the result, it's like the timestamp and the fact that it was successful. I'm not really checking the result, I'm just showing you the result here. That is what's going on as we are going a full web service call. Let's say get/second/thing, and there we go.

You'll notice that every get request includes the key and the value. You'll see later that sometimes we just store a key and keep data in the key. Sometimes the values even empty, but in this case, the value is x maps to y andew're calling /kv/get/second/thing. That is going to route to this much simpler request, which is anything that has a prefix of /kv/get/ route to this code, and give me the rest of the key.

All we do is we check the token, we grab the key value, we split the key into an array because that's what we have to talk to KV is an array, and then we get it, and we send back the result. That's the result that comes back right here, it's a JSON object with a key and a value. That's pretty simple. Let's go to the KV quick start, and you see how a get works, const entry = await kv.get("preferences", "ada").

Again, you're getting it with a JavaScript array. This is a select, you could think of the get as a select with a primary key. It's all a logical key here, but it's got to be an exact match but you can do a prefix. This is more like a select where something equals, not instead of just a key, but it's like a prefix.

We'll skip the get many. The one I really want to look at is the KV list. You pass in a prefix of preferences. I'm going to show you that in the KV admin.

I'll clear it. List/second, is that going to work? Yeah. List/second says I want a array of records.

You'll see that the records here is an array, and anything that starts with /second give it back to me. You see that it's their second thing and x:y. Let's set another thing, /second/bob. Let's put an empty thing in there, empty value inside of /second/bob and now I can say list/second.

You will see there are two. We're told the key in each of the records, it's an array of records. By the way, there is a whole mechanism for paging that we're not going to play with too much. This cursor thing right here is the paging.

You pass the cursor back in on the successive things, if you have thousands and you get the first hundred, cursor is the way that you move through it. But you see, there's a key, there's second bob that's got a value of nothing, an empty object, which is different than null, and /second/thing with a key of x and y. That's the list. If we take a look at the code for list, all we do is we take the key, and we got this cursor support if we pass in the parameter, cursor, if there's more than whenever.

I don't have that working in the admin client, but it splits the key and then passes the cursor in if it really wanted to do it, and then loops through it and sends back the records. The cursor, as well, it sends back the records and the cursor if there was more than the limit of 100. I've got a const extra = ('limit':100), which says it'll only give the first hundred, but in my example, I'm only doing two. You'll see this over and over again.

Let's go see the Python. Let's go look at the Python for delete. We're going to do delete/books/Hamlet. The delete_prefix works.

I'll do this delete_prefix as well. Here we go. It's going to create a URL that looks like kv/delete or delete prefixes, and then the key and then the token. Let's go ahead and say delete/second/bob.

We can say list/second. We see that it was deleted. Because Hono makes this so easy, the delete code in the server simply routes the prefix, then grabs the rest of it, then splits the rest of it and calls the delete method. You'll notice we're sending an HTTP delete, not a post, not a get.

It's an HTTP delete. Then delete prefix is a little trickier. I'll just say delete_prefix/second. While there are no tables in a Deno KV, we often treat this first piece of the key as the table.

It'll often be called users or whatever. I'm going to delete_prefix/second. It's going to go through and grab second, and it calls kv.list with a prefix just like the list operation, splits the key. It could be more than one thing, but it has to be a prefix.

Then it basically loops through those things that it got and then it deletes them, and then it remembers them, and then it sends a nice console log, see if I can see that console log, sends a nice console log that says what we just deleted. We deleted one key with the prefix second, and if we go back here, you will see that it returned the keys that it deleted. If we do now list/second, there are no records, and that's okay. We can say list/xyz.

There are no records under the key xyz, but it's not a failure to ask the question. It's like a select, and the select gives you nothing back. Let's go back. We already talked about the delete.

The delete is a direct key. It's got a match. It's not a prefix. I used the list and delete to accomplish my delete_prefix.

I think we mostly covered everything that I've got going here. I got a full_reset_42, which allows me to wipe them all out, but I don't have a command inside the PG admin to do that. This actually doesn't check for a key. It just dumps everything.

Then we have some error work that's going to return the 401 for the bad exception, and then we have a code that you're supposed to change, which is the check token code, and you're supposed to change the token when you get to your auto grader, it'll make you put in a different token, and then you have a cron here. I've already changed it. This cron is going to do once a month rather than once an hour. Some of my other stuff maybe be once an hour, but this one, lazy-wolf-17 won't exist by the time that you get there.

That is a quick walk through of the JavaScript side of this, which I think is beautiful and simple and elegant and the Python side of this. You know Python. You can walk through this stuff, and it's not that much stuff. It's 200 lines of code on the client, and it is 157 lines on the server is JavaScript.

You have to know JavaScript, but it's not that hard. Use curly braces, and after a while, you're cutting and pasting things. I'm not going to ask you to write a bunch of JavaScript. I'm just asking you to understand enough JavaScript so you can play with this, deploy your own from my code, and get it working.

I think that's about the end of our little walk through for Postgres for everybody. I hope this was helpful, and I hope that you enjoy playing with Deno KV. Cheers.
