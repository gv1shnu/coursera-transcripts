# Variables

- **Course:** Python Programming For Quantum Computing
- **Module 1:** Python Setup and Core Concepts
- **Lecture #:** 5
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/xFOTB/variables
- **Extracted:** 2026-06-22 15:06:51

---

Okay. Since now we know about the Integers and Floats, let's dive into the Variables. So we cannot go on with pre-defined values all the time, because we may want to change the numbers as we go along. Because why, because maybe you need an input from the user, or maybe you need an input from the Internet, okay, so you're going to download a number and store it into a Variable.

So we store some values into the Variables, so that we can reuse them anywhere, anytime we want, and we can change them afterwards, in anywhere, anytime we want, when we try to code, okay. So we are multiplying 0.5 with 3, in this case, maybe this number will need to be 4 at some point, maybe you're dealing with a user age number, okay. So, user age will increment in, along the way. So we don't want to just write 3, or 1, or 1 million in a single code most of the times, but rather, we want a variable, we want a value that we can store those numbers into, we want to change it, or we want to reuse it in anywhere we want.

So let's do this. What I'm going to do, I will just sum 3 and 5 together. And then later on, let me Markdown this, and write Variables in here and hit Shift Enter, let's do this with Variables. Let's say that x is now 3, okay, and y = 5.

Now, whenever I call x, I get the value of 3 in my code, whenever I I call it y, it will give me the number of 5. So if I type x+y, it will give me 8. For example, if I want x to the power y, it will give me 3 to the power 5. Okay, so as you can see, now, I can use x and y in the code whenever I want.

So I defined x as 3 in here. So if I want to change this value, can I do it? Of course I can. Now, I can say x is now 4.

And from this point on, x is now 4, if I just say x+y, it will give me 9 instead of 8 anymore. So whenever I change the value, from that point on, the value is 4 actually. Let's do an example about this. Let's say, we get an input of radius of a circle from the user, and I want to find out the circumference.

Okay. And as you know, the circumference is 2 Pi r, the radius. And how do we get the radius from user? We call a method called input.

Okay, so if you type input and open a parenthesis, it knows that it has to ask for an input. If you just print, okay, we used the print methods before, right? So, it printed out something. And, as you can see, it shows in green, it means that it's a built-in Python function, okay, Python method.

So input is something like that, and Python knows it has to ask for a user input in this case. So if you say r = input of something, it will ask for an input from the user, and, it will just set the r value to the user input. And, whatever you write in here, within quotation marks, it will display as a message when asking input. If you hit Shift Enter, it will say r is, and this is where the user actually use the input.

For example, let's give 5, and now, r is equal to 5. Now if I want to just multiply r, 2, and 3.14, for example, and 3.14 is Pi, actually. As you can see, we get an error, okay. It says that, can't multiply sequence by non-int type of 'float'.

So, when you get an error, what do you do? You got the error message here, right? So, if you don't know what this means, what you can do, you can Copy this and open Google, okay, and just paste the message here and hit Enter. And, most probably, you will end up with a website called stackoverflow, and any other resources for Python as well, let's go into stackoverflow, and let me Zoom in a little bit.

As you can see, stackoverflow is a great website where developers share the solutions with each other. So you ask a question and people try to help you for free. And, there are tons of questions that are asked before, so there is a pretty good chance you will find whatever you are looking for, okay. So, for example, I found out the same error message that we are getting in stackoverflow, and if you go down, if you go below, you will see it has 6 valid answers, and people are trying to help each other and trying to make people understand the problem.

Okay, so of course, you can browse the other questions, other resources from Google as well. And don't worry, I will explain what this problem is in a minute. But, for general programming purposes, I really suggest you to look for stackoverflow results in Google, and try to understand the error message that you are getting, okay. So let's go back to our code, and the problem is here, is that r is not an Integer or a Float, actually, r is actually a string.

And, whenever a user gives an input, it is stored as string, a text. We do not see strings yet, we will see in the next lectures, but just know that they are basically texts, okay. So how could I know that? If I had written type and pass x as an argument, it will give me out an int, okay, so if you want to learn about type of some Variable, you will just say type(x).

And, let's, for instance, define our pi number, 3.14, in a Variable, and if I type, type(pi), it will give me float, because this has decimals, and x is 4, so it's an Integer. So let's try r in this case. So if I just call r, it will give me '5', but see, this has quotation marks. So this isn't actually an Integer, this is a string.

So if I type, type(r), and hit Shift Enter, it will say that it's a str. So, how can Python multiply a string with a Float? So, if you want to just multiply Jack, for instance, with 5, maybe you can multiply it because you can just write Jack 5 times, but you cannot write Jack 3 and Pi times, 3 and 3.14 times, okay. So, it doesn't make any sense.

So if I want to multiply x and pi, it's okay, because they are both numbers. But, in our case, we need to make sure that 5 is stored as a number, not as a text, because, we don't have capability to multiply text by numbers, especially with Floats, okay, and we will see that in detail in the following lectures, but, for right now, know that you have to store this as an Integer, and in order to do that, I will create a new Variable called r_int, and this will be Integer version of our r string, and in order to do that, I will just write int(r), okay. So this is known as casting. And if I call r_int right now, it will give me 5, and if I call type(r_int), it will give me int.

Now, I have an integer, and I can find my circumference in, that was my point in the first place, right? So now I can multiply r_int with x and with pi, without getting any errors. And please note that this is known as casting, we casted the string to be an integer. So let's try to multiply all of this together, and we get the final result, okay.

So, now we have learned about storing values into variables, we learned about different types of, actually numbers, and different types of data structures, and what can or what can't we do with them. Don't worry at this point because we're going to learn much more about them in the future, but I just wanted to show you a preview. Now, in the next lecture, we're going to see how we can download and open this Python Notebooks.
