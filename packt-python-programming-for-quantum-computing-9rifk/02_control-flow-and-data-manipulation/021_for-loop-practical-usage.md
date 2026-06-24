# For Loop Practical Usage

- **Course:** Python Programming For Quantum Computing
- **Module 2:** Control Flow and Data Manipulation
- **Lecture #:** 21
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/crseQ/for-loop-practical-usage
- **Extracted:** 2026-06-22 15:09:49

---

Hi. Within this lecture, we're going to continue learning about for loops, and we're going to focus on practical use just this time. So we have seen how to work with Lists, now we're going to focus on more complex usages of for loop. So let me create a new list, called my_new_list in here, and it will contain some Tuples.

So let me create Tuples with strings in here, like "a" and "b" is going to be one Tuple, and "c" and "d". And, I think you understand how this is going to work. I will create four Tuples in here, and mind the parentheses and quotation marks in here, like parentheses, quotation, and comma quotation as well. So, what I have in here is that a new_list with a Tuples of strings in them.

So, how can I use for loop in here? Of course, I can just say for elements in my_new_list, let me call this my_new_list and a column in here, and if I say print(element), then it will just print the Tuples in here. But, what will be more practical if I just cast them this element to be a Tuple as well? What do I mean?

Rather than saying elements in here, I could have said for tuple in my_new_list, but naming the variable tuple isn't going to make it. So you had to specify this will be a Tuple by just creating a Tuple Variable in here, like (x,y) is in my_new_list, and now, if I say print x or print(x, y), it will print out the Tuples again. So this gives us the same output, but, what I can do now is just say print x rather than x, y. So I can just reach the first element in Tuples.

So I reached "a", I reached "c", "e", and "g". So, this is pretty, right? I can just take out the elements as Tuples and I can do that, print(x) and print(y). So, I don't have to go nested for loop in here, like do one for loop for Tuples, and then just do another for loop for inside that Tuple as well.

I can just say for (x,y) in my_new_list, and take this elements as Tuples in a single line, single for loop. So, this is pretty. So let me show you another thing, with my_tuple_list, let me create another list, and this time, this will have numbers in it, and this will be triple, like (0,1,2), (3,4,5), and like (9,10,11). So, can I do this (x,y,z)?

Of course we can. So for (x,y,z) in my_tuple_list, and with a column, of course, I can say print(x), and it will take the first element out of that each Tuple. So this will be helpful when working with Tuples. And let me show you how to work with dictionaries as well, because we didn't see them in the previous lecture, right?

So, let us create a new dictionary, called my_dictionary this time, and this will have a key value pairing of "key1", and the "key1" has value of 100, "key2" has value of 200, and "key3" has value of 300. So, this is my_dictionary. And, if I can say for, and how do I cast the dictionary elements in here. So I can reach my_dictionary items by saying my_dictionary.items, right?

So if you hit tab in here, and you will see all the things like items, keys. If I call items, it will give me dict_items as in here, like 'key1, 100, 'key2', 200. So I can use the same thing in dictionaries as well. All I have to do is just say for a,b in my_dictionary.items, okay, and hit a column in here and say print(a) for instance.

If I hit Shift Enter, it will give me just all the keys, and if I hit print(b), it will give me all the values. And so I can say, for key and value in my_dictionary, and it will make more sense. So print(key), it will give me all the keys. And don't be confused because of this parenthesis thing.

So I didn't use a parenthesis in here, but I used before, so I could have used in here as well. So it really doesn't matter. So if you can just clear the parenthesis from here, it will still work. So decide whatever you want in here.

So let's stop here, and within the next lecture we're going to see something called continue, break, and pass.
