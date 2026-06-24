# Class

- **Course:** Python Programming For Quantum Computing
- **Module 3:** Functions, OOP, and Advanced Topics
- **Lecture #:** 36
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/A5WEx/class
- **Extracted:** 2026-06-22 15:12:31

---

Hi. Within this lecture, we're going to cover a subject called object oriented programming. So maybe you have heard this term before, right? But, you don't know what it means.

So I'm going to explain what it means and how we can integrate this object-oriented programming things in our software. So if you Google object-oriented programming, you will have like a thousands of results back. And, I'm just showing this to you as an example, okay. I just googled it and opened the first page that came across.

So this is Wikipedia. And if you analyze these pages in here, it just mentions that objects and some properties of object-oriented programming, like inheritance, polymorphism, and, there is a lot to learn about object-oriented programming. But you don't have to just read all of this, I'm going to cover most of them in this section. So I'm going to create a New Python Notebook from here, and I'm going to Zoom in a little bit and change the title of this Jupyter Notebook to OOPClasses, okay.

So the main thing that we are going to learn first, is the classes. So what is a class? We started back with Variables, okay. It was actually the smallest part.

So let me mark this down. We're going to cover class right now. As I was saying, the Variables was the smallest part in our program. And then we moved to the functions, right?

So, we took this Variables and put some of them in the functions when it's necessary. So functions were actually a little bit bigger than the variables, right, rather than just writing this Variables down in here as a plain text, we just moved some of them into functions. So you can think of class as the biggest part where it surrounds everything like this Variables, some functions, methods, everything, okay. It's the biggest structure architecturally that surrounds all of this things.

And when you write something like this, like my_list is a list object. It means that it create an instance of the list class. So, this is actually a class. It defines, what type of object that will be created when we do this, okay.

So we create an object, we create an instance. So let me mark this down for you. So we will cover this instance, and you will hear me use this term class, object, and instance together all the time, because they are inseparable. So, we will create our own class and we will create our own instances, so you will understand it better, don't worry.

For right now, this terms may seem vague to you, okay. And remember when I did this, my_list., I see some methods and some properties. And we haven't talked about that before, but some of this properties, actually all of the properties are called attributes, okay. So let me add this to our heading in here, so this is attribute.

We define this attributes, we define what kind of options that our object can get in our classes. And, we define actually the methods, functions, that work with our object in the class as well. And we will do all of this things, later on. So, right now, let me show you how to create a class, how to create your own class, rather than working with the old lists, dictionary, some kind of built-in Python classes.

So, all you have to do is just use the keyword class, and then you give the class name. And, please be aware that I am using a capitalized word right now. And I haven't done this before, right? So there are actually a few conventions in programming, not only in Python, but I'm talking general.

So there is a thing called snake case, okay, and something like this, like we're using right now. So, it's my_string. And there is a thing called camel case as well. So in camel case, you use my and then String and start the second word with capitalized letter, okay.

And in classes, we kind of follow this camel case, but we just make sure that first letter is camel, first letter is uppercased as well. So, sometimes this is called Pascal cased, but, just don't worry about this names or conventions. All you have to know is that classes are so important, we are just writing them with uppercase all the time. So, if I had written MyMusician, it would have been like this, MyMusician and uppercased.

Well, I'm going to go with the Musician, and open parenthesis, close parenthesis, and the colon. So this is basically the same thing with defining a function. All I did was, rather than saying def, I said class, and, then I used an uppercased word. Now after that, in here, I had to define a function right now.

And, this is called a special function. What's so special about this, it starts with two underscore and then init, and then two underscores as well, and then open and close parentheses, and then a colon. And don't worry, I'll tell you all about this. So this is an init function, an initializer function, okay.

When we create an instance of our class, when we create a musician object, this special function will get called first. So whatever we write under this function, will happen when we create a new instance. So if I say MyMusician is a musician, it will call this function first and do whatever I write here. So we generally define the attributes under that function, because this is the first thing to do when creating an instance.

So, other thing that you should know is that you have to write self in here, you have to write self in every function in a class. And functions in class are called methods actually. You have to start with self, and self refers to the instance of this Musician class. So self actually refers the little MyMusician object.

And thus, we can reach the MyMusician object, like my_list object in here with self keyword. Don't worry, you will understand better with examples. And then after, as a regular function, I can just write whatever inputs that I'm going to take. Like I'm going to take name and age input, because, I'm going to assign this name and age input to be attributes, and we do that by saying self.name.

So, why do I do this? So, self refers to the instance. And, if I want to create a new attribute, all I have to do is just say self.attribute name is now this, like self.age is now age. So I think this got too confusing if you're just learning about programming.

So, let me show you with an example, my_musician is a Musician, okay. And if I hit Shift Enter right now, it will give me an error, because, it will say me, init missing 2 required positional arguments. We didn't specify the name and the age, so let's do that, "James" and 50. So if I hit Shift Enter, now my_musician instance is created.

So let's see my instance, my_musician.tab, and it will give me age and the name, And, if I call age right now, and if I call name right now, I will get the current values that I have assigned, so init function actually worked, okay. So if I call age, I will see the 50, as expected, and if I call my_musician.name, of course, I will see 'James'. So, can I change this name for instance? Yeah, my_musician.name is "Lars".

And if I hit Shift Enter, and if I call this one more time, like my_musician.name, then I will see 'Lars'. So, I can play with my attributes, like I did when I played with my_lists, okay. Now I have created my instance, but let's go back here and understand it better. So, why do we have three names in here, name, name, and self.name.

Actually, these two are the same thing, right? We give, we take this input, and we assign this to be an attribute. So, this two names are actually the same, but the attribute name is not the same. So, actually, this attribute name could have been something different, like name attribute, okay, self.age_attribute.

Then this names are same, and this two ages are the same thing, and, it really doesn't matter what I call the attribute. So if I hit Shift Enter, Shift Enter, now I hit Shift Enter here, it will give me an error. Why? Because, the musician object has no attribute age anymore.

So, the real name is now age_attribute. So if I hit Shift Tab, I will see the age_attribute, and it's 50. If I hit Tab again, I will see the name_attribute here and it's 'James'. And, I don't have to do that with name, but rather name_attribute.

I can also set the name_attribute to be something else, and it will be name_attribute again. So, the attribute name is different than the input and the assigning value. But for convention, people always use this three, the same keyword, okay. So I will use the same keyword as well, but now you understood the logic behind it.

So rather than saying name_attribute, people, programmers, software developers, generally follow the same convention, same rule, to say this name, and say the input name, and the assigning value, name, as well. So if I add the third input in here, like an instrument, okay, musicians have instruments, right? So, I can say self.instrument is actually the instrument that I got from the user. So let me do this, for example.

So if I call Shift Enter right now, it says that instrument is missing. Now I have to add the instrument in here, like a "Guitar", okay, Shift Enter. Now, it shouldn't be the age_attribute, because we changed it. It should be only the age and not the name attribute.

So let me delete this and hit Shift Enter to update this. And, let's say my_musician.name or instrument this time, let's call this, Shift Enter, my_guitar, and let's delete this, okay. And now I think you know the basics of classes, instances, and attributes. Now let's stop here, and within the next lecture, we're going to learn how to create methods inside of this classes.
