# Break Continue Pass

- **Course:** Python Programming For Quantum Computing
- **Module 2:** Control Flow and Data Manipulation
- **Lecture #:** 22
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/nkRMz/break-continue-pass
- **Extracted:** 2026-06-22 15:10:00

---

Hi. Within this lecture, we are going to learn about break, continue, and pass keywords. So let me create a new Notebook from here, while I'll explain what this keywords actually do. So this keywords are used with for loops in order to make them more efficient.

So we have already learned about for loops, right? So let me just Rename this book, like ContinueBreakPass, and we'll see what they actually mean. So we learned about for loops, and we know how this for loops actually works. But for right now, please let me just create a new list and a new basic for loop, in order to explain this keywords one step at a time.

So what we're going to do actually is to create a new list called my_list, and this list will have 10,20,30,40,50 and 60 in it, okay. So hit Shift Enter. So you know how to look through this, right? So for number in my_list, and with a colon, you'll say, print(number).

And, if you do that, it will just print out the numbers, and you know what's going on, on background, right? So it starts with 10 and sees the operation under this for loop it's printing, so it prints number 10 and goes to the another element, like 20, and prints that number. If you just multiply it by 5, for instance, it will just multiply them one by one. So we discussed this before, and we know that it starts with the first element and continues until the last one.

But what we didn't discuss is to have an interruption in the loop. So we can just skip a number, or we can just cut the loop anytime we want, using if statements and using continue and break keyword. So best way to understand is to examine an example in here. So let me create a new loop under here, like for num in my_list, and for example, let's say I want to stop when I see 30, okay.

So, let me just print num * 5 again. But, before I do that if, if only the element is 30, then, I want to stop, okay. So, what I'm going to get is multiplying 10 and 20. So how do we do that?

So I just say if num is 30, then I'm going to break it, okay. And, if I hit Shift Enter, as you can see, now I have 50 and 100. So what happened here? It just started with 10, and, the number was not 10, so it printed out 10 times 5.

It went to the 20, and, the number was not 20, okay, was not 30, and, it just printed out 20 * 5. But, in the third position, it saw that number is actually 30. And, please mind that this print is not under here. If I do that, it won't print out anything, because, if number is 30, then it's going to break this, it means that it will stop the loop, and it's not going to print anything.

So, print is not under here, but it's indented for the for loop, okay, but break is under the if statement. So remember, indentation matters. So we define code blocks with indentations in Python. So, what happened is that the loop saw that the number was actually 30 and it broke the rule, right, it broke the loop.

So it didn't continue. So let's say, what happens if we used continue. So, let's say for item in my_list, if item is 30, again, let's say continue this time, and, print out the same result that we did before, so we can compare, and if we Shift Enter, we'll see that we'll have 50, 100, but not 150, okay. So what happened here was that, it saw that if item is 30, and when it got to the 30, it continued to loop, but it skipped the 30.

So this time, it didn't break the loop, it continued looping true, but skipping this very element, this 30 element in here. So continue actually skips the current element, at continues the loop. So, if there comes a time when you want to exclude a single element, but actually not breaking the rule, not breaking the loop, you may use this continue keyword. So now we have seen break and continue.

And what does pass do? Actually we use pass for programming purposes only. So what we're going to do, we're going to start a loop again, like, for example, for item in my_list, actually, we used item before, let's say, for no in my_list, and, this time, I don't know what to write under this. So if I hit Shift Enter, so it will give me an error saying, unexpected EOF.

In order to overcome this problem, I had written down print("hello") before, now I will write down pass. And as you can see, I got no error. So pass actually means literally passing, right now, without taking any error. And once I finish this, I will come back and write whatever I want in this block.

So, we generally use pass to avoid crashes or avoid getting problems, errors, while we're coding. So maybe you will not come across this when you deal with ethical hacking, but, please know that pass is used for this purpose. So, if you just see it anywhere or any time, you know what it means. So actually we're done with the continue, break, and pass.

We're going to stop here, and within the next lecture, we're going to talk about while loops.
