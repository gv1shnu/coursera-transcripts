# Simple CUDA Lab and Assignment Walkthrough

- **Course:** Introduction To Concurrent Programming
- **Module 5:** Earn credit towards a degree!
- **Lecture #:** 27
- **URL:** https://www.coursera.org/learn/introduction-to-concurrent-programming/lecture/JJKfK/simple-cuda-lab-and-assignment-walkthrough
- **Extracted:** 2026-06-19 21:39:30

---

I would quickly like to go over the structure and the goals associated with the CUDA Software Keywords, programming assignment. Note that there is a lab associated with that assignment which has all of the same code. So let's look at the programming assignment. Note that there are three steps to you completing this assignment.

You're going to have to make a bunch of changes before them. Once you think you have everything running, you're going to have to execute, make clean build and that needs to complete successfully, then you're going to execute the simple dot EXC which is built by the previous step. And output it into output dot txt. This should be in the project folder.

Then you'll click the submit button. So let's look at that. All right, so let's explore what is in the VS code environment. Good first thing to do is always to open up the terminal.

That's probably one of the most powerful tools here in the project folder. Aside from some VS code metadata, there's the make file note that many of these files are slightly obfuscated or broken on purpose to challenge you to complete them. So an example would be the make file while much of it is written correctly. The compiler that you will use has a placeholder here.

You're going to have to know which cross compiler, which I've mentioned multiple times is used to compile in video code. I've already run through this through and complete the assignment. So there's a dot txt file here that would not normally be then there are two files that are important. There is a simple dot cu which has all the actual code.

And for the most part, the major things you'll have to modify are associated with these keywords. But another place you'll need to work is how do I execute the colonel. This function is written pretty much as you need it except for it has these X, Y and Z variables here and then the text. Here's his number of blocks and grid and then replaces the number of threads in a block.

That's pretty close to that same line code. You just have to copy and the appropriate variable names and the same thing here somewhere. You'll need to find pointers to float primitives and pass them inappropriate such that the addition of vectors or multiplication in this case can be done appropriately. So when you've done that thankfully have this make file here.

When you fix this, you will just be able to run. Clean just gets through of any executables that were previously created. Once that's done, you're able to execute well that's done via something like this and you're going to output to hit enter here. And then once that's done you click submit and says that the submission was done successfully.

That does not mean you got 100% on this assignment. You're still going to have to look at the results in this under submission. All right, we've got our results back says I have a score 100 and it says that I passed. New instance is a very simple assignment.

There is only one part and you have to get 100% of it. Let's look at the output from the greater. It's very simple. It says that run the API part, which is the only part in this assignment was found and your grade is going to be a hundred.
