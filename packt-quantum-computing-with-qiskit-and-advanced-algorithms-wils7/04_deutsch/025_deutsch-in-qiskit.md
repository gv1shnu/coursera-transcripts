# Deutsch in Qiskit

- **Course:** Quantum Computing With Qiskit And Advanced Algorithms
- **Module 4:** Deutsch
- **Lecture #:** 25
- **URL:** https://www.coursera.org/learn/packt-quantum-computing-with-qiskit-and-advanced-algorithms-wils7/lecture/cPRjH/deutsch-in-qiskit
- **Extracted:** 2026-06-22 15:23:39

---

Hi. Within this lecture, we're going to write the Deutsch algorithm in Qiskit. Now that we know how this works, it would be very easy for us to convert this in Qiskit in Python code. So, let me just open the circuit composer, and we're going to actually build this in circuit composer first.

So make sure you have 2 qubits in the circuit composer and delete everything that you see over here. So remember how this circuit goes. First we start with the Hadamard gates, but also we start with the X gate in the second qubit as well. So, we are in the ket+ state and ket- state in the second qubit.

So over here I'm going to put an Identity gate, because I need a buffer over here to make the barriers look better. So let me show you what I mean. If I delete the Identity gate from here, as you can see, it kind of distorts the view. So Identity gate doesn't do anything, as you would know by now.

So, the next step would be to apply the CNOT gate. So this would be our Uf function. So we only represent this in order to see the result, in order to see this is a Balanced function. Of course, we can try this with any other gates as well.

However, we know that this is a Balanced function, so I'm going to go with the CNOT. So, after the CNOT, remember what we do, we need to measure this first qubit over here and we are not going to even do anything on the second qubit. So I'm going to apply the Hadamard gate on the first qubit and then the measurement. So, that's it.

It's very easy, as you can see. And, right now, we don't even understand when we look at the possibilities or probabilities from here. So we need to measure this and see how it goes, because, at last eventually, we actually need only one state in order to understand that this is a Balanced function, okay. So what we need to see over here is the state 1 when we measured the first qubit.

So, let me go back, and let me run this in the open_qasm_simulator over here. And, of course, we can just do this in one shot, but I'm just going to leave it as 1000 shots, so that we can see if every time we get the 1 as a result back and just run this. For some reason, over here, for obvious reasons actually, we cannot see only 1 bit when we measure this. So in the measurement we expect to see the result of the 1 bit, but let's see how it goes, okay.

So let me go to the Composer jobs, and here you go. I believe that is now Completed. So I'm going to just open this, and here you go. So, we have this, like 100% of the time.

So we have 01, and, in fact, we need to focus on the first qubit, which is the second bit over here. So, we actually get 1 out of this. So this is exactly what we expected to see. For some reason, we're seeing 01, okay, and we are not interested in the second qubit being 0 or 1, we don't really care about it.

And indeed, in fact, we're actually measuring only the first qubit. I don't know why it shows the other qubit as well in here, but anyway, I believe it's clear over here that we're going to get 1 out of the circuit, and that is exactly what we needed to see. And, of course, we need to do this in one shot as well. So, as you can see, in the qasm, OPENQASM codes over here, we are measuring only 1 qubit and just putting into 1 classical bit.

I don't know why we are seeing 01 over here, but it really doesn't matter, because we're going to write the code in Qiskit and just do this without the circuit composer as well, maybe then we're going to get the actual result, not maybe, we should get the actual result once we do that. So, let's import this stuff. So these are the regular stuff that we always import, so I believe by now you should know how this works. Later on, we're going to create a circuit that we will be working on with 2 qubits, and indeed, we can actually create this with 2 qubits and 1 classical bit as well, right?

So let me just write QuantumCircuit over here. So you can either go with 2 and 2, but it doesn't matter, because we're not even going to actually measure the second one, so I'm going to go with 2 and 1, and then I'm going to apply the Hadamard gate on the first qubit, okay, and then, let's go to the second qubit with the X gate and then the Hadamard gate. So, that's it. And then, maybe we can just apply the barrier over here to make the circuit look better, and let's draw this and see how it looks like in matplotlib.

Here you go. Now, we have the Hadamard, we have the X gate and the Hadamard, so ket+ over here, ket- over here, and then we're going to add the CNOT gate, right, in order to represent our function. And remember, in the theory, in the Deutsch algorithm, we don't need to know what is the function, okay. We are just representing this function as CNOT, but, indeed, in order for this algorithm to work, we don't even need to know about this.

So we're just giving and we're just doing an example over here. So I'm going to say cx(0,1), okay, and I'm going to add another barrier over here, so that you can follow this step by step, and then I'm going to add the Hadamard gate to the first qubit, because we're only going to measure this one, and then you can just write the circuit.barrier in order to have another barrier, and then finally let's draw this and see how it looks like. So I'm going to draw this with 'mpl', and here you go. So that's exactly what we needed to see.

So Hadamard gate, X, H, CNOT, and the H at the end. Great. Now all we need to do actually is to add the measurement on the first qubit and then execute the circuit on a real computer or a simulator. So, I'm going to measure this, and I'm going to measure the first qubit, in the first classical bit.

We only have 1 classical bit actually in this case, and then, that's it. So if you just apply this, then you can just draw this as well, like with the 'mpl', so that we can see the measurement over here as well, here you go. Now, our circuit is completed. Now, I'm going to create the backend, so we're going to use the simulator, and also we can use a real quantum computer as well, so that it can be an exercise for us.

So I'm going to go ahead and just choose the 'qasm_simulator', like we always do, but then, we can come back and just run this real quantum computer later on. So I'm going to get the result by saying that execute the circuit, of course, and then, as a backend, we're going to use the backend over here, like this. And, for the shots, maybe we can just give one shot right now or 1000 shots, whatever you need. But I'm going to just do this with 1000 shots to see if we get the actual result back, like we had 01 in the other case, which was weird, let's see what we got over here.

And, in the counts, I'm going to say result.get_counts, in order to get the counts back, and then I'm going to plot this or just visualize this using the plot. And don't forget about the circuit over here, okay. And finally, let me just write plot_histogram and give the counts as an array over here. Great.

If you hit Shift Enter, then it will be executed on the qasm_simulator, and here you go. Now, yeah, this is the correct one. As you can see, we only have 1 bit, so this is 1. Now that we know the function is balanced, okay, in the circuit composer, we didn't get this clear result for some reason, but over here, we only get one result for every shot that we took, and, I believe that's it.

So that is how Deutsch algorithm works. As you can see, we managed to find out that this is a Balanced function, and it's going to take only 1 shot, okay. So, that is great. However, it can be different in a real quantum computer, right, because they are not perfect.

So I believe it would be a good idea for us to go back to the simulators and the providers thing that we have seen before, and just see what was the code that we run in order to get the provider backends over here. So remember how we do that? If you don't remember, you can always come back to your notes and just copy and paste these things, right, so that it would be better for you, because, you don't have to memorize every property, or you don't have to go to the documentation each time, you need to understand how it works. So, let me just load the account and then get the result over here.

And remember, we worked with lima, I believe, in the previous sections, now maybe it's time to just take a look around for the other quantum computer as well. So, let's give it a note, Real Quantum Computer, okay, and this time I'm going to just come back here and just follow along with the same step. So first step would be the load the account. So if you haven't given your API key yet, you should do that by now, and, I'm going to say load account, and since I have given my API key before, it won't ask me again, here you go.

Now, next thing would be to, just let me run this one more time, next thing would be to just do this if you didn't do that already. And then, next thing would be to just get the providers, okay. And then after we get the providers, we can just ask for the backend. And for the backend I'm going to use this for loop that we have done before.

So I'm going to just copy and paste this thing to see what kind of real quantum computers are available right now and what are the jobs that are pending, or what are the qubit counts, okay. So, all you got to do is just hit Shift Enter and wait for result to appear in here. As you can see, we already see the results right now. So, let's start to analyze the results, and let's try to find the least busy one over here, okay.

So, as you can see, right now lima is a little bit more busy, busier than the other ones, like belem or quito. So, in athens we have 7 pending job, in melbourne we have 400, again because it has 15 qubits, so many people choose to use that. So this time I'm going to go with another thing rather than lima. So let's go for belem, for example, or quito, maybe you can go for athens as well.

So, most probably you will see some different results over here, so make sure you choose the most appropriate one. By the way, I'm going to make sure that we haven't used the belem before. So I believe we used the lima in the previous sections. So, let's see.

What was the Jupyter Notebook that we have actually run this on a real quantum computer. So let me run couple of those. So I believe it was a HelloQuantum, right? So let me open a couple of those over here, and let's see in the HelloQuantum.

Yeah, here you go. Yeah, we have used lima. So I'm not going to use lima again, so that you can see it actually works in any computer that we choose from here. So, I'm going to go with belem.

Again, you can go with your own preference over here, but make sure you're not going to go with something very busy, okay. So, I'm going to hit Shift Enter. Now I define my quantum computer over here. Of course, we're just going to execute this on this backend with the specific shots number.

So I'm going to say quantum_result, and just say execute(backend), and let's see the backend over here. So I believe we specified this to be backend and this one to be quantum_computer, right. So first of all let me just write circuit, don't forget about the circuit. And for the backend, I'm going to say quantum_computer, okay.

And, for the shots, I believe it's good to go with 1000 shots, so that we can see how it goes, and then get the result back. So, what we're going to do? We're going to wait until this is finished. And remember the job watcher?

So I haven't actually enabled in here, I totally forgot about it, but you can actually go back and see how to enable the job watcher, like you're going to have to import these things and just start the job monitor, so that you can actually see how your job is doing, okay. So, in this case, we're going to have to wait until this star actually turns into some kind of integer, in my case it's going to turn into 13, I believe. So, that's how we actually will understand that this execution is completed, and then we can get the counts, and then we can plot the histogram and see the results. So, again, you can do this only 1 shot, and it's really proof actually in the simulator as well, because we did it with 1000 shots and they all came back with the same result.

So you can do this in one shot and you can see it yourself. However, in the real quantum computer, it's a little bit stretch to go with one shot, because, as you already know by now, they are not perfect, and there is going to be some kind of noise, okay. So when we actually write this, so we're going to write quantum_counts, quantum_results.get_counts, okay. So, if some kind of error happens in the first trial, then we're not going to get 1, but maybe we're going to get something like 0 or something like that.

So, you can write this, but don't execute it until this has been completed, okay. So I'm going to wait until this has been completed, and I'm just going to write, execute this later on, and, here you go. Now, this has been completed for me. As you can see, star turned into 13, and I believe we have the result right now.

So, what I'm going to do? I'm going to just hit Shift Enter to execute this one, but, for some reason it gives me some error over here, yeah, because I misspelled the results, yeah, here you go. So I'm going to delete this and hit Shift Enter one more time, here you go. As you can see, we again have the one result over here, so that we can understand that this is actually like a balanced function, but with a minimal amount of shots over here, we have the 0 as well.

So, this is again due to the errors that we came across within this execution in the real quantum computers. But if you look at this, if you look at this shot, you can easily understand the result is 1, right? So that's good enough for us. So, here you go.

That's the Deutsch algorithm. I believe it made you much more clear in your head to how to work with quantum gates, how to build circuits, how to actually implement an algorithm, to get some result back. So that was cool until now, but it's going to get cooler, because we're going to actually focus on the algorithms that we can use in daily life problems in the future as well.
