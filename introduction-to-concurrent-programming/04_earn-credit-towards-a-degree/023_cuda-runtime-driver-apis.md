# CUDA Runtime Driver APIs

- **Course:** Introduction To Concurrent Programming
- **Module 4:** Earn credit towards a degree!
- **Lecture #:** 23
- **URL:** https://www.coursera.org/learn/introduction-to-concurrent-programming/lecture/db7AR/cuda-runtime-driver-apis
- **Extracted:** 2026-06-19 21:38:48

---

We are going to focus this video lecture on the CUDA Runtime and Driver APIs. Aside from revisiting the overview of the various layers of the CUDA software architecture, we will dive down into the runtime and Driver APIs. Once again we will use the CUDA software layers diagram to show how different parts of the development process interact for this discussion. The CUDA application that you develop will communicate to the runtime or driver A PIs.

The decision of whether you would like to have your code more directly communicate its desires and the underlying in video hardware is very important. Vision will define what your code looks like and how it will be compiled in the intermediate files that will be used. The runtime API is an abstraction of the driver, saving developers from task like initialization of modules and managing context. Another simplification is that in the runtime API all kernels that were compiled into any associated GP code are available to host code.

No need to selectively load modules and kernels into the current context. To write code that utilizes this, API you will need to write in a C++ language in general, this is the most common form of development. If you would rather develop lower level code that allows you to exert more control over what the compiled code is and how it affects what happens on the GPU. Then the CUDA driver API is your tool.

The most interesting feature is that even though it is lower level code can be written in assembly, but also any language that can link and execute dot. c u b i n objects can be used. The API itself needs to be explicitly initialized in the host code with the Q and it function. The major complications in writing driver API code is that the major components such as devices, code modules and the context in which the GPU code is executed must be managed by your code.

So consider if the extra power is worth the other considerations needed to exercise that control, or if it makes more sense to go with the simpler APIKA, the runtime API.
