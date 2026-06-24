# C++ Parallel Programming Syntax And Patterns

- **Course:** Introduction To Concurrent Programming
- **Module 3:** Earn credit towards a degree!
- **Lecture #:** 13
- **URL:** https://www.coursera.org/learn/introduction-to-concurrent-programming/lecture/xfaFZ/c-parallel-programming-syntax-and-patterns
- **Extracted:** 2026-06-19 21:36:59

---

Hello and welcome to the video lecture on parallel programming in C Plus Plus. There are four major concurrent programming classes in the C ++, Standard Library. As you may have noticed, they're all names spaced with the letters STD, which is the name space for standard Library or STL. The names for each class maps to their usage, so the classes support threads, new texas, atomic data and futures.

Which may be new to some with less for development background, especially in newer versions of programming languages that are popular. The thread class has the responsibility of creating in CS lingo construction, joining and attaching threats using the pattern of standard thread name a thread variable. And the function that will be executed by the threat and create an instance of a thread within the current operating system process. The thread will start to execute independent of the context in which it was invoked.

The joint method holds the continued execution of the calling context, the code that called the thread. Until the thread associated with the variable name completes what it has been to ask with. If you want a thread to execute completely out of the control of the calling context., use the detach method of the thread variable. This will allow a threat to continue to operate until its work is done, or the calling process is executed completely.

Usually via sig term or sick kill signal, which can be achieved via the control C, control D command. C etcetera based on the calling operating system, provide a means for mutually exclusive access to a specific section of code. Consider like a barrier to any thread that comes while the music's is still in effect because they are not variables that are passed around. You utilize the static methods of lock, try lock and unlock around sections of coat.

They only affect any thread that attempts to access the critical section, that the music's locks. A normal pattern of use from you texas is to identify a critical section of code called the music's lock function. Before entering the critical section to block and current access to the same section of code, and then call unlock when it is completed. If you would like a thread to move past a critical section of code and not wait for a lock.

Using try lock will allow a threat to try to get the music's lock and if it fails, continue its execution. I used sort of this might be when threads can execute a number of unrelated tasks. Maximizing their processing or the thread might want to indicate that lock was attempted to failed. Lock the try and then sleep pattern if used correctly, can limit thrashing over the critical section, but can go badly if a thread sleeps for too long and is underutilized.

Also note that if the variables modified inside of the lock and possibly outside of the lock there is no guarantee of coherence between the two operations. Atomic variables allow for more coherent access to data, atomic variables mean that a variable cannot be accessed. Or modified until the current operation on the variables completed, think of this when you want to incriminate variable. That is at least two operating system level operations adding to the variable and then saving the value without atomic.

Two relieved increments could result in only one effective increments, most prove types in C ++ can have the atomic. You are applied to them is not good practice to make all variables atomic. But if you believe that two threads will access the same variable, and you want to ensure that all operations have their intended effect. And this is a good tool, also offense can be used to ensure that all threads have access to an atomic variable.

But do not proceed until all variables have reached the fence, atomic thread fence is a way to acquire. And release to give all thread access to the fence variable and then have them indicate that they wish to release the fence and therefore proceed when appropriate. Futures are more modern parallel programming construct, allowing threads to continue with execution of its responsibilities while still being able to interrupt that others thread. Once the result of an operation is completed in modern languages, they use network communications.

This can be when a request is made outside of the context of the current threat rather than wait for an answer promises made to respond. When a result is returned to gain access to the results of a promised operation, a future is returned. If you would rather have threads wait for result functions can use a sink to indicate that a function will continue outside of the calling context. A later point execute, using weight allows for calling context to halt continued execution code, until a call function returns.

A result, get allows asynchronous execution of the function to eventually get the result of that operation.
