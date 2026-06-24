# Advanced String

- **Course:** Python Programming For Quantum Computing
- **Module 1:** Python Setup and Core Concepts
- **Lecture #:** 8
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/5bMOB/advanced-string
- **Extracted:** 2026-06-22 15:07:27

---

Okay. Now we are done with the basic operations of strings. We're going to now move forward to advanced operations, since we are going to use them when writing ethical hacking tools. So I'm going to use another Notebook.

As usual, I'm going to close this and create a new Notebook called Advanced Strings. If you please, you can continue with the previous one, of course. I'm going to Zoom in a little bit, and I'm going to change the name to StringsAdvanced for this operation, okay. So I'm going to Rename this, and let's start.

First, I'm going to create a variable called my_string, and it will be equal to "hello world", as usual. So, we have learned to call the strings, like, I can call my_string, and it will give me the output of 'hello world', but we did not learn how to get a single element out of my string, a single letter, okay. So let me write this as a note. So I'm choosing Markdown and putting two hashes here to specify that I'm going to use this as a heading, and I will say it indexing, okay.

So, what is indexing and how can we use it? So if I write my_string and open a parenthesis, but a square one, not a regular parenthesis, okay, not a curly parenthesis, but a square one. And, after that, if you write 0, for instance, and hit Shift Enter, it will give you the first letter. So why first letter, because indexes start with 0 in strings.

And indexes generally start with 0, we're going to learn something called Lists. Maybe you have heard them as arrays in other programming languages, but in Python, we call it Lists, and indexes always start at 0. So, suppose you want to get o out of hello, how do you get it? I suggest you pause here and try to get the o yourself.

I hope you managed to get it. Since o is the fifth element, I will just say 4, and it will give me 'o', why? Because index start at 0, and index 4 is equal to the fifth element, which is o. Okay.

So I hope you get the general idea. You can use indexes to get individual elements out of a string. So suppose you want to get the last element rather than the first element, what do you do then? You may write -1 in here, okay, and -1 means the last element.

Of course, if you try to just get the -2, it will give you the second last element of that string, which is o. So it is pretty useful when you want to get the last letter of a word, last letter of a sentence, I don't know, we will use them when writing ethical hacking tools. So, we have more complex methods than this, surely, and let's see about them. We want to know something called slice, okay.

So, there comes a time when we need to get a specific portion of that indexes, like we want to get the elements between 2 and 5, or up to 5, or from 5, what do we do then? We need to know a concept called slice. Let me create another string called my_string_2, and give it "1234567", for example, and please pay attention that I'm surrounding this into double quotes, because if I didn't, if I written it like this, it means that it's an Integer, but I'm not going to work with Integer, I'm going to work with a string, so I'm surrounding it with double quotes. So this are strings.

Now, if I write something like this, what will I get, the first element of that string is 1, right? So, it's pretty clear, I think right now. But what if I want to get a certain proportion of that string? I would have then used this colon sign and say, 2, for example, let's hit Shift Enter, and let's see the result.

What we get here is that 3457, and so on. So, what does it do? It just omits the first two element of that string, okay. It starts with the second index.

So, it just omits the 0 index, first index, which is 1 and 2, and starts with the 3. So this is called slicing, okay. Actually, let's delete this, because this is a regular cell, not a Markdown cell. Let me write it down as a note, so I'm choosing Markdown, I'm going here to specify, this will be a heading with hashes, and say this is slicing.

So let's move on. So, what do I mean by slicing? I can specify which index I'm going to stop or start with slicing, with using colon, of course, like we did in this example. So, what if I want to just get 567890.

So I can write my_string, with colon, of course, and I want to omit index 0, first, second, third, okay. So, I will just start with 4, and it will start with the fourth index. So, I will have 567, and so on. So, the first number, before the colon, specifies the starting index.

And if I type something like this, my_string_2 and 2 after the colon, it means a stopping index. And, it says that, stop at index 2, so, it just gives out the 1 and 2, the index 0 and the index first, okay. So you might think that when we specify the fourth here, it just included the fourth index, and when we specified the second here, it just didn't include the second index. And that is exactly what Python is trying to do actually.

It doesn't want any intersection. So, the first one is starting index, it includes the fourth, and second one is the stopping index, and it doesn't include the stopping index. So, I can get the first part of a string in a separate way and the second part in a string in another way, okay. So, let's write it down, okay, with a hash again, it's a stopping index.

So if I write down my_string, second, fourth, this time, I will get what's left of this 567890, so I can get 1234. So, this is the logic behind, including one index in one method and not including it in another index, okay. So, is it possible to use them both in the same line? Of course.

When I type 2:4, it means that start with the second index and stop at fourth index. So it will start with the 3 and it will stop at 5, right? So, let's hit Shift Enter, and it will tell us 34, and it will stop at 5, but not include 5, so we will get 3 and 4. So we can get middle of a string, we can get the top and bottom of a string, we can get starting point, ending point, middle point, some portion, with using slicing techniques.

So, always remember that the first one is the starting index, but second one is actually a stopping index. So, what if you want to get something like 678 as a number. So, pause the video here and try to get it yourself. If you did get it, very good, if you didn't, you should have written 5:8, because why, so, the fifth index is actually the sixth, and it starts with the starting index, and the eighth index is 9, it won't include the eighth index, so we will get out as '678'.

So this is how you work with slice. But we're not done yet. We have something called step size, okay, let me write it down for you, and it will specify how many sizes that we are going to skip when we are working with slicing. What do I mean with it?

Let's write down our my_string_2. If I type two colons this time, and hit Shift Enter, it will give me my_string as it is, because I didn't specify any starting, stopping index, and the second, the last part, before we close the parenthesis is actually the stepping size, and we didn't specify any stepping size either. So, what if I did? So, let's see an example.

Let's say ::, and, for example, 3. So, it will just skip 3 steps when it gives out the output. So we get 1, and we just skip to the third index, okay, after 1. So, we omit two indexes in the middle.

So we can, for example, we can say, my_string_2[::2], and we only get this odd numbers, for example. You're going to find this very useful when you deal with complex set of strings, and you can combine all of this methods into 1 single line. What do I mean? You can say, start with second, stop at fourth, and step size is actually 2.

So it will give you only the 3. So it turns out that only 3 fits in with our [unclear] filtering. Of course, you may want to do some other complex examples as well. I really suggest you guys to just work around with this, play around with this, and the final trick is using -1 as step size.

If you use -1 as step size, what will happen? It will just reverse the string, okay. So this is pretty useful. When you want to reverse a string, you can just give the -1 as a step size, -1 doesn't make sense to use as a step size, but this is a trick in Python that we use.

So, we're done with the strings here. Let's move to the next lectures where we will learn other data structures as well.
