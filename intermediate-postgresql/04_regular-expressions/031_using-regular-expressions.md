# Using Regular Expressions

- **Course:** Intermediate Postgresql
- **Module 4:** Regular Expressions
- **Lecture #:** 31
- **URL:** https://www.coursera.org/learn/intermediate-postgresql/lecture/l35ER/using-regular-expressions
- **Extracted:** 2026-06-22 20:29:33

---

We just got done using where clauses and regular expressions to pick which rows to show. Now, what we're going to do is we're going to actually do stuff with the columns that come back from those rows, so we're actually parsing the results. Now, in general, if you just need the whole column, you just select email and away you go, but basically, we can then also use regular expressions to parse the columns. If we take a look at this first thing, we see we're going to select substring of email, and so this can be select email.

Here's a where clause, just like we did before. But basically, what we're going to do here is we're going to actually pull out those digits. This is read that email address and find zero through nine, which is digits, so that bracket zero through nine is a digit and then we have this plus. Now this plus is a modifier that modifies that, and that's one or more.

If you put a star, there'd be zero or more which would match everything because zero or more digits is everywhere. Plus means one or more digits. But it also is going to be greedy in that it's one or more contiguous digits. If there were like a string that had like one, two and a string that had three, four and a string that had five, six, it would get the first one.

We'll talk in a second how you get the second one, but in this case, it gets the first one. You see that 79 from one of the email address is in one and so this actually you can see this is pushing out and expanding and like find me all the numbers that are contiguous. Then we can do a much more complex one. This is a way to pull the domain name out of an email address, and so this one takes a little bit of explaining.

If you go back to your cheat sheet matches any character, plus is a modifier that matches that. That says that means any character, one or more of those characters followed by an at sign. What that does is if there is something here and then at sign, it's a way of scanning up till the moment that you find the at sign. Then what we have is the parentheses character.

The parentheses character says start extraction here, start extraction at the character after the at sign. Dot star means any character as many times as you want [inaudible] Then chop that out, and then dollar is the end of the line. This literally stated basically says scan the line delay find an at sign and then give me everything from the at sign to the end of the line. That's what this regular expression says.

It's awesome, and again, if you just got to look at these things. Remember the plus modifies the one before it, and the star modifies the one before it. Parentheses the start, at sign is just a character, dollar sign is the end of the line. The only thing that's really just a character that's not programming in this whole thing is the at sign.

That's basically, how to pull the domain name off of an email address column. You can do that in Python, and I'm sure you have done that in Python if, especially if you've taken one of my classes. But here's how you do it in regular expressions. You can actually use this exact same regular expression in Python, and if you took my Python class.

But I'm for everybody, you actually saw this example which I borrowed liberally from Python for everybody. This one here is pretty much the same. It is adding a distinct, so that now that basically says all of the domains of all the email address is from this database. That's what that's doing.

I could even say an order by. We'll do some order buying here. That's the same regular expression that basically says go up to the asterisks, start extracting, extract all the way to the end of the line. Now, we can do other things.

Now, this one here that you'll see is a little ugly. I'll just tell you that this part here email from that email from that and all the places it says email, those are identical. I couldn't put that like in a variable or something, so just think of that as like gets us this email address from a column of email. What we're going to do is we're going to select, pull up the email address, and then we're going to count each email address.

Then we're going to do a group by this same thing, which is that domain name and the email. You can almost think of this as domain name. We're going to select it, I'm going to count them, and then we're going to use a group by, of this same thing. This is a variation on distinct except that when it's taking the apple.com and it turns out that there's two of them, it remembers that were two of them.

Uiuc.edu, it remembers that there are one UMUC that remembers there one and there were two umich.edu addresses. You can put these in various parts of the select statement. That looks a little cryptic by the time it's all said and done, but it runs just fine once the database engine can take a look at that. Now, that was, remember, I said that if there's a 1, 2, 3, 4, everything I've shown you so far is going to pull the first one out and ignore all the rest.

It could be 5,6, right? So it ignores the rest of them. Sometimes you want to get all of the matches. The substring call gets the first match in a text column, ignoring the other matches, even if the regular expression would match more than one.

But we can get an array of matches which is different than a column. It's like an array that you get when you do a select statement. We use the function regexp_matches, which basically says, it looks pretty much the same as a substring, is just now I want all the matches instead of whatever. You have to in your code do something a little bit differently when you've received these.

The application that we're going to do is hashtags. We're just going to be looking. We put some hashtags in like these might be tweets or whatever. We have hashtags and then we're going to take a look at how to pull these hashtags out.

Here's our tweets with lots of hashtag in them. We can put this in a where clause, but this is exactly what we did before, where it was like okay, find all the tweets that have hashtags in them or the hashtag SQL. So this one goes through and finds SQL, finds SQL. We could've done that with a light clause if we wanted to and we don't see the one here that says UMSI Python.

That's just a where clause. That is something that we did before. Now we're going to use regular regexp_matches. Let's take a look at the code.

Pound sign. That's just a character. Parentheses says start extraction, other parentheses says end extraction. Then we have a set.

This equals one character. Inside it are what the logit characters are. Capital letters, lowercase letters, and numbers, and underscores. We've decided that's what our tweets or our hashtags are, is a pound sign, followed by then at least one, the plus means at least one, upper, lower numbers, and underscores.

That's what we're matching. But what we've done is we've said regexp_match, and that means go across the line and find it and because we didn't put the pound sign in the parenthesis, I could have put the parenthesis outside it. You'll see in the matches, we don't get the pound sign. Again, that was my choice.

I could have done it either way, but I just wanted the tags without the pound signs. That is the list of tags and if we can use select distinct, G means all way across, that's all the way across. We do a select distinct, we remove all of the tags in this database, there they are and we've removed any duplicates. But then we can also do things like say, okay, I want to select an edition.

This is the same. In addition, I want to know what the primary key of the tweet is that had that particular thing in it. Tweet 1 has SQL and FUN, tweet 2 has SQL and UMSI and tweet 3 has UMSI and Python. This would be a thing that you could then do something with, but you basically extract it and expand it and kept track of which tweet you're in.

Who knows what you're doing with this, but that's the thing that you can do. The main thing we talked about here is this regexp_matches, which goes across the whole line, grabbing as many times as this pattern can be fit to that line. Then giving you an array of all the things where they matched. That sums up this set of string manipulation lectures.

I'm going to do a code demo where I do one of my favorite examples of reading three email addresses, parsing email addresses, and calculating counts of things, and we're going to do it all in SQL. Some of you who may have taken my class online or others that use my book see, I have done this in Python with dictionaries and lists and tuples and sorting, etc and we're going to do it all in one or two statements with SQL in this particular demo. So I'll cover that demo. This is a tantalizing look into it.

We're going to actually read a file. We're going to pull it all in as flat text lines in a database and then we're going to run some regular expressions. We're going to use a where clause to pick the right lines and then we're going to do some group buys, and order buys. When it's all said and done, we're going to end up with a list of e-mail addresses and counsel at times those people sent the e-mail.

We're going to do it two ways: We'll do it with and without a select statement. We'll take a look at some of the performance implications and why it is that you don't want to use a select statement.
