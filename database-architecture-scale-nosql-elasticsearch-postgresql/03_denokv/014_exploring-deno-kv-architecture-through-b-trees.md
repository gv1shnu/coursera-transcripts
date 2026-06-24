# Exploring Deno KV Architecture Through B-Trees

- **Course:** Database Architecture Scale Nosql Elasticsearch Postgresql
- **Module 3:** DenoKV
- **Lecture #:** 14
- **URL:** https://www.coursera.org/learn/database-architecture-scale-nosql-elasticsearch-postgresql/lecture/CSBZb/exploring-deno-kv-architecture-through-b-trees
- **Extracted:** 2026-06-22 20:48:38

---

So now let's talk about the Deno KV database architecture at sort of the high level. It's really because we're in a database class and we're thinking about different kinds of architectures, ACID and base architectures, we just want to take a look at this to better understand base architectures. Now I'm not really going to describe to you the actual Deno architecture at the low level. The super scalable Deno KV is built on FoundationDB, which is an Apple product.

And you can go into AI or Google and you can say FoundationDB technical overview, like I did, and you can look at it and you'll probably be bored to death after about five minutes because it's really complex. But it's worth a look to see kind of the basic ideas of distributed consistency, right? Eventual consistency is what they're talking to you about when they're talking about FoundationDB's technical overview. And so I'm going to give you sort of a very light version that's not even intended to be accurate.

It's intended to explore the notion of why it is that Deno has chosen its KV features. So the key thing is, like a lot of NoSQL things, it organizes schemaless JSON documents. It has no tables. It just uses keys.

It has a hierarchical logical key. It doesn't have auto increment integers. It doesn't have auto assigned GUIDs or serial primary keys. All ways that we generate primary keys.

You can generate primary keys kind of in the server using a software GUID style primary keys and then store them. But the database really doesn't care. It doesn't support them directly. Logical keys are JavaScript arrays.

And you can store under one logical key, one database, and then retrieve that back by key. You got to know the key. You got to set it or get it. It's a logical key, right?

Logical key is something we're supposed to know outside of the database. Data can be scanned by logical key prefix using list. That's kind of like select. And the only sort order you got, there's no order by in here.

The only sort order you get is logical key order. And it's kind of like a B-tree in Postgres SQL. And so elsewhere in this class, we've used this as a sample data to model. It's some books and some titles, ISBN, language, and authors.

And we'll do some modeling later. I like to think of Deno's KV as sorted dictionaries. Like imagine that dictionaries were always sorted. Always sorted by key.

So you could put something in. But then if you made the key be a tuple, like a to tuple, which is books, wizard, up late, then that's sortable because tuples in Python are not modifiable. And so they're also sortable and they're comparable. Now they're compared by looking at the first element of the tuple, and then when there's a match there at the second element.

And it's not just one. You could have five tuples or eight tuples or nine tuples. A dictionary where the key is a multi-entry tuple and the value is a dictionary. And if we were to do this and fill this dictionary up, but it was to stay in order by the tuple, and you'll kind of see the Python down there.

I mean, if you print it out, you see it in insert order. But then if we sorted it, then it comes out in sorted order. Now, it would look like this, right? So sorted order would bring all the authors together.

The author is Barb Oakley, author is Charles Severance, author is James. You notice that those are all sorted. That would be cool if Python would maintain that. Now, the interesting thing is that there are libraries in other languages like Java tree maps that do this kind of thing for you automatically that use trees internally.

Now, you'll notice when you start seeing me, I'm going to simplify the serialization of these tuples as like slash author slash Barb Oakley or slash author slash Charles Severance, just because it's easier to read than the JavaScript array. Python doesn't do this, right? Other languages do. Using tree maps in Java is a good example of doing this.

And so it turns out that all of the rules can be met by a B-tree. A B-tree is a logical key index, and we use them in SQL all the time. It's a type of index. There's other kinds of indexes, but B-tree is a very, very common index because it grows slowly, it gives us logarithmic time to find records, and it can be expanded.

And what's cool about B-trees is if you think about it for a while. So let's just talk about B-trees for a while. The idea of a B-tree is there are blocks of keys, and these blocks are of fixed size and they're stored on disk. And if you're looking for a key like 9, there's a root block.

You grab it and you start looking, and that top one that's got 7 and 16 in it, that shows you where all the keys are. There's four total blocks, and we know exactly where 7 and 16 are, but we do know that anything between 7 and 16 is in the middle block, anything below 7 is the far left block, and anything above 16 is in the far right block. And of course these trees get a lot deeper. So you just go in and you're saying, I'm looking for 9.

So you go to 7, and you go to the right of 7, and then you find the 9, and you're done. Now if you're looking for 10, 10 doesn't exist. And so this is the simplest B-tree picture. They get a lot more complex, but I don't want to try to represent that on a slide.

Now, DinoKV is likely some variation of a single large B-tree structure spread across all the deploy nodes at data centers around the world with some kind of backing storage to make it moderately permanent. And they're all connected to a low latency network that coordinate with each other. So you can insert a record on any of the 100 nodes, and eventually that record will be viewable by all the other nodes. And that's what eventual consistency is.

So let's take a look at a 3-node DinoKV instance. So we've got 3 nodes, actually 100 nodes, right? But what we do is we replicate that top node in all of the deploy instances. And then the other nodes are not just pointers to disk blocks on the same server.

They can be pointers to disk blocks on another server. So the pointer is really which server and which disk blocks. Now, there's going to be redundancy. Don't worry about that.

Let's just kind of think about this. And so you see these links, the links themselves are not particularly important, but you see that we've got the original 4 blocks, the root block is replicated, and the 3 other blocks just happen to be in 3 different nodes, but no matter where you start. So if you're looking at, like, give me record 1, the server 1, it finds it on the same server. And if you say get record 6 on the second server, it finds it on the first server because it follows these cross-server links to find disk blocks on faraway servers.

And the same for, like, if you're on the 100th server and you say get slash 12, it's like I go find where that's at. Oh, that's on server 2. And then it goes to read the disk block off of server 2. So it works pretty good if you can replicate those root nodes across it.

And again, this is way simpler than the real world. Okay, so let's insert a new one, a set operation, okay? And we're going to set number 4. And we're talking to server number 2.

So server number 2 has a map, a sufficient map to find where record 4 exists. If record 4 exists and is already there, it just replaces the JSON document. But let's say it doesn't exist. So it finds its way onto the right disk index on server 1.

And it finds the right place on that index. And it goes like, oh, wait, this one's full because they can only have 4, right? There's some finite size of these blocks. And they run out of space.

And so what you have to do is you have to split the block. This one happens to be in the middle. 4 doesn't have to be in the middle. What you take is you take the middle one and you move it up.

So you can see that we have split the original 1, 2, 5, 6 block into a 1, 2 block, which is 50% full, and a 5, 6 block. And then inserted the 4 in the right place in the root node on deploy server 1. At this moment in time, the other servers don't know about it. So server 1 has correctly inserted record 4.

But the others don't know about it. The problem is while server 2 is in the middle of a set, server 1 can do a get of 4. And it gets the right answer. But server 100 does a get of 4.

And its view of the universe goes and looks. And you'll notice that I've got two copies of the block in server 1. I haven't gotten rid of the old 1, 2, 5, 6 block yet. And server 100, looking for 4, sees it's not there.

It's behind the times, like a third of a second behind the times. Eventual consistency means that eventually we'll see the right thing. But it doesn't have to see the right thing. If this were ACID, it would see the right thing already.

But we're sort of sitting here a third of a second into the set operation. And it's inconsistent. But if you happen to be doing the same thing on server 1, you get record 4. That's inconsistent.

But all we need is eventual consistency. It's either there or it's not there. And eventually it's there for all of them. Okay?

So now we're finishing up that third of a second. And so what happens now is in that third of a second, the new root node, 4716, is copied to all the servers. And then we kind of clean things up in server 1. We get rid of the old root node.

We get rid of the old full index. And now we update all the pointers. And so anybody at this point now can do a get of 4. And they find it, right?

Because they have a new root node. And that all happened in a third of a second. And so I made this as simple as possible to give you a sense of how in a third of a second eventually consistency could happen. And to some degree, how B-trees could be like the path.

They're such a natural thing because they have all these independent areas. You can have kind of multiple trees. You can have trees that are half finished or two ways to get to the same place. And it all works.

And for that one third of a second that it's inconsistent, it's okay. It just keeps working, right? But you can also see why looking at those pictures, there's no way to have an integer auto increment to make a primary key, right? Those are strings.

That's why they're called 0, 1, and 0, 4. It's just not reliable. You can't increment one place in a distributed system. This needs to be distributed because there could be thousands of those.

Now you can go Google this or do AI. There's a thing called a ULID, University Unique Lexigraphically Sortable Identifier, which is a special B-tree friendly GUID that kind of sorts, right? And it's kind of based on time and randomness and server name. GUIDs are sort of time and randomness and server name.

But the ULID kind of orders that stuff so that they kind of fill the B-tree up nicely and split nicely and are nice from a B-tree and distributed B-tree standpoint. So up next, we're going to start moving into the Deno server. And to do that, you have to learn JavaScript. So my next lecture is titled, it's very short, and it's titled JavaScript in Three Slides.
