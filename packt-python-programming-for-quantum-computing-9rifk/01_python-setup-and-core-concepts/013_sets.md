# Sets

- **Course:** Python Programming For Quantum Computing
- **Module 1:** Python Setup and Core Concepts
- **Lecture #:** 13
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/6JuQc/sets
- **Extracted:** 2026-06-22 15:08:22

---

Hi. Since we now completed the subjects of Lists and Dictionaries, now I'm going to create a new Python Notebook, and I'm going to Rename this as Set. So that's what we are going to learn within this lecture. So Sets are collection of data structures like Lists and Dictionaries.

But in Sets, you cannot have an element more than one time, okay, they have to be unique. So, we didn't see that in Lists, right? So let me create a List for you, so my_list = [1,2,3, and 1 again. So, we have 1 two times, right?

So if I call my_list, I will see 1, 2, 3, and 1. And, let me turn this into a Set. And, I have to see 1, just one time in that Set, because Set contains unique elements. So, let me do some casting.

Actually we have done this before, right? So we had said int, to just convert a string into an integer. So if I say, let me just mark this down for you. So this is casting, okay.

So if I say, I want to convert my_list to be a set, so set(my_list). So this converts my_list to be a set. So if I call my_set, let me show you what we get. So I have 1, 2, 3.

And I don't have that second one, because they have to be unique in a set. So, what can you do with a set? If you have a List with duplicated items, you can convert it to be a set, and you can just get rid of this duplicates. So let me create a new set for you and show you how to do that.

So you have to use this curly braces, and just type the elements that you want to be in. So, let me type 1, 2, 3, and 1 again, and let me call my_set_2, and it's still going to show me 1, 2, 3, because, it will just omit the second one, because, they have to be unique values. So, let me call type this time to see what type my Variable is, this is a set. So, in sets, you have unique elements.

So, let me do another example, just to make sure that sets are working the way that we want. Let me create another one with a string this time, so this is "a", "b", "a", Shift Enter, and if I call my_set_3, then I will see only 'a' and 'b'. So you have the possibility of including strings, integers, and everything, like we used to do in Lists and Dictionaries as well. So it's kind of a dictionary in a way that we define it with curly braces, but we don't have key and value pairings in here, we only have elements as we have in Lists.

So, sets are just like this, and let me show you something else. So we already created Lists, Dictionaries, and sets, and we always gave the initial values when we create them, right? So we said that my_set is 1,2,3. But what if we don't know the initial values?

So can we create an empty List, can we create an empty set? Yeah, of course, we can. But why do we want to do that? Maybe we are just downloading from the Internet, maybe we're getting data from some other class, some other program, I don't know.

So, maybe we have to initialize this as an empty list. So, my_list is going to be an empty list, just like this, okay, so square braces here, and this is empty. So if I do type(my_list) right now, I will see this is a list, but if I call my_list, it will just pop out an empty list. So if I say my_list.append, now I can append the data that I got from anywhere.

So, I can say my append, my_list is 1. So, I can append as many as I want right now. So if I create a set, for instance, my_set_4, this time, I can do this. So, empty curly braces.

So I can say my_set_4, and it will pop up an empty set, okay. If I just verify this type(my_set_4), this is a dict. And as you can see, it says that this is a dictionary, because it can be a dictionary and a set, okay. So, if I don't give this, I can give this, right?

I can have key value pairings here, or I can just have single elements. So, Python confuses if I wanted to create a dictionary, or, if I wanted to create a set. So, I don't know how to deal with this at this moment right now, right? So what can I do to make sure that I created a set or a dictionary.

There is a way to do that actually, besides having this empty curly braces, or empty square braces at all. So I can say "key1" is 1, then my_set_4 is going to be definitely a dictionary. But at this point, maybe, I just wanted to create a set, and, the way to, proper way to do this, actually, my_set_5, is going to be a set with parentheses. So now, I definitely have an empty set.

This means that I have created an instance of a set class, and we're going to see what it means in the future. So if I call my_set_5 right now, it shows that this is an empty set. It's definitely a set, not a dictionary. So I can say my_set_5.add, and add whatever I want to add, like 1.

So, this is my_set_5.add, like 2, okay. Let's say my_set_5, and it will give us 1 and 2. If I say my_set_5.add(2) again, and if I call my_set_5, it will only show me 1 and 2 just once. So my_set_5 is definitely a set.

So we can use this thing in other examples as well. Like, if I want to create my_dict_2 to be an empty dictionary and empty instance of a dictionary, so, this will be a way to do it. So I can say my_dict_2["key1"] is now 1. If I call my_dict_2, I will see the key value pairing of 'key1' and 1.

And can we do that with Lists? Of course, my_list_10 = list. And, now I can append anything I want. Let me call type(my_list_10), this is a list, and if I call my_list_10, this is an empty list, and I can say my_list_10.append, and insert any value that I want in here, like "a", and if I call my_list_10.append(2), then it's all included in the list, like append, I don't know, and other list.

And if I call my_list_10, it will be all displayed to me. Now we know about sets and now we know how to create empty Dictionaries, Lists, and sets as well. So let's stop here, and we got a couple more data structures as well, and we will see them in the next lecture.
