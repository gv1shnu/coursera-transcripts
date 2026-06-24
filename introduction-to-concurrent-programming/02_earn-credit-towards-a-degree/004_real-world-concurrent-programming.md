# Real World Concurrent Programming

- **Course:** Introduction To Concurrent Programming
- **Module 2:** Earn credit towards a degree!
- **Lecture #:** 4
- **URL:** https://www.coursera.org/learn/introduction-to-concurrent-programming/lecture/d8ZjP/real-world-concurrent-programming
- **Extracted:** 2026-06-19 21:35:18

---

Hello, and welcome to the first lecture of Module 2, Real World Concurrent Programming. Multiprocessing, concurrent, parallel, and threaded programming are all synonymous. Modern programming is built around maximizing the utilization of the multiple processors and cores of modern computers, and the best way to do that is via running multiple processes and threads. This is done without developer intervention by the operating system, but you have the ability to improve the efficiency of your software by writing quality code with threads that process data independently.

Some highly complex tasks, such as artificial intelligence, audio-video processing, and signals processing can be written with multiprocessing in mind, but beware as this can go awry. Parallel processing has been the basis of software that requires lots of computing power, but also allows for asynchronous interactions with the user. What is a thread? It is an independent collection of sequentially executed programming steps.

Think of a program with multiple independent threads like train tracks that separate and come together at certain points. When the tracks are apart, multiple trains can go as fast as they want, but when they are together, each train is limited by the speed of the train that is in front of it. With modern CPUs, think of laptops or consumer desktops, you will often have 4 to 8 cores, and each core can have between 1 and 4 threads managed by the scheduler. The heart of any OS's multi-threaded capability is the scheduler, which shuffles different programs, including operating system tasks, between active and inactive states and moving them between cores, moving data around caches, etc.

Computers have multiple levels of memory, from the hard disk to registers shared between cores. They allow for common data amongst threads, even the instructions that multiple threads from the same program execute. The goal of memory caching is to limit the amount of time that is spent waiting for data or instructions to be retrieved from slower and more distant caching, which causes threads to become inactive. What we see in this diagram is a CPU scheduler, shifting between threads on different cores.

In this case, presume that all 4 cores are on the same processor and share at least an L2 cache. Why are threads made inactive and shifted between cores? They have their state changed due to cache misses, and the scheduler doesn't want to waste CPU cycles on waiting for data or instructions, so instead, it finds something that needs to be run and makes it active. There is, of course, lost time in switching between threads, so constantly switching has a cost as well.

Memory caches are hierarchical in nature, and they really work on the principle that memory that is physically closer is more performant. Caches are not just used for storing localized data and or instructions for a CPU, but it is also used as a sharing mechanism between cores and as a way to store data and or instructions that limit the number of times that requests have to go to RAM or even hard drive space. There are L3 caches, but apply a little less when we get to GPUs, and won't be discussed in detail here.
