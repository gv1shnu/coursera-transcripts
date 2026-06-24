# Zip and Random

- **Course:** Python Programming For Quantum Computing
- **Module 2:** Control Flow and Data Manipulation
- **Lecture #:** 25
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/nFRcz/zip-and-random
- **Extracted:** 2026-06-22 15:10:33

---

Hi. Within this lecture, we're going to continue learning some very useful methods and essentials of Python. We're going to continue with the random first, okay. So let me choose Markdown from here, and write this as a heading random.

So, as its name suggests, random method, lets us create random numbers, or, other some random operations. Why do we even need that? Maybe you want to write a game using Python, and you need a random number, or maybe you're just creating another software, and you need a random number between 1 and 10, for some reason. Actually, we come across this kind of problem in real life situation often.

So, Python has a library built in for random as well. And we can use this library, we can use this module package, and we will see what they are in the following sections, don't worry if you don't know what a module or package means, we will use that random. And, in order to use it, we will say import random, okay. And, this import means importing some kind of package or external library to our own project.

But in this case, we only will need random, so I will say from random import randint, okay. So we're just taking a portion out of that library actually, because we only read random integer right now, and we will see some other modules as well. Random integer lets us create random integers, it's rare later. But how do we do that?

We have to give either range, okay. So all we have to do is just say random int or randint and open parenthesis, and say, 0,1000. So it will create a random number between 0 and 1000. So if I do this one more time, with the exact command, like you see, we get some different results, because they're completely random.

There is a very small chance that you get the same result over and over again. So, what can we do more with random? We can shuffle some Lists. How do we do that?

Let's suppose we have a list of my_list_2, and this is again, list(range(0,10)), okay. And if you call my_list_2, you will see that this starts from 0, and all the way up to the 9. But, I want it shuffled, I don't want starting from 0 to 9, maybe I want 5 4 9 7, I don't know. So if we import from random import shuffle, and, if we say, shuffle(my_list_2), like this, shuffle(my_list_2).

And if we hit Shift Enter, now, my_list_2 is shuffled actually. Now if I call my_list_2, as you can see, now, this is randomly distributed, rather than consequently increasing. So we can use this, and this will come in handy when you will face this kind of problems in ethical hacking programming, okay. So, let me Markdown another method for you, and this is called zipping, okay.

So, like this. So how do we, why do we use it anyway? We mentioned that you have multiple lists, and you want to combine them together. So we can use the zip method in order to do that.

Let's suppose that we have three individual lists, and we want to create a new list, combining all of this elements. Maybe we can achieve that by writing very complex for loops within nested each other, right? But we don't have to do that actually, because, we have a built-in function that does that easily without struggling the program, without having to consume too much RAM for us. So let's suppose I have a sport_list in which I have running, swimming, and let's say basketball, for instance; "run", "swim", and "basketball".

And in another list, we have some calories_list, okay. So, maybe you're running is 100 calories, and swimming is 200 calories, and basketball is 300 calories. And, let's suppose that I'm writing a fitness app, and I have a schedule here, like day_list, like "monday", "tuesday", "wednesday", okay, so I'm assigning some support to the consumer, to the user, and I'm letting the user know the calories of that list. But for some reason, I don't have dictionaries, because this is not actually a pair, but I have three individual list.

So if I say zip(sport_list, and calories_list, and finally the day_list, it will zip it and save it in a memory location, okay. So this is where it's saved in my computer. But, in order to get this as a list, I had to say zip, as a list, then, let me just create a new_list Variable and say Shift Enter. Let's see if I can get that.

I won't get that, because I still didn't convert it into a list, I didn't cast this as a list, right? So, what do you do if you come across this kind of a problem? All you have to do, go hover over the zip, and hit Shift Tab, and you will see the documentation, and you will see this will return some zipped object, okay. So this is a zip object, not a list.

So, yeah, I had to cast this as a list in order to make this work, right? So, when I'm creating that new_list, up here, not down in here, but up here, all I had to do is just say new_list and cast this as a list. And if I hit Shift Enter right now, my new_list will be actually a list. Now, as you can see, I have all of this combined together, and, I can reach them easily by creating a for loop, right?

Now I can just place them into the user as one element. So, let's do that for element in new_list, with a colon, print(element), and it will print out the individual elements for us. So I think we are done here. Let's stop here, and within the next lecture we are going to see some advanced method of Lists.
