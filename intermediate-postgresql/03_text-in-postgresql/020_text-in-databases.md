# Text in Databases

- **Course:** Intermediate Postgresql
- **Module 3:** Text in PostgreSQL
- **Lecture #:** 20
- **URL:** https://www.coursera.org/learn/intermediate-postgresql/lecture/E1L1e/text-in-databases
- **Extracted:** 2026-06-22 20:27:34

---

We're going to talk about texting databases, but really, this is much more than that. After the first two lectures, we've really been just using any excuse to teach you more in depth SQL skills. And you may or may not use some of these skills in text, but they're just skills that you need. So the first thing we're going to talk about is how to generate some test data in Postgres.

So we're going to talk for the first time. I've been talking about performance all along, but now we're going to start talking in more detail and actually looking at how you decide about performance. So the problem is every, all my little example so far, like I put five records in and I'll show you some queries. But now I want to put some more data in.

So the problem is if you think about it, you gotta let's say you need 10,000 records or 100,000 records or even a million records. So you can check to see how fast a query runs with various indexing options, etcetera. And we're also going to look a little bit about how much space we start using as we make different decisions, so we'll get to all that. But the first thing is a prerequisite is to fill your database up with data.

And so you could write a Python program and you could open some stuff up and you could write some four loops and then write stuff into the database or you could use shell scripts. But it turns out that Postgres has some wonderful mechanisms that allow you to generate random data. And so there's some functions, and we look at each of these with some examples. But the repeat function allows you to create long strings, so you just take a string like, you know, ABC say, give me 1000 and that's like 4000 character, 3000 characters, ABC, ABC, ABC kind of doesn't matter.

Then there's random, which gives you a random number between 0 and 1, and we use functions like trunks so you can multiply that by 100 and then trunk it and then get an integer between 0 and 100. Or you can say, give me a number between 1000 and 9000 and then you get a bunch of 4 digit numbers so we can figure all that out. The one that's kind of cool is a thing called generate series, and and it's a way to generate multiple rows. And so generate series is how we generate a lot of rows.

And so we'll look at each of these with a simple example. So the first simple example is a random. So basically random just gives you a number between 0 and 1. It's a floating point number, right?

So I call it twice, I get two different numbers. And then I just multiply by 100 I trunc it, so trunc says, so that becomes like the random number between 1 and 200. It's a floating point, but trunc says convert that to an integer. Now the repeat one right, so I'm just taking, the word neon with a space and repeating it five times.

So that's sort of a horizontal concatenation. And so sometimes when you're building keys or whatever, you just want them long. You'll see in a set, kind of we make, just put some random stuff in it, and then just a bunch of text, and that's usually good enough. But this generate series is really kind of cool.

If you think about it from Python function, it's kind of like, it's like the range function in a sense, if you think about Python so far, I in range 5 that actually that then generates 5. And so generate series 1 through 5 generates a series of numbers, but it also then if you can concatenate it, it generates rows. So these first two generated one row, just that's a random number. That's a long string.

But this is five rows. And so we combine all these things together to generate lots of rows of long data with some randomness. That's what we're going to accomplish. So here we see a select statement, right?

So we're going to have a string vertical double vertical bars, concatenate string concatenation. So we're going to take, sql4e.com/neon concatenated with a random number that's between 0 and looks like a million concatenated with repeat the word lemon five times and then to create more rows we also concatenate it. This this is all one thing. So this general series is so cool, like explodes into the numbers 1, 2, 3, 4, 5 vertically.

And so that forces all these things to be calculated five times. And so we end up with five rows with reasonably long bits of information and a random number and then a sequential number. And so with these techniques, you can construct a whole bunch of data. Okay, so it's random trunc, repeat and generate series, and then you just insert these things in.

And so up next, we're going to talk about, we're going to use this and we're going to talk about some of the text functions that we can do with data once we have it in the database.
