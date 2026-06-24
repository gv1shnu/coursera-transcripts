# Lists Advanced

- **Course:** Python Programming For Quantum Computing
- **Module 2:** Control Flow and Data Manipulation
- **Lecture #:** 26
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/9Ng7y/lists-advanced
- **Extracted:** 2026-06-22 15:10:44

---

Hi. Within this lecture, we're going to cover some advanced methods regarding Lists, okay. So let me mark this down by saying list advanced here. And, actually you're not going to use this very much, but, you can come across when you're browsing through Internet, or GitHub, or some Python code.

So, it's better that you know what this means. So let me create a new_list, but initially it will be empty. And remember, then we say, new_list, and this will be an empty list, then we could have said, new_list.append, and append to 1. Now if I call new_list, it will be a list containing 1, right?

We have learned about this before. So let me delete this lines, because this won't be my real example in here, I just wanted to show you, remind you how this works. So, let me go up here, Edit, Delete Cells. So now, what I actually want to do is to create a new_list, an empty list, and create a string and get that letters out of that string, and append them into a list.

So, like, my_string is "metallica", for example, and I want to get every letter from that string using for loop, of course, for element in my_string, with a colon, new_list.append(element). And, as you might guess, it will just take metallica and append them in a list as individual element. So, if I call new_list, as you can see, now I have all the letters appended as a list. So, this is not advanced, of course, we have seen this before, but there is a representation, an advanced representation that will do the same thing in a one single line, okay.

So let me write this down for you. So new_list will be a list, and, this will be element for element in my_string. Don't worry, I will explain what this does. So if I hit Shift Enter right now, and if I call my_new_list, I will see the exact same result.

So, what's happening here is actually the same thing with that code, right? So let me explain what's happening in here step by step. So I'm creating a new_list and I'm casting this whole thing as a list in here, right? So I'm creating a list out of that element for element in my_string thing.

And element for element is in my_string, means that go to my_string and take every element as element, okay, take every element in that string and cast this to a Variable called element, and append that element in a list. So, what happens if I want to change that element? Let me create a new_list and you will understand it better. Let's work with numbers this time, number for number in my number list, so I don't have a list, so let me create with list and range in here, and we get an error because I didn't say in, I said multiply, okay.

Let me say in. And if I call new_list_2 right now, I will see that it's appended to my_new_list. What if I want to just take this numbers and cast it to a Variable called number, but then, append this as a change value, like multiply all of them by 5. Then, I would have said number * 5 for number in list, okay.

So this is just a representation of for loop in a one single line. And if I say like this, it will just take to power to the 5, and, this is practical, as you can see. As I said before, maybe you won't use this very much in your own programming, but you may come across this, and, in order not to get you confused, I just wanted to show you that this methods exist, and you may, of course, use it anytime you need it. So we are done with useful methods part here.

Let's stop here at this point, and within the next lecture, we're going to cover Sublime Text Editor.
