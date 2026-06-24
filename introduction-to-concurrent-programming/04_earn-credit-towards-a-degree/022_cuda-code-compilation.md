# CUDA Code Compilation

- **Course:** Introduction To Concurrent Programming
- **Module 4:** Earn credit towards a degree!
- **Lecture #:** 22
- **URL:** https://www.coursera.org/learn/introduction-to-concurrent-programming/lecture/TBpgQ/cuda-code-compilation
- **Extracted:** 2026-06-19 21:38:37

---

Hello and welcome to the video lecture that will go over the compilation process in CUDA, using the nvcc command. In order to understand the nvcc compiler, we need to investigate the various available options for the command. One of the easiest ways to know various parts of this command is to use the -h option, to indicate that you would like to see its help content. The first thing that you will see is the usage pattern for the command.

Then you'll see a description of input and output file formats, followed by command options for handling them. The next important area to investigate is how to handle linking the device and host code into one executable. Make sure to pay attention to whether the linked and compiled code will create a relocatable executable. Another command option lib, allows you to compile all output files into a library file, which can be very useful for larger shared projects.

There are an option is a good command to compile, link and execute code in just one step. The last two categories of options are those for debugging, profiling and output architectures. By default output code does not allow for profiling of GP code or debugging host code. The profile and debug options allow this type of additional content to be included with execute rules.

If you would like to target specific hardware and software architectures, the arch code and gencode options will be required. Real architecture is determine how the code is generated and how it will be compiled for specific hardware architectures. While virtual architecture are about the features associated with different compute versions, the arch option allows you to determine which GPU hardware architecture your code will support. The code option can be used to determine how embedded PTX code will be compiled free, so specifically real and virtual architectures.

The gencode option provides a simplification of the previous two options. All right, let's bring this all together now. So on the left side you will see some example hello world code that is intended freeze with CUDA using the nvcc command. There are two example nvcc compilation executions.

One that aims to have PTX files generated, and you also notice it doesn't do anything about architectures. So you see warnings about compiling for deprecating architectures. The second command outputs a .exe specifically and targets a specific architecture 6.2.
