# Imported versus Direct

- **Course:** Python Programming For Quantum Computing
- **Module 3:** Functions, OOP, and Advanced Topics
- **Lecture #:** 44
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/bOcKF/imported-versus-direct
- **Extracted:** 2026-06-22 15:13:56

---

Hi. Within this lecture, we're going to see how to differentiate between direct and imported calls of modules or Python scripts. In order to do that, we are going to see a special variable. We have seen some special methods, like _str_ or len before, right, but now we're going to see something called name, and it will have this underscore things again.

So let me Save As this file, and I'm going to save this as a yoda, okay, and I'm working in Mac right now, but it doesn't matter, you can just work with Sublime Text in Windows as well. So this will be yoda.py. I am going to open a New File in here, and I'm going to Save this As anakin.py, okay. So I have different two Python, and they're all saved in my Desktop in here.

So within yoda.py, I will create two functions, first of which will be func_direct. So, this will just print out something, and it will say "yoda direct" or something, okay. And, I will create another function called func_imported, and within this function, I will do the same thing, but now I will just say, "yoda imported", rather than direct. And, I only have two functions in here.

Now if I want, I can call this functions from anakin.py, right? And you know how to do this. You have to import yoda, or something from yoda. So, you can just say import yoda, and we will see how to do that later on.

But for right now, let me just import one function, okay, from yoda import func_direct. So if I import this func_direct, I can just call this in here, right? So, let me try this. We already know how to work with this, but let me try this within Terminal.

So open your Terminal or Command Prompt in Windows. So let me make this a little bit Bigger, so we can see it better. And, after opening your Terminal or Command Prompt, you have to find the folder that you have saved in, my name is Desktop. So if I call python anakin.py, it should have written func_direct, but it doesn't work.

So, if I have written correct names, so it is correct, actually, most probably I didn't save this file. So let me go here and say, File, Save, and I'm going to do that for anakin.py as well. So I'm going to save both files this time, and now I can just try again and run python anakin.py, now I see yoda_direct. So it works, and, we already know how to do that, right?

But we didn't see how to differentiate between direct and imported. What do I mean by that? I have the liberty to specify what will happen if some function is imported, or, some function is called directly within the class itself. So, let me do this, import yoda, and I'm going to import all class in here, all project, and then I have to say yoda.func_direct.

And it really doesn't matter, it will just return me the same result, but, now we know both ways to do that, right? So, let me go back to my main objective in here, which is differentiating the direct and imported usage of modules or functions. So, I'm importing yoda in here, I want something different to be happening inside anakin.py and yoda.py. So I have to check this, if __name__ is actually '__main__', okay.

And as you can see, they're all special Variables. So, it starts with __ and ends with __ as well. So, this literally means that if this function is called from the project that has been declared inside, okay. So I have declared this function inside yoda.py, and if I call this within yoda.py, I want something to be happening, and I will write what I want inside this if statement.

And, when somebody else or some other project else, just executes this, then, I will do something else, like func_imported. So, it means that same function or same class will have different effects if it's imported or called directly. So I'm going to just print out something because I'm already importing yoda in here, and I will see the difference clearly. So I'm going to Save both files.

Now I'm going to call and run both files. So if I call anakin.py, now I see yoda imported rather than yoda direct. And if I call python yoda.py, I see yoda direct. python anakin.py yoda imported.

So now, I can use this __name__ == '__main__' thing, the statement, in order to have two different execution for imported and direct text. So now let's stop here, and within the next lecture we're going to install PyCharm in order to start writing our own ethical hacking tools.
