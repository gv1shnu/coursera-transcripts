# Inheritance

- **Course:** Python Programming For Quantum Computing
- **Module 3:** Functions, OOP, and Advanced Topics
- **Lecture #:** 39
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/9bRVb/inheritance
- **Extracted:** 2026-06-22 15:13:03

---

Hi. Within this lecture, we're going to cover inheritance. So inheritance is actually a very important concept in object oriented programming, and let me mark this down, so we can just refer it later on. So, this is spelled as inheritance.

So this feature actually lets us reach the classes from another class, okay. So let me tell you what I mean. So I have a class called Class1, for instance, let's keep this class very simple, okay. I will call this Class1, and my other class, Class2.

So within this Class1, I, of course, have my init method, okay. So, let me write self in here. And all I do in this init method is just print Class1, okay, or ClassCreated, whatever you want. But let's just keep this very simple, because, I want to focus on inheritance only.

So as you might remember, init method gets called when the instance created, okay. So I will just call this "Class 1 created", and I will just create another method in here and call this method_1, and I have to write self in this as well. And all I will do is just say, print("method 1"). And, after that, let me create one more and call this method_2, and, of course, add self and say print "method 2", as expected.

Now I'm done with my Class1, and it's a very simple class, if we create an instance like this, my_instance is Class1, okay. If I hit Shift Enter, then, the init function will get called and it will print out Class 1 created. Now if I say my_instance., I will see the available methods. And for method_1, if I call this, I will see method 1.

And, of course, if I call method_2, I will see method 2. So, for right now, we have created our first class. But what happens if I want to create another class? Let me just create this, class 2, and use some of the methods that I created back in Class1, in Class2 as well.

Do I have to write it from scratch, or can I just import or inherit this methods in here? Of course, I can inherit. For example, I have to have an init function, init method in here, right? So let me just write this def __init, and put self in here.

Let's say that I want to import the Class1 init, method, okay, and I don't want to change anything. So what do I do, how can I inherit this methods back in here to my Class2. It's very simple, actually. All you have to do is just come here inside of the parenthesis, and write the class name that you want to inherit from.

So I want to inherit Class1, okay. And now, I can call Class1 methods down here. Now, what do I do? I will just write Class1.__init, okay, and say self, of course.

And this means that just go and call the init method inside Class1. Let's print out something else like "Class 2 created" in order to see this both works. So let me create another instance this time, and this will be Class2 instance, okay, and hit Shift Enter. As you can see, I got Class 1 created from this line over here, and then Class 2 created.

But I didn't write down Class 1 created in Class2, I inherited it, okay. So, if I type my_instance_2 and hit . and Tab, I will see I am available with method_1 and method_2 in here. If I call this, it will say method 2.

Now I can reach method 1 and method 2 from a new instance of Class2. That is where inheritance come into play. So, can I add more functions or methods in here? Of course.

Let me create a "method 3" method, okay, and hit Shift Enter to re-run this. And now, on top of my method_1 and method_2, I have method_3 here, as well. So it's very cool. If I go back and call my_instance, my previous instance, I only will see method_1 and method_2, whereas I have the reach of method_3, in my second instance as well.

So, when you deal with this Class2, now I have all the methods in scope, whereas I have only method_1 and method_2 in instance 1. So, when you deal with a little project, a small project like this, maybe it doesn't make much sense to you. But in a big project where you have, like dozens of classes, then inheritance will help you a lot, because you can just use the methods that you have written before. It's not just a matter of copy and pasting, but also preventing some changes and using it originally by just adding some inheritance code in here.

And, for further reference, you can overwrite the existing methods like this. So you can say, def method_1(self) print("method 1 override"), for example. And, even though you inherit the Class1, and even though you call my_instance_2.method1, then, since you have overridden this, and it gives me an error, because I think I misspelled it, I had to put an underscore here, it won't just say method_1, it will just say method 1 override, because I have overridden it. And in my original instance, if I call method_1, I will only see method 1.

So, I hope it made sense to you right now, and, let's stop here, and within the next lecture we're going to cover some special methods.
