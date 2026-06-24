# Special Methods

- **Course:** Python Programming For Quantum Computing
- **Module 3:** Functions, OOP, and Advanced Topics
- **Lecture #:** 40
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/Ywu5r/special-methods
- **Extracted:** 2026-06-22 15:13:14

---

Hi. Within this lecture, we're going to cover something called special methods. And special methods are actually built-in methods that are predefined before. And we have seen some of the special methods, we have seen the init method, right?

So it gets called whenever an instance is created. So let me call, let me create a New Python Notebook from here, and let me Zoom in a little bit, and then change the name to SpecialMethods. And this can be called Dunder methods or Magic Methods, as well. So, let me create a new class and tell you all about it in this example class, and I'm going to call this Fruits, and within sides, of course, I will just start by writing down my first special method, which is init method, okay, I have to say, self, then, let me just give a name to my fruit, and then a calorie as well.

So we will just get name and the calories, and I will say self.name is name, and self.calories are actually the calories, okay. So we expect to input from the user. Let me just create this class in here and let me create a new instance and tell you later on. So, this is my_fruit, and if I just hit Shift Enter, it will just give me an error, because I didn't specify a name.

So name will be a "Banana" and the calories will be 200. So, if I call my_fruit, I will see that this is inside my main, okay. This is stored in a memory, at a location like this. So, if I call my_fruit., I will only see the calories and the name.

So, if I call calories, of course, I cannot execute it, I have to call this way, then I will see 200. But, what if I want to print my_calories or my_fruit? Then, I will get a message like this. So, this is like, this is saved here.

And if I just say len(my_fruit), then I will get an error saying that this fruit has no len method, okay. But I have this in other instances, right? So, if I create a list, for example, like "a", "b", and 1 or 3, then, I can call print(my_list) and it will print out the list itself, right? And, we have seen this before, we have used this before.

If I call len(my_list), it will just calculate the numbers of elements inside a list, so I get 3 as an output. But how do I get this print and len function built-in special methods inside my class? So I have to use this magic special methods in order to specify what will happen when the user calls print and len. So, in order to write down the print, I have to use something called _str_.

So, let me say self and, like this. So, whatever you write below this _str_ special method, it will get executed when you call print(my_fruit). So, whenever you call print, it will just look for a special representation, string representation of the related instance. And you specify what will be the string representation of that instance inside of that special _str_ method in here.

So you can write down whatever you want. And, let me just do it like this. If you call str(my_list), you will get the same result as print(my_list), because print looks for the string representation of the class, of an instance. So if I say print("example"), in here, it will just write out example, or, you can say, of course, return "example" as well, it will return this, okay.

So, let me just say Shift Enter, Shift Enter, and if I hit Shift Enter, as you can see, we get out the example in here. So what if you want to say the name and the calories of this related instance, particular instance. Of course, you have to use this formatting thing that we have seen, just start with f, then the quotation marks here, and you say name, and this has something calories, okay. So you write down calories in here as well.

So, it will be like Banana has 200, okay. And if I hit Shift Enter, now, it gives me an error, because the name is not defined. You have to say self.name and self.calories, of course. So let me hit Shift Enter once more.

And now I have Banana has 200. Now I have defined this, I have specified that you have to print out this when you say, print(my_fruit), okay. So you can just write down whatever you want in here. And for len, all you have to do is just say, def __len__ (self).

And in here, you can return anything you want as well. For example, you can just call self.calories, okay. So, now, if I re-run all of this, and below here, if I call my_fruit or len(my_fruit), then, I will get the calories. And, of course, you can just say, hello as well, but, it has to be relevant, because it won't make sense.

So, maybe you are thinking right now, how do I know this special method, okay, there has to be more than one, right? So if you go to Google, and if you just search for special methods of Python, or Python special methods, Python Dunder methods, Magic methods, and if you hit Enter, as you can see, there is a list of that, you can just go to any result in here and search for it. For example, as you can see, What are Dunder Methods? We see like _init_ or _str_, they give the same examples as well, but if you go below, you will see some other examples in here.

So you can look for the other Dunder methods, and, just search and take whatever you need at that particular class, okay. So we have plenty of them, as you can see, and I suggest you Google that out and search for it. So, let's stop here. And within the next lecture, we're going to see how to handle errors.
