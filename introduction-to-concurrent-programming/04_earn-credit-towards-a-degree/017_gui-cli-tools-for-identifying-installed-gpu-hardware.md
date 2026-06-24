# GUI CLI Tools for Identifying Installed GPU Hardware

- **Course:** Introduction To Concurrent Programming
- **Module 4:** Earn credit towards a degree!
- **Lecture #:** 17
- **URL:** https://www.coursera.org/learn/introduction-to-concurrent-programming/lecture/oEAeb/gui-cli-tools-for-identifying-installed-gpu-hardware
- **Extracted:** 2026-06-19 21:37:43

---

Hello. This lecture will show GUE and CLI tools that can be useful for you to determine which GPU hardware and specifications you have on your current machine. There are three classes of tools that we will show in this video: operating system provided tools for hardware profiling, command line tools that are generally available, and vendor specific tools for more detailed information about the hardware that they have created. The first hardware profiling tool is the Windows device manager.

Its interface is a large tree-like structure that you'll need to navigate to find display adapters, and under that you should see any installed GPU hardware. Next is the Linux's Sysinfo tool installed by default in Ubuntu and Mint Linux distribution. On the applications left side, you'll see categories for CPUs system, which is for operating system, GPUs, etc. If you have a Mac OS compliant system, the About This Mac tool will show information about GPUs under the display tab.

The Windows Command Prompt or PowerShells, wmic or gwmi commands will show a plethora of hardware information. With the win32_Video Controller flag, you'll get GPU information specifically. On Mac OS, there is a system profiler CLI tool which you can pass the SP displays data tape to narrow down into CPUs and displays. Most Linux distributions provide the lspci tool for listing PCI information.

Like most common Linux commands lspci can be strong together and use the graph command, which will pull out lines matching a pattern. You can see the graph command here. I've added the color option for use of color to make things a little clearer. Pipe the output of lspci into the Graph Command and now you have only the output needed to show the GPU hardware specifications.

The two biggest players in dedicated GPUs, AMD, and Nvidia have their own profilers. These tools are very helpful in determining which operations, such as memory copies and hardware, streaming processors, et cetera, are being actively used at any point. These tools are great for taking code that is running and identifying what is happening at any point, which can be a perfect way to identify memory leaks or vastly underperforming code.
