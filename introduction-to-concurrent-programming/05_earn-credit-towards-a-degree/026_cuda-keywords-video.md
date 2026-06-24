# CUDA Keywords Video

- **Course:** Introduction To Concurrent Programming
- **Module 5:** Earn credit towards a degree!
- **Lecture #:** 26
- **URL:** https://www.coursera.org/learn/introduction-to-concurrent-programming/lecture/csw2C/cuda-keywords-video
- **Extracted:** 2026-06-19 21:39:19

---

This video will focus on three keywords which are required and also very powerful. There are three classes of CUDA keywords. The first is a collection of keywords related to how, and where CUDA code is invoked and executed. The next three of those keywords that describe the division of computation on CUDA hardware.

Finally, the last set is a set of keywords. There are those concerning host and device memory. If you want to make sure your code is called from the correct location and executed where you want it. You will have to pay attention to these keywords.

They show the flexibility of CUDA code that you can use it somewhat interchangeably in different contexts. These keywords are part of the function signature, not how you call the function. If you want your code to execute on the CPU think you should use the host keyword. If you want Kodak's key on the GPU and be called from the CPU, then use the global keyword.

Lastly, if you want to have hierarchical code in the GPU, calling other GPU code, then add the device keyword to subordinate functions. At the top of the slide, you can see the kernel with its three less than and greater than symbols, showing that you use that to determine how many threads per block, blocks per grid, size of shared memory. If you want to associate a cudaStream to the execution of a kernel, to understand how that impacts the execution of code on the GPU. If you have n pieces of data, and specify n threads per block, or n divided by m threads per block, and with m blocks per grid.

Then each invocation of the kernel will carry a single thread on GPU. This is not always the outermost execution pattern. Say if you need to share data, memory across threads, blocks are collections of threads. The chair memory and really should have a multiple 32 threads.

As a thread sizes, threads are three-dimensional layouts of threads, which can be helpful if your data is three-dimensional by nature, like video or maps. Let's go to our final collection of keywords, those associated with memory primitives using the classic C, or C plus plus standard primitive datatype keywords, or attempt to use register memory as much as possible. Using either the cons or cons tunder keywords, or attempt to use constant memory as much as possible. There's a similar pattern with shared memory.

Note that is not guaranteed that share memory or all be block allocated. Shared memory can happen that the compiler has to push the data into global memory. The device tunder keyword is an optional keyword for indicating memory on devices, and not on CPUs.
