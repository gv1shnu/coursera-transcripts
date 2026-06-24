# Entanglement

- **Course:** Quantum Computing With Qiskit And Advanced Algorithms
- **Module 1:** Qiskit 101
- **Lecture #:** 5
- **URL:** https://www.coursera.org/learn/packt-quantum-computing-with-qiskit-and-advanced-algorithms-wils7/lecture/XIbJr/entanglement
- **Extracted:** 2026-06-22 15:20:01

---

Hi. Within this lecture, we're going to continue with the other quantum gates. And we will start with the Hadamard gate. And as I said before, this is one of the most important gates that we will see throughout this course, because we're going to use this a lot.

And the idea over here is that Hadamard gates make the qubit go into the superposition. So, of course, we have a matrix for the Hadamard gate as well, since we have matrices for all the gates that we will see as well. So, if you come over here and look at the formula, you will see that if you apply the Hadamard gate to the ket0 and ket1, you will get this states. So, in the ket0, we have ket0 + ket1, and in the ket1 state, we have ket0 - ket1.

And it really doesn't matter whether we have a minus or plus, because Hadamard puts them into the superposition, and we will see the mathematical consequences of this as well. But before going into the Math, I believe we should actually use this circuit composer and see how it looks like. So I'm in the circuit composer, and I'm going to bring in the Hadamard gate. And as you can see, I only have one qubit.

And as you can see, now my Statevector points out to both ket0 and ket1, and if you look at the left hand side, you will see that with 50% probability, I'm going to get either 1 or 0. So this is in the superposition. So, if I add another qubit over here, and, as you can see, right now I have q 0 and q 1, and, if you look at the Q-sphere right now, I have two vectors, one pointing to ket0, and the other one is to ket 01. So, still, one of the qubits is pointing up to the 1 and 0, but other is pointing up to 00, okay.

So, over here, if I delete everything, I will see that both qubits in the ket00 state, and if I add Hadamard to q 0, I will just get the same result that I got over here, because one of the qubits are still in the 0 phase or 0 state, not phase. But if I just put the other one into the Hadamard, into the superposition as well, now, with 20% possibility, I'm going to get either one of those, so, 00 01 10, and 11. If you look at the probabilities, then you will see that we have even 25% chance of getting one of those. So we understand that Hadamard gate actually lets us to have all these possibilities when we apply them to a qubit.

So we can just add them to one qubit or any qubit that we want. So we're going to see the mathematical consequences of the Hadamard gate as well, but first of all I want to show you something called CNOT gate, because we're going to use CNOT gate with the Hadamard gate a lot. So CNOT gate actually is very similar to NOT gate, but it's a controlled NOT gate, okay, and you see the matrix over here with, of the CNOT gate. So, over here, we have the matrix, and, of course, we can just apply this to both qubits and see what it happens, we're going to do that, but I just want to show you something rather different.

So CNOT gate has an alternative, okay. But in Qiskit, we use the CNOT gate, but this is the alternative matrix. So, if you just study this quantum computation somewhere else, maybe you can see a different matrix for the CNOT gate, it depends on the calculations and the style. So in Qiskit, we actually use the CNOT gate, okay, so that's why we're going to focus on this matrix.

And what controlled NOT gate does is actually it does this q1 XOR q2 thing, okay, because this is controlled NOT gate, not actually NOT gate. And you have to remember this representation as well, and we will see it in the circuit composer. But, the logic over here is that it actually applies this XOR logic. So this is Exclusive OR and we have seen this in the classical gate.

So what it does is that it actually takes the q1 Exclusive or q2. So what happens if it does that? So let me show you the consequences first and then talk about it. As you can see, if you apply the CNOT gate to the ket00, you're going to get ket00 back, right?

So if you just apply this to ket 01, you're going to get ket11, ket 10, ket 10, and if you applied to ket11, then you're going to get ket01. Of course, we can prove this by applying the matrix itself. For example, I have just done this for the CNOT ket01. So as you can see, this is the CNOT gate and the other matrix is the ket01 gate.

If you just multiply them, you're going to get ket11 as a result, maybe you may want to pause the video and just do the Math yourself, but you will just clearly see that it is equal to ket11. So what happens here is that is actually it applies the NOT gate to the second qubit if only and if, the first qubit is 1, okay. We're going to see this again. But right now, just so you know that.

this is the CNOT matrix, okay, and you can apply this to two qubit circuit. Now when you do that, you cannot apply this to 1 qubit, obviously, because it actually has a controlled gate, or control qubit. So it checks the control qubit, and if it's 1, then it applies the CNOT gate to the other qubit. So, over here, it adds up to ket11.

And you can try to pause the video and just do the Math for the other ones as well for yourselves, to exercise this, okay, and I really suggest that. You already know how to come up with the ket00, ket11 matrices. So, what my point is over here is that, if we apply the Hadamard gate and the CNOT gate, at the same time like this, what happens? So let me go back to the circuit composer, and we're going to see the mathematical proof of this as well, don't worry about it, you will understand why it does that.

So if I bring over the Hadamard to ket, q 0, and bring the CNOT gate to here, so, you can see that we get the result ket00 and ket 11. So what does it mean? It means that both qubits are now entangled, right? Because we either get 00, or we either get 11.

So remember this. So let me just go back. Remember this Superposition and Entanglement matrice that we have seen before. So this is the matrix that I'm talking about.

It actually lands up in this, 1 over square root 2, 1 over square root 2. And for the possibilities of 10 and 01, we don't have anything, we have 0. So, how it goes there, right, how it goes there? We should actually calculate this, with matrices and see for ourselves.

So let's go to the mathematical foundations, the mathematical proof of this. So you know the Hadamard gate, okay, maybe you don't know it by heart, maybe you didn't memorize it. But, of course, you can go back and see it for yourselves anytime you want. So if I apply this to q1, so what is the position of q1 when it first initialized?

It's actually ket0, right? So, what I did over here is to apply the Hadamard gate to the ket0 itself, so we multiply this matrices. So what do we get as a result back? So we get the result back as 1 over square root 2, 1 over square root 2.

So as you can see, we already proved that Hadamard puts 1 qubit into Superposition by just doing this mathematical calculation. That's why we have seen so much Math before we went down and see the Hadamard and CNOT and other gates as well. So, right now, over here, if I draw a barrier or something like that, I know that my first qubit is in the Superposition state, but the q2, q2 is in, still in the ket0 state, right? So, if I want to get the total state out of this total state of the circuit, then I should do a tensor product, right?

We know that. So if I do the tensor product, then I'm going to get this result. So, I'm inside of a thing before applying the CNOT, I am inside of the circuit, where q2 is ket0 and q1 is ket+. So if you see ket+, it means that it's in the Superposition.

And if you see ket-, it's again in the Superposition with a different phase, where you're going to see what it means later on. So if you see ket+ or ket-, it means that we're in the Superposition. So, over here, I know that this matrix is 1 over square root 2, 1 over square root 2. If I get the tensor product, then I'm in a total state like this.

So, you know how to get the tensor product, right? If you don't remember, go ahead, go back and see for yourselves in the previous slides. So if I do this calculation, then what I need to do actually, to get the end of the circuit, I need to apply the CNOT gate to this total state. So I know the CNOT gate, if I apply this to here, then just do the calculation, I get 1 over square root 2, 0, 0, 1 over square root 2.

And guess what is this. This is the Entanglement state that we have seen before. So, by 50% chance, we're going to get ket00, and by 50% chance, we're going to get ket11. So, we know that they're going to be same every time.

So both qubits are going to have either 0 or either going to have 1. So, we can just see it here visually, and we can calculate the matrices in order to prove ourselves that it actually works mathematically as well. So, let's remember one more time, Hadamard puts a qubit into Superposition. If we actually use Hadamard with the CNOT gate, then we can actually entangle them together.

We're going to use this a lot in our circuits, in our algorithms, so you should know how it works. Don't worry, we're going to see the ket- state. So, if you remember the, one of the previous slides, I have said that if you apply the ket1, if you apply the Hadamard to ket1, then you're still going to go into the Superposition, but with minus in the between, in the middle, okay. It really doesn't matter it's still in the Superposition, but we're going to see that concept later on.

Now let's stop here and see you in the next lecture.
