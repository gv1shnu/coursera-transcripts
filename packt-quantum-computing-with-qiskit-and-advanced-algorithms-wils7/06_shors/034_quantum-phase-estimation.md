# Quantum Phase Estimation

- **Course:** Quantum Computing With Qiskit And Advanced Algorithms
- **Module 6:** Shor's
- **Lecture #:** 34
- **URL:** https://www.coursera.org/learn/packt-quantum-computing-with-qiskit-and-advanced-algorithms-wils7/lecture/Db5qu/quantum-phase-estimation
- **Extracted:** 2026-06-22 15:25:17

---

Hi. Within this lecture, we're going to see the Quantum Phase Estimation or QPE, and we're going to apply this in order to actually complete our Shor's Algorithm Mathematical Foundations. So what happens over here? We have a qubit called ket psi, okay, and we apply some U-gate over here.

So it applies some kind of phase, but we don't know the phase, we don't know the state of the ket psi as well. So this is e to the i theta, and it's ket psi one more time. So we apply a phase over here, but we want to find out that angle. So we want to estimate that phase, and QPE actually helps us do that, okay.

So how does it work, what does it even mean to apply this U-gate and try to find this phase? So, indeed, we have seen this before. So we know that this is 1 over square root 2, ket0, ket1. And if we get the probabilities, it will either return 50% 1, 50% 0, and this is superposition, we know that before.

But it could have some phase, right? Like, maybe it's in the ket- state, maybe it's in the ket+ state. So, if we try to calculate the possibilities, it is possible to get the square magnitudes of this with e to the power i * pi over 2 with 1 over square root 2. If we get the square root of this, square magnitude of these things, we can end up with 50% one more time.

And, in fact, we have seen this before when we have seen the Z gate, remember, maybe we have some phase and it doesn't even affect the outcome, we still get the 50% possibility. Sometimes, however, we have that phase, and it affects the outcome, okay, depending on the situation, it may land somewhere else, and it may affect the outcome. So, the idea over here is that how do we find that theta, so that we can actually understand what kind of a phase we are in, if we don't know the state? So Quantum Phase Estimation helps us do that.

So how does it do that? Let us start by seeing the most simple representation of this. So over here, in the circuit, we have ket0, okay, we have a qubit and also a ket psi. We don't even know how many qubits are there in this ket psi, or we don't know the state over here.

So we start with applying Hadamard to the ket0, and then we applied some controlled U rotations to the ket psi and then apply Hadamard to the ket0 as well. Let us see how does it help us to understand the Theta? So if we applied the Hadamard gate, we know that this will return into ket0 ket1, and we can actually represent this like 1/ square root 2, ket0, ket psi, + ket1 ket psi, okay. But if we apply this phase over here with controlled U-gate over there, so what does it do?

As you can see, we changed the Target and also the Controlled gate, like we have seen something similar in the QFT, but this time Controlled and the Target gate are reversed. So it will apply this, like that. So 1/ square root 2, ket0, ket psi, and ket1 with some phase. So if we apply the Hadamard one more time to the first qubit, then we will end up with like this, okay, since we have ket1 over there, it will be minus, and if we actually do the simplification over here, we will end up with a formula like this.

So ket01 + e to the power i Theta, and the same thing with ket1 in minus state. Of course, the real question is, how does it help us? Okay, so let's go straight into the final result of this, because if you want to calculate the possibility of 1 over here, we're going to have to get this. So 1- e to the power Theta I, and just multiply this with 1/2 and get the squared magnitude of this.

And also it's the same for the ket0 state as well, only it changes the sign. So, what does it tell us? So remember one of the first lectures in the qubit section. So, if we actually rotate the measuring device or the state itself, then it will change the probability, right?

So over here, if the Theta is 1, for example, the possibility of getting 0 is something like very close to 100%, so it's 0.99999. But if we increase the Theta, okay, if we change the phase over here in a beta, it increases the Theta, then possibility of getting 0 is going to go down. And once we increase this more, possibility of 1 will increase as well. So, that's it, that's how the phase works actually, that's how the Theta works over here.

So what we try to do is to find that Theta. So, of course, how can we find that Theta? We can actually do this like, maybe 1000 times, or maybe, I don't know, 5000 times, and just measure the result, okay, just see the possibility of getting 0, for example, and try to estimate that Theta. So, of course, I don't know how many shots would it take to calculate this, because, as you can see, if the Theta is 1, the possibility of getting 0 is very high, and it's also the same for Theta is 10 as well.

So maybe Theta is 90 or 180, then it would be much more easier for me to understand this, but if the Theta is 10, then I believe we're going to have to just run this like thousands of times in order to just estimate the phase over here, or estimate the Theta over there. So rather than that, of course, we can use multiple qubits in the first state, like, we have only 1 ket0 over here, we can increase that number, so that we can leverage of having more than 1 qubit over here, and we can calculate this much more efficiently. And again, all we try to do is just find this phase, find the Theta over there. So this is very similar to QFT, by the way, if you just remember the QFT, we're going to see it mathematically as well.

So what we're trying to do over here, we just reversed the Target and the Controlled gate over there in the Controlled rotations, but we're just going to do the same thing with more than 1 qubit, more than 1 qubit over here, like apply the Hadamards to all ket0s over there and then apply the U gates or U rotations to the ket psi one more time, but for each qubit that we have over here. And again, it will just land up in something very similar to QFT as well. So let me show you how it goes. So this is ket0 * n, okay.

Since we had n qubits over here, we don't even know the state of ket psi or how many qubits are there. So it goes like this, ket0 + ket1 *n, and if we apply the phase over there, so it will go like this, e to the power i Theta, 2 to the power n-1. And it will go all the way up to the 2 to the power 0, okay. So we'll end up in some state like this.

So what does it tell us? If we go to QFT back, okay, as you can see, they are very similar. So everything seems like very similar to me, at least when I look at it. One difference over here is that if we try to compare the QFT with QPE, the phase is different, the Theta, the angle is different over here with the 2pi i/2 to the power n, okay, so that's the only difference in this equation.

So what does it tell us? So if we apply this like that, like if we apply the Hadamards, then if we apply the Quantum Phase Estimation, and then if we try to inverse the QFT with QFT adjoint, okay, so we would get something out of this, right, because it's very similar, but it's different as well. So what we get over here when we apply the inverse of the QFT or the adjoint of the QFT, which is the transpose complex conjugate, complex conjugate of the QFT, then we end up with 2 to the power n Theta. That's how we actually find the Theta, okay.

So, we're going to apply the Hadamard, we're going to apply the Quantum Phase Estimation gates that we will be doing over here, and then we will apply the QFT dagger, QFT adjoint, and we will end up with the 2 to the power n Theta state. So, let's start it from the scratch, okay, and let's actually tie this together with the Shor's algorithm. So in the ketx we have 4 qubits, in the ketw we have 4 qubits as well. So we are trying to find the factorials of the 15, prime factors of the 15, and since 15 is 1111, I'm just using 4 + 4 qubits over here.

So, we want to end up with the pq, okay. So what we're going to do, we're going to, of course, apply the Hadamard gates first, and then we're going to apply this Uf gate. So this will be our Quantum Phase Estimation actually, but this will do the modular exponentiation over there. So, if you don't understand the relation between the modular exponentiation and the Quantum Phase Estimation that we have seen, they are very similar to each other, but we will see it at the end of this lecture, don't worry about it, but we're just going to apply this as a function.

And remember, when we try to do something like this, like a black box logic, then we should do it like this, the ketx, ketw state. So if we apply the Uf over here, it should apply it like this, ketx, ketw, Exclusive OR with the function itself, so it can be reversible. If we apply the same thing one more time, it will end up with the ketx ketw state. So we have seen that before.

Third step would be to measure this, okay, so we're going to measure the ketw. And, of course, I will tell why. So, later on we're going to just apply the QFT adjoint and then measure it to find this p and q itself. So let's see all of those things mathematically.

So it will start with the ket0 ket0 states, okay, we have 4 ket0s, 4 ket0s over here. So if we apply the Hadamard to the first four qubits, then we will have that kind of notation over here, multiplied with the other qubits with the w qubits, we didn't change anything in the first step, okay. So, once we apply the Uf, the function over here, to all of these things over there, and by the way, in the documentation or in some other essays, you can see this like, ket1, ket15, ket7, and we talked about this. So if you see ket15, it's actually ket1111, so it's the binary and decimal conversion over there.

So if we apply this Uf, then, it will just have this kind of impact on the second qubit. So, ket0 Exclusive OR 13 to the power of 0 mod15, 13 to the power of 1 mod15, and it will go on and on, like 13 to the power of n mod15, okay. So, it will just change the phase or change the actual state of the second qubit while keeping the first qubit same, so first four qubits are in the superposition right now. So, that's okay, but we know that if we do the Exclusive OR with 0, okay, so it happens that the ketw is in the state of 0, it's initialized like that.

And if we apply this, like that, like if we do something with, if we do Exclusive OR, something with 0, it will just give the same thing itself, right? So if we Exclusive OR 0 with 13 to the power of 0 mod15, then we're going to end up with this. So, over here, after we end up with this, then I'm going to write everything together. So, we are trying to write the total state, like the ketx and ketw together, and we're going to measure it and see why we measure it later on.

So, over here, if we write everything, and if we actually use that abuse of notation that I have talked before. So we're going to end up with like this, ket0, so we got rid of all the Exclusive ORs, because we are exclusive in owing with the 0 itself, okay. So if you just calculate the ketw's over here, like 13 to the power of 0 is 1, 13 to the power of 1 is 13, 13 to the power of 2 mod15 is 2, 4, sorry, and 13 to the power of 3 mod15 is 7. So, the r is over here, 4 actually, and you can see it immediately.

But in the mathematical computation, there is no way to see it like this, okay, and it could have been much more complex. So, we should write it down, first of all. And when we measure this, we will see the r itself. So over here, ketW is either 1, 13, 4, or 7, okay.

So, if you look at all the ketw's, it's either 1, 13, 4, or 7. And then, if we write the ketx's over here, it starts from 0 and then it ends up with the 15 over there. So the total state becomes this one. So ket0, ket1, ket2, ket3, along with the ket1, ket13, ket4, ket7.

So this is the total state in the second step. So the third step would be to measure the ketw's. So, if we measure the ketw's, we have four possibilities, like 1, 13, 4, or 7. So, we're just going to assume something, okay, we're just going to assume that we have measured 7, for example.

Of course, you can do this with another assumption as well, like 4 or 13 or 1, but I'm just going to assume that we have measured 7 in this step, and you will see why I'm doing this. So if we measured the 7, what would be the possible states of the ketx? Of course, we can just take a look at over here and see the possible values of x, right? So this is either ket3 or ket7, ket11, and ket15.

So in the 1/4 chance, so x is going to be 1/4, ket3, ket7, ket11, and ket15 over here, because we assume that we measured 7 in the ketw. So again, it doesn't matter, we could have measured 4, we could have measured 13, we could have measured 1, and it would change the possible x values, but we're just going to go with this assumption. So if we actually add this up together, then the coefficient will change and we will actually add this tensor product, ket7 over here. So 1/2 ket3, ket7, ket11, ket 15, tensor product with the ket7.

So let's actually implement the QFT dagger over here. So QFT by itself, you know the formula. So ket x tilde is this. If we try to take the adjoint of this QFT, then what we will do, we're just going to take the transpose and also change the sign of the imaginary parts.

So, all we got to do is just change this number, change this i sign to be minus, okay, that's it. So this will be the QFT dagger formula that we should be working on. So it's very easy, we just change the sign of the e, okay, it's very easy. Now, let's try to get the x's over there, and we know that the n is 2 to the power 4, which is 16, so 1/16, y is from 0 to 15, to e to the power -2*pi*i, 3 y/16 kety, okay.

So we know this over here. So, I'm just doing this with the x3 by the way. You have to do this with x3, xy, x7, x11, x15 as well. So I'm just showing you how this would work.

So in the case of x being 3, it would work like this. So if we generalize this a little bit, it will go from 0 to 15 with something like this. So something like -3, -7, -11, -15. So, if we actually calculate this, then it will end up with a very similar notation, like 1/8, 4 times ket0, 4i ket4, -4 ket8, -4i ket12.

So how does it end up like that? So let me show you something. I got this from the Qiskit documentation as well. Of course, you may not know how to calculate the exponentials like e to the power -3, pi/8 plus something.

So you might not know how to calculate this. So it's very easy to calculate this with NumPy, okay. So I'm going to share this code with you as well. I got this from the Qiskit, and here is the proof.

So only four values got left after this and the other ones will be canceling each other out. So that is one of the examples of the interference as well. So if we calculate all of the 16 values, okay, if we add up them together, then we will end up with the four values over here, and these are the four values. So if we measure them, we're going to get actually 0, 4, 8, or 12 as a result back.

So, if we get this result back, okay, in binary or in decimal, it really doesn't matter, you can convert this between each other. Then, we can know that r is 4, right? So the period is 4, and then if the period is 4, we can try to calculate the x. So, it doesn't matter what we choose for an a, okay, so in this case I have chosen 13.

So what I'm going to do, I'm going to just get the r and just calculate this within the mod15, and it will give me the 4. So, if you remember, we calculate this x+1, x-1, and we find the GCDs of it, and it will give us 5 and 3 as a consequence. So, as you can see, we can use this Quantum Phase Estimation, and all this modular exponentiation thing that we have learned in order to find the prime factors. And by the way, finally, if you remember that, I said that if you don't see the connection between the modular exponentiation and the Quantum Phase Estimation, here it is.

So this is the function that we have defined. So this is more than a to the power 2 n -1, x1, 2 to the power n -2, x2, it goes like this, right? So this is what we have been doing in order to find the modular powers that we talked about in the Shor's algorithm in the first place. And, if you remember the Quantum Phase Estimation formula, it's exactly like this, right?

So that's why we are using this. So this was the Quantum Phase Estimation formula that we talked about. That's why we are using the QPE in order to find the modular exponentiation, and then we actually use the QFT dagger to get to the final result. So, maybe, it made sense to you, maybe it didn't make sense to you in this section, in this lecture, okay.

So if you actually understood the Shor's algorithm in a classical way, it would become like easier for you to understand this whole circuit in detail in the quantum way as well once the time comes. So, again, if you're learning all about this in first time, okay, if you're learning about this like from scratch for the first time, this section or this lecture might have been hard for you. Once you get some experience, once you get your hands dirty, and once you actually follow along with me for the next lecture to understand about the next steps of the quantum computation journey, I really suggest you to come back and just study this one more time from this source, from this course, or for another source as well. I'm going to share some other sources that you can look at, at the end of this course, in the next section actually.

So, again, maybe we won't even have to deal with that kind of stuff in the future, we will just use the Python libraries in order to break the RSA encryption, like I have shown you in the beginning of this course, so remember, over the beginning of this section, we have used some very simple code, and not bothered with this at all. But, anyhow, I'm going to share some resources with you on this Shor's algorithm as well, like manual implementation of the circuits that I have gotten from the Qiskit documentation itself, so maybe you can read them in your own time later on, to more comprehensively grasp this issue as well. So see you guys in the next section.
