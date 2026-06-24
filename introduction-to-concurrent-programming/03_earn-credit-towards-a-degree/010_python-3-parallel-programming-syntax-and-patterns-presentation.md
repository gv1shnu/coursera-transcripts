# Python 3 Parallel Programming Syntax and Patterns Presentation

- **Course:** Introduction To Concurrent Programming
- **Module 3:** Earn credit towards a degree!
- **Lecture #:** 10
- **URL:** https://www.coursera.org/learn/introduction-to-concurrent-programming/lecture/Enm21/python-3-parallel-programming-syntax-and-patterns-presentation
- **Extracted:** 2026-06-19 21:36:25

---

Hello and welcome to the video lecture describing how to perform parallel programming in Python 3 programming language. There are three main libraries in the standard Python 3 programming language distribution. There are numerous other libraries can be downloaded that works similarly. We will only go over these three since they're available out of the box and are very well supported.

The underscore thread and threading libraries are low and high level interfaces to Python 3 threads. Asyncio is a library implementing a number of core functionality for asynchronous execution of code. Lastly, multiprocessing is a library that aims to go beyond just threads for concurrent software. To make use of the thread or threading libraries, just add an import statement at the top of your Python file for overall access or at the top of your method for method level access to these libraries.

Threads are started with the Start New Thread method. What you pass the name of the function that the thread will execute. Then the arguments and the keyword arguments that map to the args, kwargs of a name function. This acts as shorthand for the Run End Start methods, which may be extra boilerplate code.

When using the thread library, you can take the return value of the Start New Thread method or similar function, which is a handle on this started thread and lock, acquire lock, and then release the lock on a critical section of code. This is a very common pattern of use for locks on critical sections of code. Semaphores can be used to signal access to a variable by default, single thread at a time or a bounded semaphore can be used to allow a predefined number of threads to access a variable. There is also a scheme for communication between threads using events and event handling.

Lastly, a barrier can be placed in code to make sure that all active threads execute up-to, but not beyond the barrier prior to all threads hitting the barrier. This is a good way to synchronize data, especially if one or more variables need to have a coherent value across multiple threads. Asyncio is a common language construct among multiple languages, which allows in a very simple manner for management of asynchronous code. Once imported functions can use the async keyword to indicate thing maybe executed in an asynchronous fashion.

Think of this like the situation when your code, once you get information from a network server, but you don't need to have your whole system wait for the execution of one or more lines of code. There is some guarantee that async methods will eventually complete and the library will handle this. Back in the Python 2 days, web applications that made time-intensive processing in the middle of a call for data from your browser would either have to sit and wait, or as Python 3 became more available, developers monkey patched this library into Python 2 code. But that wasn't very pretty.

To call the function and let it execute in its own thread, the calling code just needs to wrap the async method in the Asyncio Run method. Alternatively, if you want the code to wait for the execution of an async method, the await keyword is used, common when sleeping a thread. Some more advanced capabilities of Asyncio include creating tasks. Unlike the run call that returns a method that is called by the thread, create task not only executes the code routine, but it returns a task object that can be used to retrieve result.

A task can be used as part of a sequence of calls that can be executed in parallel with the gather method. The sleep method is very important as it allows for executing threads to wait a predetermined amount of time. This is handy if your code is doing something aside from handle the result of a calculation. But we'll want to wait for a result that is eventually going to be returned.

Also, if you want to have threads that have a loop that has executed as long as they exist, think of pulling a file system for change and then performing a calculation or showing the contents of a file in an application window. The multiprocessing library is very powerful as it takes the idea of independent execution of threads inside of a Python 3 context and allows for execution of code outside of the current calling process and even on a remote machine. Spawn, fork and forkserver, all have three general goals. Create new processes out of the current process, though they have different results.

Spawn is the most common version. Create a new Python interpreter process which will be similar but not the same as the current process. Basically the Python interpreter will have the existing libraries. Fork is a more of a copy of the current process, though it can change over time.

Forkserver is the most elaborate. It creates a server that when called fork's a new process. It can be called repeatedly. It also handles any dead processes that may occur over time.

The constructor for our process is very similar to how you create threads in other libraries. You pass keyword arguments to the target function to be executed and args that we pass to the associated method. In the process is execution. You call start, and when you want to halt the calling threads execution until the processor is done called join.

For processes to be able to communicate with each other, either queue or pipe can be passed as an argument to the various processes. Queues are sequentially access data structures, and pipes are two-way mechanisms for communicating between two ends of a pipe. It is possible to have more than two processes access the same end of the pipe. But simultaneous read writes will corrupt the queue.

If you want multiple read writes between a parent and child process or processes in this case, it may make more sense to have multiple queues. Like with the two previously mentioned thread libraries, the lock, acquire, and release object, and functions can be used to manage access to critical sections of code. To share data between multiple threads, you can use the value object for a single value object to be shared and array to share a collection of primitives, if you would like to split up multiple processes for constantly completing work. Our worker pool is a common pattern.

You create a pool object with the number of processes that you would like to have spawned. Then each time you want to have a parallel execution by the pool, just perform functions on the pool such as map, which is a function that you pass the function that you would like to perform the action on an array of values. Then the pool of workers execute the function with a value in the array until the array has been completely mapped. This form of functional programming is becoming more common and programming languages are handling it more and more efficiently.

There are also other common primitives, like in the thread and threading libraries. But of course, they execute beyond the scope of the current process and across multiple spawned fourth processes.
