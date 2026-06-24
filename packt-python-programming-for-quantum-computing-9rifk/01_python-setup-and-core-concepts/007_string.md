# String

- **Course:** Python Programming For Quantum Computing
- **Module 1:** Python Setup and Core Concepts
- **Lecture #:** 7
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/47QmK/string
- **Extracted:** 2026-06-22 15:07:14

---

Hi. As we talked before, now we are done with the Variables part, we are going to learn how to work with strings, that are texts, in this lecture. So I'm going to Save this Notebook, and I'm going to Close it, okay, because I'm going to create another one in which we will have the strings. Of course, if you want, you may continue with the first Variables Notebook as well.

So let me Zoom in a little bit more, so you can see it clearly. Now we're going to work with Strings, so make sure the Code is selected here, and let's write our first string. Our first string will be "hello world", as usual. So I'm writing a string and I'm hitting Shift Enter after that.

And as you can see, I'm placing into two double quotes. And if you place it into single quotes, it will be okay as well, okay. But I always prefer double quotes actually, because, if you try to write something like, 'i'm a pilot, for instance, okay, the second single quote will be closed, and the rest of the code won't be interpreted by Python, okay. So, if you hit Shift Enter, it will say invalid syntax, because Python doesn't get after the second single quote, okay.

What I can do, in order to overwrite this, overcome this problem, I can wrap this into double quotes, and I can still use the single quote inside a string. So I generally prefer double quotes when working with strings, you may choose whatever you please, okay. So, this is a string. And, of course, we can assign strings to the Variables as we did in the previous lecture, okay, like x = "hello world", if I hit x, it will just give me the output of 'hello world'.

Can I change the string? Of course. Now I can say, x = "hello" only. And if I hit x again, it will give me the output of 'hello'.

And in Python, we can do something that we cannot do in the other programming languages generally. We can say x is now 3, okay. Now x is a number rather than a string. If we did that in Java or another programming language, it should have complained us and said it, you cannot convert this into an integer, because you defined it as a string.

But in Python, we can do that, it's a very flexible language. Of course, this may create a problem as well. Think of this case. You initialized a Variable as a string, and then you convert it to a number, and then you change it back to a string, and now you're going to learn some other data structures as well, like Boolean and stuff, we can change it to whatever we want.

But at a certain point, we may get lost, and we may want to know what kind of a data structure we're dealing with, okay. Then, we have a method to know what kind of type of variable that we are dealing with. So let me say, x is "hello world". Again, now x is string, as you know.

If I type, type(x), it will give the output of the type of x variable. By the way, let me show you a length method as well. So if you type len(x), it will show you how many characters do you have in your string, okay. So let me Markdown it, let me write it down as a note, so you can memorize it better.

So if you type len(x), it will count the characters in a string and give you as an output, and it will just include the spaces as well, as you can see, it has 10 characters, but including space it has 11 characters, so it gives out 11 as output. So len and type are spatial methods that we can use with strings, and we can use with most of the Variables and most of the data structures as well. So maybe you'd think, is there any other function, spatial built-in function like that, yes, there is print function like we've seen before. If you type print(x), it will just print out the hello world, the current value of the variable x, okay.

So we have len, type, print, of course, we have other spatial methods as well, that's what we're going to learn in future, but for right now let's stick it to strings, okay. So let me talk about spatial escape characters. So, before we go on and write print, let me mark it down and say escape characters, as a note to you, okay. So what are escape characters?

So what if I want to split a string into 2, okay. So let's say, I want to write inside a print method, "hello python", okay. But, rather than having a single line, I want hello at one line, and Python in the down, okay. So, if I write like this and hit Shift Enter, as you can see, we get an error, because we cannot do that.

In order to create a new line, there is a special syntax that you should follow. All you have to do is do a backslash, okay, not a forward slash, but a backslash like this, and type n as a new line, okay. If you type \n, and hit Shift Enter, as you can see, it writes hello and python on separate lines. Now let's put a space and hit Shift Enter and see what happens.

Python will be still on the separate line, but with a space. So, if I undo it, and hit Shift Enter again, now, it is the exact output that I want to get. So are there any other spatial escape characters? Of course.

So, if I want to give a tab between hello and world, I will just have to write \t, okay. As you can see, it just creates a tab space between hello and python. So, at this point, actually you may think that these are just text, why are we spending too much time on them, because, we're going to use them when writing ethical hacking tools so much, I want to emphasize the importance of them. In the next lecture, we are going to see some advanced method of strings as well.
