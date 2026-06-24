# Concurrent Programming Problems and Algorithms Presentation

- **Course:** Introduction To Concurrent Programming
- **Module 2:** Earn credit towards a degree!
- **Lecture #:** 6
- **URL:** https://www.coursera.org/learn/introduction-to-concurrent-programming/lecture/tp2v1/concurrent-programming-problems-and-algorithms-presentation
- **Extracted:** 2026-06-19 21:35:39

---

Well, and I hope you will enjoy this discussion on concurrent programming problems and algorithms to solve them. For canonical challenges and the algorithms in the world of parallel programming are, Dining Philosophers, Producer-Consumer, Sleeping Barber, and also Data and Code Synchronization, which is more of a parallel programming mechanism than a problem. Each of these are at the heart of different issues that you will encounter, and a solution for them will solve numerous analogous issues. So keep them in mind as a pattern to look for when programming with parallelism.

I hope you enjoy this depiction of the dining philosophers problem using Ron Swanson from Parks and Rec. This seems a little less scary than having Socrates and Plato waiting to eat. Each philosopher wants to eat, but they need two forks to be able to do this. Don't ask me why they need two forks, but they do.

They can only do one thing at a time, pickup a fork, eat eggs, or put a fork down, etc. So they need to eat with both, and in a naive implementation where a philosopher tries to pick up the left fork and then the right, and then eat, and then put the left fork down, then put the right fork down. This will fail since this will most probably result with each philosopher having one fork and being very hungry. Does this seem familiar?

Is a little bit of a few of the problems encountered in the previous video. If you expect each philosopher to neatly and politely get forks and eat without ever trying to pick up the same fork, then it is resource contention, with the fork being the resource. If you have the philosophers hold their ground and never drop a fork, then it is deadlock, almost literally. If each philosopher drops the fork, they hold and tries to get the other fork, they probably have livelock.

Consider a way to solve this. Could the philosophers communicate to each other? Or have a central authority determine the order? There are many solutions to this problem, but they aren't always easy.

So think before you write the code. Producer-Consumer or reader-writer pattern is a very common tool these days. A very common way that is used in message queues, which allow for data to be added sequentially and non-sequential in a streaming or batch fashion. Then users pull or subscribe to the message queue, and it returns data either in the order it was placed in there or as it becomes available.

One or more processes call them producers, can then add data to be consumed by the consumers. If there is more data than the queue can handle, there are a number of strategies based on how the data is used. If the more recent data is more important, then the queue will drop the oldest data. If only a sub-sampling of data is needed, then data can be randomly dropped from the queue.

If all data's important then newer data can be stored for access once space is available. Think of it as slower and less costly, and consumers can be told to hold back from doing anymore processing. There's a chance of race conditions if the data structure or queue allows for overriding of values or the pointer index for the producer ends up being ahead of the index of the consumer, and that's why producer may never end up with new data. The Sleeping Barber is similar to producers- consumers but or is not important, the threads are trying their best to optimize the barbers work.

The waiting room is like the queue or data structure from the previous slide, but the barber or barbers can only put one customer share at a time. The waiting room is of a finite size, and two issues can occur. First, if the barbers are chatty and slow and cutting their hair, and there are lots of prospective customers, we can have something like livelock or overutilization where they stick their head and see the waiting room full and leave. The second matrix case is that there are no customers and the barbers should sit around sleeping and talking about how much better baseball was back in the day.

This is a situation of under utilization. There are solutions to this problem, from one or more barbers. When I think of this problem, I think about inverting the problem in having the number of customers in the waiting room determine the number of barbers. Many, if not most languages provide a mechanism for synchronizing data or code.

This generally locks access to data or code, so you use it with caution. If you make all data synchronize, you end up with dead or livelock. If the threat attempts to access a synchronized piece of data, any thread that requires that data will wait. This is useful in ticketing systems where you want to lock access to code or data until it has been fully used by the previous holder of the call ticket.

Semaphores are implemented with Fox, but have a limited number of states to manage access to data or code more indirectly, allow for multiple axises. Concurrently, think of this like sitting categories for flights. Those in-class 1A can be seated before those who are class B or 2. Multiple individuals can board at the same time, which should minimize the possibility of being blocked by other passengers.

The major note here is that there are rarely bulletproof solutions to multithreading problems. But you can come up with a reasonable solution based on prioritization of coherent data access and acceptability of under or overutilization.
