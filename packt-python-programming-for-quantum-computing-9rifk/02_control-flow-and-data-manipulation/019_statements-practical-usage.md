# Statements Practical Usage

- **Course:** Python Programming For Quantum Computing
- **Module 2:** Control Flow and Data Manipulation
- **Lecture #:** 19
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/dJR8D/statements-practical-usage
- **Extracted:** 2026-06-22 15:09:28

---

Hi. Within this lecture, we're going to learn some new tricks, working with if statements. So we have seen how to work with if statements in the previous lectures. But, I'm going to make your life very easy with some practical usages, mainly in strings or Lists-like objects.

So let me create a string called "Hello World". So this will be my_string, okay, and I can check if my_string is actually "Hello World", right, you know how to do that. So if my_string is equal to "Hello World", and I will say, print("true"), for example, or print("equal"), I don't know, you can just print whatever you want, but equal, yeah, if I can print it, if you hit Shift Enter, it will turn print, and, if you change one letter, it won't hold True, okay. So this has to be exact upper case, lower case, capital letters, all matter.

So this is not being run right now, because this is not the same. But, what if I want to check if "Hello" is actually in that my_string. And this is that simple, if "Hello" in my_string. So this will check if "Hello" is actually in that string, and, if this is True, let us say print("true"), and, if this is False, let us say print("false").

So if I hit Shift Enter, it will turn true. So this is a very good check to do that. So let me just say if "hello" with a lowercase, and as you can see, it turns out false, if I change it again, it will turn out true. So this is a very practical way to use in, operator, I mean, you can just use this with strings, you can just use this with Lists, and Dictionaries as well.

So let me create a list and show you what I mean. Like I can say, my_list = (1,2,3,4,5), for example, I can check to see if any element is that Lists. So, I can say if 2 in my_list, then do this, like print("true"), for example, and, elif is not the case, or else print("false"). So, let me hit Shift Enter and it will turn out true, and you can check this with other elements as well.

So, this comes very handy, right, when you want to check a single element in a list. And maybe you cannot think of a way to do that or a reason to do that right now, but let's suppose you download a data from Internet and you want to find out if that list actually contains something, then it will be really helpful. So can we use this in with Dictionaries? So let me create a dictionary, my_dictionary, and remember we have to have a key and value pairings in here, like "k1" : 100, "k2" :200, and let me give another one, "k3" :300.

So this is my_dictionary, and let's suppose I want to find out if 100 is in my_dictionary.values, okay. So remember, if you hit Tab, it will pop open, and you can see the keys, for example, you can just say, print("true"), and, if this is not the case, else print("false"). So, what will be the result, this will be false, because I said keys, not values. So, you may want to change the keys to values, for example, or you can just search for k1, for instance, to find out if this is actually working, right?

So, let's suppose I delete this 100 and say "k1" is set. So, this is actually true. And let's suppose 100 in my_dictionary.values, this will be again true. So if I say 140 instead of 100, this will be false.

And you got to point right, if I say 200, this will be true. I suggest you play around with that in order to get comfortable with the situation, and, we're going to stop here because we are done with the if statements. In the next lecture, we're going to learn about some loops.
