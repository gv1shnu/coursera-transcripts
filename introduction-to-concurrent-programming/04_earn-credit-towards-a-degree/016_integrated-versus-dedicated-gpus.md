# Integrated versus Dedicated GPUs

- **Course:** Introduction To Concurrent Programming
- **Module 4:** Earn credit towards a degree!
- **Lecture #:** 16
- **URL:** https://www.coursera.org/learn/introduction-to-concurrent-programming/lecture/Dl0Rj/integrated-versus-dedicated-gpus
- **Extracted:** 2026-06-19 21:37:33

---

Hello, and welcome to the first lecture of the fourth module of this course. We'll focus on defining the capabilities and differences between integrated and dedicated GPUs. The three topics for this video will be concerning learning about both integrated and Nvidia GPUs, which are a subset of dedicated GPUs, and some use cases and framework comparison. Let's start discussing integrated GPUs.

Most base versions of consumer laptops and desktops are configured with this type of hardware, they don't support Fender's specific programming frameworks such as CUDA but can be used with general or heterogeneous programming frameworks such as OpenCL and OpenACC. Often, the same company that makes the CPU for a machine will make the integrated GPU that it uses since the GPU is on the same chip. That is what integrated means in this case, integrated with the CPU. Positives are that they're physically close to the CPU and shared system memory.

They also get less hot and use less power, so they help with battery life. Downsides are that they're much less powerful, lagging well behind dedicated GPUs since they must be co-resident with the CPU. Nvidia makes the most commonly available programmable GPUs. By that, I mean that AMD makes their own GPUs that are very powerful, but they don't have the same level of adoption of programming directly on the GPU.

They're more oriented to video and gaming applications. Nvidia GPUs are getting better and getting more processing with less power consumption and therefore less heat. Powerful laptops can be built with Nvidia cards included, but they are more commonly found in desktops and servers. Unfortunately, you cannot get a Mac with an Nvidia GPU, only AMD, which is probably related to their (Apple's) lack of interest of support for OpenCL and CUDA, focusing more on their own GPU programming framework Metal.

A common use case for integrated GPUs is under less-defined programming or heterogeneous workflows since GPU might or might not be used and therefore the cost of the hardware and extra power consumption is lower. Dedicated GPUs have become more heavily used under use cases such as cryptocurrency mining verification, natural language processing, and computer vision. In the case of NLP and computer vision, programmers are often either directly or indirectly using neural networks since they map really well to the Nvidia hardware, performing when there are many processors doing a small amount of work. If a program needs to take advantage of different types of hardware for different tasks, OpenCL is widely used in open-source computing software that is built around programming as many hardware platforms as possible.

OpenCL code is in separate files or compiled into C or C++ code as text that is then sent to the hardware compiling in place. The follow-on to OpenCL is OpenACC or Open accelerator, which removes the requirement to have separate code, but rather has developers use macros around sections of code that can utilize accelerators such as GPUs and field-programmable gate arrays. CUDA is the most widely adopted framework and gives more access to the developer throughout the Nvidia hardware.
