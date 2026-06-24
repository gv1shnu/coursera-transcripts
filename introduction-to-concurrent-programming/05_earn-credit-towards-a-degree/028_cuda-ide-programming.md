# CUDA IDE Programming

- **Course:** Introduction To Concurrent Programming
- **Module 5:** Earn credit towards a degree!
- **Lecture #:** 28
- **URL:** https://www.coursera.org/learn/introduction-to-concurrent-programming/lecture/zmoj5/cuda-ide-programming
- **Extracted:** 2026-06-19 21:39:40

---

As a long-term developer, this video lecture on IDE programming for CUDA is of particular interest to me and I hope to you as well. The first three IDE options are the most advanced and popular environments for CUDA development. They have less bells and whistles. Text editors have a very important role in CUDA development, and though they're not editors of code, build tools in conjunction with IDEs, and editors, make a complete development and build process for your CUDA code.

JetBrains suite IDEs include CLion, which doesn't include any specific capabilities for debugging and profiling CUDA GPU code, but is a general C, C++ IDE. It does include integration with the CMake build tool includes a new CUDA project wizard for creating the basic structure for our CUDA program with CMake build files included. Along with projects structure, the IDE also provides capabilities such as code completion, general C, C++ formatting, and other aids the development process. Eclipse.

Well, originally a Java IDE, has numerous variants, including one that allows for profiling and debugging CUDA projects with the Nsight plugins. Major advantage of this editor is the ability to take one IDE and apply it to different projects in different languages and have the view of those projects change automatically. As you can see, there are numerous tools and views specific not just to your project, but your goals within a project. Java will need to be installed on the machine to run the IDE.

But for the most part, this is pretty common these days, or it can be done pretty easily. Microsoft provides two options. The first, Visual Studio is a fully feature IDE and includes numerous integration points for CUDA development, including profiling and debugging via the Nsight plugins. It is probably the best option for development on Windows-based machines, as it is most fully featured.

VS Code is a supercharged text editor built for generally is with many plugins available via the marketplace that allow for syntaxes systems, shortcuts for general memory and management code, and just in general is a very flexible editor which we'll use in our labs. Text editors don't often provide all the features of IDEs, but they can be augmented with plugins. Basing your preference vim and/or emacs are two very Linux command line tools for editing your code. They can make texts like code replacement, syntax highlighting, and project structure navigation easier.

Texts made in similar GUI texts editors are available for most OSs and can have support for editing of the various files within a project. Build tools take the code for a project and their own configuration files and compile the code according to targets. Make uses a single makefile that includes bash shell environment variable declaration, rejects based identification of code, object files and bash scripting to execute simple to complex hierarchical built. Cmake is a more modern and programmatic Build Tool option.

In the example, CMake is told which version of CMake to use, the standard version of C++, which files to compile and how to compile the code.
