# Concurrent Programming Patterns

- **Course:** Introduction To Concurrent Programming
- **Module 2:** Earn credit towards a degree!
- **Lecture #:** 8
- **URL:** https://www.coursera.org/learn/introduction-to-concurrent-programming/lecture/ibTdt/concurrent-programming-patterns
- **Extracted:** 2026-06-19 21:36:01

---

Hello and welcome to this video that we'll discuss patterns that you will use in parallel programming. Many of the solutions to parallel programming challenges fit into these five patterns: divide and conquer, map-reduce, the repository, pipelines or workflows, and recursion. Learn to recognize that one of these patterns can be used in your program to make it more efficient and you'll save yourself a lot of time avoiding trying to reinvent the wheel. One of the most common ways to solve computer science problems even without concurrency is divide and conquer.

You've probably seen how can we use it in searching and sorting algorithms. The basic idea is to split up the data until it is small enough to answer the larger question, order or equality for the smaller amount of data. Once the thread has an answer, return that answer to a call that and it will take the responses from all the smaller datasets and answer the question with less work. This makes it back to the main calling context and should've taking less time than doing pairwise comparisons.

It's not always the best answer. Finding the same value in a set might take any comparisons and thus, if this dataset is not always sorted, you'll pay an extra cost for the breaking down and bringing back together. If recursion is not allowed, or really inefficient, which is the case in CUDA, then this should not be used frequently. Also a program implementing this will need to be well-designed and or maintain a complex state for all of the various divides, etc.

Map-reduce can be thought of as a subset of divide and conquer. The main difference is that each time a map-reduce cycle is run, it immediately breaks down into individual data points and the same operation is applied to all individual pieces of data. Each mapper returns only one value and the reducer has a job of taking n return values and reducing it to a single value. An example would be testing if a value is in a set, each mapper would return zero if the value passed to it was not the search for value and one if it is.

The reducer would just add all the values and convert zero to false and greater than zero to true. The nice thing about this way of doing things is that it scales well regardless of the size of data and quality of competing resources, presuming the MR system is well architected and communications is not slow. What mappers and reducers do can be more complex or they can be strung into a series of MR jobs that feed into each other. The repository pattern can be used when state needs to be maintained across multiple threads or processes.

Each process can run independently and when it needs information or wants to change the overall state, it makes requests of the repository. The repository needs to ensure that data is maintained atomically within itself but processes are responsible for maintaining their own state. Based on concerns of data consistency or staleness, this system may want to encourage more or less use of the repository since it is possible for a process to work on data for awhile and want to update it. But doing so could overwrite the changes that were made based on a newer state.

Pipelines and workflows are similar. They're both represented as directly crass without cycles. Though that is not strictly the case since workflow systems allow cycles but data will still flow out of a note. Pipelines are workflows in which each step gets input from the previous step and outputs to a single future step.

Workflows often employ fan out and fan in patterns where either the same input is the output to different logical steps or data is divided up and sent to the same logical code. Note that map-reduce and divide and conquer can be implemented using workflows. They neither are exclusive to the other. Programming languages handle divide and conquer and map-reduce especially now in a more functional programming way.

A key way to solving many complex problems can be via recursion. Almost any problem can be solved recursively though not always most efficiently. Functional programming languages and framework such as Lisp, Closure and Lodash are built around some level of recursion. In these cases, data is divided into head and tail or first and last.

Functions operate on the current data and call themselves with the rest. Recursion does not always have to be handled in that way. It can be divided in a number of ways, including in a binary manner. Recursion requires management of state since you need to ensure that it is an infinite which means that recursive algorithms need final states often when only one or two pieces of data are inputs to a function.

Recursion is not advisable when you are using a large data across multiple local or distributed CPU's, not on the same processor and GPUs don't perform well in this pattern.
