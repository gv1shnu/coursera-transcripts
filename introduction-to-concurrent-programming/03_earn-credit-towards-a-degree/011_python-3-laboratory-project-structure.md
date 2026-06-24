# Python 3 Laboratory Project Structure

- **Course:** Introduction To Concurrent Programming
- **Module 3:** Earn credit towards a degree!
- **Lecture #:** 11
- **URL:** https://www.coursera.org/learn/introduction-to-concurrent-programming/lecture/6qSXA/python-3-laboratory-project-structure
- **Extracted:** 2026-06-19 21:36:38

---

Get ready to explore the Python 3 Laboratory and Assignment Structure via this video lecture. Let's open up the Python 3 parallel programming lab activity. I like us to focus on what is under Python examples in the root directory. The basic structure of the Python 3 programming labs are some required but an important files such as the.init_ py.

Sometimes you'll see a _pycache_ and the requirements.txt, which is used for installing the appropriate libraries. The core functionality is across multiple.py files including core.py based on the lab activity you would like to explore or library you start_ new_ thread_ example. py, threading_lock_ acquire_ release_ example.py, threading_ semaphore_example. py.

The core.py, has a purpose of holding a number of variables and functions that the other three example Python files use in common. All these depend on core. py. The main focus of the three parallel programming example files for Python programming language are on the base level programming libraries, threading and thread.

It will give avenues for exploration of threads, acquiring and releasing locks and semaphores. Now that we have core.py open, we're going to discuss its two parts. At the top there are two static, publicly available functions, thread_function and critical_section_acquire_release. Thread_function basically does what the thread is supposed to do.

In this case, it outputs that it starting and finishing and in-between sleeps for one second. The critical_section_acquire_release, does the operation of taking a sync object and acquiring a lock on it, doing some work, which is that thread function, and then releasing the lock. Note that the sync object can actually be either a lock or a semaphore. We'll discuss this in more detail later.

The core class is also a described functions. It has a constructor which is the dunder init, which adds parsing capabilities for arguments. Very useful for command line arguments. It has the parseargs, which basically calls the parseargs function for the argparse library and the add_arg_parse_argument function.

But what it does is it tells the parser of the command line arguments to add an argument. It takes four values. The flag that is used in conjunction with the dash or double dash based on how you undo it. But that's like the dash h for help, then destination variable for that argument, then any default values, and then any descriptive text.

The basic thread example is in the StartNewThreadExample.py file. That constructor sets up the core object to parse the dash n argument that is used to retrieve the number of threads that will be executed in parallel. The run function is used to concurrently execute the same code, which in this case is thread_function from core.py for each thread. The parse args method sets up the core object of this class to process the past command-line arguments for the number of threads variable.

The example for acquiring an early signal lock in Python is in the ThreadingLockAcquireReleaseExample.py file. This code should seem familiar to the previous file. This is purposeful, and was designed to fit into a simple pattern that can be updated or expanded while keeping functions organized coherently between different examples. For each thread started in the Run method that created thread objects are executed in parallel, executing the same critical section of code.

The lock object is used specifically to ensure that no two threads enter the same critical section of code at the same time. ThreadingSemaphoreExample.py holds the semaphore example code. The semaphore example shown here, executes a user defined number of threads with a predefined number of entrance into a critical section of code based on the size of the semaphore. Each thread executes the same critical section, acquire release function with a different type of synchronization object.

Semaphores are locks that allow a larger number of threads to execute the same section of code.
