# Methods

- **Course:** Python Programming For Quantum Computing
- **Module 3:** Functions, OOP, and Advanced Topics
- **Lecture #:** 37
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/lgQhI/methods
- **Extracted:** 2026-06-22 15:12:42

---

Hi. Within this lecture, we're going to cover how to create methods inside of a class. But before we go on with methods, I will show you a way to create default attribute values for class instances. So we already defined our attributes in here.

But suppose that we have an attribute that are preset, and we don't have to take this from user. Maybe user can change it whenever he or she wants, but we have to give it a default value. Can we do it? Of course, we can, and, we don't have to do it under init method, because this we already predefined when the class is, the instance of a class is created, okay.

So, I can think of an example for this. So, our class is a Musician class. And, let's suppose that we have an attribute called job, okay. So the job, the occupation of a musician will be always a musician, right?

So I can just assign this to be musician under here, before I go to init function. So, let me Shift Enter all in here. And, if I call my_musician.job right now, as you can see, it's already in here. If I call this, it will be 'musician' by default, even if the user didn't specify it.

And if the user wants to change this, can he do it? Yeah, of course. If I call this right now, it will be 'singer', okay. So this is how you can create default valued attributes in your classes, okay, you don't have to get it from user, you don't have to put it under init function, you have to put it under the class and give it a default value.

So now let's move on to the methods, okay. So we now know how to create attributes, how to create instances from a class, but we always talked about this methods, functions that are built inside classes. So how do we create functions, how do we create methods inside class? So it's pretty easy, it doesn't have a difference from creating a regular function outside of a class, okay.

But they are called methods this time. So, I will use def again, and then I will choose the function name or method name as sing, for instance. And, in here, I have to write self again. Because why, because this self refers to the instance, and you have to use self inside of every function, every method in a class, because you may want to give a reference to the instance, right, and we will do an example about this as well.

So, whatever I write under this method, like print, let's sing some song like, we are the champions, for instance, okay. So let's say, "We are the champions!". Whenever an instance calls this method, it will print out, "We are the champions!". So let's try this.

So I'm hitting Shift Enter to re-run all this cells. And now, if I say my_musician.sing, and as you can see, sing is in here. And, of course, I had to put parenthesis at the end, because if I didn't, it will say that this is a method, it's inside of this musician object and everything, but if I call this parenthesis, it will execute the method, and it will say, We are the champions!. So, we didn't use self, right?

So how do we use it, how do we refer the instance from a method? So, let's suppose that I have to write out the instrument of the instance inside of my singing method, right? So, let's use this formatting that we have learned before, and let's open a curly braces in here, okay, at the end. And inside of this curly braces, I had to write down the instrument.

So, let's hit Shift Enter, and, if I hit Shift Enter to my_musician.sing, it gives me an error, it says that 'instrument' is not defined, but I have already defined instrument in here, right? And I have already specified this James, this musician has a guitar, but, I didn't specify that it belongs to the instance, current instance. And, in order to do that, I have to say self.instrument in here. So now, it refers to the current instance, and if I hit Shift Enter, now, if I hit Shift Enter in here, it will say, We are the champions!

Guitar. And it will work if you create another instance with another name, age, and instrument, it will just write down the instrument of that instance. I think we are okay. So within the next lecture, we will see some practical usages.
