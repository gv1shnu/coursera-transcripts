# Writing Own Modules

- **Course:** Python Programming For Quantum Computing
- **Module 3:** Functions, OOP, and Advanced Topics
- **Lecture #:** 43
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/kNCTw/writing-own-modules
- **Extracted:** 2026-06-22 15:13:46

---

Hi. Within this lecture, we're going to see how to create our own modules, and I'm going to use Sublime Text for that. So, I'm working in Windows. Now if you're working in Mac, so you're going to follow the same steps with me.

What I'm going to do, I'm going to write my own module, then, I'm going to create another project and use my module within that project, and I'm going to keep this very simple, I'm not going to even share this files and folders with you guys, because it's going to be very, very simple, so, you don't even have to follow that too because you know how to write all of this things. So, I'm going to open my Sublime Text, and, within this project, I will only have one function. And within that function, I'm going to print out something, then I will use that function in another project. So let me Save this As a Python file, because we are in Sublime Text, okay.

So let me save it in Desktop, for instance. So I can say this is a module, I will name it atilmodule, and you can name it with your own name or something, whatever you want, but you have to save this file as a py file, because why, because we can write other scripts, other programming languages in this Sublime Text as well, so we have to specify that this is going to be a Python file. So now I have saved it, let me create my first and only function inside here. Actually, I suggest you stop here, pause the video, and write this function on your own, printing out something only.

I hope you managed to write it. All you had to do is just say def func or another name, okay, and then put parenthesis at the end, and within that function, just say print something like, this is an "atil module function". Then, if I just Save this and go to my Terminal, and try to start this, let me Save this, okay, and let me open my cmd, Command Prompt from here, and within that Command Prompt, of course, we have to find the file that we have saved. So I'm going to Desktop, you know how to work with that at this moment, I believe.

So if I call this, it won't print out anything, because why, because we didn't even call this function, so it won't get executed at all. So we have to add this func line in here as well, right? We forgot to call our function. So very beginner mistake in here.

So if I write, if I call the same command again, like python atilmodule, as you can see, we now see the output in here. So it's working, very good. Now I, at this point, you know how to write all of this, right? Nothing new, but for something new, I'm going to create another project, okay, and I'm going to save this project as a Python file as well.

So I will name it atilproject.py, and consider this as a main project, and I want to use my previous project or my previous module that I have written before in my new project. I can do that, right? So all I have to say, import, and I will just import one function only. So, I'm going to say from atilmodule import func.

So it means that, and you don't have to execute it. So, you cannot put a parenthesis at the end. But in here, you can just call the func. Even though the func is not defined in here, it's defined in this actually, okay.

And even if we don't execute it in this module, we can execute it in here, in our main project, because it's defined in atilmodule, and if you hover over it with your mouse, it says that in Definition, it is atilmodule.py, and it's in the first line. Now we can see where this function resides. So if I go to my Terminal in here, and if I just call this Python module and python atilproject, now I see the same result in here. Even though I didn't define the function in my atil project, I defined it in atilmodule, I can import it in my project and use it.

So this is not different than what we have done in the previous lecture, right? But now, we have written our own module and used it in our own code. So within the next lecture we're going to see how to differentiate imported versus direct.
