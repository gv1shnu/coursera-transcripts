# Shor Easy Way

- **Course:** Quantum Computing With Qiskit And Advanced Algorithms
- **Module 6:** Shor's
- **Lecture #:** 32
- **URL:** https://www.coursera.org/learn/packt-quantum-computing-with-qiskit-and-advanced-algorithms-wils7/lecture/1q99Y/shor-easy-way
- **Extracted:** 2026-06-22 15:24:55

---

Hi. So, without going into the further details of the mathematics of Shor's algorithm, I need to show you the easiest way to do this using Qiskit, okay. As I said before, many of the computations, or many of the operations that we will be doing on the quantum computers in the future, will be based on some popular libraries that would be developed by IBM or Microsoft or Google, or any other big companies, they will just create layers of abstraction for us and we will need to use it in order to make things easier for us, okay. So let me show you one of those algorithms.

So I'm going to open a New Notebook from here, and we're going to see how to do this with a couple of lines of Python code. So, it would take so little codes for us to break the RSA encryption in the future if we have enough number of qubits. So let me just name the ShorsAlgorithm, and I believe we are in QX13 right now. So I'm going to import the Qiskit, okay, or just from qiskit import everything, like this, and then I'm going to, import, from qiskit.algorithms import Shor, So, here you go, that's all we need.

And remember I talked about the aqua, so they migrated to the qiskit.algorithms. So it's very easy to use this. So all we got to do is just create the backends by saying that, Aer.get_backend, and we're going to do this within the 'qasm_simulator'. And the reason why I called this quantum_instance rather than backend or something like that, this Shor algorithm that we imported, asks for these parameters, like quantum_instance, so that's why I named it like this.

Of course, you can name this Variable anything you want. And, since we have imported this Shor's algorithm right now, we can just go ahead and use it, and, we're going to create an instance out of this Shor's algorithm, and it actually asks for the backend that we will be working on. So, the backend parameter is quantum_instance, so that's why I named this quantum_instance. And, it's very easy to get the result back, like, we have to just say shor.factor, and just write the number that we want to factor, like this, and also we need to specify the random number that we will be choosing again.

So, I have chosen to give 7 this time, okay, you can just choose your own random number. And all you got to do is just write the Factors or the prime factors of this, is something like result.factors. So, all we got to do is just this. And as you can see, it will create this and it will just find the factors for us, so 3 and 5.

It's that easy using the Qiskit, okay. And, again, in the future we will be dealing with just this stuff. But, of course, in order to deal with this stuff as well, you need to read the documentation, you need to understand how it works, and also you need to understand the theory. You need to understand what's going on behind these curtains.

So, in order to read the documentation, you can either call the Help function from here, okay, you can just say help(shor) for example, and it will just show you the documentation of Shor, or, of course, you can go to Qiskit's documentation online, and just read about it over here. For example, I can see all the parameter names from here, that's how I learned about this in the first place, okay, I went to the Qiskit documentation, I have read about it, so that's how I'm supposed to actually understand all of this without having an online tutorial or something like that. So, even though it's very easy to use this, we still need to understand what's going on behind the curtains, because there are a couple of very important quantum algorithms or quantum concepts that is being used in this Shor's algorithm, one of them is being the Quantum Fourier Transform, the other one is Quantum Phase Estimation, we need to learn about those stuff as well, and consider this like an optional section. So we're going to deep dive into the details of mathematics and also the QFT and QPE as well, but, it would do very good for us to comprehensively understand the quantum computation.

So we're going to stop here and continue within the next one together.
