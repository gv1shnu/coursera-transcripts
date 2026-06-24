# CUDA Driver and Runtime APIs Lab and Assignment Walkthrough

- **Course:** Introduction To Concurrent Programming
- **Module 4:** Earn credit towards a degree!
- **Lecture #:** 24
- **URL:** https://www.coursera.org/learn/introduction-to-concurrent-programming/lecture/hMYi2/cuda-driver-and-runtime-apis-lab-and-assignment-walkthrough
- **Extracted:** 2026-06-19 21:38:58

---

Now I'd like to go over the CUDA runtime and driver APIs programming assignment. Let's open it up. Instructions here are pretty verbose. It says, the steps needed to take to get the FATBIN assignment part work, the PTX assignment, which are both part of the driver API, and then the runtime API, which is much simpler.

The FATBIN assignment part, basically you have to make sure you're in the driver API folder. Then you have to make some changes to the CPP file, then you compile the part C file into the FATBIN file. Make sure a link in the CUDA, the [inaudible] and generate this driver tester o, by compiling C plus plus code in driver tests as CPP. That references the fact that, so that just like with the PTX, you need to know where the FATBIN is.

Keep everything in one folder, at least at this time, especially we narrating driver API code. Once you have this output object, you can compile that driver test into the executable driver test to execute and just do dot slash and then driver test, you're going to execute the driver test command and output its output standard I/O to your project folder as output that FATBIN TXC of processes almost exactly the same with PTX, except for you have the dash PTX flag. Also the binary files will be in that PTX form, which you're going to have to change his travels as CPI to point to this mat some [inaudible] PTX. I'll quickly show you where to do that.

You done that. The last thing to work on is runtime assignment. That's a lot easier because the codes are all there. Basically just got to make sure your project folder in your route and then go to runtime API under that.

Then execute mvcc-o vector_add, which creates the vector add executable and point it at the vector at that see you CUDA file that create the executable which will execute the next line, and output that content to your users project folder as output-runtime.txt. Now that the extensions have been loaded, and in a second, you'll see that Submit, Assignment parts, button show up near the very bottom. We can start talking about what exists where. For the driver API, it's all under the driver API folder.

Note that I said there will be a mat some kernel CUDA file that you basically need to point to or from your dot cpp file. This is how the driver API works. Let's open up the drivertest.cpp file. You see right here there are two lines, one comment to that, and one which will be executed.

Then that execute right now looks for the module and marks some curl up PTX. It looks here. If you switch out what was commented out, like this. Now it will point to the fact that, this is compiled CUDA code.

You don't want to look at this, it's binary in nature. Then basically you can do this in a lab or in your assignment, you can look through and see the different steps are taken to create all the parts of a driver API project. Then it executes them. I said, we're doing the output-fatbin part, going to the driver API.

You're going to compile this into a FATBIN, then into compile.cpp into this driver, test that out. Then you're going to use mvcc one more time to create the executable. While these files are binary. The driver test.

The FATBIN PTX file. Don't waste your time opening them. What you can then do is you can execute the command and the terminal. Let's open up the terminal and let's go down into the driver API.

Then what you should be able to do is that /drivertest. We're going to see, this isn't part of the assignments this over, we can see what it's doing. It goes out, gets more information or runs of kernel. Now in the example of the assignment you're going to output what you have into output and then tap Add and then output there.

Now note I have already done this for all three of the assignments, it's there. You'll do the same thing for part PTX from this folder. Then what you want to do is you get to go into runtime API and close out the driver API, then start working on runtime API, or you change the change directory Part D and push back down into the runtime API. Runtime API is similar [inaudible].

You don't have to do the -o. It just makes your life easier because if you told you the -o by default, these cross compilers make everything A dot out, which isn't good practice for an individual project. You're going to name this vector_add and then the input is vector_add.cu. It's going to take a little while to compile and then you can execute vector_add.

It's going to take a while it's doing vector addition of 5,000 elements, you see that the test passed and it's done. Last thing for the assignment is to click the Submit button here. It goes and submits the three-part. Now we see that the lists submission completed.

It doesn't know the amber anymore. We see the score and it was passed. Now you can look at individual created outputs and says of this process, your grade and note that see your grade for a part. Then there are weighted differently.

Just keep that in mind. For these assignments you need to get 75 percent correct. Thank you very much and hopefully you enjoy this lab and assignment.
