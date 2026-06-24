# Teleportation in Qiskit

- **Course:** Quantum Computing With Qiskit And Advanced Algorithms
- **Module 2:** Teleportation
- **Lecture #:** 17
- **URL:** https://www.coursera.org/learn/packt-quantum-computing-with-qiskit-and-advanced-algorithms-wils7/lecture/0GdnT/teleportation-in-qiskit
- **Extracted:** 2026-06-22 15:22:11

---

Hi. Now, within this lecture, we're going to apply the quantum teleportation circuit or algorithm in the Qiskit as well. So I'm going to create a New Python Notebook over here, and I'm going to change the name of this one as well. So this will be QX04-QuantumTeleportation, okay.

So, we're going to actually do the same things that we have learned before. I'm going to import the Qiskit, and I'm just going to make this matplotlib in line, in order to draw the circuits in a better way. Of course, you can import the quantum tools of visualization, like the plot_histogram. We don't need the Bloch sphere in this one.

So I'm just going to get the plot_histogram, and I believe that's it. Do we need anything else? I don't think so. If we need anything else, we can always import it later on as well.

So, let's start creating our circuit. So I'm going to say QuantumCircuit. So remember, we need 3, 3, so 3 Quantum bits and 3 classical bits. And over here, of course, we're going to do some kind of operations.

First of all, I'm going to change this x to 0, I mean, apply the x to q 0, because we're going to transfer that one state into the q 2. Of course, when we learned about theory, I said that we didn't know the state, but in order to actually make sure this works, we need to come up with a state, so I'm just going with the state 1. So I'm going to add a barrier over here. So, I talked about the barrier a little bit in the circuit composer, but it's not very clear there what we are doing, so you will see it in a much more clear way, right now it's just a barrier to make the circuit look better, okay, so we can actually follow this step by step.

So, after that, I'm going to put the Hadamard gate on the qubit of the BOB, so it will be Hadamard 1, okay, and then I'm going to apply the CNOT to the 1 and 2 in order to entangle the 1 and 2 together, like this. And I believe this is a good place to draw the circuit after a barrier, okay, so that you can actually understand what's going on and what is the barrier. So, let's draw this with the output of 'mpl' obviously, and if I hit Shift Enter, as you can see, this is our circuit, and these are the barriers. So this is the X gate, and this is the Hadamard and CNOT gate, and these are the barriers, so we can actually track them in a much nicer way.

So, right now you can see all of those gates step-by-step, right? So this is what barrier does, it's nothing fancy. So you can try to do this on the circuit composer as well, but it works much better in here, as you can see. Great.

Now the next step would be to have the CNOT between q0 and q1, and then the Hadamard gate and then the measurements. So let's apply those. So I'm going to add the CNOT to 1 and 0, and then I'm going to apply the Hadamard gate to the first qubit, and then we can just say circuit.barrier, right, so I can have a barrier over here, and then maybe you can draw or add the measurement, whatever you want. So I'm just going to draw this, so that you can see it in a better way, here you go.

Now, once the ALICE actually applies this, she goes and measures the qubit, and depending on the situation, BOB can do the adjustment. So I'm going to measure the qubit 0 and 1 and put those measurements in the classical bits of 0 and 1. Remember we can do that by specifying some list over here. So I'm going to add some barrier after that as well, and I'm going to draw the circuit one more time.

So I'm drawing this more frequently maybe than I should have, but, as you can see, it can actually show us the progression one step at a time, it would be better for us. So, after the measurement, then BOB will do the NOT gate, I gate, or the Z gate, depending on the the situation, so that situation depends on the values of q1 and q0. Now, what will happen over here, we're going to add the CNOT gate to the q1 and q2. So I'm going to say 1,2, and add the control Z gate, which is the cz over here.

As you can see, it's pretty intuitive to do 0 and 2 together. So this is CNOT gate, this is controlled Z Gate. So, as you can see, you can easily understand what's going on in the Qiskit, it's very intuitive. Now, I'm going to say circuit., maybe you can just put a barrier over here or just get along with a measure.

So I'm going to draw the, measure the second qubit, which is the third qubit actually, q2, okay, and then I'm going to say circuit.draw, so that you can see what's going on over here. Here you go. Now, yeah, that's exactly what I had in mind. Now since we are starting with the 0, q0, and since we are flipping the state to ket1, it should have ket1 or it should have 1 at the end when we measure the q2, right?

So, you can see all the steps over here, and this is again the controlled Z gate rather than controlled X gate, and beware of the representation of this shapes. So you're going to have to memorize this shapes, by the way, you will get there eventually, but you're going to have to understand that this is controlled Z gate, and the previous one is controlled NOT gate. So I really suggest you guys to spend some time on the circuit composer. So, let me get my simulators.

I'm going to say, Aer.get_backend, and I'm going to call this 'qasm_simulator', okay, and then, later on, I can just go along and say result = execute, and I'm going to execute the circuit, obviously, and the backend that I want to execute the circuit on is the simulator that I have just created. So if you want you can specify the shots, like 1024, then, of course, you're going to have to call .result in order to get this result and save it in this Variable that we have just created. Now, after you get the result, you can just plot the histogram by specifying the counts of this result, by writing result.get_counts, and just specify the circuit. Now, if I hit Shift Enter, then we will see all the results in the histogram, and here you go.

Again, the first bit over here that you see is the q2, so they all should be in 1, and here you go. As you can see, we see the 00, 01, 10, 11, it depends on the situation, but we are not interested in those, we are interested in only q2 value, which is always 1, and that's exactly what we had in mind, because we have the state 1 over here, we actually teleported, or we actually transferred that information from q0 to q2. So that is how teleportation in Qiskit works, and maybe you may wonder that will this solve a real life problem, not yet, okay. This is a gate for us to go into the quantum algorithms.

Now, we're going to start learning about Quantum algorithms, and believe me, they make much more sense than this, they are very easy to understand, at least for some time, and then it will get complicated again, but they are actually easier than the teleportation circuit, and we're going to start seeing them in the next section.
