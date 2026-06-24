# Running on Simulator

- **Course:** Quantum Computing With Qiskit And Advanced Algorithms
- **Module 1:** Qiskit 101
- **Lecture #:** 8
- **URL:** https://www.coursera.org/learn/packt-quantum-computing-with-qiskit-and-advanced-algorithms-wils7/lecture/o6OPP/running-on-simulator
- **Extracted:** 2026-06-22 15:20:35

---

Hi. Within this lecture, we're going to finalize our circuit and run it on the simulator and then later on, we're going to run it on a real quantum machine. So over here, we created our circuit with 2 qubits and 2 classical bits, but, of course, we can do so much more with it. For example, I can run circuit.draw, it will run the circuit for us.

But as you can see, we don't see many things over here, right now we don't even have the lines. So we should see something like this in order to understand it in a better way, right? So, this is exactly what we're seeing right now, I believe, because we have the q_1, q_0 and 2 classical bits, but we don't have this cool lines that can actually contain the gates that we apply over there. So circuit.draw is very good, but actually there is a better way to draw the circuit so that we can understand where we are currently, because not every time we can go back to the circuit drawer and just put it over there to visualize it, right?

So we need a visualization tool, in order to make it much more efficient. So what I'm going to do, I'm going to go to my Terminal, and run pip install matplotlib, okay. So matplotlib is a visualization library that we generally use with data science. And by the way, if you install the Qiskit, it should come with Qiskit as well, and if you are using the quantum labs on the IBM computer, then you shouldn't worry about it, because matplotlib is already there already, but all you get to do after you install the matplotlib, you can come over here and write this, %matplotlib inline, okay.

So this will ensure that you can use the matplotlib library in order to visually draw the circuits and have a much better looking user interface. So what do I mean by that? If you don't do it, it won't work. So let me just see what I mean.

I will write circuit.draw, but this time, I'm going to specify an output, okay. So I'm going to write output over here, which will be equal to 'mpl', so matplotlib, or matplotlib, okay. So here we go. Now we have a much better looking circuit drawing over here.

So this is q0, q1, and 2 classical bits. Once we add the gate over here, it will be just displayed over there for us to track where are we going. So that's it. Now we created the first 2 qubits and 2 classical bits, but we don't have any gates right now.

So what I'm going to do, I'm going to add a Hadamard gate to my first qubit. So, after I add this Hadamard gate, I can just continue adding the new gates as well, and also I can draw the circuit to see how it looks like. So in order to actually apply the gates, we can use the circuit itself, and it is already embedded inside of the circuit property. So if you say, circuit., and hit Tab, so let me just do this one more time.

And as you can see, we can see all the functions and properties of the circuit. So, all I did was circuit. and hit Tab on my keyboard. So as you can see, h is over here, i is over here, c x is over here, x is over here, okay.

So we have a lot of different gates, a lot of different operations for this circuit, like ccx, we're going to see what it is in a couple of lectures. But I want to go with h, which is the Hadamard gate, and all I want to do just to specify which qubit that I will be putting this on. And, of course, it starts with 0, like an array or a list. So, all I want to just say is circuit.h and specify this will be on the qubit 0.

You can just do it with this, like this, if you want to apply this to multiple gates, like give it in a list, but in this case, I just want to add h to 0, and then draw this with the output of 'mpl' in order to see what's going on, and here you go. As you can see, the Hadamard gate appeared in the q0. Now, of course, you can just do your things, and at the end of the day, you can draw it to see the big picture, but also you can just do this one step at a time, once you're, since we are first time doing this, it will be much more helpful for us. Now let's add the CNOT gate, which is the cx gate, and all we get to just say is to cx(0,1), okay.

So we call this the control qubit and the target qubit. So it controls the 0 qubit and it actually targets the first qubit, the qubit 1 in this case. So, 0 is the control qubit, okay, 1 is the target qubit. So remember, it actually checks to see if the control qubit is in the state 1.

If that's the case, then it applies the NOT gate on the 1. So, after that, I believe we can measure this, or if you want, you can re-draw this to see how it looks like. So, let's do the measurements here. So I'm going to just say measure, so that you can understand how to do the measurement as well.

So, for the measurement, we have to specify which qubits that we want to measure, maybe I want to measure only 1 qubit, maybe I want to measure the both qubits. And also, we have to associate them with the classical bits as well. So what we're going to do, like this, so let me just put the H and CNOT gate over here. So once I bring down the measurement, as you can see, they're automatically associated with the classical bits.

So this 0 means that it's associated with classical 0 and the other one is classical 1. So I'm going to do the exact same thing over here. I'm going to open an array, a list over here, and I will just say 0 1, and open another list, and I will just say 0 1 as well. So it means that measure the qubit 0 and qubit 1 and associate them with the classical bit 0 and classical bit 1.

So once I draw this, as you can see, we got the exact same thing that we have done in the actual circuit composer, right? So this is the same thing. We have the Hadamard gate, we have the CNOT gate, we have the measurements in place, we have 2 qubits, 2 classical bits, and that's it. That's our first circuit ever, that's the HelloQuantum circuit.

And, right now, they should be entangled together. In order to confirm the entanglement though, we need to run this, we need to execute this on a simulator or on a real quantum computer to just get the result and see if we actually get 0 0 and 1 1 state as the results. So, of course, we need to understand how to do that. First of all, we're going to start with the simulators, and then we're going to just run this on real quantum machine as well.

So in order to run the simulator, remember the module that I've talked about, it's Aer, okay, a-e-r. So, all you got to do, just say Aer, okay, since we imported the Qiskit and everything inside of the Qiskit, Aer should be available to you, you're going to have to write get_backend, get_backend, and write the simulator name that you want. So it's 'qasm_simulator'. So remember, we done that, we came over here, and we chose the qasm_simulator from there.

So that's exactly what I've done in this line. Of course, you can think that, how am I supposed to know the names of the simulators and the quantum machines? Don't worry about it, I'm going to show you. Of course, you can see the names from here, from this list as well, right?

But, I'm going to show you a different way to get this. But, as you might remember, we have other settings over here as well, like Shots. So, if we want, we can specify Shots, or if we want, we can just leave it blank, or, we can just give it a name, or we can execute this. So I'm going to show you all of this when the time comes, don't worry about it.

So what I did was to create the simulator. Now I'm going to execute this one, okay. So make sure you write execute, and open the parentheses. So execute is a function that comes with the Qiskit, so you don't have to just import anything else.

All I got to just say is circuit. So we're going to execute the circuit with the simulator that we have just created. So if you do it like this, it will run the circuit in the simulator that you specified, and, of course, we should appropriately change this spelling to the right one. And as you can see, it's now being executed or it's already been executed for us.

But, if you say .result, then, you're going to actually get the result and you can just save them inside of a Variable. So I called the Variable result as well. Now if we run this like this, it should make much more sense, because we can get the results back. Now I have the result, okay.

I ran this inside of a quantum simulator, a quantum computer simulator, and it simulates the behavior of the quantum computers. Again we're going to see how to run this on a real quantum machine, don't worry about it. Right now we're just seeing how to run this on simulator, and we got the results back. So it's like waiting for this to run in the circuit composer, and what we did, as a next step, remember, we went to the left hand pane and see the result for ourselves.

That's exactly what we're going to do, we're going to try and see the result for ourselves in here. In order to see the results, we can visualize them in a way that it displays a bar chart. So in order to do that, you're going to have to import something called plot histogram. So all you got to just run is from qiskit.visualization, okay, that's how it goes, from qiskit.visualization, import plot_histogram.

There are other libraries or modules that we will be using during this course, don't worry about it, we're going to see every one of those. So now I'm going to say plot_histogram, and it expects me to give some kind of count, some kind of numbers to them, and you can get it by saying result.get_counts, get_counts, and you need to specify the circuit. So here you go, that's set. So, as you can see, we get 00 for like the half of the operation and 11 for the half of the operation.

We haven't specified the Shots yet, we're going to see how to do those, it will be much more important when it comes to running this on a real quantum computer. In simulators, since it simulates the running stuff, generally gives you the idea or gives you the exact probability that you should see, and over here, we see that they are indeed in an entangled state, because we, of course, we always get the 00 and 11, but not 10 or 01. So they are very correlated with each other. So we either get 1 and 1 from the other side, 0 and 0 from the other side.

Of course, maybe at this time you cannot imagine how to use that kind of information or calculation in a real world problem. No worries about that. We're going to come back to the quantum algorithms once we finish all of this stuff, and then you will understand how it works. Right now, the thing that matters is you understand how Qiskit works, and how quantum computers work.

[No audio]
