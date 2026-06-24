# CUDA Software Layers

- **Course:** Introduction To Concurrent Programming
- **Module 4:** Earn credit towards a degree!
- **Lecture #:** 21
- **URL:** https://www.coursera.org/learn/introduction-to-concurrent-programming/lecture/h0uL1/cuda-software-layers
- **Extracted:** 2026-06-19 21:38:27

---

In order to determine how you'll use the CUDA developer tool kit, you'll need to understand it in more depth. That is the goal of this video lecture. We will start by discussing the general communication between various software layers. Next, we will talk about the two main workflows for CUDA code compilation via the nvcc command.

The next topic at the top software layer, the application layer. Lastly, we will discuss a very important part of the CUDA software architecture. We will use the CUDA software layers diagram to show how different parts of the development process interact. For this discussion, the CUDA application that you develop will communicate to either the runtime or driver APIs.

The decision of whether you like to have your code more directly communicate its desires to your underlying hardware will be very important. That decision will define what your code looks like, and how it would be compiled, the intermediate files here. If you have chosen to use a higher level access pattern via the runtime API, then you can embed GPU code inside of host code. To do this, you'll need to compile both types of code via the nvcc command.

Once the host code is linked to the GPU, that ptx or that cubin files, they can interoperate. You'll still need to use a host oriented compiler such as GCC or G++, which wore output in the executable. Thankfully, this workflow can be simplified via the nvcc command to have an output, host base executables, which it does by default. This is the most common use of Nvidia for most users, and what we will use in this course.

If you are targeting the driver API, you will need to compile the GPU and CPU code separately and then have the host executable interact with the GPU code via the driver API. This is less commonly used since the process is more specific to hardware and compiler combinations, whereas the runtime workflow can generate more generally usable executables. You're going to be developing the CUDA application very soon. Let's look at what you need to consider when you're starting to write code.

Your application will be part host space, and part GPU targeting code, which can coexist in the same file or be separate, though any code files with CUDA code should have the.cu or.cuh code and header extensions. You can definitely write code in other languages via language specific abstractions or APIs such as pyCuda or jCuda. They will use CUDA within them, but you can write normal code that matches the languages development patterns to vary popular libraries that create neural networks and other mathematical constructs, or TensorFlow and PyTorch. When Nvidia GPUs are present and CUDA drivers are installed, these frameworks will use CUDA as well.

A common way to use CUDA capabilities is to use the Nvidia CUDA developer tool kit libraries. Some are designed to remove the need to write complex CUDA code, or to make complex data structures and algorithms available within your CUDA code. They're almost all maintained by Nvidia, and new libraries are added as new use cases or domains, need more powerful or trusted options.
