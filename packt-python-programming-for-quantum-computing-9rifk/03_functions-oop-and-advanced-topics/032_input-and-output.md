# Input and Output

- **Course:** Python Programming For Quantum Computing
- **Module 3:** Functions, OOP, and Advanced Topics
- **Lecture #:** 32
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/CrD3Q/input-and-output
- **Extracted:** 2026-06-22 15:11:47

---

Hi. Within this lecture, we're going to continue learning about functions, and we're going to focus on getting an input and returning an output, as we discussed before. So let me start by marking this down, and give a heading here with the hashes, okay, so this will be ## input & return, okay. So these are one of the most important reasons that we're using functions.

So let me create a function here, like hello_programming, this time rather than hello_world. So all I have to do is just hit colon here and say print(hello). But again, in another line, rather than saying print("hello_world"), or rather than saying print("world"), I want to say, a programming language and want to get that programming language input from the user, okay. So I want to print out like "hello_python" or "hello_java", but I want it to be given by user.

So I can take an input using a function, right? All I have to do is just come here, between the parenthesis, when I first define this function, and write here whatever I want to take as an input. You can write anything you want, because this will be a Variable, like you can write name, you can write your name, Atil, I will say name, because it makes sense, because we are asking for a name from user, right? So, user will give us this name here, so it will be stored in a Variable, and we will use this Variable here, then we print out the result, right?

So if I hit Shift Enter right now, and if I call hello_programming, and open a parenthesis, now I have to give an input in here. If I don't give an input and hit Shift Enter, as you can see, we got an error saying that, this has a required positional argument, so we have to give it a name. So let's give Python, for example, and hit Shift Enter again. And as you can see, we have this hello Python section.

So, let's say, hello_programming("Java"), this time, and we'll have this hello Java output. And, what if I want to prevent this from crashing, right? Maybe user don't know what he or she is supposed to do, and, just give out an empty input. It will crash now, right, as it did in the previous examples, but there is a way to overcome this problem, and this is a way to give an input with a default value, okay.

So when you create a function like hello_programming again, so I will call this hello_program, and, I will just make this Variable equal to "python", okay. And this will be my default value, but it can be changed by user. So I will write exactly the same thing, print("hello") and print("name"). But now, if I call this without an input, like hello_program ( ) and Shift Enter, now it will write down hello python, okay.

But, if I change the name, or if I give an input right now, hello_program("java"), for instance, now it will print out hello java. So you can define some predefined default values to the input Variables, and the user may change them afterwards when they were dealing, interacting with your functions, okay. Now you know how to get inputs from user, right? Now let's learn about returning outputs.

So we talked about this return too much before, but we didn't see actually what it was. So let me create a sum function here where we'll sum some numbers, so I will get number1 and number2 from user, okay, and, of course, I will sum them and show it to the user. So, this will be like number3 is now number1 and number2 combined, okay, summed, and then I will print out the result. So this is really simple, okay.

So if I hit Shift Enter right now, and if I say sum, and say number1 and number2, so if I sum this, the result will be 13. So, my math function is actually working. Let me try that with a negative number as well, in order to make sure, so, 10 and -500. Yes.

So it gives us the correct result, which is -490. So, what is not working actually is that we are not getting an integer back from here, we are just seeing the result as a string, okay. So, we just see it, we cannot do this, that we used to do in here, we cannot assign this to another Variable, because, it is not returning anything, it's just printing out something for us. What do I mean?

Let me define another function here and call this summation this time. And, actually, I think we have to change this to summ, because summ is actually predefined function of Python, so, we should not mess up with this. So, let's re-run this with Shift Enter, and now let's create summation function, and, within here, within the summation, I will get num1 and num2 again, I will call this num1, num2, and let's call num3, and get three numbers at once. So, within the summation function, I will sum up three numbers.

But I will return this time num1 + num2 + num3. So what does return do? Let me show you, (10,20,30), and if I hit Shift Enter, now I get 60. Now, this works pretty well too.

So what is the difference between returning and just printing out the result. So, let me do this, my_result = summation, okay, (10,20,30) again, and if I call my_result, I see the 60, because it's returning something, and in here, in def summ, we didn't return it, we just printed out. So, let me demonstrate this. my_integer is now summ(10, 20), okay, so it turns out 30, but, if I call my_integer, it won't return me anything.

Because, if I call type(my_integer), I will see NoneType. So, this is nothing, actually. Because why, because we are printing out the number, and, when I called this summ, it just printed out the result, but, it doesn't return anything like we do in here in summation. So it's just printing out like this hello_world program, okay.

So, I cannot assign this to a Variable. I'm just seeing the result, but I cannot assign this to a Variable. So it is important for you to define what you will do with a function, okay. So if you're going to need the results later on, it is better for you to return the result and not just print that out.

So, let's move on to another example. Can we do, like if statements in functions? Of course, we can, we can do everything in functions, they are piece of code blocks. So, let me do an example here, like def control_string, okay.

And I will take a string as an input, like say, s this time, okay, and I'm going to control this s. And if the first letter of this string equals to m, then I'm going to make this m capitalized, uppercased, okay. So, there is a way to do that, right? May we pause the video and try to do it yourself.

I hope you got it. All you had to do is just s(0), and take the first letter out of that string, and control if this s[0] == "m", okay. So if this is actually m, then we're going to say print out "mm", for right now, for just an example. Let's check this out, control_string.

Let's give it something else, like "paris" for instance, and, that doesn't start with m. So, if I do this, I won't get any print. Let's do this with metallica for this time, control_string("metallica"), and I got out mmm. So, this works.

Now I can just do whatever I want, like I can make this capitalized, I can print m manually, right? So, try to do it on your own again. So let me copy and paste this in here, and if this s[0] == "m", I want to capitalize this m, and actually printing out the big M won't work, because, this will give me only an output of capitalized M, right, I won't see the rest of the string. So, what I want to do actually, not printing out this, but printing out s.capitalize, because I know that string has this method.

So I have worked with this functional method before. So if I hit Shift Enter right now, and let's try this with control_string again, and let's give it "metallica" one more time, and we will get out to Metallica capitalized, okay. So let's try with something else, like "amsterdam" this time, and we won't get anything in return. As you can see, functions have great tools to work with inputs and outputs, returning outputs.

I suggest, we stop here right now, and within the next lecture, we're going to continue with advanced functions.
