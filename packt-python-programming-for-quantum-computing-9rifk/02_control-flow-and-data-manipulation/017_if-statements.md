# If Statements

- **Course:** Python Programming For Quantum Computing
- **Module 2:** Control Flow and Data Manipulation
- **Lecture #:** 17
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/hJkNy/if-statements
- **Extracted:** 2026-06-22 15:09:06

---

Hi. Within this lecture, we're going to see If Statements. That is to say, we will check if a condition holds, if a condition is True. So I'm going to create a new Python Notebook in here, and let me Rename this as IfStatements.

So actually, we did a quick introduction in the previous lectures, right? We have seen some Booleans, and we actually check them to see which one is greater, right? But we didn't write a condition, we didn't say, if one is greater do this, and if other one is greater do that. So, in this lecture we're going to see how to do that exactly.

Let me just write an example, like if 3 is greater than 2, and we have to put a colon at the end. So this means actually, if this condition holds, if this condition is True, then do the following. And in order to specify the following, I hit Enter. And as you can see, now I have an indentation in here.

So I have a space of Tab, and the code starts from this place. So this is very important in Python. Whenever you want to create a coding block, like we do in here, we have to use the indentation, and, it always guides us to use this indentation. So, in other programming languages, you see this curly braces.

So you write some conditions under curly braces, and this is a coding block in other programming languages. But in Python, we do that with indentations, okay. So this space here is very important, and you shouldn't read that, because, we write what will happen if this condition holds under this if block, and we specify the block of code with spaces. So, so long story short, the spaces indentation is very important to Python, and we have to follow the guidance of this Jupyter Notebook in here.

So if I say print, and if I write something like 3 is greater than 2, or whatever you want, actually, okay, so let me write this, just "3 is greater than 2", and hit Shift Enter. And as you can see, we get the output of "3 is greater than 2". And the reason that we are getting this output is, 3 is actually greater than 2, and this if conditional, so if I write "xxx", then I'm going to get this x, okay, so it doesn't matter what I write in here. Whatever happens here, will get executed if this condition also, let's say, print, and, as you can see, if I hit Enter, we start at an indentation again.

So, let me write some other print command in here, like print("3 2 1"). Okay, so if I hit Shift Enter, then I will get atil samancioglu and 3 2 1. So, what happens if this condition does not hold, or what happens if we actually work with the Variables? So, let us do a real example here.

So I'm going to create a number Variable, again, and let me say x is 5 and y is 4 for this example. So what I can do, I can check to see if x is greater than y, and with a colon, and if I hit Enter, then I have my indentation in here, and I will say print("x is greater than y"), okay. So, "x is greater". Let me hit Shift Enter in here, and we will get this x is greater.

But, what if I want to specify the case that y is greater. Then, this condition will not hold, and this print statement will not get executed, right? But what if I want to tell the user, y is greater. Because, if I change the y to be like 6 right now, this won't get executed at all.

So there is a way to do that actually. So let me hit Enter and I deleted the indentation again. So I'm going to write else. And this literally means, if this condition holds, just print x is greater and else, if this is not the case, just say "y is greater".

And please pay attention that, this still gives the same output, so x is greater. So, let us change the values and see if this works. So, let me do this like 3 and 4. With Shift Enter, I re-run all the cells, so, y is greater.

So, the first condition is not True anymore. So this print execution in here does not get run, but the as execution gets run. And, you see the point of indentation this time clearly, right? So, indentation in under this x is greater than y just works if that condition holds, and else if it doesn't hold, the indentation, under else, below else, is executed.

So they're kind of like separate coding blocks, and they get executed if the condition is [unclear]. So let me show you another case, if x is 4 and y is 4. So, if we run this, we still get y is greater, because why, x is not greater than y, so else is getting run. But y is actually not greater, so our program is not working properly.

So we have to add another condition in here, saying that if actually x is equal to y, right? So we do that by saying elif, so this is the short version of else if, okay. So elif x is equal to y, I will say print x is equal to y or "x is y". So, this will get run if I hit Shift Enter, so I have an invalid syntax, because I didn't actually run the condition in here, so x == y, okay.

Remember we used double equal sign here, so now x is y. So, x is 4, y is 4, so our program is working smoothly. So we can have as many elifs as we want, so we can add as many conditions as we want in here with elifs. And else, if none of this conditions hold, then we can use else to specify what will happen if none of the above is True.

So I suggest you play around with this values and print values in here, but, we're going to go deeper and see the other conditions in the following lectures.
