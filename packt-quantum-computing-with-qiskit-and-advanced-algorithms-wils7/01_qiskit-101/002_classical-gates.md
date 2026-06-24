# Classical Gates

- **Course:** Quantum Computing With Qiskit And Advanced Algorithms
- **Module 1:** Qiskit 101
- **Lecture #:** 2
- **URL:** https://www.coursera.org/learn/packt-quantum-computing-with-qiskit-and-advanced-algorithms-wils7/lecture/PjVSw/classical-gates
- **Extracted:** 2026-06-22 15:19:27

---

Hi. Within this section, we're going to finally start working on quantum computers and just start programming quantum computers as well, because, maybe you remember that we talked about we need to know about the Math fundamentals, like matrices or statistics or probability, and also we need to know about some kind of superposition, entanglement, or interference principles, like quantum physics or the qubits fundamentals. And also we need to, we needed to know about the Python as well. So maybe this is the first time you learned about Python, maybe you knew that before, it really doesn't matter.

We're just ready for starting to learn about Qiskit and also starting to learn about quantum programming as well. So, what we need to do right now before we just deep dive into the Qiskit, we need to learn about classical gates. So, when we deal with classical computers, like regular computers that we use in our daily life, without or with knowing, we actually implement many classical gates. When we write a code like in Python, or in Java, or in any other programming languages, it will be eventually converted into 1s and 0s.

And, of course, processors processes this information, and they need to manipulate their information on the transistors to become 1 or 0, or like 5 voltage or 0 voltage, depending on the situation they are in. So, of course, we need some methods, we need some tools like gates, in order to manipulate 1s and 0s, and that's exactly what we're going to learn in this lecture. And in fact, we're not even going to deal with that kind of classical gates during quantum computations, but without knowing them, I believe it will be harder for us to learn about quantum gates, because we will be dealing with the quantum gates a lot. Maybe in the classical computation or classical programming, we don't even think about this stuff, okay, but we are not there right now for the quantum computation, we will build our own circuits, we will actually work hand in hand with the circuits and the bits a lot during quantum computations.

So we need to understand what's going on behind the curtains when we deal with the logic gates or the classical gates. So I opened the Wikipedia for logic gate. So, I believe if you have studied the electrical engineering, or the computer engineering, or software engineering, you have seen this Truth table, you have seen all this classical gates, and again, maybe you haven't seen them, it really doesn't matter, we're just going to see what it looks like in a minute, but know that this is not a subject for quantum computation, this is just the subject for regular computing, or regular computer engineering, okay. So over here, what we see is the classical gates or the starting of the classical gates, we're going to start with the most basic one.

Right hand side, we see the Truth table, which is the values that we get by applying that gate, and over here we see A and Q, A is the input, the Q is the output, and you see all gates have different shapes. So maybe you know this shapes, okay, maybe you know all the shapes and they're very different from each other, not very different, but they have some unique properties. You don't have to memorize this shapes at all, but just so you know, this happens to have some kind of shapes for each different gates that we're going to see. So let's start with the Buffer gate, which is the most basic one.

It doesn't do anything. If you give 0 for input, you get 0 for output, if you give 1 as input, you get 1 as output. So, it is literally Buffer. So, we can use this as a Buffer gate.

And we have a NOT gate, for example, it actually does something, so it's better to start with this, maybe. So if you give 0, you get 1, if you get 1, if you give 1, you get 0, okay, so it reverses the value of that current bit. So, let's see the AND gate. This is another gate.

And, right now we're not only dealing with one input, as you can see, we have two inputs, A and B, and for the output we have Q. And, beware of the shape. So, this is a different shape, as you can see, and it represents the AND gate. So NOT gate converts 0 into 1 and 1 into 0.

So what happens when we deal with AND gate. So, in AND gate, you should have both 1s as inputs in order to have 1 as an output. For any other inputs, you get 0, okay. So if you have 0 0, you get 0, if you have 0 1 or 1 0, you get 0.

But if you have 1 1, then you get 1 as an output. So this is not only for computer engineering, you can understand this, because the AND is just like the AND that we have seen in Python or maybe you have seen in philosophy classes, so it's the AND gate. And, for a different approach, you can see the OR gate as well, and beware the shape changes a little bit, okay. So over here, in the OR gate, if you have only 1 for any input, then you get 1.

For example, if you have 0 0 for both input, then you still get 0. But if you have 0 1, or 1 0 or 1 1, you still get 1. So it's sufficient for you to have only one input as 1, in order to get a one output as 1, okay. So over here, we have seen the OR gate.

So another popular gate that we were going to be working with is NAND okay, NAND or NOT AND. So, if we look at this, we can see if we have 1 1, we get 0. So it's a little bit different, right? So in the only case that we get 0 is the 1 1 state.

So this is kind of opposite of the AND gate. So, that's the name, NOT AND, by the way. So if you have this inputs, then you get 1, but if you have 1 1, then you get 0. And we have NOT OR as well, so this is the exact opposite of the OR.

So if you have 0 0, you have 1, and if you have something else, you get 0, okay, you can call this NOR or NOT OR, and as you can see, this is how it works. So this is a different one, so EXCLUSIVE OR or XOR. We're going to be dealing with this a lot, both in quantum computing, and, of course, in classical computation as well. So it's a little bit different, if you have both 1s or both 0s, then you're going to get 0.

But if you have different inputs, like 0 1 or 1 0, then you're going to get 1. So this is EXCLUSIVE OR. So if you have the same input, then you're going to have only 0. And, the opposite of this is EXCLUSIVE NOT or XNOR.

So if you have same inputs, you're going to have 1, if you have different inputs, then you're going to get 0. So, of course, you can just understand what's going on by just looking the Truth table over here. So, it happens that we have very similar things going on inside of the quantum computing world as well, and we're going to try to associate the gates that we're going to see with the classical ones. But, of course, that's not always the case, okay.

Maybe you will not be able to associate the quantum gates with the classical gate, but knowing the classical gate, at least knowing the existence of them and the terms, it will be very helpful for you to understand the quantum gates. That's why we have seen them. We're not even going to work with the classical gates, as I said before. We have just seen them as general culture, and, it will be very helpful for us to comprehend the quantum gates in a more, actually broad manner.

So let's stop here and continue with the quantum gates and see the similarities and the differences. [No audio]
