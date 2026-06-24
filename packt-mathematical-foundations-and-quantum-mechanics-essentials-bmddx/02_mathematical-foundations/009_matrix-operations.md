# Matrix Operations

- **Course:** Mathematical Foundations And Quantum Mechanics Essentials
- **Module 2:** Mathematical Foundations
- **Lecture #:** 9
- **URL:** https://www.coursera.org/learn/packt-mathematical-foundations-and-quantum-mechanics-essentials-bmddx/lecture/LjuAY/matrix-operations
- **Extracted:** 2026-06-22 14:45:07

---

Hi. Within this lecture, we're going to continue with matrix multiplication, okay. And, as you can see, if we multiply a matrix by another matrix, it gets a little bit complex, more complex than what we have seen so far. But the idea over here is that, first of all, we have to satisfy some prerequisites, before we even start multiplying it, because that's how it goes, you're going to have to take the first row of the matrix, or the first matrix, okay, first row of the first matrix, and multiply it with the first column of the second matrix.

So, we're going to take 0 and 2 and multiply the corresponding numbers with 2 and 5 in the second matrix. And you can see the results are over here at the bottom. So, 0 * 2, and 2 * 5. If you add them up together, you get 10, and you write 10 as the first number in the result matrix, okay.

And then you take the same row again, and just multiply it with the second column of the second matrix. Now, this will result in 6. Now you get second row of the first matrix, and you multiply it with the first column of the second matrix one more time, and you get 11 as a result. If you do the final thing, which is multiplying the second row with the second column of the second matrix, you get 15 as a result.

Of course, adding all of those together is very easy, it's just basic Math, but you're going to have to remember this, and how it works. Okay, and the idea over here is that we started with the first row and multiply it with the first column of the second matrix. So we're going to have to think about this a little bit. Because, what happens if you don't have the same amount of elements in the first row with the second column, okay.

And as you can see, over here, we have two as columns, okay, 2 columns in the first matrix, and we have 2 rows in the second matrix. So if you think about it, number of columns in the first matrix, number of columns over here, has to be exactly the same of the number of rows in the second matrix. Otherwise, this will don't even work, right? And, if we get this two numbers over here, it will be the result of the row and column numbers of the result matrix.

So what do I mean by that? I'm going to show you some other examples, don't worry. But know that you're going to have to have same numbers of the columns in the first matrix and the same number of the rows in the second matrix, otherwise, you can't even do the multiplication. For example, over here, we have 3 * 3 two matrices, 3 * 3 over here, 3 * 3 over here.

Since I have 3 columns over here and 3 rows over here, yeah, I can multiply them, because I can just get this and multiply it with this one, and the result will be 9, and I will just write it over here. And, for as an exercise, you can just pause the video and try to do the rest on your own. Okay. And as you can see, it all gives you the same result, it all goes like this, and it leads to a 3 * 3 column at the end.

So, this 3 * 3 again is actually the rows of the first matrix and columns of the second matrix, so the remaining numbers that we haven't used before. So, let me show you more clear example over here. So, in the first one, I have 3 * 2 and in the second one I have 2 * 2. Now, I can actually multiply them, because I have 2s over here, and the result will be 3 * 2.

Why, because I will just multiply this with that one and I will just write it over here, okay, as 10, and then I will continue to do my job until I have finished the first one, right, first matrix. So the result will be 3 * 2, because, as you can see, I will continue to do this until I do the 9 8 row over here as well. So the result will be 3 * 2. Again, pause the video and feel free to complete this on your own as an exercise.

But the idea over here is that if we can multiply it, and we can just know how many rows and columns we can get as a result immediately. Over here we see another example. I have 2s over here, then I know, I can actually multiply them. And if you do the Math, you will see it will be 3 * 1, so 3 rows and 1 columns.

So, we understand if we can actually multiply them by looking at the columns of the first matrix and the rows of the second matrix, and we can understand the result by looking at the rows of the first matrix and the columns of the second matrix. Okay, that's it. And that's how you do the multiplication. Again, this is very important for quantum computing, because, basically, that's all what we're going to do during quantum computations, we're going to multiply matrices.

You can see why it is so. Don't worry about it. But right now, know that. So, another example over here can be, you try to multiply these two together, and, you can see for yourselves, you cannot actually inverse this, right?

X * Y != Y * X, because, if we just try to inverse this, we cannot even multiply them, because, it doesn't make sense. It has 2, it has 2 rows and 1 columns, the second one, and it doesn't even correspond with the first one. So, this is not equal to each other, know about that. However, the equation below holds.

If you just sum two matrices together and multiply it with another set of matrices, then you can actually do this. Okay, XQ + XZ + YQ + YZ, this equation holds. But, again, you cannot actually multiply the matrices together and just inverse it, and it won't be even equal to each other. So, there is another term you should know about the matrices, it's called Tensor Product.

And Tensor Product is not the multiplication, okay, we don't multiply matrices with Tensor Products, we do this stuff. If you Tensor Product two matrices together, then you're going to have to follow this pattern. If you see the sign, it's not multiplication, it's Tensor Product. Again, you're going to have to do this, xz, xq, yz, yq pattern over here.

For example, you can see, we're just going with the corresponding numbers one by one, xz, xq, yz, yq. And in the below example, you see, we go 1 2, 1 5, 1 7, then 3 * 2, 3 * 5, 3 * 7. And it creates like a 1-column matrix for us, and this matrix has 6 rows. So it's a little bit different than multiplication itself, but we're going to use Tensor Products as well.

So, better to know about the differences and better to know about terms, as usual. So that's it for the many operations on matrices, but we have some other important stuff about matrices as well. So we're going to stop here and continue within the next lecture, starting with the Identity Matrix.
