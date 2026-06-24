# Concurrent Programming Pitfalls

- **Course:** Introduction To Concurrent Programming
- **Module 2:** Earn credit towards a degree!
- **Lecture #:** 5
- **URL:** https://www.coursera.org/learn/introduction-to-concurrent-programming/lecture/dsvV3/concurrent-programming-pitfalls
- **Extracted:** 2026-06-19 21:35:29

---

Hello. In this video, we will discuss issues that arise when writing multi-threaded programs. There are many issues that can occur if care isn't taken when writing concurrent programs. They include race conditions, dead lock, and live lock, non-optimal resource utilization in contention over resources.

One of the most common pitfalls that you encounter when writing multi-threaded programs, is s race condition. This occurs when threads execute in a sequence different than intended and can have dire consequences. In this case, the programmer wanted the first thread to execute its three instructions, and then the second thread to execute its three instructions. Unfortunately, the instructions were interleaved, and therefore, the final integer value is not what the developer wanted.

I want to make it clear that in this case, there isn't an incorrect final value, since each thread performed its instructions in a valid manner related to the shared variable, it is often best to consider minimizing shared or global variables, or if they're acquired, have a plan to ensure that each threads access is atomic, which we will talk about later. Similar to a race condition, but morally to memory and not the order of execution is resource contention. The more threads and shared resources, the more often this will occur if the programmer hasn't given sufficient consideration to this happening. This is a more asynchronous version of a race condition, which can extend from threads to completely separate machines.

What happens is that resources are needed to be accessed in different ways by different independent threads and they access the same memory, file, etc and this can lead to conflict in constant rewriting of values. Consider the case of databases where values need to be incremented, but each time a value is retrieved from the data base another thread is accessing the same row. Now, it can happen that between the time that the first thread accesses and updates the row and end threads do the same thing that numerous increments go uncounted since the last updated value is what is counted. This is a very significant issue with databases.

Thankfully, they have numerous ways of ensuring consistency. Dead lock is similar to resource contention, except that one or more threads or processes require multiple shared resources and will not perform their action until they have access to all that they require. At the same time, they need other required resources. They do not relinquish their hold on a shared resource.

Multiple threads each have a shared and required resource and simultaneously are waiting for other resources and cannot proceed to the point when they can release them. None of the participants in the dead lock will make it out of this situation. The first response is to have threads drop their holds on resources, but this will devolve into threads dropping resources and then frantically trying to get all the resources that they can and possibly not helping at all. Live lock is like dead lock but each thread is actively doing something that never makes it out of the overall process that requires multiple resources.

This can happen when a programming loop tests for access prior to making a final change and goes to sleep for a small or no time. Consider a do while loop that doesn't change in externally visible display until it can save the value to a resource. Numerous threads executing the same loop might come to the same while test and not be able to access unnecessary variable, and thus keep incrementing another variable. This could result in a buffer or stack overflow or executing an instruction of millions or even an infinite amount of times, or recursively executing the same code in locking up a program.

This can even happen if you incorrectly use some programming language asynchronous capabilities, so be careful. A slightly less worrisome issue is over or underutilizing the computational power of your machine or machines. Though, if this happens with a powerful system or replicated over a large cluster of competing resources, this can be expensive. As the name should indicate, this is when you have too few or too many threads, and they have nothing to do or the few threads are performing a series of computations that could be broken down and run in parallel and therefore more efficiently.

If too many threads are going from active to inactive status due to not having work to do, the cost for context switching can outweigh the speed offered when many threads are being used. This can be handled by scaling the number of threads based on the amount of data or CPU utilization. When threads are too few, they may be in constant use and small memory leaks or inefficiencies can compound, and CPU utilization may spike, which makes all running threads sour. Also, if a thread requires a lot of data, or lots of instructions, cache hits can occur more frequently, and therefore the system will be slowed by data transfers to and from the cache or RAM, or even in the worst case, the hard drive.
