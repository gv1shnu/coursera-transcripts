# Nvidia GPU Architectures

- **Course:** Introduction To Concurrent Programming
- **Module 4:** Earn credit towards a degree!
- **Lecture #:** 18
- **URL:** https://www.coursera.org/learn/introduction-to-concurrent-programming/lecture/7V8FG/nvidia-gpu-architectures
- **Extracted:** 2026-06-19 21:37:54

---

This will be our first venture into Nvidia specific hardware, and software capabilities. As of early 2012, there have been seven major generations of GPU hardware that allowed for CUDA based programming. It all started with the Tesla architecture in 2008, and up to the current Ampere hardware architecture. Note that with each generation of hardware, there were improvements with performance, and software capabilities.

These improvements worked to lower power consumption, at the same time increasing processing power. The seven Nvidia GPU architectures are listed here. Each is the main architecture that Nvidia's manufacturing for approximately two years. You'll go over to put aside the next few slides.

Covering around 4-5 years worth of hardware per site. Tesla, and Fermi architectures were produced from 2007-2012. Tesla was the first architecture that allowed for CUDA programming. It is a small number of cores with a large power usage.

For the Fermi architecture, the most popular cheap card in the architecture is shown here. Quadrupling the number of cores, doubling memory, and improving the memory speed by 33 percent as compared to Tesla. While there is only a small increase in power usage, and output heat. Kepler, and Maxwell architectures were manufactured from 2012-2016.

The major efforts in Kepler were to make GPs more programmable double cores, and memory. Memory speed was lowered along with overall power consumption. Maxwell cards again nearly doubled cores while increasing memory bandwidth, and lowering power consumption. Note that in these two generations you should not only see power consumption going down slightly, but since more cores are available, the performance per watt is effectively doubling with each generation.

Pascal, and Turing, the two previous generations of GPU hardware prior to the latest generation were produced from 2016-2020. Pascal worked on making the memory model more unified, so less worrying about memory configuration, and added NVLink, which makes memory transfers faster, and easier between host, and device. There is a small bump in the number of cores, about 50 per generation. The power usage improvements are slowed in these architectures.

Card memory is much higher, and is almost twice as fast as the Maxwell architecture. Ampere is the current hardware architecture, it introduces Tensors and retracing from touring, and creates more dedicated cores, and almost doubling of cores occurred while halving voltage, which means quadrupling of performance per watt. Memory bandwidth has maintained or slightly lowered based on which specific card was installed.
