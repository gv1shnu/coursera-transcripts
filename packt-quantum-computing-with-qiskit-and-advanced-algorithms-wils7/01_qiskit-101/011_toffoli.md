# Toffoli

- **Course:** Quantum Computing With Qiskit And Advanced Algorithms
- **Module 1:** Qiskit 101
- **Lecture #:** 11
- **URL:** https://www.coursera.org/learn/packt-quantum-computing-with-qiskit-and-advanced-algorithms-wils7/lecture/A4QhG/toffoli
- **Extracted:** 2026-06-22 15:21:06

---

Hi. Within this lecture, we're going to discuss the importance of understanding the quantum gates intuitively, so that, in fact, actually, we have been working with the quantum gates for a while now and we have seen a couple of those, and we will see many more in the following lectures as well, and we have seen the mathematical operations, right? That was the important one. So, if we come over here to the Qiskit documentation, you will see that we have many more quantum gates as well.

So, if you see a quantum gate that you have never heard of before, then, right now, I believe you have the capability to understand what's going on, because you know how to multiply the matrices together, you know how to go from one state to another state, and you can actually try to understand the effect on that quantum gate on a particular circuit. However, it's also very important to understand it intuitively as well. For example, there is this gate over here, the Toffoli gate. And if you look at the left hand side, you will see that we have many more sections over here in this documentation, and we will cover all of those things, and many of those things during the course, and I will just show you what to do after we finish this course as well.

So, let's assume that we have never seen this Toffoli gate, and in fact, we have never seen it in this course. As you can see, it says that this is a three-qubit gate with two controls and one target. So it performs an X on the target if both controls are in the state of ket1. So, what does it mean?

Let's go back to Hadamard and CNOT gate. So we have actually seen this, right? So it took this Q-sphere into ket 00 and ket 11, we knew that it's actually in the entanglement state. So, we know how this works.

But do you know how the CNOT works? We have talked about this, but, do you know how it works intuitively, like, without having to multiply the matrices together and see the effect? Of course, you know, we talked about this, but, maybe we should make it much more clear over here. For example, CNOT has one control gate, and one target gate, like one control qubit and a target qubit.

In this case, the control qubit is q 0. So let me delete this Hadamard and let me see what happens. As you can see, it's in the ket 00 state, if I delete the Hadamard. So what does it mean?

So it didn't change anything, right? Because q0 and q1 are initialized in the ket0 state, it's always the case unless it's stated otherwise. So, if I put the CNOT over here, nothing happens. Why?

Because it checks to see if the q 0 is 1, then it applies the NOT gate on the q 1. If q 0 is 0 to begin with, then it doesn't do anything. That's why we call this control gate, controlled NOT gate. For example, if I bring a NOT gate over here, as you can see, it brings down to ket 11, because q1 is in the state of 1 right now, as you can see, it's in the ket 01, and the 1 being the q0 over here.

But if we put the CNOT gate, it will check to see if q 0 is 1. And q 0 is indeed 1 in this case, and that's when CNOT will apply the NOT gate on the q1. So it's controlled NOT, okay, it's controlling the q 0, and it's checking to see if the q 0 is 1, and if that's the case, then it will just apply the NOT gate, so, in the Tofolli gate. As you can see, it says that it's a three-qubit gate, so rather than two-qubit.

Right now we're dealing with the three-qubit, okay, and it performs an X gate or a NOT gate on the target, if and only if the both controls are in the state of ket1. So it's basically CNOT gate with three-qubit, right? And that's the reason we call it controlled NOT gate, okay, not controlled NOT gate, but controlled controlled NOT gate, or controlled controlled X gate. And, as you can see, the representation is very similar to the NOT gate.

So rather than having one controlled qubit, we have two controlled qubits in this case, and q2 is the target qubit. So, as you can see, since now we know the CNOT gate and the Hadamard gate, it would be very easy for us to understand this, right? So if I add another gate over here, and let me delete everything, let's bring in the Toffoli gate. As you can see, nothing happens.

So in the Q-sphere, I see ket 000, okay. So, both, not both, but all of the three qubits are in the 0 state right now. So what happens? If I bring a NOT gate to q 0 or q 1, what happens?

If I bring the NOT gate into one of those, then, q 1 still will be in the ket 0 state. And as you can see, q 2 is in the 0 state, unless we apply the NOT gate into q 1. If we apply it into q 1, then both q 0 and q 1 will be in the 1 state, that's when Toffoli gate will apply the NOT gate to the q 2. So, unless we have both 1 states in the q 0 and q 1, q 2 will not execute that gate, it will not be executed on that Toffoli gate.

So Toffoli gate will implement this NOT gate on the q 2 as long as q 1 and q 0 are both in the ket1 state. So, here you go. Now right now, we know that Toffoli gate looks exactly like the CNOT gate, but for like three-qubits, okay. So it's easier for you to understand this right now.

I believe before this section if you read about this, you wouldn't understand it, but now it's easier, and we're going to make it much easier with the following sections as well.
