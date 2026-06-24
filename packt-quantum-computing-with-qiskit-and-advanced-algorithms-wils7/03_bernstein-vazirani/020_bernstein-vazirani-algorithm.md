# Bernstein Vazirani Algorithm

- **Course:** Quantum Computing With Qiskit And Advanced Algorithms
- **Module 3:** Bernstein Vazirani
- **Lecture #:** 20
- **URL:** https://www.coursera.org/learn/packt-quantum-computing-with-qiskit-and-advanced-algorithms-wils7/lecture/G2iFa/bernstein-vazirani-algorithm
- **Extracted:** 2026-06-22 15:22:44

---

Hi. Within this lecture, we're going to actually apply the Bernstein Vazirani Algorithm on the Qiskit. So I'm going to open a new Python project over here, and, I believe we were at something like QX04. So I'm going to go with the QX05, and I'm going to name this BernsteinVaziraniAlgorithm, and, don't worry about all of these Jupyter Notebooks, by the way, because I'm going to share all of those things with you, and actually I shared the actual PDFs, and I'm sharing all of the GitHub links after each lecture ends.

So, here you go. So, over here, we're going to start with the importing stuff. So I'm going to import the Qiskit and also the visualization tools as well. And by the way, we're going to start by making like a very simple version of this Bernstein Vazirani implementation, then we're going to make it much more complex and automatic.

So, let's import the plot_histogram as well, but I believe I misspelled this, yeah, here you go, visualization import plot_histogram. So, let's do the matplotlib in line as well, here you go. Now we're ready. Now we want to come up with a secret number.

Of course, we can just ask the user to give this number as well, like taking with an input or something like that. However, I'm not going to do that over here, it's very easy to do that. If you remember the Python section, you can just ask it by writing input. I'm just going to give a constant secret number over here, and we're going to change it later on.

So I really suggest you to follow along with the exact same number that I type over here, then you can just change it and try it on your own, once the lecture ends, okay. So right now I'm just writing 1000101. So what we want to do over here is to come up with a circuit that will actually find this exact same number, like the ordering of the qubits once we measure this, okay. So how do we do that?

Of course, Bernstein Vazirani algorithm has a way to accomplish this. So, let me just create a circuit and then we're going to talk about this. So I'm going to say QuantumCircuit, and we need a circuit that has 1 2 3 4 5 6 7 plus 1 qubit, okay, so 8 qubits and 7 classical bits. So we're going to use a helper qubit or an Ancilla qubit.

So we're not even going to measure that qubit, but it will help us to conduct this operations while we draw our circuit. So, it goes like this. Bernstein Vazirani says that you're going to have to put Hadamard on all of the qubits, and then put CNOT for the 1 bit, okay. If the bit is 1, then you're going to have to have a CNOT with that bit and the Ancilla bit, and then you're going to have to apply another Hadamard and then you're going to have to measure it.

So why does it say that? Of course, we're going to take a look and see how it goes. So, don't forget that we're just going to have to create the qubit number as the length of the secret number + 1, okay. So we have 8 bits over there, and we created 7 bits over there, and we created 8 qubits with 7 classical bits, because we're just going to measure 7 bits, eventually.

So, here you go. Now we are ready to work on the circuit. So, what I'm going to do, follow along with the algorithm. So I'm going to apply Hadamard to all of these gates, and actually almost all of those gates.

So I'm going to apply Hadamard to 7 qubits, okay. And, before applying the Hadamard on the Ancilla qubit, the helper qubit, I'm going to apply a NOT gate, and we're going to see why it goes like that at the end of this lecture. So I'm going to apply the X gate to the last qubit, and then Hadamard gate to the last qubit as well. So eventually I applied Hadamard qubits to all of, Hadamard gates to all of the qubits, but I applied one X gate as well.

So I'm going to draw a barrier over here to just make the steps much more clear, and I'm going to draw the output in the 'mpl' so that you can see how it looks like. So, here you go. It seems that it's working. As you can see, our 8 qubits are generated, and now we have Hadamards on all of the qubits, and in the 8 qubit over here, we also have the X gate, and we have 7 classical bits as well, so that we can measure the first 7 qubits to get the exact same result that we expect to see.

Okay, so what is the next step? So next step would be to apply the CNOT gates. As I said before, we need to apply the CNOT gates between the qubits that will have the value of 1 and the Ancilla qubit, which is 8 qubit over here. So, why is that?

Of course, we want to have a qubit ordering of 10001010, or whatever the secret number is. So we need to flip the bit of the qubits that will have the value of 1. Of course, we're going to do this automatically, but right now I just want to do this manually to show you that algorithm works. And then we will actually improve this code in order to make this in a more automatic way.

So I know that my secret number starts with 100 and continues like 0101. And, the last one will be the q0 over here, and it will go like this. So I know that q0 should have the number, the state of 1 when we measure it, okay. So I'm going to apply a NOT gate or CNOT gate between the q0 and q7, and then I will continue as long as I see the 1s.

So, let me show you how to do that. Of course, we're going to say cx, okay, Controlled NOT, circuit.cx, and over here I want to put the cx between 0 and 7, so 0 and 7. And the next step would be to apply this to the third qubit, okay. So, you can come over here and just write circuit.cx, and this is 0, and this is 1, and this is 2, so 2,7.

As you can see, the third qubit has also, has the value of 1. And the last qubit, which is the 6th index over here, has also the ordering of 1 over there. Now I'm going to add a barrier, and, I believe we have to draw this at the end of this cell, and see how it looks like. So, it looks like a little bit messy, because we have, I believe, just run this twice.

So I'm going to come over here and say Kernel, Restart & Run All in order to make sure that we just run it once. So, here you go. Yeah, that should be it. As you can see, what we did over here is to apply Hadamards to all these gates and then have the CNOT.

So it's very basic, actually. It just flips the state of the q0, q2, and q6, and then, if we apply the Hadamards one more time, and if we apply the measurement, then obviously we're going to get these numbers, right? The interesting thing over here is the Ancilla or the q7. So, we're applying the X gate and then the Hadamard gate, and we're controlling or we're just targeting this with the other qubits that will have the value of 1.

So, let's do the Hadamard gates and then let's do the measurements as well, and then we can talk about the qubit 7 in a much more detailed fashion. So, maybe you can change the ordering of this, it won't matter, okay. So if you want to have like a better-looking shape, then you can change the ordering of this, like if you Restart this and All, and you can see that it starts with the q6 and it ends with the q0. So if you prefer this, then it's okay, you can change the ordering of this, because it doesn't matter, it actually involves 1 qubit at a time.

So, at the end of this, I'm going to apply the Hadamard to all of the 7 gates again. It doesn't matter if I apply the Hadamard to q7, because we're not even going to measure it, okay, so you can just leave it alone. So I'm going to measure all of this qubits again, so from 0 to 6. So I'm going to write 0,1,2,3,4,5,6 over here, and, of course, we're going to put it in the classical bits as well.

So, I believe that's it, maybe we can just draw this right now and see how it looks like. So I'm going to say Kernel Restart & Run, and, here you go. Yeah, here you go. Now that is the Bernstein-Vazirani algorithm.

So you may think that, yeah, we did everything manually, so we did everything over here by hand, so we flipped the states by hand, and it doesn't make sense. Yeah, I agree. Again, I say that we're going to make it more automatic, okay. So, we're going to check to see if the bits are 1, so we're going to flip the state and the stuff.

But right now we're trying to understand how it works. So what do we have over here? We have the 100101, right? So we applied all the cx gates, and, somehow it's going to work.

So what happens if I didn't actually put the X gate or Hadamard gate in the q7? So it would still work, right, because we have the CNOT gates. So it will some kind of flip the states, and maybe we will be able to see what's going on over there, right, because it's in the Hadamard, so 50% of the time we're going to get the actual number. So let's run this and see.

So I'm going to create my simulator over here with the 'qasm_simulator', and I'm going to execute the circuit, okay, with the simulator as the backend. So I'm going to do it like this. And, for the shots, maybe we can just go with 1 to see if it actually finds it 1 shot, and then I'm going to get the result. So, later on you can get the count from this circuit, from this measurement, and you can compare it with your own secret number.

So I'm going to say counts = result.get_counts, like this, and then I believe we can just print the counts before even plotting this in a histogram. So if I run this, as you can see, we have this number, so 100101. So this has to be the exact number that we came up with, as the secret number, and we managed to find it in only 1 shot. So, you can try this with 1000 shots as well.

And as you can see, it gives back to the same result. So it doesn't even matter if we do it in 1 shot or 1000 shot or even 8000 shots. So, the algorithm works, and the question is how it works. So maybe we understood that it works with the CNOT, so it actually flips the state, because it's in Hadamard.

And, if we do not have this Ancilla qubit, it should have like a 50% of chance of giving 0 or 50% of chance giving the right number. So maybe you didn't understand that intuitively, because you are just starting with the quantum computation, let me show you why we're applying this X gate and Hadamard gate. So I'm going to comment out this X gate over here. So we are basically putting everything together in the Hadamard gate and then we're applying the CNOT gates.

So if we do it like this, then, it won't do good actually. So as you can see, we only have Hadamard gates and the CNOT, and then the Hadamard gates, and then the measurements. So let me just go down and see what we got out of the circuit. So as you can see, we have only the 000s over here.

So, it isn't good, right? So maybe it's about shots. So let me just make this in 1000 shots and just Shift Enter this. And as you can see, we cannot get something, anything out of this really.

So putting the q7 in the Hadamard is actually not a good idea, so let me comment this out as well. So, we only have a qubit, okay, we only have a qubit that we can use just to, just as a target for our CNOT gates. So let's see what we got over there, once we do that. As you can see, right now, we are getting the 0s, and we are also getting the answer itself.

So it's a 50% possibility right now. So, it makes sense, if you think about it, it makes sense, because we are applying the Hadamards and then the CNOT, so half of the time it flips the state, half of the time it doesn't flip the state, so, we're going to end up like this. But if we apply the X gate and the Hadamard gate, then we can get rid of the 0s over here. Of course, you can try to figure this out on your own by applying the NOT gate over here and then the Hadamard gate and then the CNOT gate, and you can try to draw the exact same circuit that you see over there.

So you can see what's going on over here, okay. And, of course, you're going to have to do this with multiple qubits, like this, and just put it over here, something like that. But don't worry about it, okay, don't worry about it, because we're going to see this in the mathematical form later on as well. Just, right now, if you didn't understand this intuitively, just so you know that if we put the X gate and the Hadamard gate, it will just get rid of the 0s, and it will just give us the answers.

So, that's it. That's why we are using this NOT gate and the Hadamard gate over here, and then we're applying the CNOT gates and then Hadamards and the measurements. Great. Now let me delete all of this stuff and run this from scratch, and let me come over here and say Kernel Restart & Run All.

Great. And, as you can see, we get this in 1000 shots and also in 1 shots as well. So again, if you didn't understand the X gate and Hadamard gate, in the next section, in the following section, we are going to see the mathematical proof of this, or mathematical foundations of this for another algorithm, then you will understand it in a much more clear way. However, right now, it should make sense to you that Bernstein-Vazirani works, and we can guess the secret number in only 1 shot.

But as you can imagine, we did this in a very manual way, so we flipped the states by CNOTs and stuff. So, I believe we should make this in to a much more automatic way, at least that it makes sense. So, of course, this actually proves that the quantum computers can outperform the classical computers in some ways. However, at least, we actually know Python and we have been studying this for a long time right now, so at least we owe ourselves that we should make this automatic and in a much more structural way.

Let's do that in the next lecture together.
