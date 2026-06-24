# Linear Transformation

- **Course:** Mathematical Foundations And Quantum Mechanics Essentials
- **Module 2:** Mathematical Foundations
- **Lecture #:** 11
- **URL:** https://www.coursera.org/learn/packt-mathematical-foundations-and-quantum-mechanics-essentials-bmddx/lecture/y21nu/linear-transformation
- **Extracted:** 2026-06-22 14:45:27

---

Hi. Within this lecture, we're going to finalize our matrices by learning about something called linear transformation. But before that, we need to learn about some special terms about matrices as well, first of which is the Unitary Matrix. So we call a matrix Unitary if the X Adjoint is equal to X inverse, so X being a matrix, obviously.

So what's the Adjoint, you remember the Adjoint, it's the Transpose and Complex Conjugate of a matrix. So you either take the Transpose first or the Complex Conjugate first, and then apply the other one. So, if you do this, and if you just find it, that it is actually equal to X Inverse, then it means that you have a Unitary Matrix. So, it actually means that if you multiply an X by its own Adjoint, you will get the same result with X multiplied by X Inverse, which is Identity Matrix, obviously, right, because we have seen this before.

So let's consider this first matrix. So how do you get the Adjoint of this. Of course, you draw a diagonal, and then you can switch the left hand side with the right hand side, right. So, as you can see, the elements over here is 1 over square root 2, and if you switch it, nothing will be changed, and if you just change the Complex Conjugate, if you apply the Complex Conjugate, then it won't change anything, because we don't have any major number over here.

So if you just do this multiplication, you will get 1, okay, just 1 over 2 + 1 over 2 will give you 1, and then you will get 0 if you do the following, and it's actually the Identity Matrix, as you can see, right? So this is the Identity Matrix that we are talking about. So we call this X multiplied by X Inverse, and this is equal to Reversible, this is equal to Identity Matrix. And, this represents the Reversible Operations in quantum computation.

So we're going to be dealing with this a lot. So we're going to be dealing with matrices a lot, as I said before, and we will need to understand that we are going to be dealing with Reversible Operations and Unitary Matrices a lot. At least we have to know the term of this, because we will need to reverse the operation sometimes, for example, putting into a superposition and then just taking out of the superposition. So, another matrix term that we need to know is called Hermitian Matrix, and this is true if X Adjoint is actually the X itself, okay.

And this represents the Irreversible Operations, so you cannot reverse this operation. So, let's take the Adjoint of this matrix, for example, okay, so we have this, and remember, this can be a + sign or a dagger sign. So if you draw the diagonal over here, if you switch this to 2+i with each other, and then you change the sign, then you will get the same thing, right, we just make the Transpose and then we change the Complex Conjugate, we change the signs of the imaginary parts. So this is Irreversible Operations, and we will see that kind of matrices as well in the upcoming lectures.

So for right now, it's actually enough for you to know about the Irreversible Operation is actually the Hermitian Matrix, and the Reversible Operations are Unitary Matrices. Okay. So, of course, these are just terms, and you're seeing right now, and maybe you're thinking how we're going to actually implement this in quantum computation, again, we will come there, we're just learning about the background right now. So another very important concept is called a Column Matrix.

So this is only a column, okay, it has multiple rows, but it has only 1 column. So we call this Vector in quantum computation. Okay, so maybe you have learned about the real vectors in Physics in high school or in maybe college, but we're not talking about that vectors. When we say Vector in quantum computation, we mean a Column Matrix.

Okay. So we're going to talk about state Vectors, Vector states, and so much and so forth when we go into the qubits, and when we say Vectors, we are actually saying a Column Matrix, okay, we will represent the possibilities or probabilities actually qubit can have, we will represent all these values into one single Column Matrix, and this is one of the examples. Okay, so these are all Column Matrices. Now we generally won't see like 2 rows, but 3 rows, 2 or 4 will be much more in common, but a Vector is a Column Matrix.

So, where does the Linear Transformation come into play. So, let's talk about this a little bit, let's say that we have an x axis and a y axis, like we used to see in high school. Okay, so of course, we can represent some dots like x1, y1 and y1 being here, x1 being here, right? So you know this stuff, this is just a y and x axis, and this is the same way for the x2, y2 as well.

So, of course, we can write a formula to just make the x1, y1, into x2, y2, right? So this is called Linear mapping or Linear Transformation, I'm just showing you the wikipidea.org. Of course, you don't have to just open this, but just so you know, this is not only for quantum computation, this is also for general mathematics. As you can see, we can see the vectors going to some other place, going to some other coordinates, other x and y in the x and y axis, okay, and this is called Linear Transformation.

So, what happens over here? So we go into something new, right, x2, y2, and we can obviously formalize this with some coefficients like A B C D, right, so this should be equal to Ax1 By1, Cx1 Dy1. Okay, so x2, y2 being the points that we have landed later on when we applied this transformation. And it happens that, we can actually represent the same thing with column vectors, column matrices, the column matrix over here, x2 y2, and x1 y1 was our initial point.

And if we just multiply this with the matrix, over here A B C D, okay, we don't know the values yet, so, it really doesn't matter. But as you can see, if you just do this calculation, it will give you this, right, x2 =Ax1+By1, y2=Cx1+Dy1. So it actually transforms some vector into another state, and this is what we're going to be dealing with a lot during the quantum computations. So if we come over here, you can see the rotation formula, right?

So this is again a formulation. So if there is an angle over here, like alpha, you can calculate that angle by a given formulation in Geometry. This isn't something that we're going to be deep diving during quantum computations, but just so you know, these are the values, these are the formulas, okay. So, for example, if we take 1, 0 as xy, x1, y1, okay, so this is our initial state, and just consider that we are taking this vector from here to an angle that is 45 degrees, okay.

So we are trying to just transform this vector into that state. So this should be the formula, okay, 45, cos(45) -sin(45) +sin(45) and cos(45) for here. Maybe you don't even know the values of those, it really doesn't matter, you can just go and google it. Okay, so, it should be around something like 0.7, that if you do this calculation, then you're going to get the same result that I'm getting over here.

So again, we're not going to do this with cosines or sines later on in the quantum computation part, I'm just showing you that this kind of formulation exists, and this is how we transform, this is how we do a Linear Transformation, Linear Rotation over here. We're going to be dealing with this kind of rotations in qubits all the time, because we will have a state, okay, a state vector representing some number, like 1 or 0, and we're going to transform that state into another state. This can be anything between 1 and 0, because qubits don't actually hold the 1 or 0 like bits, okay, it can be just between these two numbers, and we transform that vector state into some other vector state by using that kind of matrix multiplication. So, that's what I'm talking about.

We're going to be dealing with this a lot. Okay. Even though we're not going to do the mathematical computations by hand manually, when we go into the Qiskit, Python will do it for us, obviously, you should know that we are actually doing this kind of transformation when we deal with quantum gates and quantum bits. So, that is why we have learned about the matrices in this section.

And that's it for the Math fundamentals. We're going to stop here and continue within the next one.
