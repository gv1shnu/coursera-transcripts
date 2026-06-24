# Class Practical Usage

- **Course:** Python Programming For Quantum Computing
- **Module 3:** Functions, OOP, and Advanced Topics
- **Lecture #:** 38
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/PNCjY/class-practical-usage
- **Extracted:** 2026-06-22 15:12:53

---

Hi. Within this lecture, we're going to cover some practical usages of classes, like we generally do. But I'm not going over the same example, because it got too complicated. So I'm going to create a new class to tell you all about this practical usages.

So I'm going to call my class DogYears, because, I want to calculate the human representation of a dog's age. Maybe you know that there is a general saying that a dog's year equals to 7 years of a human's age. So if a dog is 1 year old, it means that in humans terms, it means 7 years old, okay. So I'm going to calculate this in my class.

And, of course, I don't need a class to calculate this, I can just do it with a simple line, or I don't need any function at all. But I'm going to do it in a class, so that I can tell some practical usages of class. So, what do I do first? I have to just create a year_factor Variable and make it equal to 7, because I'm going to multiply a dog's age by 7.

So next, I'm going to create my init method, okay. So def __init__( ), and a colon. And don't forget to add a self in here. And what do I get as an input from the user?

Of course, I want to get an age, so that I can multiply this age by 7, right? So only thing that I need is age, and then I can just say that self.age is age, because while I'm creating a new attribute called age to my instance, I'm making this equal to the input that has given to me. So, next thing that I'm going to do is just to create a calculation method, in which I will just multiply this age and return it, okay. So what I have to say is self.age multiplied by year factor, right?

So, we have seen this, we have to refer age as self.age. So I have to say self.age * self.year_factor. Now, if I create a new instance of that class, and give it an age, it will just multiply it and display the result back to us, right? And, let me just try it.

So I'm going to create a new dog here, my_dog = DogYears, okay. And if I hit Shift Enter, it will give me an error, because I didn't give any attribute, right, because I have to give age. So, let me give the age here. So let's choose 3, for example, and then hit Shift Enter.

Now, my instance is created, and if I call my_dog.age, I can see the 3. And if I call my_dog.calculation and execute this method, then I will get back 21. So our class actually works. But what happens if I don't want user to give an input, or, what happens if I just want a default value in here, can I do that?

Of course I can. I can say age is 1 or age is 5, for example. We did that back in functions, we can do it in methods as well. So, the default value of age will be 5, and if I just leave this blank, and hit Shift Enter, it won't give me any error, and if I hit Shift Enter again, then I will get 35, because 5 * 7 is 35.

So we can have pre-defined values of this inputs. But can we have pre-defined values of attributes as well? Yes, we can. We don't have to take this from user at all.

So I can say self.name is actually "Bar" for instance, okay. So, let me run this and see what happens when we create a new instance. So I'm hitting Shift Enter, Shift Enter, so they're all working. Now, if I call my_dog, then I will see .name in here, and if I call my_dog.name, it will display 'Bar' to me.

So what does it tell us? It tells us that we don't have to get input from users to assign them to attributes at all, we can create our own attributes for default values, like we do in this year_factor thing in here. Okay, so, as I was saying, this is actually more complicated than it should be, like, I can say self.age_multiplied and make it equal to age * year factor or age * 7 in here, right? So I can get this in 1 simple line as an attribute.

So, if I call my_dog and there is no name anymore, age_multiplied in here, then, I will get back 35. So, as in the name example, I didn't take a user input, but, I just took an existing input here and multiply it by a number. So you don't have to take every input to make it an equal to an attribute, okay. So, you can create your own values for attributes as well.

Another usage that you may have to be familiarized with is that if you have to take this year_ factor thing from here, for example, in this calculation method, then, you don't have to say self.year_factor actually, because this is like a global variable in here, and it's same for all instances. So you can say DogYears.year_factor, and it won't change the result, it will be the same. As you can see, we still get the correct calculation. So let's stop here, and within the next lecture, we're going to see some other usages of class.
