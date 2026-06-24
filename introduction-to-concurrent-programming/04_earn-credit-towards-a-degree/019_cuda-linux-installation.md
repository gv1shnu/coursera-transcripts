# CUDA Linux Installation

- **Course:** Introduction To Concurrent Programming
- **Module 4:** Earn credit towards a degree!
- **Lecture #:** 19
- **URL:** https://www.coursera.org/learn/introduction-to-concurrent-programming/lecture/A2eHC/cuda-linux-installation
- **Extracted:** 2026-06-19 21:38:05

---

Hello. Welcome to the fourth lecture of this module, which will go over CUDA Linux installation. As we record this, we are just before Nvidia GTC 21, which is in April of 2021. We're going to install for Linux, so choose that in the target platform, then we're going to choose an architecture which is X_86, which our AWS easy to incents will be, and then a major decision is which distribution of Linux we're going to use.

In this case we're going to use Ubuntu because it's fairly common and well supported, and we're going to choose one of the long term supported versions, which as of now is 20.04. Now, the last step is to choose which installer type we're going to choose. The Debian package manager version, which will pull everything down over the network, and then once you click that, you will see the base installer commands. There are six commands you have to execute on a Debian package manager.

The first is getting the binary installer. I paste this command into the Linux command line and get the binary installer. The next thing I do is move that package manager information into the app commands preferences directory, I'm then going to hand the public key for the distribution into the apt key repository. Next, I'm going to add the repository associated with that public key to the apt command.

Now that repository with the CUDA installation information is now available. I'm then going to update the apt repository with the latest information from the newly added apt repository. Final step will be to tell the apt command to install the CUDA library. We'll also install a number of dependent packages such that at the very end of this command, you'll be able to execute the required commands like NVCC and also you will have the C libraries, it may also be necessary to run the apt install command, trying to get Nvidia CUDA toolkit.

Sometimes CUDA does not come distributed with NVCC, so just do this just in case, and this always installs the NVCC command. Now let's view the test at say CUDA file using the Vem editor in Linux. You will see that there is a global kernel at the very top, that is a method with the global [inaudible] named saxpy, which is a simple mathematical operation. There is a main, which is a rather large operation which does allocation and copying in both directions of memory while performing the operation.

It then prints out the maximum error it sees in the calculations that have been run. We're then going to compile the test that's using the NVCC command, and output the test at exe, executable. We'll then run the test at exe using the dot slash Linux command. You'll see a output of max error, which in this case is zero.
