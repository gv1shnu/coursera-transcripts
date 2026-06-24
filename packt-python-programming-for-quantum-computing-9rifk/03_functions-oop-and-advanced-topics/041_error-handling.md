# Error Handling

- **Course:** Python Programming For Quantum Computing
- **Module 3:** Functions, OOP, and Advanced Topics
- **Lecture #:** 41
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/aNS18/error-handling
- **Extracted:** 2026-06-22 15:13:25

---

Hi. Within this lecture, we're going to see how to handle errors. Even if we don't have any flaws in our code, we have to expect to see some errors, and we have to know how to handle them. Because, maybe your user can give some false inputs, and, maybe it will lead the program to crash, but we don't want that to happen, so we have to know how to work with errors.

So let me create a New Notebook from here, and, let me just give it a name, let's call this ErrorHandling, okay, and let me Rename this. So let's suppose we have to get an input from user in order to make a calculation. So let me create a summation function in here as usual, and, within this summation function, we will ask for two numbers from user, (num1,num2), and we will return num1 + num2. So, this is a basic sum function, right?

We have seen this before. So let's get some input, so x will be input 1, so let's say "Enter number: " to user, and ask for an input, so user will give 10, and let's for, let's ask for a y, this is the same again, input("Enter number: "), okay, and user will give something like 20, then, we want to sum this two numbers, but if I say x and y right now, it will return me '1020', because why, because we didn't convert them to be integers or numbers, they are just strings, right? Remember the input function? So, all I had to do is just say, x_int, and convert this, cast this to be an integer, okay, and say y_int is again int(y), then, if I call summation(x_int, y_int), then it will really sum up these two numbers and give me 30.

So we know this, we have seen this before, but, let's suppose the user will give a false input, okay. So user has given some right inputs like 10 or 20, but users cannot be controlled. So, they can just say, james in for a number, right? So, if I say james here, and even if I give a real number in here, it won't convert this to be an integer, right, because this james doesn't make sense to be an integer, it isn't a number.

And, as you can see, my app, my software has crashed at this point. And I didn't even get to the part that I converted y_int to be an integer. It just crashed, and nothing is happening right now. So let me do another example, let me delete all of this, and let me do it in one line, actually.

So let's suppose I have another function in here called numberpower, okay, and this just takes in a number, 1 number only, num1, and returns num1 ** 2, okay. So it just multiplies number with self. So if I say numberpower(3), for example, I will see 9. But, if I want to say numberpower, and get a user input like this, okay, a = int(input, okay, ("Enter a number: "), and if I say a to 10, and, let's say, james, it won't convert this to be an integer, it won't even calculate the int, it won't even just assign a value to a.

So, what do we do? Let me write down the things that we are going to cover next. We are going to see some keywords like try, except, and finally, and we will use this keywords to handle errors. We first try this, okay.

So if I say try: and hit Enter, and beware, we have an indentation in here, we will first try to assign this value. So we will first try to convert this to be an integer. And if we have an exception in here, I will say except, and I will say, whatever will happen when we get an error, okay. So I will say print("Enter a number"), for example, and I will just use some exclamation points to be angry with the user.

So, if a user gives 10, then it's okay, but if a user gives james, then, I will say Enter a number to user. So, I don't even have my number at this point. If I say type(a), it gives me an integer, because I think, yeah, if you just call a, it still thinks a is 10. But, we didn't.

If we just say my_int in here, and we define it for the first time and say james, now if I call type(james) or my_int, sorry, then I will get an error because my_int is not defined, it doesn't even see my_int as a defined variable in here. So let me delete this. So the point is, I didn't get a crash, even though I said james, right? So my program goes on.

I get an error, but I handle this error tastefully, so, my app doesn't crash, so user can actually continue to use my software. And we achieve this by using try and except. And if I do this infinitely, then, I will ask user to give a real number. And how do I do this infinitely?

I take all of this code inside of an infinite while loop, okay. So all I have to say is just while True, for example, or like while 1 is greater than 0, so if I say while True, and if I choose all of this and hit Tab, then it will be low, it will be below this while loop with an indentation, it will try to convert this to be an integer, and if it fails, it will go to except and print("Enter a number!!!"), okay. And, then, I will say continue, because I want my loop to be continue if I get an exception. And then, I can use an else.

So I don't have an if in here, why else? It means that try, and if you get an exception, just print this and try again, maybe this time you will succeed, then, go to the else here, okay. So else will get called. Now I can say print("OK") this time or something.

So if a user finally gives their input as an integer here, I want this loop to be ended, so I will call break rather than continue. And we have that finally word here, and this will get called whatever happens, okay. So, it really doesn't care, it will get called every time. So let me give you an example and you will understand it better.

So Enter a number. If a user actually gives a number, it will say, OK, and finally. So, this is OK, and finally will get called any time. So except, we didn't get any exception.

So let's say james again, and see an exception. It says that Enter a number!!! and finally gets called again, so it really doesn't make sense, but this gets called every time, and we get another chance to give an input for a number, okay. So this is actually working right now.

We handled this error, and, we used except, try, and finally, to be able to not crash the software. And so if I say lars again, it will ask for a number again, and say Enter a number, if I give -10, it will say OK and finally. So I can customize this messages here and create a real good error handling setup. And you don't have to use finally, for example, I'm just showing it to show you that it actually exists, and if you want, you can use it, but if you don't, if it doesn't make sense to you, you may not use it.

But for right now we know how to handle errors. So, we can just continue using our program when we come across with errors. We'll use this while True and try, except thing a lot in ethical hacking parts as well. So let's stop here, and within the next lecture, we're going to cover some modules and packages.
