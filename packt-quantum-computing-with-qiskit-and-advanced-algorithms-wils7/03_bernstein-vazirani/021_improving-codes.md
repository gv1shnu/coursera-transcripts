# Improving Codes

- **Course:** Quantum Computing With Qiskit And Advanced Algorithms
- **Module 3:** Bernstein Vazirani
- **Lecture #:** 21
- **URL:** https://www.coursera.org/learn/packt-quantum-computing-with-qiskit-and-advanced-algorithms-wils7/lecture/qswjb/improving-codes
- **Extracted:** 2026-06-22 15:22:55

---

Hi. Within this lecture, we're going to actually improve this code a little bit, so that we can make it much more automatic and much more structural. For example, after we get the secret number over here, we can actually make the circuit like adaptive to the length of the secret number, right? So I have given 7 bits of number right now, so maybe it would be 5 bits, maybe it would be 10 bits.

So depending on the length of the secret number, we can adjust the classical bit number and also the qubit number as well, right? So, it's very easy to do. So I can come over here and say that len, so this is the length of the secretNumber + 1. And, if it's 7, then it's going to be 8, if it's 5, it's going to be 6.

So it will adjust itself. So I'm going to do the same thing for the classical bit as well. But rather than +1, I'm just going to leave it as it is. Yeah, here we go.

Now, we managed to adapt our quantum circuit, at least in the size of the qubits, according to our secret number length. So far, so good. So I'm going to do Shift Enter. Now, what I'm doing over here is adding the Hadamard gates, right?

But we should make this again, adjusting to the length of the secret number. So I'm adding all of this gate for the 7 bits right now, right? So I'm adding the Hadamard to the 7 qubit right now. So it's actually the length of the secretNumber, and then adding the Ancilla qubit at the end of this.

So what we can do over here is to create a range, right? So remember the range. So if I say, range(len(secretNumber)), then it will create this, for example, for the 7 bits, it will create a range from, like a list from 0 up till the 6, okay. So it will be exactly the same thing that I have done over here, but it will be adjusting, it will be automatic.

So, for that one, we can just give the (len(secretNumber) because, for example, this is 7 bit, and, we already put 7 over here, because the 7th index means 8 qubit, okay, and it's exactly the same thing for the Hadamard gate as well. So far, so good. Now, of course, we won't change the barrier, but, when it comes to the CNOT gates, we have to apply the CNOT gates for the bits that has a value of 1, okay. So if I add a 1, if I change the ordering of 1, if I change the ordering of 0, then it should adjust itself.

So what we're going to do, we're going to see if the bits are 1, and then if this is 1, then we're going to apply the CNOT gate, okay. If they are not 1, then we shouldn't apply anything. So, of course, we're going to do a for loop over here, okay. In order to just assign these 1s, assign these characters to a Variable, so that we can check that Variable against 1.

So I'm going to do this for loop with two Variables. So, I'm going to call this index, and the second one can be called number, I believe, or we can call this 1, okay, whatever you may want to call it. But, I'm going to say enumerate. So remember this function, you will see what it does in a minute, if you don't remember it, and just enumerate the secretNumber.

So let's see what we got over here if we do it like this. So I'm going to print this in a formatted way, okay, and I'm going to print the index first. So the index would be the index of the current bit, and I'm going to say is {one}. So what this will give me is like index 0 is 1, index 1 is 2, index 3 is that.

So I'm going to just comment this out and just execute this, and as you can see, we can get this. So index 0 is 1, index 1 is 0, index 2 is 0. So that's good. But as you can see, we're getting this starting from the left.

But we want to start this from the end of this bit, okay, from here, because in the Qiskit, this ordering of the qubits are in a reversed way, if you remember that. So we need to make sure that we reverse the secretNumber before we add the CNOT gate. So there are a couple of ways to do so. So, let me first actually show you the reason why we are doing this, and then we can actually reverse it.

So, what I'm going to do, I'm going to check to see if the number or the 1 is equal to actually string 1 or character 1, okay. So if that's the case, I'm going to put a CNOT gate between the current index, okay, like index 0, index 1, and for the last qubit, which is the len(secretNumber), which is the Ancilla qubit over here, okay. So this will actually do the work for me, and it will be okay for me. But, I want to add this starting from the right hand side, so that it could make sense when we actually work with the reverse ordered qubit.

So I don't want this one to be index 0, okay, I want this one to be index 0. So, in order to do that, we can actually reverse the string. You know how to do that in Python, right? So you can come over here and just put ::-1, for example, and it will work.

So if I run this right now, as you can see, everything seems reversed. So it starts with 101, and I believe even though we changed it, we do not actually executed this, so Shift Enter, okay, do Shift Enter, Shift Enter, and Shift Enter, and here you go. As you can see, the index 0 is now 1, index 1 is 1, index 2 is 0, and that's exactly what we need to do over here, so that we can put the CNOT gate. And also you can do it like this as well, reversed and secretNumber.

It really doesn't matter, you can choose the way to do this, it gives the exact same result as you can see. So, I believe we haven't seen the reversed in the Python section, so I just wanted to show you this one as well. So far, so good. So now I know that I added the CNOT gate, and now what I want to do is to add everything over here with the Hadamard gates, okay, so add the Hadamard gates to the qubits that I'm going to measure, and then actually going to measure them.

So let's do that. So I'm going to do the len, range(len(secretNumber)) one more time, okay, so we are actually adding another Hadamard gate over here. And, of course, we're going to add a new barrier, so that it would make much more sense, it would actually clearly show us, and then we're going to do the range thing over here to measure them as well, so, range(len(secretNumber)), and also do the same thing for the classical bits, because we will have the same number of classical bits over here. We are not measuring the helper qubit, the Ancilla qubit, remember?

So, I'm going to draw this, obviously, to show you later on, but for right now, I'm just going to run this and see how it looks like. Great. Now, before executing this, I'm just going to draw it one more time. So I'm going to just take this over there and just draw it over here, and let's see if we get the result that we expect to see.

Yeah, we are getting complicated results over here. So, most of the time we're going to have to come over here and say Kernel Restart & Run All things, and it will be okay. So, here you go. Now, good.

So, it seems like it's working. We changed the numbers, we changed the secretNumber, and also the CNOTs and the all other stuff has been changed as well, so it's adapting itself according to the secretNumber. So, here you go. We have the result over here, and let's compare this result with what we have over there.

So I'm going to take this and just go over here, and just paste it over there to see if they are the same number. Here you go. They are the same number. So far, so good.

As you can see, we managed to actually do this, right? So we managed to make it automatic, we managed to make it adaptive. So you can try this with another number, like just delete and add some stuff over here. Of course, it should have 1s and 0s, and you can try this like that.

So let me just run this, but before doing that, let me just copy and paste this over here, so that we can actually compare them once we run this, okay, so here you go, run this from scratch, and let's come back and let's see if we get the same result. As you can see, the circuit adapted itself, and exactly what we expect to see over here. So, this Bernstein-Vazirani algorithm works, and it's fun, and it actually shows us the quantum computers can outperform classical computers. We are just doing this with only one shot, okay.

So I hope this actually got you more excited about the quantum computers. So again, maybe we cannot just use this algorithm in real life problems, and in fact we're going to see another problem like this, or another algorithm like this that can only prove that the algorithm works in a much better way in quantum computers in the following section, but at least, this is fun, and we can even make a game out of this, and I made one, and I'm going to show this to you at the end of this course. So, we're going to stop here and continue within the next section together.
