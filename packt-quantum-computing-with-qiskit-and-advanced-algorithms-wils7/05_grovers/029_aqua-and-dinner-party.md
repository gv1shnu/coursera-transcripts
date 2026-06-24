# Aqua and Dinner Party

- **Course:** Quantum Computing With Qiskit And Advanced Algorithms
- **Module 5:** Grover's
- **Lecture #:** 29
- **URL:** https://www.coursera.org/learn/packt-quantum-computing-with-qiskit-and-advanced-algorithms-wils7/lecture/JaDPj/aqua-and-dinner-party
- **Extracted:** 2026-06-22 15:24:21

---

Hi. Within this lecture, we're going to actually continue seeing the Grover's search algorithm, but this time we're going to see it in a way that we're going to actually implement this in a real life problem, and we're going to do it in an easier way. So, remember, when we talked about the Qiskit for the first time? I said that there are a couple of modules that you need to know about, and one of them was the qiskit-aqua.

So aqua is Quantum Algorithms & Applications module of the Qiskit. As you can see, it says DEPRECATED over here since April 2021. So DEPRECATED means that it will be replaced by a newer method or newer module or newer function, newer class. So, there would be a better way to use this in Qiskit generally.

So I'm going to show you how this works. But right now, when I'm shooting this video, even though it's DEPRECATED, this is still working, and the newer version is not working for some reason, I'm going to talk about it, don't worry about it, okay. So when you're watching this, you will be able to do what I'm doing. Don't worry about it.

So what is qiskit_aqua? They actually provide some algorithms, and they make it automatic to just write a couple of Python codes, like a couple of lines, and it would create a circuit for us, so that we wouldn't actually go ahead and create the circuit from scratch or try to adapt the circuit in a way that it actually serves our purpose, and it creates a layer of abstraction generally. And indeed, this is going to be the way that many of us will be using the quantum computers when they become available to general public, like in maybe 5 years. So they will have these libraries, and we will just give some inputs, and we will take the outputs from the circuit measurements without even having to create the circuits.

So, if you think about it, we don't actually deal with gates when we generally write some code in classical computers, and, it's going to pretty much be the same in the future for the quantum computers as well. So, over here, I have found some Migration Guide. So what is the Migration Guide? It actually leads us to the replacement of the aqua module in the future.

But as I said before, even though we can actually see this clearly, like what we should do or what we should have done in the previous modules, so it's clearly stated over here, but, in fact, it doesn't work right now. So I have found the bug in the codes actually, I have understood what was wrong with it, and I have submitted this issue to the Qiskit, and I tried to contribute to the Qiskit ecosystem. So, in future, I believe they will fix it, and we will actually update this lesson to run this on the latest quote, but right now it doesn't work. So, I'm going to show you the aqua module, and it will say it's DEPRECATED, but don't worry about it, it will work anyway.

So, I'm going to create this Python Jupyter Notebook and call this DinnerParty. So why we are calling this DinnerParty? Because we are going to talk about a dinner party, and we want to actually call some guests or invite some guests to our party. However, of course, we have some constraints.

We want to have as many as possible guests over here. However, some of the guests are like in a fight or something like that, they don't want to talk with each other, so we have to just take this into consideration when we invite them. But again, the end goal is to have as many as guests as we can have on this dinner party, okay. So we can solve this problem with Grover's algorithm as well.

And we're not even going to create a circuit or some other thing for this purpose, it's going to be with the aqua, with the layer of abstraction that we have been given over here. So, let's see our example. Of course, I'm going to go with my favorite band, which is Metallica. So it says that we can either invite JAMES AND LARS, OR KIRK AND ROB, and we have another constraints, AND NOT LARS AND ROB.

So, if it was JAMES AND LARS, OR KIRK AND ROB, then it would be very easy for us, because we would just invite them all, because we can actually invite JAMES AND LARS, OR KIRK AND ROB. And if we invite them all together, then it won't matter. But we have a constraint over here, okay, it says that AND NOT LARS AND ROB. It means that you cannot invite LARS AND ROB at the same time.

So, this problem is very easy. You can actually see the result for yourself, you can just think about it, and you can find that, yeah, I can just invite JAMES, KIRK AND ROB, or JAMES, LARS AND KIRK, but not LARS AND ROB together. Okay, so we have two main alternatives to invite. So far, so good.

But, if it was like a very big data, then we would have to just go along and try to determine every possibility. So, we're going to do this, like using Grover's search with quantum computers, and it would be very easy for us to do. So, right now, I'm going to import the aqua.algorithms as well, and we are going to import Grover. So, as you might have guessed, we have other algorithms over here, like Bernstein Vazirani, Shor's, we're going to see Shor's in the next lecture, and other ones like Deutsch as well.

So I'm going to import this LogicalExpressionOracle, we're going to talk about what it is. And finally, I'm going to import the tools.visualization as usual. So, I'm going to import the plot_histogram from here. So I believe we have to do this matplotlib inline as well, and here you go.

So aside from the Qiskit and the regular plot_histogram, I imported two things, first of all, the Grover itself, okay, so this is the ready to go circuit that has been created for us, and something called LogicalExpressionOracle. So it happens that they created a LogicalExpressionOracle, and we can try to make this constraints or like LARS AND ROB, KIRK AND JAMES, something like that, into a string, and just feed it to the LogicalExpressionOracle, okay. So what we're going to do, we're going to try and write this expression like this constraints in an expression, in a string. And there is a way to do that.

So this LogicalExpressionOracle is built for that purpose. If you have used something like regular expression or regex before, it's something like that, but this is just to write the logicalExpressions rather than regular expressions. So let me show you what I mean. First information that we have over here is '(James & Lars)'.

So, all you got to do is just write it like that, and then we have an OR, okay, let me put the OR sign over here. So OR sign is this piping sign. You can do this with Alt and dash or option or dash on Mac on your keyboard. Of course, it depends on the keyboard.

You're going to have to just come up with this yourself. So, the other one is (Kirk & Rob). So JAMES AND LARS, OR KIRK AND ROB. So I have literally written this down in the string.

But now, I have to write this as well, AND NOT LARS AND ROB, okay. So if this was the case, then we would have just invited them all. So I'm going to just close the parenthesis over here, okay, and do the not sign. So I'm going to do &, and in order to do the not, we're going to have to use tilde.

So how do I know even to use the tilde in this case? Of course, I have looked this up from the documentation, otherwise, I wouldn't have known. So I have looked it up from the Qiskit documentation. I went into the LogicalExpressionOracle page, and I've seen that it should be & tilde, if I want to express this Lars & Rob thing.

So what I did was to just write this in a string, okay. So, it happens that I can create the groverAlgorithm over here by saying that Grover, okay, so this is the class that I have imported. So, I can say Grover and ask for some LogicalExpressionOracle. So, in this LogicalExpressionOracle, I'm going to specify my own logical expressions.

So, that's it. So if I hit Shift Enter, as you can see, it says that this is going to be deprecated, so better you shift to the newer version. But again, the newer version doesn't work at this point, so sorry about it. So, if they fix it, I'm going to just update this, and you can see the newer version as well.

But it's not that different. Again, it's a couple of lines in Python, and it will give us the same result back. So, over here, I have created the groverAlgorithm. Now, as you can see, I didn't create a qubit, I didn't create a classical bit.

All I did was to say groverAlgorithm = Grover and this logical expression. So let me get the simulator from here, and I'm going to just get the result back, not by saying execute this time, because I don't even have a circuit, all you got to do is just say groverAlgorithm.run and just specify the backend that you want to run this on. So, once you do that, it will be executed on the backend. Again, you can get these deprecated messages, it doesn't matter.

Now I can come over here and print the result. So as you can see, result is kind of a dictionary over here. So this should be the key, and, the key measurement gives us some value. So let's try to find the result["measurement"] over here, okay, to get the measurement results, because this is a dictionary.

And as you can see, these are our results. So what I want to do, I want to give these results to the plot_histogram, so that we can actually see what's going on over here. So, here you go, these are our results. Of course, if you don't know how to read this, it would be very hard for you to understand this, but these are actually in reverse order, of course, but also they are here like alphabetically.

So if you come over here, you can see how they are actually ordered alphabetically over here. So, what do we have over here as the first one, so let me write this. So we have James - Kirk - Lars and Rob, right? So this is our alphabetical order, J, K, L, and R.

So, in the first bit, or in the first probability over here, we have this James, not Kirk, Lars, not Rob, okay. So we skip the Kirk, because it's 0, and we go to the Lars, and then that's it, we skip the Rob as well. So if you look at the second alternative, we have James, Kirk, and Lars, okay, not Rob, because we cannot call Lars and Rob at the same time. So, in the third alternative, we have Kirk and Rob over here, okay, and in the final alternative, we have James, Kirk, not Lars, but Rob.

So, here you go. As you can see, we can actually see that the James - Kirk - Lars alternative is the way to go, or the James - Kirk - Rob alternative. So we have two alternatives over here, because these are also alternatives, but we want to actually invite as many guests as possible. So in this case, we have two alternatives.

And, of course, this was a very easy problem to solve, and again Grover algorithm makes it like in one shot in this case, but if we had like a much bigger data, then it would take much less with the Grover's algorithm than the classical computer itself. So, again, this is a very good implementation of solving a real-life problem in a quantum computer. So, this aqua module and its newer versions in the qiskit-terra itself are going to be very popular among the quantum computations and quantum computer scientists in the future as well. Great.

Now, I believe we are ready to finish this lecture, and before we finish this, I want to show you some Easter egg. As you can see, I'm the guy in the middle, and I have managed to invite them all to my dinner party. So if you're a Metallica fan, I believe that will do some good for you. Now, we're going to stop here and see you in the next lecture together.
