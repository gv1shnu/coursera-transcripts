# Exploring CRUD in Deno KV Using KVAdmin.py

- **Course:** Database Architecture Scale Nosql Elasticsearch Postgresql
- **Module 3:** DenoKV
- **Lecture #:** 16
- **URL:** https://www.coursera.org/learn/database-architecture-scale-nosql-elasticsearch-postgresql/lecture/pJOhv/exploring-crud-in-deno-kv-using-kvadmin-py
- **Extracted:** 2026-06-22 20:48:59

---

So now, I want to talk a little bit about the Python code and its corresponding server code that I called kvadmin.py that we're going to use to kind of code the closest bit of code that we're going to do to be reading and writing this database. Now, here's the thing that leads me to this kvadmin. There is no pgadmin, no dbeaver, no phpMyAdmin. There is not a built-in.

Again, I don't understand why. This probably will change in a week. They'll release one. But for now, as of this recording, there is no administration tool except a way to read data.

That's it. There's no command line tool like pg or MySQL. And all you can do is go into your KV dashboard and look at the data. You can't insert data.

You can't delete data. It would be so easy for them to write this. And it turns out that over, there's a dno1 and a dno2. People started writing admin tools because it's just a reasonable thing to do.

But then dno changed so much between 1 and 2 that all those admin tools were stranded. And people just are waiting for dno to do it. And by the time you're doing this, you may be able to just use a dno admin tool, which is great. I just hope dno puts it into dno rather than us having to go download another dependency.

That's not the dno way. The dno way is the basic stuff should be in dno. So let's hope that dno builds a simple admin tool and renders this sort of obsolete except as a programming exercise. And I love to build these little admin tools in a way to show how so I can write an end-to-end piece of code.

So what we're going to do is a piece of Python code is going to run on your computer that's going to log in to the dnoKV and send web services back and forth. So the actual admin tool is a Python bit of code. And the dnoKV is some JavaScript code that receives web services with the token that receives web services and writes the dnoKV. There are some Python dnoKV client libraries, but they seem really hard to get started.

And so just what the heck, let's write our own little JavaScript. We can look at the JavaScript. Let's write our own little Python. Let's write our own little web service protocol.

And then let's just write it all and then examine it all. So that's what we're doing here. So we're going to write a dno web server. And I'm going to use a framework called Hono.

There's a bunch of them. Dno has its own one called Fresh. I just looked at a bunch of sample code, and I thought this spoke to me better. And so what Hono is is Hono turns a generic Python runtime into something that listens on a port and then routes requests to controllers.

And so we import from an online place, dno.land. That's the official dependency place. So we say const app equals new Hono. And that's creating a giant piece of software and object that is the Hono server.

And then we add routes to that. We're saying if we receive a get request that has a prefix of slash hello, we are going to call a function, that async, open paren, c, close paren. That's short and the little arrow and the curly brace. That's short for like an anonymous function passing in the parameter c.

And so the code for that anonymous function passing in the parameter c is inside the curly braces. And so we're just not even going to look at the incoming data. We're going to create a JavaScript object, answer colon world. That's a key value inside of JavaScript.

And then we're going to send back a JSON response to the browser. Now we've registered that. And then to listen for incoming requests, we have to say dno.serve app.fetch. And so away we go.

So once that's running, and I've got it running on hono.pgfree.com, you can say HTTPS HONO.PGFREE.COM slash hello. And it will run that code. Probably take a while for it to start, because I'm using the free one there for HONO.PGFREE.COM. That's a DNO application.

You say hello, and it says world in JSON. Now just here you see it, the technical difference between JSON and JavaScript objects. In const result equals answer world, you'll notice that answer does not have double quotes in it. But if you look at the response from the HONO.PGFREE.COM, the quote answer quote is the key.

And so JSON is a kind of subset of JavaScript objects where the keys are supposed to be explicit strings, not just unstringified text. So that's the difference between JavaScript objects and JSON. Now let's jump into our client code. This kvadmin.py, you run kvadmin.py on your computer, whether it's a Windows or Mac.

And you've got install instructions and a walkthrough for this. You run it, and then it's just a series of commands like pg. So samples is a way to dump out some sample JSON so you don't have to do it all the time. It has a set command, and you give the set command the key in my little slash syntax.

It's really a JavaScript array that's first one is book, second one's Hamlet. It's easiest for parsing, and you've got to put it on a web service request. And so we might as well just start with this kind of serialized version of this array. And then it asks, well, this is going to be a POST request to a URL that includes some JSON, which is the key value pairs that are inside of this JSON object.

The language is Old Anglican, and it's William Shakespeare. It's Hamlet. And we'll give it the ISBN of 42. And so that POST to that URL that's shown with a token.

And that token ensures that you have to know the security password in order to store data. And you get back from that OK true and version timestamp. And the version timestamp, again, I'm not going to go into that in too much detail, but the version timestamp is part of its eventual consistency. If two sets start racing, then it uses the version timestamp to resolve the sets which happen.

It has to order those. And one of them has to win. So it's OK for two sets to simultaneously race to an eventual consistent database, but one of them has to win. You can't have a situation where after it's all settled down, you are doing get from one server, and it's a different value than the get from another server.

And so the version timestamp is telling you which set won. You can do a get, again, with the book slash Hamlet. And that creates another URL, slash kv, slash get, slash book, slash Hamlet with a token. And then it goes and retrieves that JSON blob for you.

And it gives you both the key and the value, which you're going to see. We're going to make good use of that. And it also tells you the version timestamp. And so that would be a way for you to check to see if the data you set into the database is the data that was eventually there, because you could look at that version timestamp and say, yep, after it all settled down, I do a get.

And that's the version. The version timestamp is the one that I got when I did a set. So now let's talk about what's going on in the server. Now, if you recall, we already looked at a really simple kv server, so we sort of know what HONO is.

And we know about application route, so we know about dno.serve. The next line, const kv equals await dno.openkv, that's the magic, right? That's the cool thing that we're in an application, whatever the name of our application is. Like mine is called kvadminapi.pgfree.com.

But there's a database for it, and I don't have to make the database. It's just always there, and I don't have to have security to connect to it, because if I'm in this application, that's my database. Wonderful. And so we just take a look at the routing.

It's app.get slash kv slash get. And then the rest of it is the key. And the key is just a string. And it's going to call an async function, pass the request data in as C.

And we're going to check the token. And that's just looking for the key, whether it's 42 and whether it matches the code in check token. And the install instructions tell you to mess with check token so that you can set your key to not to be something other than 42. And the check token is going to throw an error, an exception that will give a 401 if the token is wrong, to say you're not authorized.

So check token either works and comes back, or it sends a 401 back to the browser, or whatever it's calling it. Then it pulls the rest of the path, const c.rec.param key. That is the rest of the path, which is books slash Hamlet. And then I split that.

And then that becomes an array, which is a two-entry array with books and Hamlet as the first two entries. And then we're going to do an await, because that's a time thing. You're going to have to talk to the database. That's going to take a jillionth of a second or something.

Do a kvget of the split key, which turns it into that array. And then take the result and send it back to the browser in JSON. So now let's take a look at what's equivalent to kind of the SQL select, which is list. List slash books.

Now, this is a prefix. So it's any key that starts with books. Now, it doesn't give you the exact key books, but it's slash books slash something. And that turns into a simple web service request, kv slash list slash books token equals 42, which we then send to the server.

And it retrieves the book that we're looking for, which is the Hamlet book. Now, you'll notice the records now is an array. We only have one of them. But if you had a bunch of them, you could have many, many key value pairs in this array.

But it gives you back the key and the value, because you don't know what the key is, because you just said, give me all the keys that start with books. And away you go. And you get the time stamp. But you also get this thing, if you're doing paging, like limit, a limit clause in SQL, the cursor is sort of the limit clause.

And there is a limit clause for this as well. And if you want to do repeated lists, where you want to take 50 and next 50, next 50, there's a mechanism for that. And the cursor that you see there at the bottom, that's what makes that part work. So just to finish our crud up, we can say delete slash books slash hamlet.

And we're going to send a HTTP delete request, which is like a get and a post and a put. HTTP delete request to slash kv slash delete books hamlet token equals 42. And that will delete it. We just get a status of 200 for that that says I did it.

And then if you do list slash books, you will see that there are no records anymore. The records is an empty array, because we just got done deleting slash books slash hamlets. And so this is a real quick overview. I've got a code walkthrough that walks through both the client and the server code.

And we'll go through this in a lot more detail rather than just putting it on slides. So I hope that you found this useful. Cheers.
