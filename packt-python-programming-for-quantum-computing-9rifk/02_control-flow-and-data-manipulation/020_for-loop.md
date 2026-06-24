# For Loop

- **Course:** Python Programming For Quantum Computing
- **Module 2:** Control Flow and Data Manipulation
- **Lecture #:** 20
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/iZ8gn/for-loop
- **Extracted:** 2026-06-22 15:09:38

---

Hi. Within this lecture, we're going to learn about something called for loops. So let me create a new Python Notebook from here and rename it, while I'll explain to you what a for loop is. So for loop actually provides us opportunity to execute an operation with each element in a list.

So, we will be working with Lists mainly. And let me create a list here and demonstrate an example, so that you can see better. So my_list = 1 to 5. And, I'm going to iterate to this list and perform an operation for each element in that list, okay.

So I will take 1 and do something, and I will take 2 and do something, and I will take 3 and do something. So here's how to do it. As you can see, we are writing for number. And this number is a variable that we are creating right now, so we can name it whatever we want, and, we say in, and as you can see, this is green as well, so this is a built-in Python function in my_list.

So, what I'm saying here is that take each number in that list and assign them to be a Variable called number, okay. And, as I said before, you may even call this whatever you want, maybe you can call this number, numbers, anything. So if I say print("atil samancioglu") right now, what will happen? If I hit Shift Enter, then, it will print this for each element.

And it doesn't really make sense right now, because why? Because we are not doing anything with the numbers inside of that list, but as you can see, it has written down atil for 5 times. So it has written down, it has executed this print comment for each element in that list. So, if I said print(number), then it will have been printed this, as you can see.

So let me do a real example, like for number, or let's call it item this time, for item in my_list, okay, colon, and I'm writing that code block here and going to work with item right now. So what I want to, I will perform an operation on that item, like I can multiply it by 5, I can divide it. So let us create a new_number out of that item and call it item * 5. So let me print that new_number and hit Shift Enter.

What do you think will happen? Of course, it will multiply each item in that list and print it out for us. And, this is the main idea of working with for loops. So, with a single line, you can actually create this for loops and execute a complex or a simple on a whole list.

So, what did it do, it just took 1 and multiplied it with 5, and, it just took 2 and multiplied it 5 again. So, it went on as long as list went on. So, let me create a new for loop in here, like for number in my_list, and let me do an example with remainder this time, so it might help you in real life examples as well, and we have learned about this remainder thing before, I hope you remember it. If you don't, let me show you let me just write down print("hello") for this to go away, Shift Enter, and let me show you what the remainder is.

So, if we did this 10 remainder of 2, it will have given us 0. So this gives the remainder after dividing operation like 10, the remainder of 3 is 1. So, if we do something like this, if we calculate the remainder, and if it is 0, then, the number is even, and if it's not 0, the number is odd. And we can find the even numbers in a list, right?

So actually you can pause the video in here and try to do this on your own. All you had to do, come up with an if statement in here. I hope you managed to get it. All you had to do was if number remainder 2 == 0, then it's even, right?

So you can just write print number for here, under the if statement. And as you can see, we have a new indentation right now. We are under the second indentation, second tab in here, first one is for, for loop, and second one is for if statement. So we have to write down our code in the second indentation, and all we have to write is print(number) and Shift Enter.

So, what happens? It just went to the list and divided 1 by 2, and the remainder was not 0. So, it just kept 1, and it didn't print it. So, it just went to the 2 and divided by 2, and the remainder was 0 again.

So, it printed out 2. And, so it worked up all the way to the end, and we managed to find the even numbers. And, for another example, in the previous lecture, we said something like this, right, if 2 is in my_list, then print true. And 2 was in my_list, and it printed out true.

So, how can we do that with for loop? for number in my_list, if, let me call this num this time, if num is actually 2, print("true"), right? So this is a way to do it, this is harder actually. But, in order to understand the logic behind for loop, you may use this kind of exercise as well.

And another question might come to your mind at this point, can we use for loops with strings and Tuples? Of course we can. Let me show you how to do that. Let me create a string, my_string, is "James Hetfield", okay.

So Shift Enter, and I can iterate through the elements in that list, because I can say my_string(0), and it gives me the first element, right? So it acts like a list. So if I say for letter in my_string, okay, so you can call this letter or an element, it doesn't matter. And all you have to do is just print(letter) and hit Shift Enter, and as you can see, we get each individual out of that string.

And, can we work with Tuples? Yeah, of course, we can, because they're kind of lists, immutable lists. So let me create a Tuple here (1,2,3), and all we have to do is just get this into a for loop by saying that for item in my_tuple, then hit a colon here and print out the item. Of course, I can do more like multiply this item with 5 and hit Shift Enter, and subtract 10 from this and Shift Enter, and we got the result back.

This for loop actually is very helpful when working with lists, and, you're going to face this problem, face this issue where you have to work within a list, iterate through each element. Remember, if you come across this kind of a problem, you have to use for loop. So let's stop here and within the next lecture we're going to see some more advanced usages of for loop as well.
