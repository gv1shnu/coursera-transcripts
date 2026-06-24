# Tuples

- **Course:** Python Programming For Quantum Computing
- **Module 1:** Python Setup and Core Concepts
- **Lecture #:** 14
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/qcFKZ/tuples
- **Extracted:** 2026-06-22 15:08:32

---

Hi. Within this lecture, we're going to cover something called Tuples. So I'm going to create a new Python Notebook from here, and let me go and change the name to Tuple. And I've heard people pronouncing this as a Tupple or Tuple.

So, you may choose whatever you want, okay, but I call it Tuple. So, what is a Tuple? Tuple is a List-like object, okay. So Dictionaries, Sets are List-like objects, but they have some similarities, they have some differences, and I believe, you have understood them in the previous lectures.

Tuples are like, like Lists, but they cannot be changed after they are initialized, okay. So they're immutable too. So let's suppose we have actually a List, like my_list = like "a",1, and "c", for example. So, what could I do in the previous lectures, I could have said, my_list[0], and it's going to be 'a', but I could have changed it, right?

So, my 0 is now "b". So, if I call my_list, now it's 'b', 1, 'c'. So, we could change the first element, but, if I call my_tuple. So, you create Tuples with regular parentheses, okay.

So, let me call the same thing, "a",1,"c". And, if I call my_tuple with a square braces, again, I can just say, get me the first index, 0 index, and it's 'a', but I cannot do that, my_tuple[0] is now "b". As you can see, we get an error, and it says that, 'tuple' object does not support item assignment. So we cannot change this.

So let me hash this out and hit Shift Enter again, to make it into a comment, and let me Markdown this immutability, say immutable. So we cannot change the single element inside it, like, we couldn't do that in strings as well, right? So, you cannot say my_tuple[1] = 2. So, I believe you have now understood the difference between a List and a Tuple.

Maybe at this time, you think that, why would I ever use Tuple when there are Lists, right? So we can create Lists in the same way, and we can change them afterwards. So Tuple actually imposes a restriction upon us, right? But we don't know what kind of data we get from other sources.

So we're going to use a lot of external libraries when we deal with Python. And, external libraries actually are one of the strongest areas of Python, and one of the most popular reasons why Python is being oftenly used by programmers, developers, around the world. So we will use external libraries, and they tend to use Tuples over Lists, because they don't want us to change the data that we have gotten from them, okay, or at least without actually processing it. So we may get Tuples, when we deal with external libraries, we may get Tuples when we deal with another SDK, software development kits, I don't know, libraries, modules, packages.

So, even if we don't want to use them, believe me, you will just come across with them a lot, so, it's better to learn about Tuples. So, like Tuples has a count method, and if you just Run it, you will get an error saying that, count( ) takes exactly one argument. So you have to give it an argument to work with. So what argument do we have to give?

You have to give an element, like "a", so it counts the "a" inside a Tuple. So, if you want to learn count of a specific element, you use that, let me give you an example, like my_tuple_2 is now 1,1,1, and "a", and, I don't know, "c", okay. So if you say, my_tuple_2.count, and if you give 1, it will give you 3, because we have three 1s in my_tuple_2. So if you say, my_tuple_2, as you can see, we have an index.

So, it gives the index of a specific element as well. So if you say "a", it will give 0, 1, 2, and 3. So "a" is located at the third index, but we have more than one 1s here, right? So if I say my_tuple_2.index(1), what will it give?

So it will give the first index it encounters, the specific element, so, it's 0 for us. Yeah, it's located in the second index as well, but it just says the first location that is formed. So let's stop here, and within the next lecture we're going to learn something called Boolean.
