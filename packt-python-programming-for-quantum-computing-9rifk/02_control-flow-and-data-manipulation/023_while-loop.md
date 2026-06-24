# While Loop

- **Course:** Python Programming For Quantum Computing
- **Module 2:** Control Flow and Data Manipulation
- **Lecture #:** 23
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/9CISQ/while-loop
- **Extracted:** 2026-06-22 15:10:11

---

Hi. Within this lecture, we're going to see another loop, called while loop. So let me create a new Notebook and just change the name to WhileLoop, before I explain what a while loop is. So, while loop actually provides us to give a statement to our code, and as long as that statement holds, we are looping through the commands that we write under it.

As you remember, we did do that in for loops, right? In the for loops we actually worked with lists-like objects when we iterate through the elements, and do something for each element. So let me start by creating a new Variable called a, and it's going to be equal to 0. So I'm going to do something with this a, while a is actually less than 5 or 10 colon.

So, what does it mean? It means that as long as a is less than 5, do the following repetitively, okay. So, it's going to do whatever we write down here until a is actually not less than 5. So whatever we write here, like print("hello"), for instance, and, we have to have another line, because, what I'm about to do is just prevent us going into an infinite loop, and, because, if we do that, the a will always be less than 5, and it will start printing hello infinitely, right?

But if I do this a = a + 1, within each loop, it will just add 1 to the a. So within first loop, it will be 1, and then 2, and then 3, and then 5, and then it will be greater than 5 actually. And when it reaches the point of 5, it will stop, because 5 is not less than 5. So it will run exactly for 5 times.

So if I hit Shift Enter over this while loop, you will see that I am going to get 1, 2, 3, 4, 5 hellos. As I said before, started with 0, and, counted up to 5. So let me make this less than and equal to, and just hit Shift Enter here to run this from the beginning, because a is currently 5, and, as you can see, now we have six hellos. So, this is a great way to run some commands while some condition holds, right?

So let us do some more examples with while loops. Generally, people like to actually work with numbers within while loops, because it makes sense, right? So like a is less than 5, while a is less than 5, do this or do that. But, in the real life examples, you can work with lists or strings.

So while loop is actually kind of an if statement. Let me create a list for instance, like (1,2,3,4,5), and, I can say this, right, my_list.pop. And if you remember pop method, and if you put a parenthesis in here, it pops the last element. So it pops the last element, it pops the 5, and if I call my_list again, now, it's not in list anymore.

So I can write something like popping check, right? So let me append(5) again. So my_list is [1, 2, 3, 4, 5], and, I can just add this to a while statement like while 2 in my_list, then colon. Then, I'm going to print something, and I'm going to continue popping this, let me do this with 3, and it makes more sense, because it's in the middle.

While 3 is still in my_list, I'm going to print out something like print 3 is in the list, okay, 3 is still in the list, and you can write whatever you want. And, I accidentally hit Shift Enter, and we went into an infinite loop, as you can see. So what I'm going to do, I'm going to here just click on stop, and it will stop the execution in here, okay. Then, I'm going to write my actual code, like popping code right here, my_list.pop, and it will pop one element out of the list every time while loop executes, okay.

So, it will just pop off 5, 4, and then 3, and the while loop will stop later on. So let me go here and say, Restart the Kernel, because, maybe I think I messed it up with infinite loop thing. So, like, I'm going to go over and say Run Cells from here, and say, Run Cells Below, All Below, and it will run my while loop as well. As you can see, it's printed out 3 in my_list three times.

So, it printed out for 5, and for 4, and then for 3, and then 3 was not in my list anymore, and while loop didn't get around. So, as you can see, we can use this while loop in creative ways also. Alright. So, do we have to wait for while loops to be ended, before we skip or continue for a value.

Of course not, we can use this continue and break keywords that we have seen in the previous lecture before. So, let me create an even number here, like number is 0, and while number is less than 10, I will say, print something, okay, print(number) this time, and then x is actually x + 1. So if I hit Shift Enter, it will just print out numbers up to 10, and I got an error because there is no x, number is number + 1. If I hit Shift Enter, it will start with 0, just up to 9.

So I know this, right? Can I use something like this? Yes, number is +=1, it means that number is equal to number +1. So let me rerun that for you, and this one as well, so we got the same result.

So, we're going to see some kind of examples like this in the following lectures as well. So for right now, let me use some if statement, like if number == 5, for instance. Now, if I say break, what will happen? Let me re-run this and re-run this as well.

If I hit Shift Enter, if it reaches 5, it will break and it won't go along with the rest of the loop, right, it won't go back. Let me hash this out, I will comment this out, and let me run this with 5, and I got the exactly the same result in here. So we can actually use break in while loops, but maybe we can just adjust the while loop to be like this, if we knew what's going on before we start writing while loop, right? So we got two options here, and we can just use it depending on the situation.

So, let me create a new number called p = 0, and let me write something like this, while p is less than 20, print out the p numbers, okay, and just add 1 to p each time. So it will print out 0 to 19 as expected. So, what happens if I want to add something like value of p before here? So let me write this down for you.

So "value p: and +str(p), I have to convert, I have to cast this as string, as we have seen before, because we are writing down a string, right? We are printing as a string, not an integer anymore. So let me re-run this, and we see that value of p is 0, 1, 2, 3. So it's a good way to have a print with some extra explanation before it, but there is a new way to do that, starting with Python 3, so let me show you how to do that as well.

So we say print, and before we write the string, we just write down f and then quotation marks, okay. This means formatting. So I can say value p, okay, value p, and open a curly braces in here and write the variable name in here, like p. So, my Variable name is p.

And, if it was number, for instance, I would have written number inside this curly braces. So, this is the same thing like we do in the above line, like printing value p + str(p), this is the same thing, okay. So let me re-run this, and you will see we got exactly the same results in here. So, let me put some more piece in here, in order to make this clear.

So value of p p p, 1 2 3 4 5 6. So, we can use this formatting with while loops in order to have clear explanations, within like Lists, numbers, etc. So we're done here. Let us stop here, and within the next lecture, we're going to see some useful and essential Python commands.
