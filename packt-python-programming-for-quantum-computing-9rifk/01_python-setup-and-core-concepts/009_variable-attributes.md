# Variable Attributes

- **Course:** Python Programming For Quantum Computing
- **Module 1:** Python Setup and Core Concepts
- **Lecture #:** 9
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/hRGA5/variable-attributes
- **Extracted:** 2026-06-22 15:07:38

---

Hi. Within this lecture, we're going to learn about some attributes and methods of Variables. So let's start by marking down and saying ## and string methods, for example, okay, if I hit Shift Enter, it will create a new line for me. So, within this new line, I will create a Variable, and I will show you some options, some attributes, some methods of that Variable.

Let's suppose it's my_name, and I will create a string called "Atil", that is my name, you can do it your own name, okay. So, let's say my_name., if you place ., it will show you the respective attributes of that Variable, but in Jupyter Notebooks, it doesn't show you directly, you have to click on Tab or Shift Tab on your own keyboard. If you click Shift Tab, it will give you some description, okay, if you click Tab, and I just placed Shift Enter rather than clicking Tab on my keyboard, so let's Delete this Cell from here, and let's write it again, my_name., and hit Tab, and it will open the different options, different attributes, that you can change actually, in this Variable. And this is a long list, let's choose the first one, capitalize.

And, the capitalize means that capitalizing the first letter, and my first letter is already capitalized, so, let's make it smaller and hit Shift Enter again, if I Run capitalize right now, as you can see, it just capitalized my first letter for me. Let's call my.name again, and let's call it properly my_name again. And as you can see, this is now not capitalized, even though I asked for it to be capitalized, it returned me the output, but it didn't change the original one. So what do I do?

If I want to sort this capitalize thing, again, to reach out, again, in another code, for example, I can create a new Variable called my_name_capitalized, for instance, and Save it to my newly created Variable, right? So, let's hit Shift Enter again, and let's Run this as well. Now, if I call my_name, it won't be capitalized, but if I call my_name_capitalized, and hit Shift Enter, it will be capitalized. So, it may sound confusing right now, why didn't it change the original one, but, why did it give out a new one?

So I will explain this later on in future lectures where we'll deal with functions. But for right now, let's go and see other options, other attributes that we can play with, okay. So if you hit . and hit Tab again, you will see some other options, let's find another one.

Let's work with split, for example. And, in order to work with splits, let's create a new Variable or change our Variable to, two words actually, Atil Sam, for instance, okay. You have to have two words in order to make split work, because it will split this, and I will show you how, let's choose split from here, and if you choose split and open parenthesis again, and hit Shift Enter, it will split it into two words, okay, and this is now actually a list, but I'm not going to go over this list right now, but as you can see, if I call my_name again, it will come up as one word, but if I want to save this to another Variable, I can, of course, do that, my_name_split = my_name.split. Now, if I call my_name_split, this comes out as a List.

So, you don't know Lists, you will learn in the following lectures. But you can reach out each single element in a List. So if you want to get Atil, for instance, you may want to say, 0, and if you want to surname, you may want to say, 1, and this is indexing, okay, like we did in the strings section as well. So, I think you get the idea that Variables have attributes and methods, and you can call them just by adding a data afterwards, and hitting Tab and choosing whatever attribute, whatever method that you are looking for, okay.

And, let's do some more examples, but let's do that with Integers this time, because, every data structure has its own attributes and methods, of course. So let's create a my_number which is 123, okay, and this is an Integer, not a string, so don't place it in quotation marks. So let's see this options in here. As you can see, there are much less attributes or methods compared to strings, okay.

So, you may want to try this, you may want to do some options from here as well, or you may want to go to the previous example and try to do some other stuff from strings as well, I really suggest it, like, upper, let's do upper, and you will see it will upper all the letters in a string. And the general idea is how do I know all the attributes, or all the options? Of course, I don't know all of them, okay. And, where should I get information about it?

If I go my_name., and choose a method or an attribute that I'm curious about, like split, then if I hit Shift Tab, at this point, it will give me some description, like we did before, right? So in here, I can see the Docstring, this is documentation string, which explains how this works. So it says that, Return a list of the words in S, okay. So I can see how this works, how this methods and attributes work, by hitting Shift and Tab in here, but this is specific to Jupyter Notebook, so let me show you another thing.

If I go to Google, and search for Python docs or Python documentation, it will pop open this 3.7.2 Documentation for me, okay. And this is official Python website. So let me Zoom in, not to Zoom Out, and this is official Python website, so, I can search for whatever I want, and find detailed information about it. So, let's suppose that I want to work with strings.

And as you can see, there are some versions in here, and, you may want to learn about versions or general Pi term, whatever you want, you will find it here, trust me. But for example, I want to learn about strings specifically, then what do I do? Then, of course, I can go to Search in here and search for strings, right? So, let's search for strings, and it will list some options for me, I will choose the first one, and I will see the string class or string Variable in here, and I will see the attributes, methods, and I can find whatever I'm looking for about strings in here.

So, if there comes a point that you cannot find or you're not certain what to do, or which attribute you want to get or which method you want to choose, you may always go here and read about it. One of the best things about Python is that you have a lot of resources on the Internet, and that is why Python is very popular, so popular at this days, and you have to take advantage of this, okay, you have to read the documentation, you have to search for libraries and modules and packages, and, don't worry, we will see what they are in the future, but you have to read and understand each word, because, unlike other programming languages, Python has very proper decent documentation in here. So let's go back to our example and see some other things that we can do with strings for the last time. So what if I want to combine mathematical operations with my strings?

For example, if I want to multiply "james" by 10, by 10, can I do it? Of course. If I hit Shift Enter, it will print out james a 100 times. But remember, when we deal with Integers and Floats, we couldn't multiply a string with a Float, right?

And, yeah, we cannot do that because it doesn't make sense to have a 10.5 james, okay. So, it won't multiply, even if I delete this and hit Shift Enter again, it won't do it, and I get the same error that we got before. But if I want to multiply it by 10, then it's okay, because it makes sense, it's logical, it will just write james 10 times. So what else can I do with strings?

Do you think we can sum, we can add some strings to another. Of course, we can do it, but we cannot sum a string with an Integer, right, so it doesn't make sense, let's try to do that with james and 5, it says that it must be str, not an int. But, if I convert this string into an, this Integer into a string by surrounding it with quotation marks, if I type Shift Enter right now, I will get 'james5'. So it actually adds the strings together.

If I type james and lars, it will give me an output 'jameslars'. So, it may come in handy, right? Let's suppose that you have a name, and you have your surname as well, so, let me type my, Samancioglu, and Shift Enter. So, if I want to get my full name right now, I can add my_name and my_surname together, and, this is very helpful.

Let's run it. So, it added, and let's call my_full_name, and I will see my_name and my_full_name. What if I want to have a space in here? Of course, I can do that, Shift Enter, Shift Enter, Shift Enter, and I will have the space.

Or, I could have, let's delete this and, Shift Enter, and in here, let's add a space, actually a string, which is a space, which contains a space, and then Shift Enter, Shift Enter, now, I have the same result. So, other than that, can I divide a string into 2 or into 5 or 7? For example, let's try that. Let's say my_name or "james" / 2.

Of course, it won't work because it doesn't make any sense. All you can do is to multiply it. So we're done here, let's stop here, and within the next lecture, we're going to work with Lists.
