# Applying Grover's on Qiskit

- **Course:** Quantum Computing With Qiskit And Advanced Algorithms
- **Module 5:** Grover's
- **Lecture #:** 28
- **URL:** https://www.coursera.org/learn/packt-quantum-computing-with-qiskit-and-advanced-algorithms-wils7/lecture/DENJr/applying-grovers-on-qiskit
- **Extracted:** 2026-06-22 15:24:11

---

Hi. So far, we have understood how to do, like a search algorithm in a classical way. Right now we're going to go ahead and do this in a quantum computational way. So I'm going to take a note over here and just write Quantum Model Grover's Algorithm, okay, or you can alternatively call this Grover's search algorithm as well.

So, we're going to work with Oracle Circuits and reflection circuits and some other things that we haven't learned before. So, what we will do? So first of all, we're going to have 4 states over here, like 01 10 00 and 11, and we're going to search for the 11 state, okay. So in the previous example, we searched for 5 or 8 within a series of numbers, and right now we have 4 numbers, like 00, 01, 10, and 11, and we're going to search for 11.

Of course, it doesn't really matter, because you can always convert binary into decimal and decimal into binary as well. So we're going to be working directly with the binary this time in order to keep things simple. And, I want to just do this with two qubits okay, I don't want to actually increase the number of qubits, because it will increase the complexity, so that we can understand this in a much comprehensive way. So, remember what we did in the Oracle in the previous lecture?

We have actually stated that if the winningNumber is 8, then we're going to look for 8, and we're going to return True if the finding is actually 8, okay. So what we're going to do in the Grover's algorithm is that we're going to flip the phase, change the phase of the WinningState 11. So, we're going to essentially make it -11, okay, -ket11 state. So it will help us identify the WinningState when we measure it.

Of course, this doesn't make sense to you right now, because we're not only going to work with Grover's or the Oracle Circuit in the Grover's algorithm. So we're going to have the Oracle Circuit along with something called reflection circuit, and it will help us to actually increase the possibility to find this WinningState in one shot in this example. So over here, again, our winningNumber was 8, and we're searching for this winningNumber over here. Essentially, the Grover's algorithm will have three steps.

We're going to, of course, start with applying Hadamards to both qubits, and then we're going to actually implement the Oracle, okay. So we're going to just apply the Oracle gate or Oracle Circuit into our circuit, and then, we're going to just apply this reflection circuit as well. So this will increase the possibility of finding the WinningState in a way that it would be very efficient for us. So we're going to see this algorithm, we're going to see the actual reflection algorithm in this slide later on, but, just so you know, let me show you the mathematics of putting things into Hadamard and flipping the state of the WinningState, okay.

So, let me show you. So we're going to start with putting Hadamard into both qubits, and then our vector will be like this, right? So, for each value, for possibility of 00 10 11 and everything it will be 1 over 2. And, if we apply the phase shift for the WinningState , we're going to apply it over here.

So remember, the last one is the possibility of ket11. So we're going to change the phase of this. Remember, this is the ket11, this is the superposition of the both qubits, and this is after we changed the phase of the WinningState. And, beware that we are not dealing with entanglement over here, okay, we're not going to use CNOT.

If we use the CNOT, it will be like 1 over square root of 2, 00, and 1 over square root of 2. But we're just dealing with the superposition over here. If you don't understand this, then just apply the Hadamard gate into 1 qubit, and apply the Hadamard gate into another qubit, and then just take the tensor product of both of them, and it will just end up in like this, right, 1/2 for each possibility. So after we change phase to the ket11 state, then we're going to end up in this.

So I'm going to explain this W and other things later on. But, the first steps are actually very easy, because we have learnt about them so far. But the reflection, we didn't learn about it, we're going to just understand it later on. So let me show you what we're going to do in the Oracle, okay.

So Oracle will take the States and it will change the phase of ket11. So we're going to start with applying Hadamards, and indeed, we're just going to apply one controlled Z over here, and let me show you why. So if I apply the controlled Z, as you can see, it only changes the phase of ket11. So, it works that way.

So if I delete the Z, for example, if I just put Z in the first qubit, then, you can see that it changes to 01 and 11. If I put the Z in another qubit, it changes the 11 and 10, but if I apply this gate over here with a controlled Z, then it will only change the phase of ket11. So if you're looking for ket11, then we should apply this as an Oracle, okay. So if we were searching for another state, then we would have applied something else.

But if we are searching for ket11, then we should apply this. So, this is the first step. We're going to apply the Hadamards, we're going to apply the Oracle, which is the controlled Z, and then we're going to apply the reflection over here, reflection gate or reflection circuit, and then we will measure it. And, in fact, we're going to write this controlled Z, and I'm going to show you how to turn this into a gate, so that if you want, later on you can create your own custom gates as well.

So let me show you how this works. I'm going to create this calling oracleCircuit, okay, this won't be our main circuit, and I'm going to have 2 qubits again. But, we don't even need a classical bit over here, right, because we're not even going to measure this or just do something with it. So, rather than writing something over here, I'm just going to give it a name, okay.

So this will be converted into a circuit. This will be converted into like a custom gate. So I'm going to call this "oracleCircuit", and I will append this, I will add this to our main circuit later on. So this circuit will have controlled Z on it, and that's it.

So, all you got to do is just write to_gate, okay, in order to convert this into a gate, and then you can just try to draw this to see how it looks like. So, I'm going to draw this, of course, with the 'mpl'. So, here you go. That is our circuit.

So maybe you can think that, yeah, why are we converting this to a gate? You can create a regular circuit, like we have done before, and just apply this as a gate. And that is correct. I'm just showing you, so that you can know how to create your own custom gates, okay.

Because creating is easy, but adding this to the mainCircuit is another story. So let me show you how this works. Of course, I'm going to create the mainCircuit with classical bits, because we're going to be measuring this, and I'm going to apply the Hadamard gate in the first two qubits, and actually both of the qubits, because we only have 2. And then, I'm going to append this oracleCircuit here.

So all you got to do is just write mainCircuit.append(oracleCircuit), and just specify which qubits that you should append the circuit to, and in our case, we're going to put this in both qubits, okay. So, here you go. That's how you create your own gates in Qiskit. So if you had like a much more complicated gates to apply over here, then you can create that as a gate, and then you can apply that gate as many time as you want, like creating a function in Python, as you might say.

So let me draw this and see how it looks like. Here you go. As you can see, we don't even see the details, we don't even know what's inside of the oracleCircuit. Again, this might have contained like maybe 100 gates.

So, it's like creating a function or a class. You just apply the function, or you just create an object out of that class, but you don't even know what's going on inside of it. So, after you're done with your function, then you can use it as many as you want, and that's exactly what we're doing over here. So far, so good.

Now, that was the basic one, because we already know how to work with the Hadamard or how we know that ket11 actually is represented with this W state. So this is the WinningState over here. So, now we know that this is ket11 and the S1 is actually the superposition and S2 is the phase shift. But, we have to understand that, we can actually represent this geometrically, because we need to understand what reflection does, okay.

So, over here, we have the ketS1, and this is somewhat orthogonal to the W, ketW. Of course, this is not orthogonal, and we're going to actually talk about this in a little bit. But know that, we are doing this rotation from ketS1 to ketS2 with some kind of angle, maybe we can call this Tessa, okay. So we have + signs over here, and for the last one we have - sign.

So what it means that we are shifting this and we are rotating that vector, right? We have seen this in bloch sphere. So, let's assume that this is ketW and this is ketS1, okay. So we can find a vector which is ketW tilde or something like that, which is orthogonal to ketW, okay.

So I have put that vector in here, I have calculated this with an online tool, but it really doesn't matter what kind of value we have over here. Just know that this is orthogonal, and we have this Theta angle over here. Once we do the shift, once we do the shift from ketS1 to ketS2, we actually shift this with angle Theta one more time. So we are right now in this ketS2.

Now what I want to do is to shift this to ketS3 with two Thetas, okay. So I'm going to take this Theta and just add this another Theta over here and just shift it to the S3. So, why we do that, right, why do we do that? So why do I want to take S2 and turn it into S3, because, once I rotate this with angle like 2 Thetas over here, it will get close to the winning vector, right?

As you can see, it gets closer to the winning vector. So what Grover's or what reflection does over here is that it rotates this in a way that it gets closer to the state W, and, how Grover's try to make and find this or trying to make an assumption of find this WinningState is that, if we do this repeatedly, if we do this one more time, or if we do this like multiple times, it will get closer to ketW in each step, right? Every time I do this reflection, every time I do this rotation, it will get closer to the ketW. So, it will be very easy for me to understand the WinningState, okay, maybe not with 100% probability, but it will be something like this.

So, as I said before, Grover's search algorithm doesn't actually find this magically, it tries to maximize the possibility of winning this ket1 state by doing this rotation, okay. So it happens that we're converting this ketS1 to kets2 with some angle, and we're actually summing that angle and rotating it back to the direction of ketW over here, and it will be closer to ketW each time we do this. [No audio] In fact, all it does is to just change the phase of ket00s and other stuff, rather than this ket11, in order to actually increase or amplitude this possibility, so that we can find the WinningState. So, of course, we're going to use the Z gate again, in order to do that.

So let's see, this is ket00, okay. So what happens if I had this in Hadamard, okay, if I add the Z's over here, like I have done before? So if I do that, and if I add one more Hadamard over here, okay, like this, so it will be ket11 at the end, right? Why does it do that?

So, how does it do that? So as you can see, if I apply the Hadamards and then the Z gates, it changes the phase of ket01 and ket10. So it rotates this state. So we're actually having this over here.

If we delete this, we can see that ket11 and ket01 is changed if I just move it over here, ket11 and ket10 is changed. But if I put them both over here, then ket01 and ket10 has been changed. And now if I add something like a controlled Z over here, as you can see, everything, but the ket00 has been changed. So everything has been changed right now.

If I add the Hadamard, here, now, as you can see, we only changed the phase of ket00. Now, if I can change the phase of ket00, if I can make it -, then it will increase the possibility of having the ket11 as WinningState for me. Now, it's very hard to think this, it's very hard to visualize this, but don't worry, I will prove it to you. Not even using matrices or ket notations, I will just prove it to you with the circuit composer, so it will be crystal clear for you, okay.

So I'm not going to bore you. So we're not going to be dealing with the mathematics one more time, we're just going to prove this, that, if we change this phase, then it will increase the chance of having 11 as a measurement, as the final result. So remember our circuit. So we started with the Hadamards, okay.

So let me add some barriers, so you can understand it in a better way, then, we applied the oracleCircuit, so it was the controlled Z in this case, in this example, okay. So let me add this as well, and then, let me add another barrier over here. We went to the reflection circuit, which is this one, and then we're going to obviously measure this. But we don't even have to measure this, okay.

As you can see, all things point to the ket11 over here. Now we found the WinningState. So, even if we just run this in one shot, then we're going to find the ket11. So, let me open a new circuit over here, so that we can start from scratch and let me show you this.

So I'm going to put these things one more time, okay. So Hadamard, Hadamard, the Z and the controlled Z over here, and, let me see, yeah, here you go, and then, let's see what we have over here. Now we shifted the phase of the ket11, right, so we shifted this phase. Now, okay.

So I'm, actually I managed to change this phase, and that was the rotation of Pi in here. So, as you can see, the phase diagram over there shows us the rotation of Pi. So in this previous example, what we did was to rotate this with Pi, and we managed to get the ket11 state out of this measurement as a result. So, let's try to rotate this with less degree, something like Pi/2 or Pi/4.

So let's see if that changes anything. So rather than applying a controlled Z, I'm going to apply this phase gate, okay. So this phase gate is actually nothing fancier than the Z gate itself. So you can have a controlled Z gate.

But also you can actually determine the rotation over here. For example, if I change this to Pi/2, as you can see, the probability of getting 11 has now decreased. Now I can try this with rotation of Pi or rotation of Pi/4, or rotation of Pi/2. All I got to do is just come over here to qasm, okay, OpenQASM over here at the right hand side, and change this.

For example, right now I see the pi/2. If I just change this to pi/4, then as you can see, the probability of finding the ket11 as WinningState has decreased drastically, right now with only 35% of chance I'm getting this. But if I change this to Pi, then I'm going to get ket11. So changing this to Pi is nothing different than applying the controlled Z gate, okay, controlled Z gate actually changes this with only Pi.

And, as you can see, you can use this phase gate, like a Z gate, but you get to determine your own angle. And we actually use this to prove, once we actually change the phase of the ket00 with Pi, if we rotate it along the axis with Pi, then, it will increase the chance of finding the ket11 as WinningState. So that's why we are applying this. So let's write this in Qiskit and see how it looks like.

So I'm going to write the reflectionCircuit over here, and again I'm going to create this as a separate circuit and then append it to the main circuit. So I'm just going to give it a name of "reflectionCircuit", and not give it like a classical bit. So over here, what we're going to do in the "reflectionCircuit", is to add the Hadamards, of course, to the 0 and 1, and then add this to Z gate, okay, so 0 and 1, and then add this to a controlled Z gate between 0 and 1, but not like this. So let me delete it, up here you go.

And then finally I'm going to say reflectionCircuit.h to just apply the final Hadamard gates over here. And now we can just say reflectionCircuit.to_gate, okay, to convert this into a gate, and then later on I can just say reflectionCircuit.draw(output='mpl') to see the result for ourselves, here you go. Now I applied this Hadamard gate over here to Z gates over here, controlled Z and the Hadamard gate over there. So this is exactly what we had in mind.

So I'm going to append this to our main circuit, okay, so I'm going to apply the reflectionCircuit over here on the qubits 0 and 1. Later on, I'm going to measure the main circuit. We haven't done that before. So I'm going to measure both qubits into both classical bits, okay.

And then, finally I'm going to draw this and see the final result together over here. And here you go. Now I have the h, I have the oracleCircuit, I have the reflectionCircuit, and then the measurements. So, great.

Now that's exactly what we wanted. So maybe you find this to_gate thing helpful, maybe you didn't like it at all, but it's important that you understand about it. So, here you go. I'm going to get the qasm_simulator from here in order to run my circuit in the qasm_simulator.

So I'm just going to get the results directly from execute(mainCircuit, and backend will be the backend itself, okay. So shots, you can have as many as you want, I'm going to just do it with one shot and show you that we can just find it in one shot, because we have so little options over here. So let me get the counts by using the mainCircuit over there, and then finally, I'm going to plot this with a histogram, okay, so plot this with the counts. Here you go.

Now, for all the shots, and indeed we only did one shot, okay, we got 11 out of it and we found the WinningState. So that's it, that's the Grover's search algorithm. Of course, again, you can just use this with any decimal number as well by converting it into the binary number, but as you can see, the more important thing over here is to understand the algorithm. Now, if you manage to understand it, then it's great, but also we're going to see a very easy way to run Grover's algorithm and also the other algorithms that we have been seeing so far in Qiskit, so that you won't have to deal with circuits at all.

So let's see that in the next lecture together.
