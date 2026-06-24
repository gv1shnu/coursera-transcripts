# Lists Advanced

- **Course:** Python Programming For Quantum Computing
- **Module 1:** Python Setup and Core Concepts
- **Lecture #:** 11
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/CghI4/lists-advanced
- **Extracted:** 2026-06-22 15:07:59

---

Hi. Since we have learned about the fundamentals of the Lists in Python, let's dive into some more in-depth subjects regarding that. So what we're going to learn about first is called Nested Lists, okay. So if you have heard the Nested before, it means that, it's a term stating that it's something inside of something, like a Nested List is actually a list inside of a list, so let me give you an example, okay.

So let me put a Markdown here saying that this is nested list, and this goes like this. Let's suppose, we have a list called new_list, okay, so my new_list is going to be =, open the square parenthesis and say, like, 1, 4, let's have a string in here, okay. So, if I want to add a list inside of that list, can I do it? Of course, we can.

You can either use the append method, or you can just assign a new ally to it, and, like, you can say, new_list is again, like 1,4,"a", but, with, this time with a new list, inside a list. And inside that, we have 3, and "c". So, let's say Shift Enter, and now our new_list actually equals to this, okay. So, let's suppose we want to get the list inside of that list, how do we do it?

Like we can say new_list, and this is 0,1,2,3, right, this is the third index, fourth element. So, if I say, 2, it will give me "a", and if I say 3, it will give me the Nested Lists, so this is going to be 3, 'c'. So, if I want to, I can just assign this to be another Variable, like nested_list is new_list[3], okay. So if I hit Shift Enter, now my nested_list is equal to a list of 3 and a 'c'.

As you can see, it gives out the list inside of a list. So, let's suppose I want to get the 'c' out of it, so I can say 'nested_list[1], right? But actually there is much simpler way to accomplish this, accomplish reaching out 'c'. What I have could done, is just to use the new_list with 2 indexes in order to get to the 'c', like new_list[3], and it will give me the nested list, then 1, right?

So, it just calculates the third index, and then the first index of that array. So since it returns an array, it can find the first index of that nested array as well. So this is one of the areas that we see Python is really, really flexible compared to the other programming languages as well. So, you cannot do that in other programming languages, most of the other programming languages.

So let's see another example. Let's suppose we have our list again, new_list, and, can we do that slicing thing that we used to do in the strings, like getting some proportion of it, or using starting point, or stopping point? Of course, we can, like, I can say, 2:, and empty, if I hit Shift Enter, what will happen, do you think? Of course, it will start at index 2, it will get me from 2, okay, from 2 until the end.

So, this is ['a', [3, 'c']]. So, if I say new_list[:2] this time, it will give me up to 2, and it will stop at the index 2, so it will give me only 1 and 4. So we can use the slicing thing in lists as well. I believe you now see the resemblance between the strings and the List, and remember, we're going to use Lists a lot when we deal with ethical hacking part as well.

Now let's Save this, and in the next lecture we're going to learn something called Dictionaries.
