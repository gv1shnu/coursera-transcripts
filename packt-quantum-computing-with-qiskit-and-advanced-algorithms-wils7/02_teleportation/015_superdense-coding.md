# Superdense Coding

- **Course:** Quantum Computing With Qiskit And Advanced Algorithms
- **Module 2:** Teleportation
- **Lecture #:** 15
- **URL:** https://www.coursera.org/learn/packt-quantum-computing-with-qiskit-and-advanced-algorithms-wils7/lecture/iJsCY/superdense-coding
- **Extracted:** 2026-06-22 15:21:50

---

Hi. Within this lecture, we're going to talk about superdense coding, and also we're going to practice what we have been learning so far. So, what is superdense coding? So, we're actually going into the quantum algorithms a little bit starting from this lecture, and we're going to see something called quantum teleportation in the following lecture as well, and it will be very great for us to practice what we have learned, and also make our way into the quantum algorithms in a massive way, okay.

So, what do we mean if we talk about the superdense coding? It means that we can actually store 2 bits of number using only 1 qubit, okay, but that statement is not correct, right, because, even though we know that we can put a qubit in a superposition, or we can entangle them with other qubits, and we can have a computational advantage with regarding to the classical computers, however, eventually it will collapse to 1 bit, 1 classical bit, so either we're going to get 1 or 0, even though we have all these possibilities, eventually in the end we're going to get 1 or 0. So how is it possible that only using 1 qubit, we can have something like 11 or 10 or 01 or 00? So it's very simple, by the way, it's nothing fancy.

We're going to take care of this by using the advantage of the entanglement, right? So if we change one of the qubits, the other one will be affected as well, so that we can just manipulate the outcome by using only 1 qubit in the end, okay. So, it's very easy to understand this intuitively, however, we need to understand how it looks like, so that we can be ready working on the circuits. So over here we see two names, ALICE and BOB, and by the way, in all Quantum documentations, you will see ALICE and BOB, and also EVE very often.

So, ALICE will send some message to BOB, BOB will send some qubits to ALICE, depending on the quantum documentation or essay, you will see these names frequently. And EVE is generally referred as an eavesdropper, trying to listen the message or conversation between ALICE and BOB. We're going to talk about Quantum encryption and cryptology a little bit at the end of this course, but just so you know that these are popular names among the quantum computation ecosystem. So, in our case, in our example, EVE has 2 qubits, okay.

So, she will give one of them to ALICE and other one to BOB. But, before she gives them, as you can see, she applies a Hadamard gate and the CNOT gate, so it's in the superposition and also it's in the entanglement, okay. So both qubits are entangled over here before EVE actually allocates 1 qubit to ALICE and the other one to BOB. So eventually, ALICE will take one of the qubit, okay, and she will apply some gate on that qubit.

So depending on what gate she applies, when she returns that qubit to BOB, she can actually manipulate the result. For example, she can apply an I gate, which is the Identity matrix or a NOT gate or Z gate or NOT Z gate, okay, so NOT gate first and then Z gate later. So, how is it, how does it affect the outcome? Of course, it can affect the outcome, right?

So, for example, if I apply an Identity gate, it won't affect anything. But if I apply like an X gate, it will affect something, eventually, right? Because, the BOB will get this qubit and he will apply the CNOT gate and also Hadamard gate to just get the measurement, and he will measure at the end and he will get some kind of value out of this. But depending on the gate that ALICE has implemented, that value will, of course, change, because these qubits are entangled, so whatever ALICE does will affect BOB as well.

For example, if she applies Identity, which is the Identity matrix, nothing will happen, right? So, BOB will apply the CNOT gate, and he will apply the Hadamard gate, and he will get 00 state back. And indeed we actually have seen this before. If he applies the, if she applies the X gate, then we will see like a flip over here in the 1 and 0, and if she applies the Z gate, we will see a shift in the phase, and if she applies the XZ, we will both see the phase shift and also the flips in the bits as well.

So, of course, we're going to see this kind of operation in the circuit composer, but don't worry about it. But if she, if the BOB applies the CNOT gate and the Hadamard gate later on, he will end up with this values over here. So, at this point, maybe it's a little bit stretch for you to understand this through the ket notation. So let's do that in the circuit composer, so you can actually see the effect yourselves.

And indeed we have seen this, right, we had 2 qubits before in the previous lecture, and we applied this Hadamard and CNOT, then Z gate, and then CNOT and Hadamard gate. So let's start with this entanglement position over here. We're either going to get 00 or 11, we know that, we have seen that before. So, at this point, we have this ket 00, ket 11, and now you actually allocate one of the qubits to ALICE, and she applies the I gate, which is the Identity gate, which is actually a buffer, it doesn't do anything, right?

So, as you can see, it doesn't change anything. So we are still in the ket 00 and ket 11 with the 50% possibility, and nothing happens. So if we reverse this, if we add the CNOT and then if we add the Hadamard gate, what will be the outcome? Of course, it will be the first thing that we have seen, it's the first initialized values, it's going to be ket 00, right?

It doesn't matter even if I put this I over there or not. So you can use the I as a buffer when it comes to the circuit composer and also in the Qiskit as well. So, let me bring the CNOT. As you can see, it changes this to 10 and 00 11, then 00 10, okay, or 01.

So it depends on the ordering of the qubits obviously, but as you can see, it changes to the ket00 + ket01. And, if we apply the Hadamard, it will just come back to the 00 state, right? So over here we see is 00 and 01. Now, let's apply the Hadamard at the end, and here you go,, we are back in the ket00.

Now we actually prove that this is going to be the ket00 if ALICE decides to apply the I gate. So if ALICE decides to give message, some kind of message to BOB, like a 00 message, for example, then she can apply I. But instead, if she applies an X gate or a NOT gate over here, as you can see, it actually ends in 10 over there. So again, it depends on the ordering of the qubit, in some documentation you can see it is a 01, but it really doesn't matter.

What we are seeing over here is that it actually changes the outcome, okay, in a way that ALICE can manipulate this only using 1 qubit, and then it will just have the value of 2 qubits or 2 bits, 2 classical bits at the end. Here you go. Now, over here, in the Z gate, let me just bring in the Z gate and let me delete the X gate from here. As you can see, the result over here is 01 because it changes the phase over there, and we have seen that, and if I apply the X gate and then the Z gate, it ends up with the ket11.

Great. Now, it's actually nothing interesting, because we have seen all of those things before, but it made us, it made us possible for to exercise what we have learned, and it led us to understand this in a little bit more depth. We now know that we can actually manipulate only 1 qubit and change the value of the other qubit if they are entangled and applying the NOT gate or Z gate or any other gate might affect the outcome eventually, and we can use 1 qubit in order to store 2 bits of data, if we have to, okay. So, of course, you can just save them.

As you can see, I already saved mine in another project over here, called Superdense Coding. So once we see this circuits, you can always save them, and they will be available in your account after you return. So, that's it. But, using the Superdense Coding information, we're going to learn something new, which is called quantum teleportation, and we're going to see it in the next lecture together.
