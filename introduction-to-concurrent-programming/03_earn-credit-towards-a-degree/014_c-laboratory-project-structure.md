# C++ Laboratory Project Structure

- **Course:** Introduction To Concurrent Programming
- **Module 3:** Earn credit towards a degree!
- **Lecture #:** 14
- **URL:** https://www.coursera.org/learn/introduction-to-concurrent-programming/lecture/hS6da/c-laboratory-project-structure
- **Extracted:** 2026-06-19 21:37:09

---

So let's open the lap. This directory that you see here, which is called project, will be under the coders user project folder. What you will notice are therefore pairs of dot C P V C plus source files and header files. So they are for threads, new Texas futures and atomics.

So the headers show things like constant variables, and the signatures for functions and C plus plus files show the actual camp. An important other file that you'll see here that will go over in a little bit is the make file, which describes a number of ways that the make command well, change files compile them etcetera. So let's open the make file. The make file for the C Plus plus examples manages compilation of code running of associated executable and then the cleaning of our facts, such as object and execute herbal files created during the build process.

For each of the four examples, there is a build and to run target, and then there are overall build and run all targets for building and running. All of the examples. The all target executes all the applicable targets, so cleans everything, builds it and then runs it all of the two open threat example files. You'll see the left tab is the header file.

It contains function signatures for the three non main functions. In the right tab, you see the thread example CPP. C plus plus code. There are three functions that have been implemented.

Do work, execute threads and execute and detach threat. Do work is a function that holds the execute her work for a threat in this case, logging the thread that is being run. Execute threads, executes a predetermined in this case, three number of threads in parallel and then joins them. Execute and detached thread executes a threat in detached mode, meaning it is no longer bound to the calling context.

Now let's go over the mute tax example in the left tab is the header for the music's example code. It includes the shared me text variable and the four non main functions. Now let's look at the C plus plus card. There are four functions that you will see.

Do you work with mu ticks? Lock execute threads with mu Tex Clark, do you work with me? Tex, Try lock and execute and detached threads with mu text frylock the to do work functions that do work with new text block and do work with you. TEX Try lock.

Do the work of a single thread with respect to the shared mu ticks. The to execute threads with Mu Tex lock and execute and detached threads With Mu Tex Try lock functions. Execute the do work on the number of threads past as a variable, so let's move on to the example code for futures. The left tab future example.

That age is the header file for that example and has four non main functions. There are four functions that have been implemented. Do work with futures. Execute threads with futures.

Do work with a sink. Execute with a sink. The to do work functions expanded here do the work of a single thread with respective futures and into jurors as inputs. The two execute functions.

Execute the do work based on either a predetermined or past number of futures. Executing the do work with a sink function a synchronously. So let's move on to the example code for atomics. Atomic example dot h here has four non mean functions.

Atomic example that CPP has the example code for atomic variables. There are four functions that have been implemented. Do work with atomic bullying. Execute threads with atomic Boolean.

Do you work with atomic thread fence? Execute with atomic thread fence. The two do work functions which are expanded here and here to the work of a single thread with respect to the used atomic variable, in this case, dealing with an atomic bullying in the second. Implementing an atomic thread fence the to execute functions.

Execute threads with atomic bullying and execute with atomic threat fence. Execute the do work on their associated function on the number of threads passes a variable running them in parallel.
