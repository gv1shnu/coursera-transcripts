# Quantum Algorithms

- **Course:** Quantum Computing With Qiskit And Advanced Algorithms
- **Module 3:** Bernstein Vazirani
- **Lecture #:** 19
- **URL:** https://www.coursera.org/learn/packt-quantum-computing-with-qiskit-and-advanced-algorithms-wils7/lecture/rtWSK/quantum-algorithms
- **Extracted:** 2026-06-22 15:22:33

---

Hi. Starting from this lecture, we're going to deep dive into the Quantum algorithms. And, of course, we're going to see many algorithms, and we can categorize them into 2. So first of all, we're going to see some algorithms that can actually change the world, and that can actually be used in the real life problems, okay.

So we're going to see a couple of those, and once the quantum computers get better, once they get actually close to being perfect quantum computers, like error-free perfect Quantum qubits, then, we're going to actually see those improvements in our lives as well. So we're going to see that kind of algorithms. And also, we're going to see some algorithms that can be used in order to prove that quantum computers can outperform classical computers. So, what does it mean?

It means that quantum computers do not always outperform the classical computers. It depends on the problem. If, the solving of that problem, or if the algorithm of that problem can be efficiently executed in superposition with the entanglement, then that's very good. We can use a quantum computer and we can efficiently solve that problem.

However, not every problem is that way, okay, we don't have Quantum algorithms for every kind of problem. There are specific Quantum algorithms that can change the world, and there are specific Quantum algorithms that can show that quantum computers can outperform classical computers in a way. Remember that classical computers are sometimes better, because quantum computers do not perform brute-forcing or do not try every possibility. They actually take leverage of the superposition, entanglement, and interference, in order to solve some kind of specific problems.

So, we're going to see the either of those categories. And, for example, BERNSTEIN - VAZIRANI, we're going to start with this BERNSTEIN - VAZIRANI problem, and it can actually show us that quantum computers can perform much better in this circumstance. So, every algorithm is named after the founder of that specific algorithm, by the way, so it happens that this algorithm has been found by BERNSTEIN and VAZIRANI. So we call this BERNSTEIN - VAZIRANI algorithm.

So what happens in here? So we have like a number, okay, in binary, 1011001. So we pick a number and we try to guess it, okay. So this is in a string format, by the way, but it doesn't matter, it's in binary format.

And, of course, it cannot be in integer, but we can always convert an integer into binary format, and, we can ask for a friend to guess that number, for example. If you ask a friend, he or she will say to you, okay, is it 00001? If you say no, then, he will continue like if it's 001000. So he will try every possible combination, okay, if he doesn't have any other plan in his mind.

So, considering that this number has 7 bits, he will try, maybe, 2 to the power of 7, right? So, we have 2 to the power of 7 combinations over here. Of course, he can find it on the first try if he tries randomly, or, he can find it on the last try. So this is kind of an exponential way to solve this problem.

However, if we ask classical computers to guess this number, then it can be much more efficient. What classical computer can do is that it can take a, take a bit like a 00001, as you see over here, and it can perform an AND operation. So, remember the AND operation? If both bits are 1, then the result is 1.

In every other situation, the result is 0. So, if it sees 11, it actually takes a note and says that, yeah, this is 1. Then it continues, and it goes to the 000010. So it changes the position of the 1, and it does an AND job, like an AND operation, AND gate for each combination.

So it takes 7 try for classical computer to find this number by using that kind of algorithm. Of course, this is much better than the 2 to the power 7 option, okay, but it's not enough. Why is it not enough? Because, BERNSTEIN - VAZIRANI ALGORITHM says that quantum computers can actually find this number in only one try, okay, in only one Shot.

We're going to just create a circuit, we're going to run that circuit only once, okay, we're going to specify Shots to be 1, and we will find that number. So this is very powerful, right? So this is one of the examples that can actually prove that quantum computers can outperform classical computers. Maybe it will not change the world, maybe it will not be an end product, maybe we can build a game out of this, I don't know, but, not certainly something that can change our lives.

However, it can actually prove that quantum computers can easily outperform the classical computers in some certain problems. Now, in order to do that, we're going to have to understand how BERNSTEIN - VAZIRANI algorithm works, and we're going to do this in the next lecture together.
