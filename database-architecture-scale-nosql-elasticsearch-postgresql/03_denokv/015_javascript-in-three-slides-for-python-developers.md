# JavaScript in Three Slides (For Python Developers)

- **Course:** Database Architecture Scale Nosql Elasticsearch Postgresql
- **Module 3:** DenoKV
- **Lecture #:** 15
- **URL:** https://www.coursera.org/learn/database-architecture-scale-nosql-elasticsearch-postgresql/lecture/w1IcX/javascript-in-three-slides-for-python-developers
- **Extracted:** 2026-06-22 20:48:49

---

Welcome to the world's shortest JavaScript lecture. I'm assuming that you know Python. Now, JavaScript is not based on Python, but it is influenced by Python. So Python was created before JavaScript, OK?

It was created in 1991. They're both interpreters, so they have kind of a similar object model. JavaScript was created in 1995 as part of the web revolution. Python was pre-web in many ways.

They're both interpreted. Python is written in C, so it has a lot of influence of C, but it has a very unique syntax, whitespace, et cetera. In JavaScript, it was designed for more sophisticated developers, and so it was just a variation of the C, which means it's got whitespaces ignored, it uses curly braces, et cetera. And so it kind of imitated C in many ways.

And again, Python was influenced by C, but it didn't imitate C. Python's goal was to create really cool data structures, like lists and tuples and dictionaries, things that we as developers would find natural to use. JavaScript borrowed some of those same ideas. By then, things like dynamic arrays with easy-to-extend arrays and sortable arrays, et cetera, were natural.

And so they made a really good array, which is very different than what C thinks of as an array. And an object, which is in JavaScript, which is very much like a Python dictionary. And the JavaScript object notation, which is JSON, in some ways almost looks identical to the dictionary syntax. And so that's really cool.

So I have to kind of, in my mind, go, OK, which language am I writing in at some point? Now, the if statements and the for loops are very different, because Python invented its own, really focused on its own data structures, whereas JavaScript was imitating C. So let's take a look at the real slide that makes the money. I call this Rosetta, the Rosetta Stone, because it has two languages on it, and they correlate.

And so if you look at the Python, you see x equals key value in lines 25. And that's a constant that is a dictionary constant, and it uses curly braces. And if you look at the JavaScript, it is the same, except that the keys are not strings. So key is actually a member variable of the object.

Lines is a member variable of the object x. So we print them out, and that's the other difference, is you don't have a print statement in JavaScript, which makes me sad. Why not just make print be console log? It's print to not the user, but to the console.

But you say console log, it's kind of nice. Console logs are sort of fun and useful, and we'll use them. You see y equals square bracket Bob Alice strings. And you see on the JavaScript side, y Bob Alice strings.

And the syntax is literally identical. The if statements are a little different. We're going to set a to 17 and check to see if it's less than 20. And in Python on the left, the print statement must be indented.

The else must be de-indented, and the print statement must be indented. And then later, the for statement must be de-indented. Yep. Now it turns out that good C programmers and good JavaScript programmers, you start and end blocks of code not with the indenting, but with open curly brace and closed curly brace.

And so the if, the true part of the if, is console.log below 20. And the false part of the if is in the else area, which is console.log 20 or higher, doing the exact same thing. Now ironically, good JavaScript programmers indent their code anyways. The difference is in the Python side, the indent is syntactically significant and required.

In the left hand side, it's optional, but highly recommended. So then we get to the for loop. So the for loop in Python is trying to be as abstract as it can be, and it wants to think about objects like lists and tuples and iterators. So for i in range 5, print a.

And there's a lot of different for loops in both of these languages, but the equivalent thing is for i equals 0, i less than 5, i plus plus, open curly brace. And again, the scope of the loop is defined by curly braces in JavaScript and indentation in Python. So these are two simple counted loops from 1 to 5 and printing out the value. You can take a string and split it based on a character in both languages.

You get a list in the Python side of things and an array in the JavaScript side of things. But again, lists and arrays function very similarly between these two languages. And you can do some concatenation, string concatenation. Looks pretty similar.

So if we were to run this code, either one is going to produce pretty much the same output. You see it create a object and print it out, create a list and print it out, then create a variable, do an if statement with that variable, have a counted loop from 0 through 4. That's a five iteration loop, and it goes 0 through 4. The split is a little bit different between them, and then we can create a string that is hello world.

Congratulations on enduring the shortest JavaScript lecture in the world for Python developers. The reason that I can get away with this is that I'm not going to have you write any JavaScript in this class. I'm going to give it all to you. I might have you change a line or two, but you can do that.

You can go into AI and paste a little JavaScript. What's this JavaScript do? And that could be helpful to you, so I'm not going to try to teach you all of JavaScript because I'm not expecting you to be a JavaScript programmer. I'm just expecting you to be able to look at it and debug it if you start getting syntax errors.

Cheers.
