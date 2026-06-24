# CUDA Compilation and Execution Syntax

- **Course:** Introduction To Concurrent Programming
- **Module 5:** Earn credit towards a degree!
- **Lecture #:** 25
- **URL:** https://www.coursera.org/learn/introduction-to-concurrent-programming/lecture/iXB0D/cuda-compilation-and-execution-syntax
- **Extracted:** 2026-06-19 21:39:09

---

Hello and welcome to the final module of the introduction to concurrent programming with GPUs course. This specific video lecture is going to focus on the practical aspects of taking CUDA code, compiling and then executing it. This video lecture will have three main parts. First we will discuss the C++ example.

It's compilation and execution. Then we will explore the same cycle with the CUDA runtime API and then with the CUDA driver API. Let's start with the main function of the C++ example code. The first few lines of code initialized the X and Y arrays specifically With 1.0 and 2.0 respectively.

Then the ad function is executed on the one million values and there's arrays. Followed by a test of what the max difference between the expected values of the updated arrays, and what is found which both should be filled with threes, so the output should be 0. Finally, the X and y arrays had their associated memory deallocated and exits with the code of 0. The add function is a simple wrapper around the four loop that adds the first and values of the X and Y input pointers and places the values of each generation back into the Y pointer.

Remember that the add function is running all and iterations of the loop in a single thread. So there's a very sequential set of operations. Knowing we could is you may have practiced with is just passing the input file to the cross compiler. In the above example gcc though g++ could just as easily be used in this case.

And then naming the output object as example underscore code dot exe. Execution is even simpler. By using the Lennox dot operator on the example code dot exe execute all file in the current directory. This run time API kernel looks very similar to the normal C++ sequential code.

With the exception of the global thunder keyword. We will go over this keyword later in this module. Well, let's just say that in this case it indicates to the compiler that the function should be compiled for use on the GPU. To execute the runtime API kernel, you'll need a main function like any other C or C++ code.

Like with any C++ or C program, you will need to allocate memory in this case, in the form of a pointer to the 6th floating point pointers. Two pairs of three rays for host and device memory. Your next step will be to initialize the input arrays with values and then copy the host memory to the device or GPU memory. You execute the Colonel note that you're doing the worst case of it since you are allocating one block with one thread at a time.

Generally it would make more sense to pick a number of threads per block. That was at least 32 and always a multiple of 32 due to some constraints with threads that will discuss later. If you're trying to solve a three dimensional problem, such as mapping or video, you might determine the number of blocks per grid to map to the problems face. Finally, you copy the memory from device into the associated host pointer and free up the memory.

I do not show all the operations for all of the memory, but a quick overview of the various operations, just to give you an idea of what's going on. Not much difference between this code and the runtime API example code. You have access the same information about threads and blocks. In this case, we expressly state that this code is developed for C.

This is where things get a little bit more complicated for the driver API code. You need to initialize the number of things for CUDA and the driver API code to run properly, which is wrapped in a single function shown in the next slide. Like with runtime API code, host and device memory needs to be allocated. But note that you will need to specify all device memory as CU device pointer type.

Launching driver API code may look a lot more like normal code. No triple less than or greater than symbols. Just passing the function pointer, various block and grid sizes, memory pointers and the size of the input memory is one argument array. After you're done with the memory hosting GPU always be allocated.

Initializing the clear related properties gives a lot of control that you do not have in the runtime API. But it is more complex. You need to determine and set the device for a CUDA which gives a lot more information about the CUDA major minor version name of the device etcetera. Once you have the device you will need to create the context for code to run on the device, then there is an intricate process of loading a module on the path to the fat man and getting a function for the module based on its name.

And then finally assigning the reference to the coup function variable. There you connect the CUfunction pointer that was passed into the function to the found function. Yes, that is very complicated. Let me repeat that.

You connect the CU function pointer that was passed into this initialization function into the found function such as they are linked together. The runtime APIs complication can be very complex if you like it to be, but generally it is the same as C or C++. Except that you need to use invidious NBCC cross compiler and link it to the CUDA drivers. The driver of the API compilation has two steps generation of the fab in binary for the CUDA kernel and then compilation of the executable.

Note that the innit CUDA function needs to know where the fat bin is located so this should work. But only if the fat been in the executed well are in the same directory and the path in the code is the correct directory. There can be other strategies, but this is the simplest. Executing a compilation for the driver API can be the same as the runtime API.

Execution of code A code is the same as standard C or C++.
