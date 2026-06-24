# Building a Deno KV Model with Secondary Indexes

- **Course:** Database Architecture Scale Nosql Elasticsearch Postgresql
- **Module 3:** DenoKV
- **Lecture #:** 17
- **URL:** https://www.coursera.org/learn/database-architecture-scale-nosql-elasticsearch-postgresql/lecture/qwMdm/building-a-deno-kv-model-with-secondary-indexes
- **Extracted:** 2026-06-22 20:49:10

---

So now we want to talk a little bit about data model design in DinoKV and the constraints that the lack of a primary key, the lack of a foreign key, although we're going to kind of simulate that in a little bit, and the lack of integer primary keys and all that stuff is like, how do you model data when you don't have all those affordances that we have in SQL? So earlier we modeled this data in SQL or a version of this data in SQL. And so we want to model this, but within the limitations of the KV key patterns, right? The key patterns are, there are no explicit tables.

There's a hierarchical logical key. There's no integers. There's no primary keys. There's no foreign keys.

There's no serial increments. These are hierarchical JavaScript arrays. We can set, as we've seen, or get it, or we can do it by prefix. And the only order is the logical key order.

So we need to design all this stuff with these constraints in mind to accomplish what it is we want to accomplish with our application. Now I want to emphasize that Dino keys are arrays, even though you see me commonly concatenating things with slashes, that's just for convenience in parsing. These arrays, just like if you used Python tuples as dictionary keys, are sorted independently. So the first one is sorted, and the only time the second one is looked at, like preferences is sorted first, the only time the second one, eta in this example, is looked at is when there is multiple keys that have identical first values.

And again, this can go up to 4, 5, 6, 7, 8, 9, 10 things, but you get to control the sort order. So eta and preferences is very different than preferences and eta. So again, just because I use a slash syntax to represent these, they're sorted based on independence of the slashes. So remember, I had this thing where I said, look, if we could just use tuples, that'd be much closer.

If we had a dictionary with tuples as keys and dictionaries as values, it kind of would be there. And if Python could keep these sorted in key value as we inserted, it'd be good, right? And so if we were to sort that, if we had this such a thing, I'm doing this with sorting on the for loop at the end of the thing, so you can see how the tuples get sorted. All the authors come first, but within author, Barbeau, Oakley, Charles, Severance is B and C, they're in alphabetical order.

And again, you've got to realize that the top part that has the tuples is the right way to think about D, N, O, K, V, and the bottom part that has slashes is my convenience. So there we go. But Python doesn't have key sorted dictionaries. So if we take a look at a classic SQL model, and like I said, we did this earlier in the course where we take the vertical replication of things like the author has vertical replication and the language has vertical replication as well.

We would pull the language and the author out into different tables. And so we would basically make the ISBN be the logical key and we would have some primary keys for each book. We would have a primary key for each language, a primary key for each author. And then we would have foreign keys in the book table that would point to the authors and the languages.

So we would have no replication and we'd be using integers or maybe GUIDs, but GUIDs are just another sort of version of big integers. So that's a classic SQL model. And hopefully by this point in the course, that's like, yeah, of course, that's the way it's supposed to be. We don't get that.

We got to translate this to D, N, O, K, V. So we're going to do logical keys and logical keys. We're going to declare that the real logical key is ISBN. We want to be able to go query all the books in a language, we want to clear all the books in the author, et cetera, et cetera.

And we want to do this with secondary indexes. Remember, no foreign keys, no primary keys, no secondary indexes, just more logical keys. Okay, so in D, N, O, for each query that we want to truly be efficient, we're going to use a different initial prefix, right? Think of this as almost like a table, but D, N, O can optimize this any way it wants using B-trees, right?

Or B-trees or something even more sophisticated under the surface. We're going to assume that ISBN is the truly unique key that can look up and that secondary keys can have duplicates, which means that we can have, you know, lots of author Charles Severance books. And so we're going to create the concept of a foreign logical key by adding, in this case, the ISBN, the unique logical key to all the secondary keys or secondary key indexes, however you want to do it. So if you look, we actually have the real content about the book, and we're putting that in slash books slash ISBN and then the number, right?

And so that is kind of the real record. And we're going to create alternate indexes, books, title, introduction, networking. Now that is not guaranteed to be unique. Lots of people could write a book called Introduction to Networking.

I could even write a second book called Introduction to Networking, but they would have different ISBNs. So what I'm going to do is I'm going to add to that logical key the actual ISBN. And because this is kind of like a foreign logical key, I don't really even need to put any data there. Some people would put the content all the places, but I'm going to say, how about we just keep the content one place?

And then the open curly brace close curly brace is basically saying, look, this is really just an index, and I've got that value in there, the 978 yada yada. It's in the key. And I can look at slash books slash title, or I can look at slash books slash title slash Introduction to Networking and get back usually one, but perhaps several ISBNs with a single list operation. Same for author.

So books, author, Charles Severance is not guaranteed to be unique. And if you just do it, a set will overwrite it. But if I say books, author, Charles Severance, and the ISBN, that's guaranteed to be unique. And that really is just kind of almost a redirect.

I mean, someday, who knows, Dino may come up with this notion of a foreign logical key. I'm making it up right now as we go, okay? Same with books, language, English. I'm not sure how useful this is, but we could say, give me all the English books, and we'd get all the ISBNs for the English books.

So that's got an order by all built into it. It's got a where clause built into it, etc., etc., etc. So now you can do a KV list, and recall this matches multiple records that have a key prefix. It doesn't do an exact match, meaning that we're looking for the prefix of books slash author slash Charles Severance in this particular case.

But if there is just a record called books slash author slash Charles Severance, we're not going to see it. We're only going to see records that kind of live further down in the tree of keys than Charles Severance, which means all of the IS, and we're going to get a list of things that are all the ISBNs of books written by Charles Severance. So we got them sorted, we got quick look up, and away we go. And this little trick of empty thing as kind of foreign key.

Who knows if someone who knows more about Dino KV will tell me that's a dumb idea. It's just the idea I came up with. This whole thing is a bit of an emergent idea. And I'd be curious what you think about whether or not that's a great idea or a dumb idea, okay?

Well, a great idea or an idea that could be improved. So if we look and we do this in KV Admin, we're going to store a book under the ISBN and put the content under the ISBN. And then we're going to do a set. And if you look at my KV Admin, it's got this third parameter that you can have.

It's got no spaces, a little bit of JSON there. So I'm going to set books, title, introduction, and networking, and I need to get rid of the spaces. And so that's where the underscores come in. And the ISBN, and that's kind of my logical foreign key, foreign logical key maybe.

And then books authored Charles Severance in the ISBN, and books language English in the ISBN, and all curly braces. And now I can ask, show me all the books written by Charles Severance. Now, this retrieves not the books, but you'll notice because you get the key and the value from list. The actual data I'm interested in is sitting there as the fourth entry of the key, which means I can then go do a get slash books slash ISBN slash 97815 etc.

So we're going to play with this a little bit more and explore all this, the CRUD client and server, and look at code that's inside the CRUD client and the CRUD server in the code walkthrough. So I hope that this has been a useful exploration of one way of creating sort of foreign keys in a key value store that is backable by B-trees. I'd be curious what you think about it, and I'll also be curious if Dino comes up with best practices or if Dino codifies this, and it could, right? Because right now, if you use my foreign key, you've got to do a get of the foreign key, foreign logical key, then you've got to look at the foreign logical key and then grab the other one.

You could actually just do this in the server. And I could make my little server do foreign key, walk the foreign keys. I'm not going to do that for now. I'm really curious if this is even a good idea at all.

But it's really a good idea from the point of view of holy mackerel, all we have is logical keys, what are we going to do about it? Okay? Hope this helps. Hope this made you think, and hope that you enjoy the assignments that we've created for this particular module.

Cheers.
