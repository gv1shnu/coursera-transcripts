# Functions Explained

- **Course:** Python Programming For Quantum Computing
- **Module 3:** Functions, OOP, and Advanced Topics
- **Lecture #:** 31
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/t0nHf/functions-explained
- **Extracted:** 2026-06-22 15:11:37

---

Hi. Within this lecture, we're going to finally learn about functions and methods. So let me create a New Python Notebook from here and rename it as MethodsAndFunctions, and tell you what are functions actually, and why do we use them. So functions are actually coding blocks, okay.

We write codes that we want to be executed when this function is called. So this is a little bit vague, I know, and you will understand better when we do it in an example. And also, you might be thinking that what's the matter with the methods? So what are the differences between methods and functions?

Actually they are the same thing, but methods are defined in classes, in objects, and we will see them in the next section, when we deal with classes, okay. So right now focus on understanding the functions and their usage areas. So let me show you a little bit of function examples. For example, if I have like this Variable, my_string = "Atil", okay.

Remember, when we deal with strings, we have done this, my_string., and hit Tab, it will give you us many options. And we talked about this before, and some of them are actually methods, right? So if we did like capitalize, or if we did like strip, if we did like upper, it performed, it executed some code over it, okay. So let me do it with upper, because I already have it capitalized in here with a capital A.

So, if I do it upper, and remember, I have to put parenthesis over here. What if I don't put parenthesis? If I don't put parenthesis at the end, it won't execute the function, but it will show us the function, right? So it says that there is a function called str.upper, and, if you want to execute it, you know what to do.

So if I hit Shift Tab in here to see the documentation, it shows me, the documentation shows me the explanation of this, Returns a copy of S converted to uppercase, okay. So I know that if I execute this with putting parenthesis at the end, it will just return a copy of this string upper cased to me. So let's do that. Let's put a parenthesis here, and it will close the parenthesis for us.

If I hit Shift Enter, now I see the 'ATIL' uppercased, okay, but I see an output, right? If I call my_string right now, I still see my_string to be lowercase as it was before. And this is happening because people who wrote this function or method, designed it to be this way. So we have to just assign this to a new variable, like my_string.upper, and if I hit Shift Enter, now it doesn't show me any output, but rather save this output to a new Variable called my_string_upper, okay.

Now if I call this my_string_upper, I will see that uppercase version of this. So we actually have seen this before. Why I'm telling you all about this right now, is that you can write this functions to Save this into new Variables like we did right now. As you can see, this is returning uppercase ATIL, or you can change the original one.

So, it's in our hands actually. But we will see that in a minute. So, for example, how do you know, how do you understand what a built-in function does? So we know that if I go to .Tab, I will see the options, right?

And, if I do Shift Tab in here, for example, let me do my_string.Tab and choose one of the functions in here, like islower, isupper, I'm searching for split here. Let's see, yeah split. If I do Shift Tab in here, I see the documentation. So I see the help documentation, and, of course, I can go to python.org and read the documentation from here as well.

But there is a built-in function for that here, so you can surround this with help, and, this gives you the detailed documentation about this method. So if you just hit Shift Enter, you will see the Help on built-in function split. So this is another good way to deal with functions, okay, built-in functions, because you may think that there are thousands of built-in functions, how can I read that from Python data, or how can I read that from little explanations from Shift Tab, maybe, you're looking for this Help built-in function, okay. So now let's go back to our main subject, how do we use functions?

First, let's see how to create our own functions, because you will understand this much better when you do it in an example. All you have to do is write this, def, okay, so def, and then the function name afterwards. So you can choose whatever you want for function name, of course, it should be relevant, because you might want to remember it later on. So, all I want to do is just write hello_world in this function, so I'm going to call this hello_world, and then after I put a parenthesis here, and with a colon.

So under this colon, I hit Enter, and what I write here with indentation will happen when this function gets caught, okay. So this is like a for loop, whatever you write below a for loop with that indentation will happen when this loop is executed, right? So this is the same principle here. Whatever you write here will happen.

Like if I write print("hello"), and maybe with another line here, print("world"), then, this function will only print hello and world. If I add a new line here and define another function, so, the previous function will be finished, okay. I have to write with an indentation below this function in order to execute my commands in this function, okay. So right now, I am going to call my function, I'm going to say hello_world, I'm not putting in parenthesis at the end.

And as you can see, this is a function stored in main__.hello_world. And we will see what this underscore underscore means later on. So don't worry about that, but our function is stored in our software. So if I just add a parenthesis to execute this function, it will just give me the output that I wanted before.

So I can write this hello_world function once and call it whenever I want in my program, right? So if I want to write hello_world again, I can just call my hello_world function. So this is very helpful. So this is very basic right now, because I'm just writing hello_world, but, maybe, I'm going to have to write like 1000 line code in my ethical hacking programs and call it like three times.

So rather than writing this 1000 line codes, and copying and pasting it, I can just call my function. So, that is where functions really come in handy. And this is not the only way to enjoy functions, actually. There are really important features of that functions that we did not see right now; one of them is taking input, and the other one is returning output.

And that's what we're going to learn in the next lecture.
