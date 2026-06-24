# Quantum Fourier Transform

- **Course:** Quantum Computing With Qiskit And Advanced Algorithms
- **Module 6:** Shor's
- **Lecture #:** 33
- **URL:** https://www.coursera.org/learn/packt-quantum-computing-with-qiskit-and-advanced-algorithms-wils7/lecture/9Twuv/quantum-fourier-transform
- **Extracted:** 2026-06-22 15:25:05

---

Hi. Within this lecture, we're going to focus on the Quantum Fourier Transform or Fourier Transform, however, you may want to pronounce this. So, we're going to actually make this short by saying QFT, and QFT is not specific to the Shor's algorithm. This is actually one of the things that we should learn in order to understand the quantum computation in a better way.

But it happens that we use this logic in Shor's algorithm, so that's why we are seeing this right now. And what we mean by QFT, we're going to actually transform the basis. So, what do I mean by the basis? We're going to take the vector from Computational Basis to the Fourier Basis.

So, what does that even mean? We're going to talk about this, we're going to see how we can actually prove this mathematically as well. So this is the Computational Basis, okay, like ket0, ket1. So vector is pointing up or pointing down.

So it's either in the 0 state or in 1 state. Alternatively, as you can see, in the ket+ state or ket- state, it actually points directly toward us or in the opposite direction. So if we are talking about this axis over here, it's in the Fourier Basis, but in the other state, it's in the Computational Basis. So, if we apply some logic like a matrix or some kind of mathematical operation, to take this vector into that position, then we call this Quantum Fourier Transform, okay, so it's very easy actually.

However, there are consequences and also there are some very helpful things that we can get out of this QFT. So in the 1 qubit state, in the 1 qubit example, what brings the Computational Basis into Fourier Basis? So as you can see, you know this very well, the Hadamard gate does that, right? So Hadamard gate puts the ket0 into ket+, which is superposition, and also ket1 into ket- state as well.

So they are in the superposition. However, it shouldn't be actually in that same specific vector state, okay. We could have some angle, we could have some phase. So in this example over here, it has some phase fill and also we are going to see that it can also have some angles as well, okay.

So, generally we cannot actually deduce the whole QFT thing into Hadamard gate. For 1 qubit, it's right, but for 2 qubits, what happens, let's see that. So over here, we know that Computational Basis is either ket00, ket10, ket01, or ket11. But in order to convert this into Fourier Basis, we have a general formula, okay.

So if you see this ketx delta, it means that it's in the Fourier Basis. And, the formula for the Fourier Basis happens to be this way. So, this formula can seem a little bit difficult or complex when you first see it, okay, but we will just simplify this later on. So, as you can see, we sum this up.

What we sum is the e to the power 2 pi, and this is the number pi, i, so this is the imaginary number, x y over N and kety. So, this is a little bit complex, as you can see. So N here is 2 to the power n, and n being the number of Qubits, okay, if we have 2 qubits, then the n is 4, if we have 1 qubit, then the n is 2. So over here, we had to know that first of all.

e to the pi*i means -1. So, why is it like that? I'm not going to go into the details of this geometrical explanation, so I'm going to share this YouTube link with you guys. If you want to see why that is, you can go over there, but it's completely out of scope of this course, so I didn't want to just burden you with this.

So if you want to memorize it, then here it is, e to the pi*i means -1. So if you want to see this geometrical explanation, it has nothing to do with the quantum computation at all. You can go over and look at that YouTube channel, but know that e to the pi*i means -1. Okay, this will help us in the computations for the upcoming slides.

So N here again is the 2 to the power n and n being the number of Qubits. So if we have 1 qubit, the N is 2, if we have 2 qubits, the N is 4, if we have 3 qubits, the N is 8. So over here, we sum this e's up by the N over here. So if we have only 1 qubit, then we will just sum this twice, if we have 2 qubits, we will just sum this 4 times, by changing the n and also x and y as well.

Great. Now, this is the general formula, but once we see it, okay, it doesn't make sense. It isn't something that we can understand it intuitively. So let's prove this works, okay.

So we're going to try and do this with the 1 qubit and we know that in 1 qubit it actually adds up to the Hadamard gate, and let's see if we can actually apply this if we can go to the Hadamard gate. So just put the tools in where you see n, okay, 2*pi*i*x*y, over 2 kety. So we know that n is 2 in this case, because 2 to the power of 1 is 2, we are working with only 1 qubit over here. So, of course, we have to do the summation.

So y equals 0 to 1. So we're going to do this twice. If y is 0, then, we're going to have this notation over here, e to the 2*pi*i*x*0 over 2, okay. So this is the first statement that we need to take care of with the ket0, of course, because y is 0 at that point.

So, we have this over here, but we have to sum this up when y is 1 as well. So 1 over square root 2, 2 to the power, e to the power 2*pi*i*x*1 over 2, ket1 this time. So this is going to be very simple, because, over here we have the 0. If we just make it 1, it means that 1 over square root 2 ket0, but over here we have 1 over square root 2, e to the pi*i*x, ket1 as well.

So, let's see what it does. If, and only if, if we know that x is 0, okay, the first qubit is in the 0 state, and we only have 1 qubit, by the way, if our qubit is in the 0 state, then it means that this will bring us to the ket+ state, right, because this e thing will go away. But if it's in the 1 state, now we know that e to the pi*i is -1, and then it will bring us to this state, 1 over square root 2, ket0 - ket1, and this is ket- state. So this is exactly what we have seen over here, right?

So this general formula seems to be working, at least we managed to prove this. So this is the formula for the Quantum Fourier Transform. Of course, it doesn't end here, okay, we're going to have to work on this to understand this in a much more comprehensive way. So, this is one of the key areas that we will understand how to build the quantum gates as well.

So we know that this is our general formula, okay, I didn't replace anything in here yet. But we're not even going to change anything in this formula, but we're going to substitute some of the notations in some other way. For example, we have the y over here, and we know that y depends on the, over here, like it will be y1, y2, y3, yn. It depends on the qubit number, right?

It will go up to the yn. So we have written this ket0 and ket1, but, what happens when y is 2 or y is 3? Do we have anything like 2, ket2, ket3, ket4, ket7. We haven't seen them yet, right?

And it doesn't make even sense, because we either have the ket0 or ket1, but what is ket7? So if we have this, like 3 qubits, there is a state where y is 7. So what is ket7? It's actually the representation in the binary state, like the decimal binary transformation, think about the decimal binary transformation.

Writing ket7 in here doesn't make sense, it's actually an abuse of notation. ket2 means ket10, okay, ket2 means ket10. So you have to convert decimal into binary in order to understand this in a better way. However, if you want it, you can write it like ket2, ket3, ket4 to be much more clear or to make it simple, to keep it simple, however, know that ket2 doesn't mean anything by its own, so it means that ket10.

So we can actually write it like this, 2 to the power n -1 y1, 2 to the power 0, y1. And remember that this is how we change, this is how we go from decimal to the binary. That's why I'm writing it like this. And, of course, we can actually summarize this by saying that y = k0 to the n, yk 2 to the power n-k.

Okay, that's how we convert decimal into binary, remember the first lecture that we have seen in this course. Now, since this is the general formula, and since we have defined y from scratch right now, rather than y, we can write it like this, right, we can substitute the y with this notation. So, how does it become? Since I'm going to do some summation over here, and since I'm in the like, superscript over here, so I'm going to, in fact, multiply this, right?

So I'm going to multiply this together. So if I write it like this, it won't make sense. And by the way, the reason that I have it here, the upper side will have 2 to the n -k means 2 to the n over 2 to the k, and the n will be actually neutralized by the other one, so we will end up with this, and we can convert this into the product notation like this. So this is the multiplication notation, and this is the summation notation, as you might already know.

Then, we can actually summarize the whole formula by this. So you may think that, yeah, this made things much more complicated, why did we even do that? So I'm going to show you why. By the way, we are just talking the theoretics over here, okay, we didn't do anything yet, we haven't changed anything yet.

So I'm showing all of this to you in order for you to understand this quantum thing more comprehensively. So we can actually summarize what's going on over here by tensor products. Of course, we're going to multiply all of those things together. And over here, it comes like this, 1 over square root of N, ket0 + e to the 2*pi*i*x, over 2 to the 1.

And, this is only for k=1. And if we change k to be 2, then we will just do the tensor product for e to the 2*pi*i*x, but this time 2 to the power 2, with ket1 one more time. So if we continue like this, we will see that when we increase the k over here, it will just go on and on, and it will just end up in a state like this, ket0 plus e to the 2*pi*i*x over 2 to the n ket1. So, if you look at this formula, if you look at what we got here as a result, the first qubit is always in the ket0 state, okay.

So, what we can do over here is that we can actually try to come up with a matrix to make this happen. So if we want that, then for the second qubit, for the first qubit, obviously we can write 10, and for the second qubit we can write this, 0, and e to the 2*pi*i over 2 to the k, like this, okay. So if we apply this to any state, then it will convert it like this. And the reason why I'm writing this k, okay, is that, as you can see, once we actually increase the k, the multiplication will continue and continue unless we reach the 2 to the power of n.

So this depends on the qubit number eventually. So, it happens that, of course, Qiskit knows this as well, okay. This is how we build the quantum gates at the end. So, if you go to the qiskit.org and just find the General U-gates, you don't have to, by the way, I'm just showing you this as a general culture.

Over here, there is something called U-gate. And this is the general representation of all the gates that we have ever seen actually. So, it says so in here, like there are cosine, sine, and some thetas, and some angles. So it's a little bit complicated.

But, it says so, Every gate in this chapter could be specified as U3. But it's out of ordinary to see this, because, it's actually difficult to read this, right? So you don't understand actually how to read this. So this is what we got in the end, like 10 0 e to the power i with some kind of angle.

So angle happens to be pi x or 2k in our case. But, we can actually deduce all the gates into a notation like this, and we call this U-gates in Qiskit. So, if we take this U-gate, okay, if we take this U-gate, and we mathematically found this out, we didn't even have to look at the Qiskit documentation at all. So if we apply this to circuit, okay, like a qubit from, starting from x1, all the way to the xn, if we control this U rotation, if we control apply this U rotation, for each qubit, let's see what happens.

If we actually apply this, it will start with the state X1 to the Xn, okay. And, once we start applying this Hadamard and the U rotations, then we will end up with something like this. With tensor products, of course, once we add the second one, once we add the second one, it will go on and on, like this. So 2 to the power 3, 2 to the power 2, 2 to the power 1.

Once we increase the U rotation, it will just continue on and on and on. So that's great. So, as you can see, we get this notation, but what do we do with that? As you can see it's exactly the reverse order of what we have found mathematically, right?

So it started with 2 to the power 1, 2 to the power 2, 2 to the power 3 over here, but it goes like in the exact same opposite reverse order over here, 2 to the power 3, 2 to the power 2, 2 to the power 1. So why I'm telling you is that, if you actually come up with some kind of QFT circuit or a documentation once you try to start your own learning process, on your own, by reading the essays or starting from some other sources, you can see some swap gates used in the Shor's algorithm, like swapping the state of the X2 with the X3 or Xn with the X1, something like that. And, the general reason for that is to just reverse this order into the regular order, okay. So, what I'm trying to tell you over here is that QFT is just taking the Computational Basis to the Fourier Basis, and there is a formula to do that, and we should know about that formula, and also you can actually make this into a gate and use it on your own purposes to create a circuit like this.

But how do we just turn this into something called quantum phase estimation and just use it in the process of Shor's algorithm? So we're going to see this in the next lecture together.
