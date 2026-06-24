# Creating Algorithm

- **Course:** Quantum Computing With Qiskit And Advanced Algorithms
- **Module 4:** Deutsch
- **Lecture #:** 24
- **URL:** https://www.coursera.org/learn/packt-quantum-computing-with-qiskit-and-advanced-algorithms-wils7/lecture/zS8TF/creating-algorithm
- **Extracted:** 2026-06-22 15:23:26

---

Hi. Within this lecture, we're going to discuss the mathematics of the Deutsch algorithm and then we will write it in code as well. So let's start with the wrong approach, okay. So let's assume that we we only want to place a Hadamard gate on the qubit that we will be measuring, and let's see where it gets us.

Let's see if we can understand in one shot that we're going to get either like a Constant function or a Balanced function. So, of course, this is the wrong approach, but it will understand why this is the wrong approach and what would be the right one, okay. So if I apply the Hadamard gate over here, this will be in the ket0, okay, because we don't apply anything over here, and then we will apply the Uf, and then we will just get the ketx back. So let's see how it works.

So, the x will be in ket+, which is the superposition, and y will be in the ket0, and we will have the Tensor product, of course, in order to get the total state out of it, and we will apply the function to it, okay, so this is our total state over there. So we know that superposition is 1 over square root 2, ket0, ket1, and then we will just tensor product with the other qubit, okay. So let's start with the tensor product, and then we will apply the Uf over here. So, if we do the tensor product, it will be ket0, okay, and ket0, like this.

And, similarly, we have the other one as well. We will just apply the Uf over here, and then we will have the ket1 and tensor product ket0 over there. So if we apply the Uf to this ket0, ket0 state, what we will have in return? Of course, the first qubit will stay the same, so it will stay like ket0, but second qubit will have this function, right?

So kety Exclusive OR with f(x). So, if we just apply this, it will be ket0, and, then the second qubit will be f(0) Exclusive OR with ket0, okay. And, consequently over here, we will have ket1 f(1) Exclusive OR with ket0. So, what happens if we Exclusive OR something with the 0 state?

So, we have learnt this before. If we Exclusive OR something with 0, then it will give the same thing back to us. So we will have ket0, f(0) with the half percent or 50% possibility, or, ket1 f(1) with the 50% possibility as well. So, what good did it to us?

So, maybe we can get whether this is a ket0 or ket1, but we will get this with 50% possibility, right? So, like maybe if we do this in two shots, maybe we can, they do something out of this, we don't want to do this in two shots, we want to do this in only one shot, right? So that was the whole point. So adding only one Hadamard gate to the first qubit doesn't do anything good at all, but it actually opens a way to us.

So we can try to think of some different algorithm or different ways to apply this. Of course, we're just going to directly into the solution, we're going to see what Deutsch algorithm does, and, believe it or not, it will be very similar to what we have been doing so far, and you will understand everything that we discussed so far in a much better way right now. So, we want to do this in only one shot. And in order to do that, we're going to apply some other gates to the second qubit, the ancilla qubit over here, and, of course we're going to measure this at the end of the circuit.

So, the Deutsch algorithm looks like this. We apply the Hadamard gate, of course, over here. But in the second qubit, we apply the X gate and then the Hadamard gate. And if you remember this, from the previous sections, I said that we're going to talk about the mathematics of this, so you would understand this in a better way why we are doing this, and that's it, this is the time that we're going to understand this, right?

And, at the end, we're going to apply the Hadamard and then measure the x, and, believe it or not, it will give us whether this is a constant function or balanced function. So, we will just see how it looks like. So, in this kety, we're going to have the superposition, but with a different phase, okay, with ket- phase. So, how does it look like?

So this is ket+, we know that. And, if we apply some superposition or Hadamard gate to the ket1 state, we know that it's going to end up with the ket-, we have seen this before, but let's see this mathematically. Let's see why it makes sense to use this. And as you can see, I have placed this psi1, psi2, psi3 over here to represent the steps, okay, so we can actually follow this step by step over here.

So it doesn't mean anything, it's just there for tracking purposes when you come back and review your notes later on. So, in the first step, we have ket+, ket- states over here. So this is ket0 + ket1, and it's tensor product with ket0 - ket1. So if you remember, it should have been 1 over square root 2, but since we have two 1 over square root 2s, then I have just written 1 over 2 over here, okay.

So, what we're going to do, we're going to, of course, do the tensor product. So it will be ket00 - ket01, and +ket10 and -ket11, okay. So we have this states over here. So, this is cool.

We have all the states with different phases and stuff, but we have the same probability right now. So what happens if we apply the f gate or the function over here? So if we apply this to ket0, the first ket0 will be the same and the second one will be replaced with 0 Exclusive OR. Now, if we just do this for every qubit that we see over here or every possibility that we see over here, then, we're going to end up with this, right?

So it makes sense to you, - + -, so beware of the signs, we flip the signs. So, if we apply this, if we apply this, then we know that if we just do this with Exclusive OR, it will just give it itself, if we do this like this, we don't know what's going to take or what's going to be the output, so we just leave it like this, okay. And, if we come over here, again we do this with Exclusive OR 0, it will give itself, so we can write ket1, ket f(1), so we don't know what f(1) is, but we know it's there. In this case as well, we don't know what's going to happen if we do this Exclusive OR, so we will just write it like this.

So this is as simple as it can get, okay. So this is what we have right now. So, at this point, we're going to do an assumption. So assume that, we're going to do the both ways, don't worry about it, okay.

We're just doing this mathematically in the code, in the execution, it will just do it like a snap of a finger, okay, so it will be only 1 shot. We will assume IF F(0) = actually F(1). So, this is a Constant function. So if it equals to F(1), then we can actually simplify this a little bit more, because we can just write F(0) for the F(1)s, right?

So this is ket0 f(0), okay, and this is again ket01 Exclusive OR f(0). So, we just replaced the F(1)s with the F(0)s. So what happens if we do it over here? Then we can actually just do some simplification, it goes to the ket0 + ket1, f(0), and - ket0 - ket1, 1 Exclusive OR f(0).

So we don't know what 1 Exclusive OR f(0) is yet, but, it doesn't matter, because, let me show you why. Of course, we're going to take this minus sign out of this, okay, we're going to take this minus sign out of this and it will become ket0 + ket1, and we can just simplify this further, and, it will eventually become like f(0) - ket1 Exclusive OR f(0). Again, we don't know what this term is, we don't know how it's going to turn out. All we know, that this is right now, 1/2 ket0 + ket1, and something else, we don't know the other one over here.

So, what we know is, this ket0 + ket1 can be simplified as ket+, okay, like superposition. And if we actually simplify this, of course, we have to change the scalar over here to 1 over square root 2, and we have this over there. So, what's going to happen if we measure this? So if we apply this Hadamard gate and then measure this, okay, if we apply this Hadamard gate to ket+, because, we don't know, we don't even care about the second qubit, we're just going to apply the Hadamard gate to the first qubit.

So let me open the circuit composer and let's see what happens if we apply the Hadamard gate to a superposition state. We already know the answer, right, because it will reverse it and it will just go back into the 0 state. So let me delete everything over here. We don't care about a second qubit, because we're just going to measure the first qubit.

So I have the Hadamard gate, okay, so it's either in the ket0 or ket1. So what happens if I add another Hadamard gate over here? So, it will return to the ket1. Even if I measure it or not, it will return to the ket0, sorry, ket0.

So, I don't care about the second qubit, because I'm not even going to measure it. So if I measure the first one, then I'm going to get ket0 out of it. So what it means that IF F(1) = F(0), then I'm going to get a ket0 out of this, because I'm going to apply the Hadamard gate to the ket+ state, right? So this can be verified by the circuit composer.

So what happens IF F(0) is not equal to F(1), if this is a Balanced? So if this is Balanced function, then it means that we can write F(0) as like F(1), XOR 1, okay. So F(0) is actually F(1) Exclusive OR 1 in this case. So by taking advantage of this information, we can again simplify this a little bit, right?

So we can just change this to be f(1), and if we can change this to be f(0), because we know that they are equal to each other. So what happens if we change these things? So we got rid of the Exclusive ORs, right? So in the previous one, we got rid of the f(1), so we ended up with f(0), now we got rid of the Exclusive ORs and we ended up with f(1)s or f(0)s.

So if we simplify this a little bit, then we're going to get this notation. So follow along with me. So we have this f(0), f ket0 - f ket1 over here, and if we just do this ket0 - ket1 tensor product with f(0), f(1), okay, ket f(0) - ket f(1). So, we know that ket0 - ket1 can be simplified as ket-, okay, of course, changing the scalar to 1 over square root 2.

So we know what is this. So we can just add this NOT gate over here, and if we can add the Hadamard gate, then it's in the ket- state. But as you can see, if we add the second Hadamard and the measurement again, then we're going to have ket1 as a result. So if we apply the Hadamard gate to ket- state, then we know that we're definitely going to get ket1 out of this.

So what does it mean? It means that, if our function is balanced, then we're going to get ket1 out of this. And if our function is Constant, then we're going to get ket0 out of this. So depending on the measurement, we can actually know the function behavior, whether it is Balanced function or a Constant function.

Again, if we're going to get ket1 or ket0, we can determine the function behavior. We don't know whether we're going to get ket1 or ket0, but, by looking at the measurement, we can immediately know, whether it is function, like a Balanced function or a Constant function. And again, we're going to do this in only 1 shot, and we're going to only measure 1 qubit. So we are using 2 qubits, 1 as a helper, but we're going to only measure the first qubit, so we don't actually care the state of the second qubit at the end.

So we don't know what ket f(0) - ket f(1) means, but, we don't even care about it, because we're not even going to measure it. So I'm not even going to apply more Hadamard over there as well. So far, so good. So, if you understood this mathematically, then you are on a good track.

If you didn't, maybe after you complete the following sections, you can come back and watch it again, and then you can understand it in a better way. So you may have to do some revisiting of the previous sections as well. So let's stop here and just see this in Qiskit as well.
