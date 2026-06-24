# Useful Methods

- **Course:** Python Programming For Quantum Computing
- **Module 2:** Control Flow and Data Manipulation
- **Lecture #:** 24
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/5nJkw/useful-methods
- **Extracted:** 2026-06-22 15:10:22

---

Hi. Within this lecture, we're going to learn about some very useful methods, that will make our life easier when we are trying to code some ethical hacking softwares. Actually, not only in ethical hacking, but also in general Python programming as well. So, let me create a New Notebook from here and start learning about this useful methods.

So let me rename this before we start to useful methods, okay, and UsefulMethods, and then click Rename here. So, first, we're going to learn something about Lists. So, as you have seen before, we always need some Lists, right? We create some Lists manually here by saying that my_list is now 1,2,3,5,4,6,7, okay.

And then maybe we do something like for loop in this list, like for number in my_list, and with a colon, print(number). And this works well, right? So, what if there is a better way to create, there is an easier way to create Lists actually. And Python has a built-in method for that.

And, this is called range, okay. So we can create some ranges, and we can use that ranges to just create Lists, okay. What if we have to create a list from 0 to 20, for instance? It will be harder for us to just write every number inside of that list.

What if we need a list from 1 to 1000, okay. So let me write down this as a heading here, range, and, this is how we create the range. So, if you just type range, it will be green, because this is a built-in function. Like if you give it 20, it will create a range between 0 to 20.

So how do we convert this range to an actual Lists? You have to cast that as a list, right? So if I do that, now, it will give me an output starting from 0 up to 19. So, the first index is starting index and the last one is stopping index.

So if I do something like, for number in list(range(20), then with a colon, print(number, it will just, just multiply it by 5, it will just multiply it by 5 and create the new list for me. So, I didn't have to just write every element, every number in that list, it just made it easy for me, right? So let's suppose I wanted to start this from index 5, all up to the way 20. Can I do that?

Of course, for num in list(range(5, 20), okay. So, all we were doing actually was 0 to 20, now I'm doing 5 to 20. And if I hit number, as you can see, now I have a list starting from 5 and stopping at 19. So we can use this, like 5 to 21, if we want to include 20 as well.

So this is the same principle that we have learned in the Slicer's case, starting points, stopping points, and, on top of that, we can use stepping size as well, right? So if I say 3 here, it will have a step size of 3. So, we'll add 3 and skip 6 and 7, then, 9 and 10. If you have 4 as a stepping size, it will start at 5 9 13 17.

So, this is the same thing that we have learned in this Slicer section. Now you have a very powerful tool to make your Lists efficiently. So, let's move on and learn about something called enumeration, okay. So what if you want to work with indexes as well?

So, let me mark down this as enumeration, and actually let me go and select Markdown from here, and start writing again as a heading enumeration, enumerate, okay. So what if I want to get indexes of the current element in a list? Can I do that without any helpful method, without any additional method? Of course we can write, we have the for loop, we can create a new Variable for our index and get the indexes out of each element.

So the first element will be index 0,1,2,3,4, or 5, okay. So, how do we do that? for num in, okay, let's for number in, let's create the list with range, since we have learned how to do that, from 0 up to 10, and, all I want to do is just print the number, and it will give me a list of 0 to 9, right? But what if I want to get the indexes as well?

So, what do we do? We create a new Variable here, okay, like index, and it will start with 0, because lists start with index 0, as we know, right? And aside from number, we can print the index as well. Let's use the formatting that we have learned before.

So place an f in here, and, all I want to do is just number is, with curly braces number, and the index, okay, index is with curly braces, index. And after that, after this, if I hit Shift Enter, I will see number is 0 and index is 0, but index will be 0 for everything, because I didn't do this, index is now += 1. So if I hit Shift Enter right now, now I see the current numbers and current indexes of that numbers. So this is a little confusing.

Let me just change the range from here from 5 to 15, for example, and if I hit Shift Enter, I will see the number 5 is at index 0, number 6 is at index 1, okay, this is more clear right now. So, what does it have to do with enumeration, enumerate method? So enumerate method actually lets us do this operation easily. So, how do we use it?

We begin by creating our for loop again, and we have to create a new list, okay. So let me just say, this is for number in list range(5, 15) again. So instead of printing the numbers and the indexes from scratch, let me just give this enumerate function in here, okay, and close the parentheses, and I have to spell it out correctly, of course. Now, I have given the enumerate function here, it will enumerate this list, and print out the indexes and the numbers for me automatically, okay.

So, let's try this and see how this works. Let me actually correct in here as well, and again, let me actually change this to item or element, doesn't matter, but we were using the number for a long time right now, and hit Shift Enter. As you can see, the element is now enumerated, and we see the index and the number respectively, okay. The first element in this enumeration is index, and the second element is the number itself.

So we have an automatic way to do this, okay. So, let me give you another example using this enumerate methods. What if I want to cast this as a Tuple, like we used to do before? Of course we can do that for index and number, let me just give a parentheses in here.

Of course, we don't have to do that, but I prefer it this way, in enumerate(list(range(5,15))). So, now if I say print(index), it will just print out the index, and if I say print(number), it will just print out the number. As we can see, it start with the index first then the number, index number, index number, okay. So, in that way, you can get the indexes and the elements in a list respectively.

So, let's stop here and continue with the next lecture where we will learn about more useful methods.
