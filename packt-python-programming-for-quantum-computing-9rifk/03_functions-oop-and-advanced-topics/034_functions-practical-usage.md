# Functions Practical Usage

- **Course:** Python Programming For Quantum Computing
- **Module 3:** Functions, OOP, and Advanced Topics
- **Lecture #:** 34
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/66Pwi/functions-practical-usage
- **Extracted:** 2026-06-22 15:12:09

---

Hi. Within this lecture, we're going to learn about some really cool, built-in functions of Python that will work well with functions. So let me create a new Notebook from here and change the name to PracticalFunctions, okay. So, this will let us work with functions more efficiently in our project, what I'm talking about.

So let me create a new function for you, and, let me show you what we can do it more efficiently with that function. So our function will be a divide function, okay. So this will be a simple function, it will just take in a number as an input, and, just divide that number with 2. And, of course, we have to return this to get an output, right?

So if I say right now divide(10), for example, it will give me 5. So, what if I have, like, a lot of numbers in a list, like this? So let me create a list here, [1, 2, 3, 4, 5, 6, 7, 8], and, what if I want to apply this divide function to my_list, okay, so I have to divide 1,2,3,4, and 5, and up till the end. So, feel free to pause the video and do it on your own.

Okay, I hope you managed to do it. All you had to do is just to create a for loop in here, like for num in my_list and divide(num), okay. So, it will create a loop here and it will just divide everything by 2, of course. But we didn't print it, so we couldn't see the output.

So let me just wrap it around the print function in here and say, Shift Enter. As you can see, it divided everything by 2, and we got the result back. But what if there is a better way to do this without having to create a new for loop, for instance. We have this in Python, a built-in function called map, okay.

And we're going to see how to use it and apply lists to functions, or apply functions to list, to be more exact. So, let me mark these down first, choose Markdown from here, and, give in a hash and a heading, okay. So our heading is map. So, we will use map like this.

So write map and open a parenthesis, and all you have to do is just give the function and the list that you want function to be executed on, okay, it's that simple. So, if you just Shift Tab in here, you will see the documentation as well. So it gives in a func and iterables. So iterables mean, you iterate through something.

So, we generally iterate through a list or list-like objects, but we are going to do it in a list. So, you have to specify the function, which is divide, and then the list, which is my_list. If I hit Shift Enter right now, it will just calculate everything and save it on a memory space. So, this is saved at this space on memory, okay.

But, of course, I can just convert it to a list, and hit Shift Enter. Now, I have my results back in here. So, I have exactly the same result as above. So I did it in 1 single line.

Actually, what it is doing here is to create a new list here, like my_new_list, okay, let me do it as an empty list. Then, rather than dividing and printing this, it just appends this results to a list, so my_new_list.append, and then later on, when it's finished, when the for loop is finished, it's going to print my_new_list. So if I hit Shift Enter, you see now I have the exact result in here. So while I did in 4 lines up here, is done in 1 line down here, okay.

So map is really good, but you have to be careful with something. As you can see, we didn't put parenthesis at the end of divide function, like we generally do, because, putting parenthesis at the end means that executing this function. If we don't put a parenthesis, you see that your function is here, but if we put a parenthesis in here, it won't understand what we are trying to do, and it will give us an error, because all we have to do is just give the function name, not execute it inside this map function in here, okay. So you have to give just the function name, not with a parenthesis, not with an execution inside of a map function.

So, can we use map with string functions as well, like functions that control strings? Of course. So let me do our classical example here, def control_string, and this will take in a string as an input, okay. And, with that input, it will just check that if string in, or if Metallica is in string, okay.

So, in string, then if this is true, maybe we can just return True or print something, yeah, this is True, okay. So I will just return True. Of course, if you want, you can just print something in here rather than returning True, okay. So, let me just check this out.

So I will say control_string, and like "Metallica", and with some nonsense in here, and if I hit Shift Enter, then this works, it will return True, but if I say Metal, it won't return True, okay. Actually, I think we should do it like this. Rather than saying if "Metallica" in string, just return "Metallica" in string and just delete this return True thing, because, "Metallica" in string is actually a Boolean, right? It is either True or False.

So, if I do it like this, it will return False, so I can see the False values as well, and if I change it to Metallica, it will return True. So, we did this before, you know how it works. So Metallica in string actually returns as a Boolean. So, now, let's suppose that we have a list of strings, and within that list, we have some Metallicas and not Metallicas.

So let me create that list first. So, my_artist_list is "Metallica", for instance, and "Madonna", and just write whatever you like in here, like "Queen", okay. And let me add something else, "Megadeth", and add one last thing like "Muslum" or something, okay. So if I hit Shift Enter, now I have my list, and I want to just convert this to a list and apply this control_string function to my list.

So, can I use map, let's try and see. So, control_string,my_artist_list, and as you can see, yeah, we can use this with strings as well. So it works both with integers, strings, and whatever you want, as long as you supply a function and a list to it. So, we now get the result of True, False, False, False, False.

So what if I want to get this elements that are True in a list, for example, if it really contains Metallica, then I want to take it and add it to a list. Of course, I can do it with for loop or something, but there is another built-in function. So, let me show you what it is, it's called filter, okay. So, if we filter out this results, it will search, within my_artist_list, that's containing Metallica.

And, it will only display the result in a new list that contains Metallica or that contains whatever we want to contain, okay. So we can just specify this in our control_string function, and it will just filter out the result and apply it to a new list. So, let me just show it how it's done. So all you have to do is just create a filter function in here, like map, and, we have to specify the function name again, so this is control_string, and, of course, the list itself.

So, if you run this, it will just save it to your memory, and if you cast it to a list, you will see that it only displays ['Metallica'] this time. And it doesn't make sense, let's add another Metallica in here, like "Metallica2", and it contains Metallica as well. So, Shift Enter in here and in here. And if you hit Shift Enter in here, you will see that it displayed a list, which contains "Metallica" in string.

So, now you know two great built-in Python functions, which is map and filter, and, if you use them when they are necessary, then you will be doing a more, much more efficient job than doing it on a single for loop. So now let's stop here, and within the next lecture we're going to learn about something called Scope.
