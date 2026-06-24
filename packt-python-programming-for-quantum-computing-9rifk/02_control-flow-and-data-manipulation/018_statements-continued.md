# Statements Continued

- **Course:** Python Programming For Quantum Computing
- **Module 2:** Control Flow and Data Manipulation
- **Lecture #:** 18
- **URL:** https://www.coursera.org/learn/packt-python-programming-for-quantum-computing-9rifk/lecture/8QG5V/statements-continued
- **Extracted:** 2026-06-22 15:09:16

---

Hi. Within this lecture, we're going to continue learning if statements, and we're going to see some tricks and new controls and checks that we can do with if. So what we did in the previous lecture was to say, if x is greater than y, do this, if x is equal to y, do that, and else, if nothing above is True, just do this. But can we do that only with Integers or Floats?

Of course not. We can use strings, like my_superhero, for example, will be an input from the user, okay. And like, say, superhero:, and we'll ask from user to state the superhero. So, if they say, like Batman in here, and, we will check to see if we can get the superhero name.

Like we can say, if my_superhero is actually == "Batman", for instance. And with a colon, we can say, print, like "Batmaaaan" in here. So, this is only an example. So you can just say whatever you want in here, like, elif my_superhero is not the Batman, but actually "Superman", then I'm going to print something else, and actually you can just adjust it for yourself as well, and, if my_superhero is "Ironman", then I'm going to print something else like "Ironmaaan" in here.

And, for the last time, let's say, else. If none of the above is true, then I can say, let's do a sad smiley in here, okay. So if I hit Shift Enter, then it will say Batmaaaan, because my superhero is actually Batmaaaan at this point. But let me give another input in here.

So, let's say Supermaan, and let's say Supermaan, okay. So you can try this on your own, but it works perfectly with strings as well. Let's do something with my_superhero == "Wonderwoman", for example, and say print("Wonderwomaan") as well. So, as we talked before, we can have as many conditions as we want in here, and else, if nothing holds, we can do or write whatever we want in here, if I say Aquaman, then none of the conditions will hold, and we will get a sad smiley.

And, as you can imagine, we will use this a lot, we will use this if conditions, if statements a lot in programming when writing ethical hacking tools as well. And actually, if controls, if statements or if conditions are very important to any other programming languages as well. So, let's suppose I want to add AND and OR operators in my if statements, let's do some Variables for that, to have an example. I believe we have to work with integers to make this clear, because strings might get confusing in this case.

So, let's say a is 10 and b is 15. So, let's create another called c, and this is 20. So I can say like this, if a is greater than b, or, b is greater or less than c, let's say less than, and, then I can print whatever I want, this doesn't make sense, but let's say "superman", okay. And now, is a greater than b, no, but b is less than c.

So, as you can see, one of the equation, one side of the equation, holds, and this is or, so it works. elif, let's say, a is less than b, and b is greater than c. Actually I put an extra colon in here, so let me delete it, and this colon is fine. So, if I hit Enter, it will be indented.

So now a is less than 1 and this is true, but b is not greater than c, so this condition will not hold. And let's say "batman" and hit Shift Enter, and we'll still get the superman, because the first condition actually holds. So, you can actually add these or and and operators in if statements as well, and, of course, you can say else, if none of the conditions above hold, just print something like "aquaman", for instance, okay. And this example doesn't make any sense, but I think you get the point in here.

So, what can we do more with if statements? For example, if we want to use Booleans with if statements, can we do that? Of course we can, and they are perfect for if statements, and you'll see why in the last part. So let's say isDead is False, and False with a capital F, of course, okay.

So we have a Boolean called isDead, like a character in a game. So I want to check if my character is actually dead or not. So I can say, if isDead == False:, then do this, print("character is not dead") at this moment. So, "character is not dead".

And, if I hit Shift Enter, then I'll get character is not dead, or elif or else, let's say else because we only have two options in here, print("character is dead") or is alive, is not dead, maybe you can write character is alive and print character is dead, in the lower part. So, I can do that, and it works with Booleans perfectly, right? But actually, there is a greater way to do that. And this is, if isDead: print("character is dead").

And why does this work? Why do we have this with Booleans, and we don't have this with like strings or numbers? So basically, what we're doing here is to say that if x is greater than y, so if actually x is greater than y, then Python will consider this as a Boolean, like, if x is greater than y, it will return true, right? So, this is already true or false.

So actually, in this case, I don't have to check if isDead is False or True, because this is already a Boolean. So we get a Boolean in return with the controls with greater than, less than, in the above examples, but we already have the result in here. So let's say, if isDead true, the character is dead, else character is not dead, to make this a little bit understandable, and now I can say if isDead print("character is dead") okay, and, like else, print("character is not dead") or alive. So, let me just work this, and it will give us, character is not dead.

I hope you got the point in the above examples, working with strings or numbers, we try to get the Boolean out of that control, but this is already a Boolean. So I can say if isDead, this is like saying, if it's true. So, I can say if not isDead and say print("character is not dead"), and remember, not just makes this thing negative, okay. So, this is like, if it's not dead.

I know this may sound vague to you right now, but don't worry, we will have much more examples when we deal with ethical hacking tools in the following lectures and sections. So let's stop here, and within the next lecture, we will continue with the if controls one more time.
