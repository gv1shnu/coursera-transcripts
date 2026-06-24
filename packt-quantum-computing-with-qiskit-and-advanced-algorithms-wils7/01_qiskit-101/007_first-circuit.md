# First Circuit

- **Course:** Quantum Computing With Qiskit And Advanced Algorithms
- **Module 1:** Qiskit 101
- **Lecture #:** 7
- **URL:** https://www.coursera.org/learn/packt-quantum-computing-with-qiskit-and-advanced-algorithms-wils7/lecture/faFNk/first-circuit
- **Extracted:** 2026-06-22 15:20:24

---

Hi. Within this lecture, we're going to start writing our first quantum code, which is HelloQuantum. And what we're going to do, we're going to actually implement the Hadamard and the CNOT gate to create entanglement between two qubits. We have seen this theoretically, we have seen the calculation of it in the matrix form, and also we have seen it in the circuit composer.

Now we're going to just make it into the Qiskit. However, before doing that, I want to go into the circuit composer and show you something else. So we have actually done that. So we put the Hadamard on the q 0, we put the CNOT between q 0 and q 1.

So over here, I can add a measurement, okay. So, this is like a gate, but, of course, it means that we're going to measure this qubit. So what happens over here is that we do all the calculations, we do all the gates, and then we actually measure to see the result. Once we measure it, of course, we lose the previous information, and it collapses into either 0 and 1.

And it collapses into the classical bits, so that we can get the final result back. So once I add the measurement, as you can see, the Probabilities and the Q-sphere does not actually give us very proper results over here. Because, as you might already remember, it has to be either ket 0 0 or ket 1 1 with the 50% probability. But once I added the measures over there, now it only shows ket 0 0 for some reason.

Maybe I don't know what's going on, maybe I go into the Statevector and go back to the Q-sphere, and it doesn't change a thing. Now maybe I can think that, yeah, there is something wrong with the ordering of the measurement, or maybe can I measure the q 1 first, then q 0 later, does it mean anything, maybe I can lose the measurements and see if it gives me the appropriate results back, and try to figure this out, okay. So, as you can see, if you add the measurement, it actually changes the calculation. So if I delete the measurement over here, we get the result, as we expect, right?

But once I add the measurement over here to q 0, it actually changes everything. Once I add the second over here, from the previous one, or the later one, it really doesn't matter. The idea over here is that we applied those measurements, but we haven't actually run this on the quantum computer or any simulator. So we need to run this and see for ourselves.

Because with the 50% of chance, we're going to get 0 0 and with the 50% of chance, we're going to get 1 1. So, we need to make sure that we run this multiple times and just see what we get as a result back. So, in order to do that, once you actually compose your circuit, you can come over here and say run, and you're going to have to choose a real quantum computer from here, or a quantum simulator. So come over here to Set up and run, and you will see the available quantum computers here right now.

The available ones might be different from what I see right now. So, for example, I see santiago, athens, and belem, and quito. So, melbourne, as you can see, they're actually named after different cities of the world, like lima, yorktown, and armonk, or stabilizer. So this stabilizer and the other ones is starting with the simulator, so they are actually simulator of the quantum computers, they're not real quantum computers.

And what we see over here is that we have some total pending jobs, and this pending jobs mean that there is a queue. For example, in melbourne, we have 144 pending jobs. If we run our circuit on this melbourne, then we're going to have to wait a little bit, but if we run our circuit in like one of the simulators, and we're going to generally use this ibmq_qasm_simulator, okay, this is the most popular one. So it has 32 Qubits, and it runs your quantum circuits like very efficiently and immediately.

So we generally going to go with this qasm_simulator, but I'm also going to show you how to run this on a real quantum computer inside of the code as well, don't worry about it. Just right now know that simulators simulate the behavior of the quantum machines, and we're going to use them a lot. So we don't have to choose any provider after we choose the qasm_simulator. So for the Shots, so Shots mean how many times we're going to run this on qasm_simulator, okay.

So I'm going to make this into 1000 or 1024, because I'm a software engineer, okay, that's why we're used to. Of course, we can just run this once, but it won't matter, because, we either going to get ket 0 0 or ket 1 1 with 50% possibility, at least, this is what we expect, and we have to confirm that this is the case, for example, if I run this 1000 times, then I expect to see at least maybe around something like 500 in ket 0 0, or 0 0 classical bit, and 500 in 1 1 classical bits, okay. So that should be the end of it, that should be the end result of it. So, I had to just run this multiple times.

So that's why I have chosen 1000 times, I believe you can go up to 8000 times at this point, but they will just increase that number in the future. So, we're going to just run this 1000 times, it will be very sufficient for us to understand whether we are doing the right thing or not. So, after you choose the Shots, of course, you can give it a job name or a tag or something like that, and this will be executed on a simulator, and then you will see the results back, and you can just compare the results for yourselves to see if you're getting the exact same thing that you would expect to see. Again, we're going to do this on the code side, we're going to do this on real quantum computers as well, but you should know how to do this from here, from the circuit composer as well, because this circuit composer will come in very handy when you learn about the gates and stuff.

So job name, I don't need a job name, Tag, I don't need a Tag, I don't have that kind of too many jobs right now. All I got to do is just run this, and wait until we see the results. We're going to get the result on the left hand side, on the navigation pane over there. And once it executes, it will just show you a notification.

If you don't see the notification, okay, I believe right now mine has been changed on the left hand side, as you can see. And even if you don't see the notification, it really doesn't matter. You can come over here to Composer jobs, that's where you will see this Completed job over there, okay. And if it's not completed, you will see it's pending or it's executing or queuing or something like that.

Once it's completed, you can just click on that, and you can see this result, the histogram that you're going to be reading. So over here, as you can see, for 519 times, we got 00, 505 times, we got 11 as an outcome. And that's exactly what we needed to see, because they are in the superposition and they're entangled actually. So, both qubits will be either 1 or 0, and it cannot be anything else in between, like 01 and 10, okay.

So we now know, we have actually confirmed that this gates work, so Hadamard and CNOT gates work, and if we add a measurement later on, we can see the results back. So that's it, that's how we're going to work with circuit composer, as well as we're going to be working with the Qiskit inside of the Jupyter Notebooks. But, if you add a measurement, you cannot see the actual results on the Q-sphere or probabilities, you're going to have to run it and see for yourselves, okay. So that's why I have shown you this one.

So, beware that we are just seeing the 00 in Probabilities, but, in fact, once we run this, once we execute this, we can see the 00 and 11 state. Great. Now, what we're going to do? We're going to take this, we're going to just exactly do the same thing in the coding side.

So we need to create two qubits and two classical bits, add one Hadamard gate to the q 0, add CNOT to the q 0 and q 1, then add measurements to the q 0 and q 1 and connect them with the classical bit 1 and 2, okay. So it doesn't show us the classical bits, like in a collapsed fashion, because we don't apply any gates over there. So I'm going to come back to here. So, maybe it won't be enough time to create all the circuit, but at least we can just import what we need to import and just create the quantum bits and the classical bits, so that we can understand how it's done.

So, let's start with the circuit itself. So I'm going to say circuit =, okay. And in order to create the circuit, we need to register something called QuantumCircuit, okay, we're just driving this from the Qiskit. So if you say from qiskit import *, then it should work.

So what I did over here, I said that 2 and 2. So first 2 means register me 2 qubits, and the second 2 means register me 2 classical bits, okay. So I created a circuit that has 2 qubits and 2 classical bits. Of course, there can be sometimes that you can see this, quantum_register, okay, and it's QuantumRegister(2).

Then it means that it's going to only have two quantum, it's 2 qubits. And you can see something like this as well, I need 2 bits, 2 classical bits, and my circuit will be composed of QuantumCircuit, again, with the QuantumRegister and ClassicalRegister. If you see that, it's exactly the equivalent of this, okay. So I'm generally not going to use this, because, as you can see, first way is much more simpler, you can just state that I need 2 qubits and 2 classical bits, but if you see this, if you see the thing below, then know that it's also valid, and you can use it as well.

So, again, first one is 2 qubits and second one is 2 classical bits. So it happens that this function accepts the QuantumRegister and ClassicalRegister as well as 2 integers, okay. So, again, I'm not going to use this one, so maybe you can just go along with the thing that we have written over here. So what I'm going to do instead is to make this into comments, so that they won't be executed, and just hit Shift Enter, so it will be in your notes.

So, all we did is to create 2 qubits and 2 classical bits, so our current state is something like this. Now what we're going to do, we're going to add Hadamard gates and CNOT gates and then measure them, but we're going to do that in the next lecture together.
