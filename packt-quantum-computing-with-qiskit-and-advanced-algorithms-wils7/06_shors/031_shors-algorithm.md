# Shor's Algorithm

- **Course:** Quantum Computing With Qiskit And Advanced Algorithms
- **Module 6:** Shor's
- **Lecture #:** 31
- **URL:** https://www.coursera.org/learn/packt-quantum-computing-with-qiskit-and-advanced-algorithms-wils7/lecture/lohBh/shors-algorithm
- **Extracted:** 2026-06-22 15:24:41

---

Hi. Within this section, we're going to focus on the Shor's algorithm. So this algorithm is very important to us, because not only it actually proves that quantum computers can outperform the classical computers in a massive way, but also it will definitely change our lives in the upcoming years. Why is it so?

So, with using the Shor's algorithm, we will be able to find the prime factors of large numbers. So, of course, it doesn't make sense to you if you don't know anything about encryption and the security of the communications that we conduct in the Internet. So when we use Internet, when we do some requests and get some responses, so many of the encryptions are conducted in a way that it actually relies on defining prime factors of a large number. So the encryption that I'm talking about is called RSA, okay.

So it happens that RSA relies on the idea that you cannot easily find the prime factor of a large number. So finding a prime factor, what is it? It's literally finding a factor of a number, it has to be prime, okay. And it's very easy for, like, small numbers, for example, in the case of 60, you can actually find the prime factors with thinking it a little bit.

For example, what is the prime factor of 15? So, 3 multiplied by 5, right? So 21 is 3 and 7, right? So you can easily understand how to find the prime factors of the small number.

But it's very hard for a large number. Think of a number that counts as 256 bits. How can you even find the prime factor of that number, right? It's very hard.

But if I give you two numbers, if I say that if you multiply it, you will have that 256 bit number, you can easily verify that, right? You can just multiply that with a calculator and you will immediately see the result. But it will take you so much time, so long time to find the prime factor of that particular long number. So the RSA encryption relies on that.

If you want to break the encryption without having the key, then you're going to have to find the prime factor of a very large number. And in classical computers, it can take thousands of years to find this, okay, thousands of years. That's why we are safe right now in the Internet, that's why somebody cannot actually break our encryption in a such simple way, so that they can eavesdrop on our communications and stuff, that's why our credit card purchases are safe right now. But it will change if we have a quantum computer that can have so many qubits.

So right now, we can actually run the Shor's algorithm to break down and find the prime factors of small numbers in the quantum computers. However, as we know that quantum industry is also improving in a fast way, and once we have like error-free qubits, or at least improved qubits rather than the current situation, and also have quantum computers that have many qubits in the future, then we would be able to break the RSA encryption in like less than a minute, rather than thousands of years, and, it would wipe out all the security in the Internet. So it's very concerning, and it's also very real, okay. So, many of the industries and many of the authorities started to think about post quantum computing encryptions as well, so that they would come up with an encryption that cannot be cracked by the quantum computers that easily.

So right now, the encryption breaking process in the classical computing is all 2 to the power n, so it's exponential. So if you have 256 bits, for example, it's 2 to the power 256. So it's going to take lot of years to break that encryption in a classical computer. However, the Shor's algorithms make it in a way that it's not exponential, okay.

So if you increase the number of bits or increase the length of the number, it wouldn't actually increase the amount of time that we need to break it at least exponentially. So, it would be very fast in quantum computers, but it won't be very fast in classical computers. That's why we are safe today, and that's why we're not going to be safe in the future. So, what we're going to do during this section, is try to understand how Shor's algorithm work, both classically and in a quantum way.

And, in fact, it's very easy to use the Shor's algorithm using aqua or any other modules, and I will show you all of that. So, first of all, we need to start with the modular arithmetic, okay. So we will need to revisit our Math foundations one more time. We haven't seen the modular arithmetic in the Math section, but I believe you know this from high school.

So if you remember that 3 = 26 in the mod 23. So what we do over here, of course, we divide 26 to the 23, and we write the remainder over here, okay. So it's kind of finding the remainder in this current mod. So it's the same for 20 and 43, it's the same for 1 and 24 over here, and it's the same for 22 and -1 as well, okay.

They are equal in the mod 23. So, what does it do to us, right, so what does it have to do with Shor's algorithm or finding the prime factors? Don't worry, we're going to come over there. So, all you need to know about modular arithmetic is that you can actually use this in the operations as well.

For example, if you want to add this 46 to 18, if you're doing this in mod 23, then you can just add 0 with 18. So it actually makes you very easy for this kind of operation, right? Rather than trying to multiply this or add this together, you can just do the mod once and then go ahead and do the operation later on, because eventually it will give you the same result. So it's actually same for multiplication over here as well.

As you can see, it's hard to just multiply these two numbers together, but it's very easy for you to just get this mod 23 and know that it's going to end up in 0, in mod 23. So, as you can see, modular arithmetic makes it easier for us to do these kind of operations. But that is not the main reason that we use it in the Shor's algorithm. Don't worry about it, I'm going to show you how to find the prime factors of numbers in general.

I'm going to show you a magical formula that we will be using in the Shor's algorithm, in a little bit. But before that, you need to know about this concept as well, so GCD, and this is called greatest common divisor. I am sure you have seen this in high school or even before that. So we are trying to find the greatest common divisor between two numbers, for example, and it's very easy to do in the small numbers as well.

If you look at over here, for example, in the GCD of 15 and 21, you can just make 15 into 3 and 5. For example, in the 21, you can make it into 3 and 7, so these are the factors of the 15 and 21. So, the greatest common divisor among these numbers is 3, okay. So we're going to do other examples here as well, but let's try to find the prime factors of 21, using this GCD and also modular arithmetic that we have seen, that we have learned right now.

So, N is the number that we want to find the prime factors, and you can easily see that the prime factors will be 3 and 7. But let's just wait here for a moment and just do this mathematically, because we want to come up with a formula to find this generally, okay, not only for small numbers, but also big numbers as well. First of all, I'm writing this, x to the power 2 = 1 in mod 21, okay, so I want to find that x, x to the power 2 = 1 in mod 21, and mod 21, because I'm trying to find the prime factors of 21. So, what can x be?

It can be 1, obviously, and also -1 as well. But it can be so many things, because we are working with inside of a mod, right, modular arithmetic. You can just write 8 over here, 20 over here, 13 over here, -8, something like that. So, there are a couple of other things here, if you think about it, you can find.

So, how do we use this? Let's choose a number from here, right, for example, 8. So, we can write this as 8 to the power 2, - 1 to the power 2 equals to 0, right, because of this. And this is actually equals to 0 in mod 21, if you calculate it, it's 64 - 1, 63, and 0 in mod 21.

And I've chosen this 8, like a random number, okay. I could have chosen 20, 13. We're going to talk about it, I have just chosen this randomly. So, over here, we can write this equation like (8 -1) * (8 + 1), right, because that's how it goes, a squared - b squared, we can write it like this.

So if we take this equation, (8 -1) * (8 + 1), and if we try to find the greatest common divisor of 21 between 8 - 1 and also greatest common divisor of (21, 8 + 1), then it's going to give us 3 and 7. So, 3 and 7, what are those? As you can see, this is 7, and the above one is 3. So these are the prime factors of 21.

So maybe you didn't even understand what you were doing, right? So I didn't expect to see this actually when I first learned about this, because, how would I know that this will lead us to the prime factors of the number that we are looking for? We are trying to find the modular arithmetic of something, we're trying to find some common divisors, and then we end up with these prime factors. It works.

So why does it work? We are going to have to think this through a little bit. It has to do something with the periodicity. So I'm going to tell you what it is, but let us just write down the general rules, the rules, the ground rules of this.

So first of all, it shouldn't have to be - or +1, the x, because it wouldn't make sense, it will just give us 0, and it should be equal to 1 in the mod, and then we will just get the greatest common divisors of this, right? That's exactly what we have done. But, let's see how it works in real life, and we will also have one more rule to follow up on that. So, we are trying to find the N over here, and just choose a random number, okay, a random number, 2, 3, 4, 5, we're just choosing a random number.

So I have just chosen 2. So we are taking powers of 2, okay, and we are writing them inside of modular arithmetic. So, 2 to the power 5 equals to 32, and it's equal to 11 in mod 21, of course. And, over here, 2 to the power 6 equals to 64, and it's equal to actually 1 in mod 21.

And then it goes on and on and on. So it kind of goes into a loop, right, 2, 4, 8, 16, 11, 1, 2, 4, 8, 16, 11, 1. So this is kind of a periodic function. It increases and it comes back down, and then it increases again, and it exactly follows the same rule, it follows the same loop.

So we can say that this is a periodic function, and the period over here is 6. So in each 6 loop, it goes back, right? So 1, 2, 3, 4, 5, 6. So we are trying to find a period of this function in this case.

And it happens that if we find this 6 over here, we can try to write this like x to the power 3 squared. So why I'm writing like this? Because, as you might remember, we are actually trying to find the x to the power 2 = 1. And in this case, x being x to the power 3, we can write it 8.

So 2 to the power 3 is 8. That's how we actually found this, okay. And again, we have chosen x to be 2, just by random, okay, we just came up with 2. And how lucky is that, right?

Is it lucky, did we get lucky? If we had chosen something else, is there any chance that we find this period? It happens that, yeah, we got lucky, but also it happens that we're going to get lucky for 50% the time. So if we try to find this module or the prime factors of n, then, we just take a random number and 50% probability.

We're going to find this solution, okay. And in here, I found this or the period to be 6, and we managed to write like x to the power 3 squared, right, because we're trying to find that x to power 2 =1 thing. So if the period wasn't an even number, then I couldn't actually divide it into 2, right, this has to be an integer. So, another rule that we should add to our ground rule is this period number, 6 in our case, should be an even number, okay, we would be able to divide it into 2.

If it wasn't, then we would have chosen another random number and just take its numbers, and try to find its period and see if that gives us the solution back to us, okay. So this is called a magic formula by many scientists, because, you first see this, you wouldn't actually understand that we're going to find this factorials of the 21 or prime factors of the 21, by just choosing a random number. But in the end, you find this, okay. And, of course, you may not find this like in your first trial, because you're doing these things randomly.

But again, there is a very high chance that you can find this. So this is how we are going to use the Shor's algorithm and also the quantum solution as well. However, we can do this, we can try to come up with an algorithm in the classical way to understand this much more comprehensively, right, because this is fun, this is how you actually improve your mathematical skills as well. So you can try this with 21, like in 15, in 60, you can try this with any small number.

But if you try this with 256 bit number, then it's going to take thousands of years in the classical computers. And, in order to understand the quantum solution, we're going to have to deal with this Fourier transforms or something. We're going to see what it does in the upcoming lecture. But for right now, I just want to show you some classical algorithm, maybe it would make you understand this in a much more easier way.

So, I got this from the Qiskit documentation or training guides. So, it's very easy to write this in Python. So I'm just going to show you this. As you can see, it actually displays this period to you visually as well.

So, let me just show you whole code over here, because it's very easy. We are trying to find this N, the prime factors of the 15, and the random number we have chosen is 13 in this case, okay. So you can try this with another number as well. So, over here, we are actually importing math and matplotlib in order to visualize everything over here, and also something called numpy.

We generally use this in data science, but it's also used for getting the numbers like Pi and trying to work with arrays and stuff. So, we are just importing the libraries that we are going to use during this code. So, over here, for example, you can call the gcd by saying that math.gcd and find the GCD between two numbers. So what we are doing here is very basic actually, we're trying to create a list of N and we are trying to get this a to the power z.

So we're taking this a to the power for each number that we have in this range, and taking the remainder of N, we are writing this in the mod N, and we are just doing in a loop, so that we can see the periodicity over here, okay. So if we visualize this with mpl, as you can see, it goes and on and on, and it actually comes back for every for loop. So, we know that period is 4 in this case. Of course, we can get this period by calling some easy function over here, okay, but you can see it from the chart as well.

So we called period(r), so that is the general notation of the period, and we can just see it from here as well. So, after we get the r, after we get the period, first of all we check to see if it's an even number, okay. Because remember, we need to write this as like this. So x squared, it needs to be an even number.

If that's not the case, then we print out 'r is odd', okay. But if that's the case, then we're going to try and see if we can just take the GCDs of x+1 and x-1, and, if we can get the numbers, if we get the prime factors out of this. So, it's very easy code, so, it's not about quantum computing. So I just taken this code from the Qiskit tutorial and I have just modified this a little bit, in order to show you this.

So you can try this with another number. As I said before, you can just change this to be 21 and 2, for example, and just hit Shift Enter or Kernel Restart, in order to see how it goes like. Let me do Shift Enter, Shift Enter over here. And, as you can see, the period or the function is completely different in this case, so, the period should be something like 5 4 6, yeah, here you go, and, it gives us the prime factors here like 3 and 7, and that is correct.

So, this is good. As you can see, the algorithm works. We can find these prime factors over here, but in order to understand the quantum computing way or quantum implementation of this, we need to understand some much deeper concepts than we have learned before. So we're going to stop here and learn about these concepts in the upcoming lectures together.
