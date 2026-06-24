# Using Libraries

- **Course:** Python Programming For Quantum Computing
- **Module 3:** Functions, OOP, and Advanced Topics
- **Lecture #:** 42
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/Ypo1R/using-libraries
- **Extracted:** 2026-06-22 15:13:35

---

Hi. Within this lecture, we're going to cover modules and packages. Now we are going to start with modules, especially libraries, okay. We used these terms before, actually we used some libraries and modules before, but we have never seen what really are they, okay.

So, let me create a New Python Notebook and rename this Notebook as ModulesPackages, then, tell you all about them. So Modules and Packages or libraries, whatever you want, and Rename. So, modules and packages are actually piece of Python codes, okay. So there are other projects that we can import into our code.

So one of the most popular reasons that Python is so widely used in the world today is the extensive number of libraries, modules and packages Python has. Of course, Python is very easy to learn, so that is one reason. But the extensive number of libraries is the other main reason. So we will use some libraries, some Python codes that other people wrote in our software when we deal with ethical hacking as well.

So how do we find these libraries? They're actually widely open popular in web, okay. So I go to Google, and if I search like python module for web, for instance, if you just hit Enter, you will have like millions of results in here. So if you go over this, like HOWTO Use Python in the web, Welcome to web.py!, Install guide (web.py), so they're all libraries, modules, and packages.

So they're actually piece of codes that are written in Python, they are compatible with Python, and you can use them for specific reasons. For example, right now this is Web-Modules 0.5.3, is kind of a web framework for Python, and we can use this Web-Module in our projects. This is not what we want. We're not going to deal with Web development at all, but, let me just show you for an example, okay.

As you can see, this Web and Database modules for easily building dynamic websites. So you can build websites with Python, you can do other stuff with Python as well. So if you search for numpy, for instance, in this website, it will show you a lot of results, you don't have to do that, actually, I will show you how to use it, I will show you how to import libraries in your own computer, in your own projects, don't worry, you don't have to follow the steps right now. So if I go to any module, any library in here, it shows a description, for example, in NumPy, this is a general purpose array processing package designed to efficiently manipulate large multi-dimensional arrays of arbitrary records.

So if I want to use this NumPy in my own project, all I have to say is just say, import numpy in here, then I can use NumPy methods, NumPy variables, NumPy features in my project. But in order to do that, NumPy has to be present in my computer. Because, as I said before, this is actually a piece of code. So this code has to be in my computer, so that I can use it.

Right now NumPy is actually installed because it comes pre-installed with Jupyter Notebook. So, you can just use NumPy in your project right now. But, for, some reason, or for some other libraries, it may not come as preinstalled. So you have to manually install the projects, install these libraries in your own computer.

So how do you do that? If you search for Terminal in a Mac or if you go to cmd, your Command Prompt in Windows, that is where you're going to install this packages. So, let me open a new Terminal here, because this runs the terminal for Jupyter Notebook right now, so if you click New here, and then let me make this a little bit bigger, so you have to search for cmd and open a Command Prompt in Windows, then you will get the exact same terminal in here, okay. So I think you can see it right now.

All you have to do is just say pip install. So pip is like a tool that lets us deal with Python packages and libraries, okay. If you go to any website that concerns this kind of packages, you can see the installation guide. As you can see, here we have to run pip install numpy in order to use NumPy in our computer.

So as you can see, for another library, it says pip install numpy-cloud. So you can find this in Web, in Google, and you can just download whatever you want in your own computer. For example, if I just say pip install numpy and hit Enter, it will say it's already satisfied, as I said before, it comes pre-installed, but, if it wasn't, I would have just downloaded it in this way. So now you know how to install and use packages, modules, in your own computer.

So, this is now version 9.0.1. If it was another version, like in here, says that you have to say 'pip install --upgrade pip'. I'm not going to do that right now, because it doesn't concern me, but, for some time, you may want to just run this command in order to avoid any confusion or conflict between versions. So, now I have imported numpy, now I can start using it, but I don't know how to use it, right?

So what do I do, I go to Google again and search for numpy python. So, NumPy actually has its own website here, and you can find the documentation and all the explanations in that website. So this is generally the case for most of the packages and libraries that you're going to work with. If I go to tutorials here, I will see the basics, I will see the commands, the methods, and the codes, and everything and examples.

So, I can just start running NumPy from here. So let me do an example. So, we use NumPy to create some kind of array, some kind of numbers, okay, and we're not going to use it in actually the ethical hacking part, but I'm doing this as an example for you. And NumPy is actually a very, very popular library in Python.

If you're going to deal with machine learning or some kind of statistical methods, you will use it. So let me create a grades listing here, okay, so think of this like grades of a class or grades of a university, a college. So, I will use NumPy to generate some numbers, and all I have to do is just say numpy.random. So random is a method in NumPy, and it's different than the random that we have used before.

Then I will say .normal, so, I'm going to use normal distribution. So if you have studied statistics before, you know what a normal distribution is, but don't worry, we will see what this is soon. So I'm going to create some fake numbers here, so it will have an average of 80, and has, it will have like 30 standard deviation, and it will generate 1000 arbitrary arguments. So, later on, I will find the mean of this fake random generated datas, okay.

And all I have to say, pass in grades. Now, if I run this, I will get out this average, this mean number in here. So, it is around 80, and it has a standard deviation of 30, and it has like 1000 data points. So, the average of this 1000 data points is 79 actually.

And how do I know how to write this, how do I know 80, 30 standard deviation? I know because I have read the documentation, the tutorial, okay. So if you read the documentation, you can just write some codes with NumPy as well. By the way, when you import this kind of library, you may name it whatever you want.

All you have to do is just say import something as something, like import numpy as np, then you can refer NumPy in your code as np. So, this may become convenient for you. As I re-run this, as you can see, I get a different number here because it's randomly generated, and now it has a different mean than before. But since I use something called normal distribution, the mean, the average is very, very close to the previous example.

Now, let me show you another library in here, it's called matplotlib, and it actually lets us to draw some graphs in our code. So, it's going to be like import matplotlib.pyplot, okay, so matplotlib.pyplot as matlib or whatever you want, okay, like matplot. So, after this, I will use this matplot to plot out, to draw a graph for my randomly generated numbers in here. So I will draw a histogram, and, I will pass in my grades.

If I say grades, and then 50, it means that it will use the grades numbers, and it will show us with 50 histograms. If I say matplot.show, as you can see, now I see my graph here. And this normal distribution means that it's normally distributed around 80 average, okay, as you can see, we have a curve-like shaped in here, and, the main point in here is that we're not going to use this libraries or packages in our projects when we deal with ethical hacking at all. But, as you can see, we have written like a four line of code in here, and we managed to get a very good graphic and randomly generated numbers.

So with using this kind of libraries and modules, we can write very, very efficient Python codes. So let's stop here, and within the next lecture, we're going to learn how to write our own module.
