# Functions Advanced

- **Course:** Python Programming For Quantum Computing
- **Module 3:** Functions, OOP, and Advanced Topics
- **Lecture #:** 33
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/OtidJ/functions-advanced
- **Extracted:** 2026-06-22 15:11:57

---

Hi. Within this lecture, we're going to learn something called arbitrary argument and keyword arguments, okay. So let me mark this down for you, and you see how it's written and how it's pronounced, and then I will explain what they are. So first, we will use, we will learn arbitrary arguments, and then key word arguments, okay.

This arguments actually let us work with more than one argument. And we actually did that in the previous lecture, right? So we did a summation with three numbers. But what if I wanted to do it with five numbers or six numbers, or whatever user chooses to do?

So it is easy to do it with two numbers. So let me create a summation_2 function in here, in which we will have num1 and num2 as input, and all I want to return is num1 + num2, okay. This is easy. So what happens if our user wants to add in a third input, then I add num3.

But what happens if user changes his mind, or her mind, and actually wants to sum two numbers? Then, we are going to use these arguments, arbitrary arguments, okay. So how do we do that? We will use the sum built-in function of Python first, in order to have a meaningful structure here.

Remember, before, we have messed with the sum, and then change it back to summ, right? So there is a sum built-in function. So let me just show you how it's done. So we say *args here, and then we say sum(args).

So we're going to sum up these arguments that our user has given to us. So let me try this a bit; (10,20,30), and I get an error, okay, and says that, this has to have in a positional argument of 'number 2', and I think this is why we shouldn't mess up with the built-in functions of Python. So, it kind of broke the original function when we first define this sum function up there. So what I'm going to do, I'm going to go over here to Cell, or Kernel first, I'm going to Interrupt this, I'm going to Restart everything from the beginning, and I'm going to re-Run this Cells, and re-Run the Cell All Below, okay.

So, I didn't mess up with the sum function right now. So it should work properly. So this is defined as summ. So, my_sum function is how it's originally built right now.

So as you can see, now this works. So, let me try this one more time with much more arguments, (50,60,70,80), and it sums up all of them. So it doesn't matter right now, how many arguments user gives, okay. Let me show you what's going on behind by creating a *args function, all it has to do is just printing the arguments.

So if I say my_func and (10,20), it will just print out the arguments, okay. It just takes the arguments and does whatever we want to do with it. So let me try this "a", "b", 1, 2, it just takes it and prints them out. So, this arguments thing, lets us work with multiple arbitrary arguments.

So do we have to call this *args? Not actually, but for convention, we generally call it args, okay. But if we don't, it will still work. So let me create a new func_2, okay, my_func_2 is (*atil), this time rather than args.

So, if I print atil right now, it will still work. So let me try this, my_func_2("at", "il",1,2,3), for example. As you can see, it still prints out the arbitrary arguments. But I really don't suggest you to change the args keyword here, because, this is Python convention, and other programmers might not understand what you're doing at this point.

This is just to show you that it works both ways. So I'm going to just make this into a command line here by adding hash and rerunning this cells. Another subject that I mentioned at the beginning of this lecture was the keyword arguments. And they let us to create keyword pairings with values like in dictionaries, when we get an input from the user actually this time.

So, best way to explain this through an example again. So let me create a function with keyword arguments this time. So, this will be an example_func, and I'm going to put two stars right now and say kwargs, okay, kwargs. And again, this time, this two stars actually matter, and kwargs doesn't matter.

So, I could have just name it atil or anything I want. So, let me print out this keyword arguments and let me show you how this actually works. So, let's call our example_func. Now I have to give some keyword, and key and value pairings actually.

So, I'm going to go with the same example that we were doing in the previous lectures, like running is 100 calories, and swimming or basketball is 200 calories. Remember, the example, right? swim=200, and basketball=300 calories, okay. If I hit Shift Enter, as you can see, it printed out the keyword arguments for us.

So it just takes in input as a key and value pairings and do whatever we want with it. So if I say example_func(a=1,b=2), it will just print out this key value pairings. But how do we use it in real life examples? So maybe we want to check something is in the keys or values.

We can do that, right, with a function? Of course, we can. What do we have to do is just create a new function with keyword arguments, and then have an if statement within this function, with the function indentation, and check whatever we want. At this point, actually we don't know how many arguments, how many key and value pairings are user going to give, but we know we can control one of them, right?

So, let's call this keyword example or keyword function, for instance, okay, so keyword_func, and it will have an input of kwargs, and then I will check if the Metallica is inside one of the keys. How do I do that? I use an if statement, of course. All I want to say just if "Metallica", and with a quotation, of course, because this is a string, if "Metallica" in keyword argument, right?

You remember in, so, if "Metallica" in kwargs, then it means that the user has given Metallica as input or key. So, print("Heavy Metalll!"), for instance, and else if or else, if Metallica is not in here, then all I want to do is just print out "Rock is dead!!", for instance, okay. So I'm checking whether the Metallica is in the kwargs, and if it is, I'm going to print out "Heavy Metalll!", and if it's not, I'm going to say "Rock is dead!!". So let's try this keyword_func, and let's start with Metallica, and Metallica will be 10, Madonna will be 20 or 5, I don't know, let's say Muslum is actually 4.

So it says, Heavy Metalll!, so it works. If I didn't include Metallica in here, let's do the Madonna again. It won't say Heavy Metalll!, but rather it will say, Rock is dead!. So let's say Mickey, and we get the Rock is dead!.

So we now know how to work with arguments and keyword arguments. Now we will stop here, and within the next lecture, we're going to cover some practical usage of functions.
