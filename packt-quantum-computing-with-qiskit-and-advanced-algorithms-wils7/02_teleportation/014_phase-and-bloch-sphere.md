# Phase and Bloch Sphere

- **Course:** Quantum Computing With Qiskit And Advanced Algorithms
- **Module 2:** Teleportation
- **Lecture #:** 14
- **URL:** https://www.coursera.org/learn/packt-quantum-computing-with-qiskit-and-advanced-algorithms-wils7/lecture/uxeFm/phase-and-bloch-sphere
- **Extracted:** 2026-06-22 15:21:39

---

Hi. Within this lecture we're going to see the Bloch sphere and also the rotations of the vectors. So I'm going to create a New Notebook from here, and I'm going to name this QX03-Phase, and maybe PhaseAndBlochSphere. Okay, so that is how we spell the Bloch sphere.

So I'm going to Rename this, and this is going to be one of the most important lectures and also, one of the longest lectures in this course. So, I'm going to start by importing the Qiskit. So I'm going to say from qiskit import, everything, which is star, and, since we are going to use the Bloch sphere this time, I'm going to say from qiskit.tools.visualization, and I'm going to import the Bloch sphere plotting library. So in order to do that, you need to write like this, import plot, okay, _bloch_, and beware of the spelling, multivector, okay.

So, the reason that I'm using the multivector, we're going to be working with 2 qubits in order to see the differences. So I'm going to say from qiskit.visualization import plot_histogram as well, and we know how it works. And, finally I'm going to say matplotlib inline in order to just visually draw the circuits that we will be composing. Finally, I'm going to import the Math, because we will need the mathematical like rotations, like the pi, the pi number or some other mathematical rotations as well, I will just explain them when the time comes.

So, what we do over here is to actually visualize all the rotations that is going to be caused by the matrices, okay. So, first of all, I'm going to start with calling aer.backends. And, of course, I'm going to go for the qasm_simulator, and I have actually mentioned the statevector_simulator to you as well, maybe you remember that. So, I'm going to first define the qasm_simulator over here, and it will be Aer.get_backend, okay.

And remember, we need to write the full name like 'qasm_simulator' over here, and also I'm going to define the state_vector simulator. So I promise that we're going to see this, and right now we're seeing it. So I'm just going to say, Aer.get_backend('statevector_simulator'). Here you go.

Now, we have two simulators. Of course, we can use them interchangeably and just see the results and compare them when we need to. So, we're going to create the circuit with the 2 qubit, and then we are going to apply some different phases or different rotations to each of this qubits and see the result to compare them, so that we can actually understand what's going on behind the curtains this time with the maximum clarity, okay, because in the Q-sphere, we actually made it clear somehow, but this time it will be much more clear. So I'm going to define a function over here, called run_on_simulators, which will take the circuit as an input.

So I'm going to use this function a lot. We're going to run this on both simulators a lot. So it's better to just create a function that does this for us rather than copying and pasting it. So, for the Statevector, I'm going to create a job called statevec_job, okay, and I'm going to execute the circuit with this statevector_simulator backend.

So I'm just going to write statevector_simulator over here. So this is the variable that I have created over there, and this will be our job. So, to get the result of this job, you can just write result = statevec_job, okay, .result, like this, like we have done before. It will give you the result, and, of course, you can use one of the visualization tools to draw this, and remember, let me come back here.

In the Q-sphere, we have already seen the statevectors popping up, but this time we're just going to use the Bloch sphere, rather than the Q-sphere, so it would be much more easier for us. So I'm going to get the Statevectors first. I'm going to say statevec = result.get_statevector. okay, it will give us the vectors.

So, you can call the statevector, statevec, whatever you may want to call this, and then, of course, we're going to show those vectors inside of the Bloch sphere. So that would give us many possibilities to understand the rotations that has been caused by the matrices. Of course, we want to measure the circuits somehow, but, we don't know how many qubits we have in this case, okay. So, maybe I want to measure the first or second 2 qubit, like qubit 1 and qubit 2 and put it in the classical bits, but I don't know how many qubits I have in the circuit, okay.

So I'm going to make this function as generic as possible. So, rather than giving the qubits like, in a static way, I'm going to get the number of qubits from the circuit, okay, and apply those logic over here. So I'm going to say num_qubits = circuit.num_qubits, okay, you can get the number of qubits like this. So, right now we know how many qubits are there in the circuit.

So I know we're going to create 2 qubits, but maybe you may want to use this function later on for some other purposes, so I'm going to try and make it as generic as possible as well. Like, if you go to google.com, by the way, I didn't even know how to get the number of qubits from a circuit, so I googled that, okay, Qiskit number of qubits from circuit, and it brought me the documentation for that, and I have just searched for it, over here, like number of qubits, and here you go. It returns me the number of qubits, now I know which property use. So, that's how I know what property to use which time, okay.

So, for example, over here, it happens that we can get the number of classical bits as well, I didn't know that either. So, if you need something, always refer to the documentation, that is my point. So anyway, over here, I want to actually measure all the number of qubits and just measure them in the number of classical bits. And I assume that number of qubits will be equal to number of classical bits, of course, that's not the case every time, but you can use the classical bit property to get the classical bits and check to see if they're equal to each other as well, but I'm not going to do that, okay, let's not go ahead and make it much more complicated than it should be.

So I will assume that number of qubits will be equal to number of classical bits. So what I'm going to do, I'm going to say i for i in range(num_qubits). So this is a way to actually simplify the for loop inside of one line, so it's going to take the, it's going to create a range for the number of qubits, for example, in 2 qubits it's going to create a list, going from 0 to 1, and it's going to take everything inside of that range and assign it to the Variable i. So, it will just measure the first qubit, and then the second qubit, as long as it continues.

Now I'm going to do the same thing for the classical bits as well. Again, I'm assuming that number of qubits will be equal to number of classical bits here, but, we're just going to initialize the circuit in that way, so it won't be an issue for us. So far, so good. Now, this will measure the circuit, and I have the statevector, and I have the simulator over here.

Now, I can just run this in the qasm_simulator as well. So I'm going to call this qasm_job, and I will execute this on the qasm_simulator that we have created in the previous cell, so that's the one that I'm talking about, okay. So this will be our qasm_job. Of course, we can get the result back from the qasm_job as well to just show it on the plot_histogram visualization tool, or any other tool that I want.

Great. Now, let me just show you how to add shots, because I have said that I will show you how to add shots parameter, and I didn't do that, here you go, it's that easy. You can just specify the parameter over here, and don't forget to add the result over there, so that we can just get the result in one line, and, I'm going to get the counts from that, we know how to get it. All we got to do is just say qasm_job or qasm_result.get_counts, okay, and since we called this job, I believe we can make it, may be, much more explicit by saying that qasm_counts, but we didn't get counts in the statevector, so, I believe this would be okay.

So after getting the counts, I'm just going to return the statevec and also the counts. So why I'm doing that? Because right now, if I run this function, it will return me the statevector and also the counts for the same circuit. So I can use the statevector to visualize it with the plot_bloch_multivector tool, and I can use the counts to visualize it with the plot_histogram tool.

Right? So, within the same function, I actually managed to use both the statevector_simulator and also the qasm_simulator. Of course, we could have done that without any function, but believe it or not, we're going to do this a lot of times during this lecture, so that it would be much better for us to have this on a function, okay. So let's create the circuit.

So I'm going to call this QuantumCircuit(2,2), okay, 2 classical bits and 2 quantum bits. And then, I'm going to get the statevec and the counts, and let me just correct this one, by calling run_on_simulators, okay, run_on_simulators, and open the parenthesis and give the circuit that we have created over here. Now if I do that, it will just give me the result, but we haven't added any Quantum Gates or something like that. Now, I know I have the statevector and count, so let me just use the plot_bloch_multivector over here and just give the statevec as an input, so that we can see it.

And also, we can use the counts to run plot_histogram as well. But as you can see, this is the Bloch sphere. So it is very similar to Q-sphere that we have seen, but over here it's very easy to see the x axis, y, axis and z axis, so it's in the 3-dimension over here. So it actually points up to qubit 0 in the ket0 state and it's also the same as the qubit 1 as well.

So, since we didn't do anything, they both point up to the ket0, of course, it will change once I start adding some kind of gates. For example, let's add the Hadamard to the qubit 0, and let's, don't do anything to the qubit 1. So what happens when we do the Hadamard gate? In Q-sphere, we know that it some kind of points to the both ways, like ket0 to ket1.

However, that's not the real thing, right? So if I run this one more time on the simulators, and beware that we're using the same function, so that's the beauty of it. So what happened over here is just a rotation like this, right? So it rotated, and it's now pointing up to the X Bloch over here.

But, once we do that in the Q-sphere, it kind of pointed up to the ket0 and ket1, so it made us visually much more sense, because we know that it's in the superposition. However, in mathematics, or in Geometry, it doesn't happen that way. It rotates it like this, and the reason why we are seeing this, because this is the actual thing, okay. So let me plot the histogram.

So, if I get the counts, as you can see, we're getting 00 and 01. So, the one thing that you should consider over here or keep in mind is that, so the qubit 0 is in either the 0 state or 1 state, and that is true as well. So if I had 2 qubits over here, and if I put only 1 in the Hadamard or in the superposition, it will get ket00 and ket01. So, the first qubit gets either 0 or 1, but second qubit will have always 0 state.

And the one thing that you should keep in mind is that the qubit 0 is in the second bit or second representation over here, but that is the thing in the classical bits as well. So we always start at the last, so it's kind of reversed, but it makes sense, okay. So, what you see over here is the mathematical representation or geometrical representation of the Hadamard gate. So again, don't get confused for the ordering of the q0 and q1 in the plot_histogram result over here, the second thing that you see is the q0.

And first thing that you see is the qubit 1. So, let me just copy this thing and paste it over here, and start it from scratch, and just paste it over here as well, and also paste this here as well. So, without doing anything, let me try to add something else. So, I'm going to say circuit.h and also say circuit.cx to 0,1.

So I create an entanglement between those two. So what will happen then? So if I run this, so we get 00 and 11, but we didn't get Bloch sphere, because it's a very bad idea to run the Bloch sphere and histogram at the same time. So I'm going to just delete this, and here you go.

It cannot even represent it, right? So even though we get the 00 and 11, state, so everything seems to be fine, but as you can see, we cannot see the entanglement over here geometrically. So it makes sense. It cannot actually represent the states like independent from each other at this time.

So we see this kind of weird thing. So, sometimes it's very clear to look at the Bloch sphere, sometimes it's very clear to look at the Q-sphere over here, because over here once we get the entanglement, we know that it's pointing up to ket00 and ket11, but it's not what happens in Geometry, right, it's not what happens in real life. So, Q-sphere is for there, just to make it much more easier for you to visualize what's going on, but here, the Bloch sphere is actually here to let you understand what's going on geometrically, or what's going on for the matrix implementations. Great.

Now, we have seen all of those things. So, let's go into something that we haven't seen before, like the rotation, some custom rotations maybe, or the Z gate. Let's try to see the phase and see what it looks like. So I'm going to copy all of those things and paste it over here, okay.

So rather than Hadamard and CNOT gate, I'm going to do something else, I'm going to do rx. So what does it mean, rx? It means that we're going to rotate in the x-axis, okay. So we can actually specify some custom rotations, and I'm going to just rotate it by math.pi/4.

So I'm dividing the pi number with 4, and I'm going to apply it on the first qubit and also I'm going to do another rotation like math.pi, okay, and I'm going to just divide it by 2 and apply it on the second qubit. I'm just doing this in order to show you how it looks like. So far, so good. Now, as you can see, in the qubit 1, we are pointing up over here.

So we actually did like pi/2 rotation along the x axis and we landed up there. So, that makes sense. So I don't know which gate is straight, but we can rotate the statevector by saying that, if that's one of the key things into our circuit. So over here, we have like 45-degree angle pointing up something around there, with math.pi or the pi/4.

So the idea over here is that the circumference of this circle is 2 pi, and we know what will happen if we use pi or pi/2 or pi/4, and it's actually Geometry, right? And I can do that in the y axis as well. So if you say ry, and as you can see, it actually rotates, it's like taking the base for the y axis. And, as you can see, in the qubit 1, we have a very similar thing with the Hadamard gate.

So once we added the Hadamard gate, it actually does this, right? So what does it mean? It means that every rotation is kind of a mathematical operations, and it happens that Hadamard gate actually rotates that vector, like in the y, so it's equal to ry(math.pi/2) in some kind of mathematical equation, right? So, let me create one QuantumCircuit this time, like 1 qubit over here, and let me apply the Hadamard.

And as you can see, they're pointing up to the same x axis. So, the idea here is that, you can actually understand the matrices in a much better way when you multiply them and when you see the actual numbers, but again, these are just transformations, these are just rotations. So let's go back to the Hadamard gate and also bring in the Z gate. So remember, it actually gave us the same probabilities, but with a phase, and we couldn't even visualize the phase inside of the Q-sphere, or it just added a different color.

So, right now if we do the same thing in the Bloch sphere, now we can visualize it, now we can know what it looks like in the rotations, right? So it would make much more sense to us. So rather than only adding the Hadamard gate, maybe after the Hadamard gate, we can add the Z gate as well, and let's see what happens. So I'm going to run this, and here you go.

It's the exact same opposite, it's the exact opposite of the Hadamard, right, so it actually reverses that to the other direction. So, you can understand that if you run the plot_histogram with the counts as an array, like this. We either get 0 and 1. It doesn't even affect the probabilities, it doesn't affect the outcome, but you can understand that.

If we rotate this vector right now, it may land to another thing, right, it may land to another value. So, for example, let me delete the Z and let me add one more qubit over here. So let me add 1 CNOT to make it entangled, and then, I'm going to reverse this operations, okay, I'm going to just add one more CNOT gate over here, not the Toffoli gate, but CNOT gate, and also I'm going to add one more Hadamard gate. So it will just go back to the ket00, and we're going to get 00 state over here.

And we're going to do this a lot, by the way. If we put something into superposition, we're going to use the Hadamard gate to reverse that operation later on in the upcoming circuits as well. So, if we delete those things, we know that it should be either 00 or 11. But if I add the CNOT gate over here, then I know that it should be 00 or 01, because that's how it works, and if I add the Hadamard gate, it will just return back to the 00 state.

But what happens if I add a Z in the middle? As you can see, now it changed the outcome, right? Before reversing that operation, I added a phase, and it actually altered the rotations. So that's what I'm talking about.

The Z gate, the phase, can actually affect the outcome, because, let me just delete this. So I mean the Hadamard and CNOT. Now if I add the Z, nothing will happen. As you can see, it doesn't even affect it, but it adds a phase, okay, it reverses the point like this.

But if I add the CNOT gate, then, again, it doesn't actually do anything without the Z, but if I add the Hadamard gate, it actually does something, and we land in 01. So, great. Now you see in that Z might not affect or the phase might not affect the outcome, but also it might. So, as you can see, phase is this, so phase is the sign in some cases, and also phase is geometrically reversing the vector into some other way, and there are some other operations, like T gate or S gate, and they are all related with the phase, they are all doing some rotations with different kind of angles, like maybe with pi, with pi/2, pi/4, and we can create our own custom rotations by using the rx and ry or rz rotations.

So, as you can see, it doesn't actually limit you, it gives you a lot of options to work on. So, it's very liberating to have kind of flexibility in a qubit. So, it actually creates limitless possibilities for us to do our calculations. So far, so good.

Now we're going to stop here and continue within the next one.
