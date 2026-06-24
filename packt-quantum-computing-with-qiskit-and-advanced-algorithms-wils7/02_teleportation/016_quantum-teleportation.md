# Quantum Teleportation

- **Course:** Quantum Computing With Qiskit And Advanced Algorithms
- **Module 2:** Teleportation
- **Lecture #:** 16
- **URL:** https://www.coursera.org/learn/packt-quantum-computing-with-qiskit-and-advanced-algorithms-wils7/lecture/KJlKY/quantum-teleportation
- **Extracted:** 2026-06-22 15:22:00

---

Hi. Within this lecture, we're going to discuss quantum teleportation. So, I believe this is one of the most interesting and also one of the most hard to grasp subjects that we are ever going to see during this course. However, it's very important for us to understand the nature of this qubits and also the gate ordering and also the gate implementations as well.

So, what we're going to do over here is that we're going to transform some state from some qubit to another qubit, okay. So, of course, we're not going to do something like a physical teleportation, we're going to teleport the information over here. So we're going to try and transfer one of the states to another qubit. So why does it, why is it important, why does it matter?

Because, you can actually clone classical bits in a very easy way, because they only possess a 0 or 1, and you can clone 1 bit value to another one easily. However, in the qubits, it's not always very easy to do that, because, you cannot clone Quantum bit clear states, you cannot clone Quantum bit states. We call this no-cloning theorem, and it actually makes sense, because, you don't even know the state after before you measure, okay. So it's in an unknown state, uncertain state.

And after you measure, you actually lose the information on the qubit as well. So you cannot actually copy and paste one state to another. So we call this Theta's I, as you can see over here, so this is one of the Greek letters. And, so, this is actually an unknown state, we don't know the state yet.

So you can think this like a ket0, ket1, ket+, ket-, it really doesn't matter. We don't know the state, and even ALICE doesn't know the state, even though the qubit belongs to the ALICE. So, in Alpha probabilities ket0, in beta probabilities ket1. Okay, so this is an unknown state, okay, we're not certain what the state is, but we're going to try and transform this state into the BOB's qubit.

So, again, ALICE has a qubit over here, in the state of ket psi. So she doesn't even know what the state is. She will do some operations, and BOB will do some operations to transfer the psi state, ket psi, to the q2, okay. Right now, as you can see in the circuit, we have three qubits, so q0, q1, and q2.

We're going to transfer this information to q2, and q1 will be a like a helper qubit or an, what we call ancilla qubit, okay. So, eventually we're going to transfer this ket psi to the q2 at the end. So, how do we do that? Of course, we're going to apply some gates and we're going to see if it will transform to the q2.

So, in this case, EVE actually has three qubits. She gives one of the qubits to ALICE, to begin with, and she entangles q1 and q2 together with applying Hadamard and CNOT gate, as we always do, okay. But after that, she gives q2 to the BOB, and, after performing some operations, BOB will have to ensure that he has the ket psi on his own qubit. So we're actually going to clone this state into the q2.

But again, it's not a very easy process. We are going to have to think this through a little bit. So we're going to see this in the mathematical side and also in the actual circuit composer as well. And then afterwards, in the next lecture, we're even going to write the Qiskit codes as well, and I couldn't find any more comprehensive explanation of this in the whole Internet, so I believe this will be very helpful for you.

So, what's going to happen over here? We're going to have this entangled state, okay, we know how it works, and then we're going to give the qubit to the ALICE, and she will do some operations on that q0 and q1. So if we follow this mathematically, how does it look like? So we have the ket psi over here and we have the entangled state down below, right?

So this is Alpha ket0, beta ket1. So, if we get this, okay, so ket psi equals to Alpha ket0 and beta ket1. If we tensor product this with the entangled state, then we can have the TOTAL QUANTUM STATE. So, the TOTAL QUANTUM STATE will be 1 over square root 2 and Alpha ket000, Alpha ket011, beta ket100, and beta ket111.

So if it's hard for you to track this from the ket notation, don't worry, we're going to see this exact thing on the circuit composer and also in the Qiskit as well. So, later on, ALICE applies the CNOT gate. So, why does she do that? Because, this will help us eventually clone this thing into the q2, and, if you follow the mathematical equation over here, it will transform the total state into that one.

So, over here we will have some bit flips, and, after that, she will actually apply the Hadamard gate as usual, okay. So when she does that, we will even have much more possibilities over here. It will start with the Alpha 000, Alpha 011, Alpha100, Alpha111, okay, and it will continue with the beta side as well. So, over here, we have a very complicated TOTAL QUANTUM STATE at the end, once ALICE does this.

Maybe you don't even understand why ALICE is doing this right now. Don't worry about it, you will see it in a minute. Okay, just so you know that, this is applying this CNOT and Hadamard, and, then she actually measures this. So she measures the q0 and q1.

So how does it help? So, the reason why we are doing the CNOT gate and the Hadamard gate and the measurements are because of this, because, at this point, ALICE can get this values, and depending on this values, BOB will have to adjust his own q2 qubit in order to have this ket psi. So we know that ket psi is Alpha ket0 + beta ket1. And, ALICE even doesn't know that state as well, so, BOB will have to actually perform some operations to adjust his qubit.

So why does it matter? Because ALICE, if she measures 00, for example, in the q0 and q1, then it means, that if we look at the first two qubit over here, the 00 states, then we're going to see the latest qubit, which is the q2, and we can get the state of the q2. So, over here, if we look at this, we know that the q2 will be Alpha ket0 + beta ket1, okay. And if she measures 01, okay, 01, so here, she will, the BOB will have Alpha ket1 and beta ket0.

And, if she actually measures 10 over here, then if you look at the 10s, then, she, the BOB will have Alpha0 - beta ket1, and, if she measures 11, okay, then the BOB will have Alpha1 and - beta ket0. So, that is a fact, that is a mathematical fact, okay. If, ALICE measures these three things and, these four things, and these are the only possibilities that ALICE would measure, then, we can actually apply some gates over here to correct this and have the Alpha ket0 + beta ket1 state to begin with, okay. So in order to get this, BOB can actually implement the I gate, okay, in the case of 00, and, BOB can actually implement the other gates respectively in order to correct this and have the Alpha ket1, Alpha ket0 + beta ket1.

For example, if he applies the X gate, it will flip this values, and he will apply this in a way that he will have the correct phase and correct state. And if he actually sees this, he can apply the XZ, for example, and it will turn this into the Alpha ket0 and beta ket1 eventually. So, this is very simple actually. But we'll have to decide, which gate to implement, by looking at the values that ALICE had measured, right?

So this is very good. So, how does he do that, okay, do we write an if statement or something like that? Of course not. We can just apply the Z gate, for example, once we see this or XZ gate, once we see this, and X gate, once we see this, and I gate once we see this.

So, if we actually control all of these gates, like a controlled X or controlled Z, then, it will just do these things for us, right? So, if we apply the controlled X, for example, it will check to see if the first qubit is 1, then it will apply the X gate. If we apply this in a controlled Z way, then, it will actually check to see if the first qubit is 1, then it will apply the Z gate to the q2. So if, we don't even have to use any ifs or something like that.

We can actually do this. We can actually apply some controlled Z and controlled X. So we can apply controlled Z. We haven't seen it before, but it's over there, okay.

And eventually, if we measure the q2, it will be in the ket psi notation. And as I said before, maybe it didn't make sense to you, just following this, tracking this with the ket notation. So I believe it will be much more clear for you if we do this in the quantum circuit composer together. So, we're going to have to add one more qubit over here, so we can have three qubits, okay.

So we have q 0, q 1, and q 2. So q 0 will be ALICE's qubit, and, I'm just going to add a NOT gate over here to actually show you that we are starting with the state ket1, okay, and eventually, at the end, we're going to have 1 state in the q 2, okay. So, of course, we cannot say something like, ket psi over here, so I'm using ket1 as an example. And by the way, we can add this barriers over here, like we can add some Identity gates, and we can add some barriers over here, in order to separate the steps, but I believe it doesn't matter right now, so I'm just going to delete this Is or Identity gates and barriers as well, in order not to complicate things.

So know that I'm starting with the ket1, and it will be eventually ket1 in the q 0, q 2, sorry. So okay, let me entangle the q 1 and q 2 together, like we have seen before, okay. So they are both entangled right now. So I'm in this state.

Now what ALICE does, she will actually apply the CNOT gate between the q0 and q1, and then the Hadamard gate, and then measure them both. So she will apply the CNOT gate, she will apply the Hadamard gate, and also, she will measure the both qubits together. Once she does that, she will either get 00, 011, 0 or 11. So, we know there are four possibilities, and depending on those, we're going to have like a CNOT over here, so it will be controlled NOT, and, if the q 1 is 1, then it will apply the X gate to the q 2, okay.

If that's not the case, it's not even going to do that. And also, we're going to have to figure out this in a way that we can actually apply this to the Z gate as well. We haven't seen that one before. It's in the Qiskit, but it's also in the circuit composer as well.

It happens that, you can actually drag and drop the Z gate, and then add a controlled version of it later on. So, if you bring in the Z gate over here, for example, to the q 0, then, you can actually have a controlled gate modifier over here. So this is called controlled gate modifier. All you got to do, just add this to the Z, and choose where you want to just add it.

So I want to add it over here and just put it over there. So here you go. The pink thing over here is the controlled Z and the final measurement will be the q 2 over there. So if I measure this, so it should have 1 as a state, okay.

So q 2 should always be 1, because I teleported the q 0 state to the q 2. So let's do this, let's try and run this and try to see what kind of measurement or what kind of possibilities that we are going to get, because we cannot see it in the Q-sphere right now or the Probabilities pane, because we added measurements, remember? So, let me come over here and choose the qasm_simulator one more time. So I'm going to make the Shots something like 1024, it's okay, and, I'm going to run this.

So once it ends, we're going to check to see the values of the q 2 and they should all be in 1s, because we initialized this q 0 as 1, we haven't actually initialized it as 1, but we changed it to a 1 before we do anything else. So, here you go. It says New job result on the left hand side. So I'm going to go into here and just click on the Completed section, so that we can get the results back from there.

So again, we're going to check the q 2, and remember this ordering of the qubits are reversed in Qiskit, or in here as well, so we're going to have to look at the last bit or last qubit in order to check to see if they are all 1s, okay. So if you click on that, now you can see the bar chart over here, and you can understand this in a better way. It doesn't matter, the first two measurements over here. The final measurement is what we are looking for, because first two measurement will wear I or will change according to the state.

So let me click on this, and let's see the results. So I'm going to open the histogram over here, let me Zoom in a little bit. So, let's see the latest qubit, which is the first qubit over here actually, q 2 is the first bit that we see over here, and the q 0 is the last thing over there. So, as you can see, q 0 and q 1 changes from time to time, but q 2 is always 1.

So that's exactly what we expected to see. So 20% of the time, it changes, the outcome changes, actually, but we are not even interested in this or this one, okay, we are interested in this one. So as you can see, this is always 1. This is q 2.

So this is q 2, this is q 2, and this is q 2, and they are all 1s. We actually transformed the 1 state into the q 2 by using the teleportation circuit. So again, maybe you didn't understand the ket notation, and maybe you haven't been able to track them, but right now it should make sense to you. So, let's do the same thing in the Qiskit, so that it would reinforce our information.

Let's meet in the next lecture together.
