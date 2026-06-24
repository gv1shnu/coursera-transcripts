# Deutsch Algorithm

- **Course:** Quantum Computing With Qiskit And Advanced Algorithms
- **Module 4:** Deutsch
- **Lecture #:** 23
- **URL:** https://www.coursera.org/learn/packt-quantum-computing-with-qiskit-and-advanced-algorithms-wils7/lecture/FQuUT/deutsch-algorithm
- **Extracted:** 2026-06-22 15:23:16

---

Hi. Within this section, we're going to focus on the Deutsch algorithm. So, within the previous lecture or previous section, we have seen the Bernstein Vazirani algorithm, and it was cool, right? So, we have seen that the quantum computers can actually outperform the classical computers in some specific problems.

And again, we're going to do the same thing in the Deutsch algorithm as well. So maybe it was a better idea to start with the Deutsch algorithm, because it's a simpler algorithm, but, in my opinion, the Bernstein Vazirani algorithm is much more fun and also easier to understand. So again, we're going to see how quantum computers can outperform classical computers in some way, and we're going to use Deutsch algorithm to do that, and it will be a reinforcement for you in order to grasp the gates and also the circuit composing in a much better way. So, what we're going to do, we're going to try and solve a problem using this Deutsch algorithm.

So, what is the problem? And, by the way, we can say that this is one of the first algorithms that can prove this quantum advantage over the classical computer, so it's very important for us, even though we're not going to use it in real life problems. So the problem over here is that we have a function, okay. So we don't know what that function does, but we know that it actually takes either 0 or 1 as an input, okay, so we can give 0 or 1 to the same function.

And for the output, we have four possibilities. We have either 00 01 10 or 11. So if the output is the same, like 00, then we can call this function a constant function, okay. Like in the case of 00 or 11, we can call this a Constant function.

But if the output is 01 or 10, then we can call this a Balanced function. So, what does it mean? It means that the output actually does not depend on the input, in the case of a Constant function, right? So whether we give the 0 or 1, we're going to get 00 or 11, we're going to get the same output.

So we call this a Constant function. But if, the output depends on the input, then it's a Balanced function. Like, consider a coin toss. So if you get a head head or like a tail tail, then it means you're dealing with a Constant function.

But, if you get a head tails or tails head, then it's a Balanced function, okay. So we want to determine whether this is a Constant or a Balanced function with a quantum algorithm, okay, so that's our problem. So in the classical way, or if you ask anyone, or if you ask a classical computer, please determine if this is a Balanced function or Constant function, what will it do, or what would they do? Of course, it's very simple.

We can give either 0 or 1, and actually we have to give both of them, okay, we can give the 0 and just see the output, we can give the 1 and just see the output, and compare the outputs, right? If they are same, then it's a Constant function, if they are not the same, then it's a Balanced function. But it takes two trials to do that, right, two shots to determine that, at least two shots. So, it's good, but it's not enough.

In a quantum computer, we can do this with only one shot, okay. We can determine whether this is a Balanced or a Constant with only one shot. So it actually proves that the quantum computers can outperform the classical one if we managed to do that. So, so far, so good.

So this is the problem. We're going to determine whether a function is Constant or Balanced, and we're going to do this in only one shot. So we can try and do this with the gates that we have been learning so far, and we're going to see how it works. But we are going to have to understand some concepts in further detail, because we will be using those concepts in real life problems as well, okay, so that is the beauty of the Deutsch algorithm.

And also, there is some other algorithm called Deutsch�Jozsa algorithm. And in that case, we don't have only 0 or 1 or just one input over here, so we have many inputs, like it can go all the way up to the 2 to the n, okay, 2 to the power n, to determine whether this is a Constant or Balanced. But in this case, we're just going to focus on this Deutsch algorithm, and if you understand it, there is no reason for you not to understand the Deutsch�Jozsa algorithm as well. So we're going to be dealing with the simplest form of this.

And, again, it will not do us good in the real life problems, but it will do us good in order to grasp the idea of the quantum computation in a better way. So, what will our circuit look like? So we're going to have 2 qubits, okay, 1 for input register and 1 for output register, so, I call them ketx and kety, and we have something called a black box over here, we're going to talk about it. So, just forget about the black box, we just have a function over here.

We apply that function to the ketx and kety, and we get some output out of it. So, this ketx will be our measured qubit, and this kety will be something like a helper qubit, okay, or auxiliary qubit. So we're going to apply the Uf or the function that we don't know what it is, okay, so we don't know what the function is, we just want to find out whether this is a Balanced function or like a Constant function. And in that case, it will just give us the output of ketx when we apply this, and, for the kety, we're going to have something weird over here.

So kety XOR f(x). So this sign is XOR, it's not tensor product. It's not an x, it's a + sign, okay, so if you see this plus circle, it means XOR, Exclusive OR. So why do we have it over here, okay, why do we XOR the kety with the function itself?

So remember, this has to be reversible, okay, so we're dealing with reversible operations here, something like applying a Hadamard and then applying it again in order to reverse it. So it means that if we apply the Uf one more time to the circuit, we're going to have to get the ketxy or ketx, kety states to begin with, okay. So, we're going to have some state, and if we apply this Uf one more time, then we should have the ketx, kety state again. So, if we do this ketyx or f(x), is it possible to apply the Uf one more time and get the same state back?

Let's see this and you would understand that why we are doing this kety Exclusive OR f(x) thingy over here. So, we actually start with the ketx and kety state, right? So, just follow along with me here. We start with the state, okay, and then we apply the Uf to the circuit, then, circuit looks like this, ketx, okay, x doesn't change or anything, but this ket becomes y Exclusive OR f(x), and beware that this is only one ket, okay, so kety Exclusive OR f(x).

So we're talking about 1 qubit over here. So again, if we apply the Uf over there, what will happen? So ketx will stay the same, right? If we apply this one more time, ketx will stay the same, and we're going to have something like this, kety Exclusive OR f(x) and Exclusive OR f(x) one more time.

So, what happens then, so, what happens? So if we Exclusive OR something with itself, like f(x) Exclusive OR f(x), then it's going to get us 0, right? So remember the Exclusive OR. So if we Exclusive OR something with itself, then we're going to get 0 as a result, and if we Exclusive OR something with 0, then we're going to get itself.

So it will return to the ketx, kety state. So that is the reason why we are doing it like this, okay, we don't even know the function over here. And, in the mathematical concept of this, or in the mathematical theory of this, we're just going to use it that way, in order to prove that it works, okay, we can just multiply this with matrices or we can just follow along with the ket notation, but it will work eventually. However, when it comes to writing code or just composing this in a circuit composer, we can just represent function, this Uf function with anything you want, like we can just represent this with CNOT, for example, or, I don't know, maybe Control Z, so we can choose something like, that acts like a function, like a gate over here.

But, when you actually think about the mathematics, then you can actually prove this with any function. So if you remember the quantum teleportation, this is exactly what we did, right? We transformed to ket psi, we didn't even know what ket psi was, so it was just an unknown state. But when we came to the writing, when we came to the actual circuit composing, we represented that state with 1, ket1, for example, we applied an X gate.

So we can represent this Uf function with anything that comes to our mind, like a CNOT, and we can see whether this CNOT was like a Balanced function or a Constant function. All that matters is that it will actually take us one shot to determine that outcome. And, why did I call this a black box? So, we're going to talk about black boxes or Oracles, in general, in the quantum algorithms.

So it means that there is some function, and we don't know the extent of it, we don't know what it does, but we give it some input and it will give us some output as a return, okay, so this is called the black box, and we can ask some questions like, if this is true, if this is false, if you take this what's going to be the answer? We don't know what's going on inside of the black box, but it happens. And, it happens that we're going to use this a lot during the quantum algorithms. The term does not matter, but you have to memorize this term, so, the black box or the Oracle will be frequently in your way.

So it's just a function, okay. And we're going to see this in details in the upcoming sections, it's not that big of a deal in this algorithm, but it will be in another algorithm that we will see or some other algorithms as well. So, let's stop here, and within the next lecture, we're going to talk about the mathematics of this algorithm, and then we will just write the code for it later on.
