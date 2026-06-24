# Lists

- **Course:** Python Programming For Quantum Computing
- **Module 1:** Python Setup and Core Concepts
- **Lecture #:** 10
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/K239H/lists
- **Extracted:** 2026-06-22 15:07:49

---

Hi. Within this lecture, we're going to start learning about Lists. So I'm going to create a new Notebook from here, and, as usual, I'm going to Zoom in a little bit so we can see it better, and let me just Rename this as Lists. So we can go on and start learning.

Actually, we did some kind of introduction to Lists before. What we did was creating a string, like my_string = "Atil", and, if we did my_string(0), we called the zeroth first index, okay. So this was the first element, and if we called my_string[1], it gave us the second element. So this is how actually string works, and this is kind of how Lists work.

But we couldn't do that in string. If I do my_string[0] is now something else, it won't accept it, because, strings cannot be changed this way, because they are immutable, okay, so let me write it down for you, immutability. So you cannot change this. So if I do my_string[0] or [2] = right now another letter, for instance, it will give me error message.

So let me comment this out by putting hash on this lines, and hit Shift Enter in order to run this again, so this will be like a note rather than code, okay. So we couldn't change strings in that way, because strings are immutable, in this sense. But let me give you an example of a List. So in order to create a List, open a parenthesis, and square one again, and write your listing sites, like 123.

So now, if you do something like my_list and get me [0], it will give me the first element of that List. So it's pretty much like working with strings, right? And, if I do something like my_list[0] is now equal to 5 for 3, other than, rather than 1, now if I call my_list, as you can see, its just 5, 2, 3. So Lists are mutable, you can change the individual elements inside a List, and strings are immutable, because you cannot change the individual characters.

So let me do one Markdown again. So this is mutable, okay, you can change the single elements inside it. So if I do my_list[2], is now 6, if I call my_list again is 5, 2, 6, it's completely changed. So let's see some attributes or methods of that list.

So if I say my_list. and I hit tab, I see the options, I see the attributes and the methods. What I'm going to do, I'm going to append something to the end, okay. So I'm going to add another element to that list, you can use the first option in here, first option in that list, and, it's called append, select it, and open a parenthesis, as usual, and insert the element that you want to insert, like 7.

Now, if I call my_list, it's going to be 5, 2, 6, 7. So maybe you realize something was different this time. In the string section, we have seen some methods and we have seen some attributes, but it was kind of different. Maybe you remember that if we call a string, like my_string is "lars", for example, if I say my_string.capitalize, it will be 'Lars', right?

But it won't change the original string, so this is my_string again, so, the L is not capitalized, but when I do the append, it actually changed. So if I call my_list, again, it's not 5, 2, 6, but it's going to be appended, like with 7, right? If you call this time, you will get 5, 2, 6, 7. So, this actually changes the original one, rather than returning a new string or new objects.

In the old-fashioned way, we had to give a new object, new variable for this, like my_string_capitalized, remember. So we had to do that in order to store Lars capitalized. But this time, we didn't have to do that. So this returns the original one, appended.

And you're going to understand this more in depth when we deal with functions and methods in the following section, but for right now, you see some kind of methods, where I, in a way, they behave when we choose them, okay. So, for example, let's see another method, my_list.tab, it will give us some pop option, and give a parenthesis and hit Shift Enter, it gives the last element as you can see, the 7. But what it's actually done to pop this element of that List? So if we call my_list, as you can see, is 5, 2, 6.

So this last element is popped out. Again, this behaves in a way that it changes the original object. So, can we have Lists as mixed data structures, like Integers and strings in the same List? Of course, we can.

Let's do that my_mixed_list = like 1, 2, and "a", and "bhf", okay. As you can see, it gives us no error. So if I call my_mixed_list[0], it will give me 1, and if I call my_mixed_list, and this time -1, remember -1 gives the last element, and it's a string. And if I call like this, it won't pop out, so it will just give me the last element as an output.

So we can have different data structures in a List, and we don't know the Booleans and other data structures yet, but we can have them together mixed in a List. And you don't have that kind of flexibility in other programming languages actually, but Python does have it. So, in other programming languages, you either have an array or a list of strings, or array or a list of Integers, but in here, we can have a mixed list or an array, whatever you want to call it, but in Python we call it Lists. So let's give you another example, like my_list[1] is equal to "a", "b", "c".

Let's suppose I have another List called my_list_2, and it's, it does have "d", "e", "f". Can you think of a way to mix this together? Of course, we can do my_list_3 = my_list_1, and that is summed with, as you can see, it gives us recommendations as I type my_list, like my_list_1 + my_list_2, if I Run this with Shift Enter, it will just sum this two together. Now let's call my_list_3 again.

As you can see, this is now summed up and as unified as 1. So can we multiply Lists? Yeah, of course, like my_list_1 * 3. So it gives us my_list_1 three times.

So, we see this kind of flexibility in all areas. But we cannot do something that logic doesn't have sense, like we cannot do this, okay, my_list_1 + 5, because, it doesn't make any sense, to sum this, but we can multiply. Can we multiply it with a Float? No, we cannot, because it doesn't make sense to have 5.3 times my_list_1, right?

So, this has the same principles that we have talked before in the strings section. We can multiply this with an Integer, but not with a Float. So can we do it like this, my_list_1., and say reverse, and it will reverse the all array for us, of course, we can do this. Now, this is reversed, like 'c', 'b', 'a', the original one is 'a', 'b', 'c', and if you go here, we have seen that my_string.capitalized return this, but didn't store original one.

So if I do my_list_1, this is now stored in the original one as well, so this is 'c', 'b', 'a'. Again, this doesn't return a new array, it just manipulates the old original one. So, Lists are very, very important, so we're going to spend a little bit more time on it. So within the next lecture, we're going to see some advanced methods and attributes as well.
