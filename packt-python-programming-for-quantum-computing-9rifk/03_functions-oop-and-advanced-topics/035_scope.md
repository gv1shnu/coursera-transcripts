# Scope

- **Course:** Python Programming For Quantum Computing
- **Module 3:** Functions, OOP, and Advanced Topics
- **Lecture #:** 35
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/YZwkt/scope
- **Extracted:** 2026-06-22 15:12:20

---

Hi. Within this lecture, we're going to learn about a very important concept in Python, called scope. So let me create a new Notebook here and change the title to Scope, okay, while I'll tell you what it is. So scope literally means scope, it's the coverage of Variables, it's the scope of the Variables that we're dealing with.

So what do I mean with that? We can create Variables in general, coding area in here, we can create Variables under functions, and functions under functions, nested functions, and they have all different scopes. So, let me show you with an example. So I created a Variable called number, then I'm creating a multiply function in here, which will take a number as an input, okay, and I will call this num.

Then, all this function does is just create a variable called number, and this is 5 right now, and this will return num * number. So whatever user is giving as an input, it will multiply it by number. However, we have two numbers now, right? We have 10 in here, and 5 in here.

So, which one will be multiplied by num? So, if you said 5, within this example, then, you're right, because, this is under the function, and let me just show it to you. So let me give 10, and, it's going to multiply it by 5. But, what may confuse you right now is the current value of number in here.

So what if I want to print number right now? So, does it give me 10, or does it give me 5, because I already assigned 5 to number in that multiply function, right? But, I also initialized the number value up in here, without doing it in a function. So if I call print(number) right now, and hit Shift Enter, what will I get?

If you said 10, then you're absolutely right. But if you said 5, don't worry, I will explain what's going on behind the stage. So if I call a is 10, and a is 5. So if I print(a), then it will give me 5, because, I reassigned its value, right?

And, why doesn't it happen up in here? Because, I'm assigning this number to return in here and just making it 5 under multiply function only. So how does Python understand what value should it display us, or what value should it consider when calculating something? So there is a rule for that.

Let me explain what it is. So let me mark this down first, and it should be pretty clear for you. So this is LEGB rule, okay, and L stands for local, okay. So, this is an acronym, obviously, and L is for Local, and E is for enclosing, so let me just write all of this down, and I will explain everything.

So E is for Enclosing, okay, and, G is for Global, and B is for Built-in, okay, so a built-in Variable for instance. So Python actually follows that rule when it tries to understand the current value of a Variable. So first, it looks at a Local level, then, it looks at an Enclosing level, then a Global level, and then, at last, for a Built-in level. And I will demonstrate everything with an example.

So let me create a string called my_string in here and call it "Atil" for instance. And after that, I will create another function, and call this like my_func, okay. And within this function, we will have another Variable, which is my_string again, and, I'm only assigning this value under my_func with an indentation, as you can see, and it is now "James". And all I have to do within this function is just to print my_string value, okay.

So this is my_string. And, that's all for right now, later on we will just add something to this function. Now if I call my_func, I will see James, because this is what is assigned under my_func. But if I call my_string, it still calls 'Atil', because, this is Enclosing, and this is Global level.

So let me make it more clear to you. I will add something under my_func. So this is going to be a nested function here, okay. So under my, my_func function, I will create a new function called my_func_2, and, within this my_func_2 I will reassign this my_string again, and reassign it to be "Lars", for instance.

So, I'm going to print that my_string this time under my_func_2 and delete this. And, I have to call this my_func_2 from somewhere, like under my_func itself, okay, because if I don't do this, it won't get called, and it won't be executed at all. So, when I call my_func, it will call my_func_2, and, as you can see, we get the Lars result back, but my_string still calls for 'Atil'. So, it is following the rule.

So let me mark this down here. So this is Local, okay, this is a Local level in here, and it first looks for Local level when it tries to find a value. And this is an Enclosing level. So this is an enclosed function.

And this is a Global level. And as you can see, or as you understood at this point, Built-in Variables are already there when you first work with Python, okay. So it looks for Local, and then Enclosing, and then Global, and if it doesn't find anything, it looks for Built-in, and if it still doesn't find a value, it just shows you an error, says that there is no Variable like that. So it can be confusing at this point, but you have to remember that this works with LEGB rule, and if you're going to use the same Variable, then you have to pay attention to that rule.

And if it is not necessary to use the same Variable, then, you can assign them to be new Variables, okay, like, rather than saying my_string, you can say my_string_2 in here, or, just a relevant Variable name. But if you don't do this, or if you have to use the same Variable for some reason, then, you have to pay attention. So, let me show you another thing. Let me just do it as an example, and just delete the Local one, and, let's see if it can find the Enclosing value, for instance, then we will delete the Enclosing value, and let's see if it can find the Global value, okay.

We still get Lars in here. So, let me just make this a comment in here, so Lars is not executed. So if I hit Shift Enter right now, and if I hit Shift Enter in here, like you can see, it couldn't find Lars in my_func_2, then it went for the Enclosing one. And if I delete the Enclosing one, and if I just re-run the cells, it will show me Atil, which is the Global one, okay.

So, it went for one level up each time, when it couldn't find the value. So let's do it backwards this time, okay. We still have our Global variable in here, let's just undo the Enclosing one. If I re-run this, I will see James, and my_string is still 'Atil' in here.

And if I just undo the Lars, and I will see Lars and my_string still works as 'Atil'. At this point, you might think to yourself that, what if I want to really change the value of a Global Variable, but I want to do it under a function, okay. Can we do that? Of course we can.

So let me show you how to do it with an example. There are several ways to do it, and we're going to cover them. So, y is 10, for example, and I will create a new function in here def func_new, for example, and it will take the y as an input, and it will just print out the y for y, okay. So we will test and build upon this as we go.

So, this will take the y, or we will call just func_new, and it will display 10 to us, right? So, if I say func_new(10), it will display 10, and if I don't say anything, it will display 10 again. So if I do this, y = 5 and print(y) right now, what will happen? So it will just take 10 and it will just print(y), because we have changed y to be 5 inside our func_new.

But, if I call the real value of y at this point, it will still show me 10, because I changed it only under this func_new, only the Enclosing Variable, okay. So, what if I really want to change it to be 5. I could have said like this, right? So y = func_new(y).

So if I hit Shift Enter, actually it doesn't make sense, because we are not returning anything right now, it's just printing out the y, so it won't be equal. And if I would have said return y, then, this will still work. So this is 10 5, and this is 10 5, but now y is actually 5, because it's currently returning y and the current value of y under func_new is 5, because we assigned it enclosingly, but we returned that value to be current Global value. But if it's too confusing, there is a simpler way to do that actually, and we will use that in when we deal with ethical hacking as well.

So, let me show you what it is. We will just order Python to take Global y under func_new. So let me rewrite this again. So y is 10, and I will create func_new once more, and it won't take anything in here, but rather, I will say global y, and, then if I say y is 5, then print(y), it will reassign y, but since I use the global term in here, it will take the global y up under here and it will reassign the global y actually.

So if I call func_new right now, it will print out the y as 5 as expected, but as you can see now, if I call y, the current value of the global Variable is actually now 5. So we can use this technique here, or we can use the global term in here to take global values and put it under one level below, put it in the Enclosing level. So, I think we are done in here. Within the next lecture, we're going to learn about classes.

[No audio]
