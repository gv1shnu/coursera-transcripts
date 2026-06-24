# Phase

- **Course:** Quantum Computing With Qiskit And Advanced Algorithms
- **Module 2:** Teleportation
- **Lecture #:** 13
- **URL:** https://www.coursera.org/learn/packt-quantum-computing-with-qiskit-and-advanced-algorithms-wils7/lecture/R1Ktg/phase
- **Extracted:** 2026-06-22 15:21:28

---

Hi. Within this lecture, we're going to see what phase is, and we're going to focus on the ZGate, okay, because ZGate will eventually lead us to the concept phase, and we will understand it in a better way with the examples that we will be following throughout this section. So we have seen many gates before, but we haven't talked about the ZGate in detail, right, maybe we have seen the matrix, we have seen the particular matrix of the ZGate, but we haven't used it really. So we know this is one of the Pauli gates, okay.

X, Y, and Z, but, what does it do? It looks like the Identity gate, like 1 and 1, or the Identity matrix, maybe you remember that, but it doesn't actually do the same thing because it has a -1 inside of it, right? So 1 and -1. So, a little bit like an Identity matrix, or maybe with a - at the end.

So what does it do? So, let me just go back here, and as you can see, I'm in the documentation of the Qiskit again, and you can see the ZGate over here, and you can actually read the description of the ZGate, and it says that this gate is equivalent to a phase flip. So, what is a phase flip then? As you can see, it says that it turns ket0 into ket0.

It doesn't do anything if it's in the 0 state, but it turns ket1 into -ket1. So, what does even - mean in the Bell state, right, in the 1 state or 0 state? We cannot even imagine that visually right now, and we're going to see how to imagine it visually, by the way, don't worry about it. Just, right now, what we know about ZGate is, the matrix values, the values that is embedded in matrix, and, it does something called phase flip, and it turns ket0 into ket0, which means nothing, and it turns ket1 into -ket1.

So, it's a little bit interesting. We need to dig deeper and understand it more thoroughly, because we will be using this a lot as well. So let's go over here and let's draw the ZGate with the four rows and four columns over here. So, as you can see, I'm applying the ZGate with the Superposition or Entanglement state over here, and I'm getting this.

So, what does it mean? So, if I apply the ZGate to 1 over square 2, ket00 + ket11, then I get 1 over square root 2, ket00 - ket11. So, what does it mean to have minus? It doesn't mean anything for the possibilities, right?

So, if I have 1 over square root 2 or -1 over square root 2, what do I do? I still do the square of these numbers, in order to have the squared magnitudes, and it will all add up to 1. Right? So let me show you what I mean in a much more clear way.

So I'm in my circuit composer right now, and I'm just going to have 1 qubit, okay. So, I'm going to bring in this ZGate over here. And as you can see, it doesn't do anything. And this is what I expected to see, because, it says so in the documentation, right?

If it's state 0, then it won't do anything, for the ket0. And if you look at over here, the little Phase circle, we have seen this before, but we haven't used it. The default one is the 0 state, and over here we are in the default 0 state, we can just confirm it by looking at the color of it. And, let's apply the Hadamard gate, okay, so I'm in the ket0 and ket1, okay.

And, let's try to see the possibilities. So, 50% of the time I'm going to get 0, and 50% of the time I'm going to get 1. Now if I apply the ZGate over here, I still have ket0 and ket1 in the Q-sphere. The interesting thing is that in the ket1, I have this Phase.

So, it appeared in red, right? So, it says that Phase Pi. So, of course, it has a meaning to have Pi over there. We're going to talk about this in the next lecture.

But now, my ket1 has a Phase. So it's -ket1, okay, having a Phase is that actually -ket1, and, the more interesting thing is that it doesn't even affect the outcome, right? So, I'm still getting the 0 and 1 as a possibility with 50% of chance, because in the end I'm going to have the squared magnitudes of this. So having the Phase, might affect the outcome or might not affect the outcome at all.

So in this case, it doesn't affect the outcome, the probabilities at least. But in a more complicated circuit, it might actually affect the outcome, the possibilities as well, because essentially, what we do over here is to change this vector into some other position, right? So, let me just delete this out. So, in the Hadamard gate, we know that it points to ket0 and ket1, and we get 50% of the time 1 and 50% of the time 0.

But once we add the Phase, once we add the ZGate, it actually rotates that ket1 into another direction, and we don't see it in the Q-sphere. And the reason for that is Q-sphere is there to just visualize the probabilities or make us understand these gates in a much more easier way. However, there is something else called Bloch sphere, okay, so not the Bloch, but Bloch sphere, we're going to see how it's written as well. So in the Bloch sphere, we're just going to understand it in a much better way, because we can see the actual 3D rotation of this vector as well.

So when I add the ZGate, it only changes the color inside of the Q-sphere, but in the Bloch sphere, we will see that it actually rotates that ket1 into another direction, and it will be much more clear for us. So again, adding the ZGate or working with the ZGate, we can add a Phase, we can change this sign of the qubit, and it can actually affect the outcome or the probabilities, because after the ZGate, once we add a new transform, once we add a new angle over here, it can just land the vector in an unexpected location. So, this gate is very, very important, and we're going to use this a lot. And, of course, you cannot imagine why we use it in a real life example again, we will come to there.

And, in fact, within this section, actually, we're going to see some kind of quantum algorithms to use ZGate as well. So I'm going to open my Jupyter Notebook and meet you in the next lecture to show you the Bloch sphere that I'm talking about.
