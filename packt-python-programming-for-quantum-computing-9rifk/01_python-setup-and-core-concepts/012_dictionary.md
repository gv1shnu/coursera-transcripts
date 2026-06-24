# Dictionary

- **Course:** Python Programming For Quantum Computing
- **Module 1:** Python Setup and Core Concepts
- **Lecture #:** 12
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/EglZM/dictionary
- **Extracted:** 2026-06-22 15:08:10

---

Hi. Within this lecture, we are going to learn something called Dictionaries. So I'm going to create a new Python Notebook from here, and let me Zoom in a little bit, so we can see better, now we are ready to learn. Actually, in the previous sections, we have learned Lists, right?

And Dictionaries are actually some kind of Lists, but rather than having a single element, this has more than one element. So, let me Rename this as Dictionary, so we are ready to start. So, as I said, Dictionaries don't have a single element, but actually a pair. So let me show you how to create a dictionary first.

So my_dictionary is equal to not a square bracket here, but curly braces, okay. So this is curly parentheses, this is how you create dictionaries with a curly parentheses, and you had to give it a "key", like here, okay, "key", and with a colon "value". So dictionaries are actually a pair of key and values. So, what do we do with that?

If you call my_dictionary, and with a parenthesis and a square parenthesis, okay, not a curly one, but a square one again, my_dictionary["key"], if you write "key" here, you get back 'value'. So this is how Dictionaries actually work. And, in what sense we can use them? This is the real question.

Let's suppose you have a list, like my_list. And let's suppose that you want to create a fitness list, like a 100 calories for running, and 200 calories for swimming, for instance. So you can write 100 and 200 inside of a List, right? But you don't know what 100 and 200 stands for in this case.

So, maybe you know, from your head, like you haven't memorized, but you don't know it. So maybe you create a new list, and, inside that list, you specify the first element as "run" and the second element as "swim", but you don't know, you don't actually combine them. So maybe you come up with an idea that my_list[0] is 100, and my_list_2[0] is 'run'. So if I get two 0s out of two arrays, two Lists, then I can match them, okay.

But, this is not useful every time. So, you need a system where you can pair each other. So this is where dictionaries come into play. So you can create a my_fitness_dictionary, and with a curly braces, you can say, "run", with a colon 100 and "swim" with a colon 200, okay.

So now, if you call my_fitness_dictionary, and maybe you realize that I hit Tab after I have written my_fitness, and it autocompleted, and if I call a 'run', it gives me 100, and if I call my_fitness with a Tab, it autocompleted, and "swim", it gave me 200. So now I have a system where I can pair a key and a value. So dictionaries are pairs of keys and values. But can we have like strings or integers or other data structures as keys and values?

Okay, of course, we can. And, this is one of the flexible things about Python as well, you can have as many as you like in a Dictionary, okay, as many data structures, data types, as you want, in a Dictionary. So let's give an example, and let's create another one in order to not confuse with the previous one. Let's suppose we have a Dictionary called my_dictionary_2, is now, {"key1" is actually 1, "key2" is actually 2, and "key3" is now, not an integer, but this time it's going to be a string, okay, like "apple".

So if I hit Shift Enter, as you can see, we get no error. So, if I say, my_dictionary_2, and open a parenthesis and say "key1" is going to give me 1, but now if I say my_dictionary_2, okay, if I say "key3" , it's going to give me 'apple'. So, in the first one I got out an integer, and in the second one we got out, and it's string. Okay, so we can use data structures, mixed, like we did in the Lists.

So it has actually some common points with Lists, as expected. So, let's create a new dictionary called my_dictionary_3, and let's open our curly braces. And this time, I'm going to write some "key1" is, with a colon, is equal to 10, and, again, let's write something with not a string as a key, but an integer as a key. Can we do that?

Of course, like, if I call my_dictionary_3, this time, and if I say, "key1" it's going to give me 10. But, I can do that as well, my_dictionary_3, and rather than saying "key1", I can say 20, and it gives out 30. So, not only in the values, but also in the key side we can use data structures mixed as well. So, in other programming languages, most of the time, you have to specify same kind of keys, like strings or integers, but in here, we can use strings, and then in the second element, maybe we can use integer as a key.

So, this is where you're flexible, again. So let's have another example in here, like my_dictionary_4 this time, and let's say with a curly braces, the "key1", "key1", as usual, is 100, and "key2" is equal to, now this time a List. Can we do that? Of course, we can.

Now, let's say "key3" is actually another dictionary. Can we do that? Of course, dictionary inside a dictionary. So, this has a key of "a" and the value of 5, for instance.

So, can we get to "key1", "key2", "key3" separately? Yes. And can we do a nested call, like we did in the previous lecture? Of course, and we're going to do an example of that in a minute, but first, let me show you a method, an attribute or a method of a dictionary, so you can understand it better.

So if you do something like this, my_dictionary_4, and, you have to get all keys of my_dictionary_4, in an example, what can you do? There is a method to do that actually, if you call my_dictionary_4, it gives out the whole dictionary for you. But if you call my_dictionary_4.keys, for example, okay, and like we see all the attributes and methods when you hit Tab, like if you call the keys with a parenthesis at the end, if you hit Shift Enter, it gives you the dict_keys. So you can see the keys here with this method.

Can you get the values? Of course, you can do my_dictionary_4., and if you go to the bottom, you will see the value. So I can call the values and see the Integer, the List, and the Dictionary as well. So, let's do an example.

Like I said before, let's try to get the key3, okay. And what is the key3? It's the dictionary. And after that you have to get the 5 out of it.

And please pause the video and try to get it yourself. I hope you managed to get it, and this is exactly the same thing like we did in the Nested List. If I do my_dictionary_4["key3"], it gives me the new dictionary, nested dictionary. And if I do "a" in here, it gives me the 5.

So, I can reach dictionary inside of a dictionary with a single line. So if I do something like this, my_dictionary_5 for this time, so this is our last example, like "k1" is 1, and "k2" is again 2, okay. If I hit Shift Enter, this is now a dictionary. Now if I want to change this, I can do something like this, "k1" is 1, okay, but I don't want it to be 1 anymore, but rather, I want it to be 3.

Can I do this? Of course. If I call my_dictionary_5, as you can see, this 'k1' is 3, 'k2' is 2. So you can change the elements, you can change the values afterwards.

And what if you want to add and append the new item to the dictionary, you don't see the append method anymore in here, but, this is actually simpler compared to Lists, you just specify the new key, and you specify the new value in here, so it's automatically appended to the dictionary. So if I call my_dictionary_5 now, I will see all the key and the values with the appended one. So now let's stop here, and within the next lecture, we're going to learn about something called Sets.
