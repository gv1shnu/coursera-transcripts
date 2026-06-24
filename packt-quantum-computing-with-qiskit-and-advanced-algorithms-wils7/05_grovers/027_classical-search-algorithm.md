# Classical Search Algorithm

- **Course:** Quantum Computing With Qiskit And Advanced Algorithms
- **Module 5:** Grover's
- **Lecture #:** 27
- **URL:** https://www.coursera.org/learn/packt-quantum-computing-with-qiskit-and-advanced-algorithms-wils7/lecture/9oZXv/classical-search-algorithm
- **Extracted:** 2026-06-22 15:24:00

---

Hi. Within this section, we're going to focus on a search algorithm. So specifically we're going to focus on the Grover's search algorithm. So what is a search algorithm?

So we need to search for something. Just assume that you have a series of numbers, like starting from 0, ending up in, maybe 50, okay. So you need to find a number over there, like 15 or 20 or 35. But, of course, they are not ordered, okay, it's a mixed list.

It doesn't just start with 1 and go up to the 50, maybe it starts with 45, then 32, then 1, then 50. I don't know, it's just mixed, okay, it doesn't go in order. So in order to find a number over there, you're going to have to just see for yourselves, you're going to have to try it one by one. So let's create a Notebook over here actually to see how the problem looks like and how the solution looks like in a regular classical computer, right, so it would be better for us.

So I'm going to name this QX08, and, it should be GroversAlgorithm, okay, or GroversSearchAlgorithm, whatever you may want to call this. So let's start this with the simple classical solution and also definition of the problem, and then we can go and do the quantum solution and quantum algorithm as well. It would be very good for us to understand this in classical way, because it's very easy to understand, by the way, it's just a list of numbers and we're just going to find the number over there, but it opens a very good horizon, it actually broadens our horizon for different kind of problems that we can solve in the real life examples as well. So let's import the standard libraries over here and just bring in the matplotlib inline as well, okay, and let's start with the classical problem and also the definition of the problem here.

So I'm going to write classical search here, okay, just to take a note, and then, as I said before, let's assume that we have a list. So I'm just going to create a random list over here, okay, you can follow along with me. So, like 5,4,6,9,1,2,3,7,8, and 0, okay. So we have a mixed list over here.

By mixed, I mean, they're not in order, they're not descending or ascending in any way, it's just random, okay, randomly ordered. So, what I want to do over here is to find the number 8. Of course, by looking at this list, you can just immediately find the number 8, but you don't know that, okay, so this list could have been like 1 million number list. And, what you're looking for, maybe it's not an integer, maybe it's a name, maybe it's like an ID, or something like that.

So remember, we're just doing this for exemplary purposes, in real life problems it would solve much bigger problems or, like in a much bigger effect actually. So we're just going to try and find the number 8. In order to do that, I'm going to create a black box or an Oracle. So we have talked about this term before, and I said that it's a function, we don't know what it does, we give some input and it produces some output.

So let's create that black box. Of course, we're going to know what it does, because we're going to create it ourselves, but, it will just make it clear for you what is a black box or an Oracle. So in this case, our winningNumber is 8, okay, we're just looking for a winningNumber in a list, and, in this list, if the number is 8, then Oracle will say that, yes, you're looking for the winningNumber, or you found the winningNumber. So, you can just return a string or return something like a response, like a Boolean, okay, I'm going to return a Boolean over here.

So I'm just going to create something called response, so it's either going to be True or False. I'm going to return that response as you might guess right now. So that is our Oracle. So I'm going to give you the number.

If that number is 8, then it will just say True, and if that number is not 8, it will just say False. So that is the definition of an Oracle. This is a function, okay. It takes an input and it gives us an output, and, of course, I'm going to do a for loop for our list over here and just apply everything into the Oracle.

So again I'm going to do the index and number thingy that we have done before. So in order to do that, of course, we need to use this enumerate function, and I'm going to enumerate the list so that we can get the indexes and also numbers in Variables. So, why I'm doing that? Because I want to show you that it will take, like maybe 9 count or 8 count, before we reach the actual number over here.

So it's going to take all the numbers, all the indexes to the index Variable, and all the numbers to the number Variable. So, I'm going to pass that number into Oracle. And, if this is True, then it means that we got the number, right, so we found the winningNumber or we found what we are looking for. So I'm going to print a statement over here with the formatted way.

So I'm going to say, "winning number index:, and open a curly brace and just write index, and just print something else, with again, formatted way. So, I will just say "execution count:, and you can actually use index + 1 over here, because index starts with 0. So why I'm doing that? Because it will just count how many shots did I take in order to find this?

And, of course, I'm going to write break over here in order to break once we find the 8 or winningNumber. So as you can see, it says that winningNumber is at the index of 8, and it took 9 counts to find this number. So, this was obvious actually. And you can say that, yeah, I can just look at it and I can just say, yeah, the 8 is the eighth index and also it's going to take 9 shots to find this.

So if you think about it, 8 could have been in the first position or the last position as well, right? So, it may take like 1 shot, but also the length of the array shot as well. So in general, if we take an average, it will become something like n over 2, right? So we can just say this is an O(n) algorithm, like it will take n times or n over 2 times to find the winningNumber or find what we are looking for in this array.

So, it happens that Grover algorithm says that, yes, classical way it can be done in n times or n over 2 times, but with Grover's algorithm, we can do this in square root of n times, okay. So it's very less, it's actually very significant improvement over here to find this in square root of n times. So, in this case, it doesn't make sense, because we only have 10 numbers over here, okay. So why would it matter to find this in 5 trials or 1 trial or 2 trial?

But again, think about like 1 million numbers or 1 million another thing to search for, then it would make much more sense. So, indeed, in the Grover search algorithm example, we're going to use four numbers, like 00, 10, 01, and 11, and it would only take 1 shot for us to find what we are looking for. And this is a very good improvement in our case, right, rather than 4 shots or 2 shots, we're going to just use 1 shot to find this. And, it doesn't find it in 1 shot, in every case, as I said before, it finds it in a square root of n, but if you just do this with like 4 numbers, or maybe like 8 numbers, it can find it in 1 shot, and you will understand it why it finds it in 1 shot and why it might not find it 1 shot.

So Grover algorithm actually increases the possibility of finding this in square root of n time. And we're going about this. Don't get confused right now. We're going to stop here and continue within the next lecture, where we'll discuss about the quantum algorithm as well.
