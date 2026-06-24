# Recurrence for Substring Hashes

- **Course:** Data Structures
- **Module 4:** Hash Tables
- **Lecture #:** 42
- **URL:** https://www.coursera.org/learn/data-structures/lecture/nYrc8/recurrence-for-substring-hashes
- **Extracted:** 2026-06-20 21:41:18

---

Hi in this video, we're going to find out a recurrent situation between the hash values of the sub strings of the text. And this recurrent situation will help us to greatly optimize the raven cars algorithm. So, we are using the polynomial hash and that is not a coincidence. This polynomial hash is very convenient to use not just for strings but for sub strings of the same string.

This is the general formula for the polynomial hash. And the idea is that polynomial hashes of two consecutive sub strings of the same texts are very similar. And we can compute one of them given the value of another very quickly. So, to ease the notation for each index i denotes the hash value of the sub string of text starting in position i, and having the same length as the pattern P by big H of i.

Now, let's look at this particular example. But, when we have a text T which is just word beach, and we encode this text using coding of letting letters to numbers from 0 to 25, so that letter a goes into zero, letter b goes into 1, c goes into 2, and so on. Then we get the code of 1, 4, 0, 2, and 7. This is just the encoding which is later used to compute the polynomial hash value because we cannot compute based on characters.

We can compute based on the codes of those characters. And also let's assume that the length of the pattern is 3. So we need to compute the hash values for all the sub strings of the text T of length 3. Let's first look at the hash of the last sub string of length 3, which is ach.

So we know that this is a polynomial hash. So, it will have some coefficients for 1 x and x squared. Because the length is 3, so it will have degrees of x from 0 to 2. And the coefficients will be correspondingly 0, 2 and 7.

So we'll get zero plus 2 times x, plus 7 times x squared. And this is the hash of ach. We just we'll need to take a module b but we'll avoid writing module beyond the slide to ease the notation. Now let's look at the hash value of the previous sub stream of length 3 which is eac.

It will also have some coefficients before 1 x and x squared. And the coefficients will be 4, 0, and 2. So the hash value will be 4 plus zero plus 2x squared, module b but we avoid writing module b here. So what we can notice is that the last two terms of the hash polynomial for eac are the same as the first two terms of the hash polynomial for ach multiplied by x.

So we need to multiply each of the terms by x from the first hash venue and will get the last two terms of the second hash value. And this is not a coincidence. This is a property of the polynomial hash function. And let's see how we can use it to derive a recurrence equation between those hash values.

So, big H of 2 is the hash of the sub string starting at position 2 which is ach in which is equal to zero plus 2x plus 7x squared module b. And big H of 1 is the hash value for eac which is equal to 4 plus zero times x plus 2 times x squared. And you can rewrite that as 4 plus x time the first two terms of the big H of two, which is zero plus 2x. And now we can write that again as 4 plus x times the whole hash of ach, zero plus 2x plus 7x squared.

And now we need to subtract the term that we added which is x times 7x squared, which is 7x cubed. So we subtract 7x cubed. And in the end, what we get is that big H of 1 is equal to x, times big H of 2. And plus 4, the first term of the new H, and minus 7 times x cubed.

The term that we signed and we need to subtract back. So this is the general way it works. To compute the previous hash, we need to compute the next hash multiplied by x, and then add one term and subtract one term. And if this is true, then it seems that we can compute previous hash based on the next hash value in time bigger of 1.

Because multiplying by x, adding one term and subtracting one term are three actions which can be done in constant time. So now let's look whether all this is true in the general station. So, big H of i plus 1 is the hash value of the sub string of the text starting in position i plus 1. And I state that the formula on the right is the correct formula for the polynomial hash of this substring indeed.

And the summation starts from g equal to i plus 1. And it means that the first term will be character T at j, which is equal to T At i plus 1. The first character of the sub stream starting in position i plus 1 indeed. And the degree of x here will be j minus i, minus 1, which is equal to i plus 1 minus i, minus 1, which is equal to zero.

So the first term is correct is T of i plus 1, times x to the bar of zero, which is 1. And then, when j goes up, j goes up, then we increase 1 by 1 the position of the character in the sub stream. And we increased 1 by 1 the degree in which x is going into this polynomial. So, this is exactly what we want.

The first character of the string is multiplied by 1, the second character of the substring is multiplied by x, third character of the string is multiplied by x squared, and so on. And, we go up until position i plus length of P. Because we started the position i plus 1, and we need the length of the substring to be exactly equal to the length of P. So we go right up to the position i plus length of P.

This is the hash of the sub string starting in position i plus 1. Now, let's look at the hash of the substring starting at position i. The formula is similar, just the summation goes not from j equal to i plus 1, it goes from j equal to i. It also goes not to i plus length of P but one position earlier than that.

And then, let's check that is also correct. We start with T of j which is equal to T of 5. And we start with x to the power of T minus i which will be equal to i minus i, which is zero. So the starting nominal is correct.

It is T of i times actually borrow zero, which is 1. And then as j goes up, we increase one by one the position of the character, and we increase one by one the degree of x, which is all correct. Now, we want to rewrite this equation. And we want to change the limits of the summation.

So, notice that instead of Jj equals to i, we write j equals to i plus 1. Because we wanted to be the same as in the previous equation. And instead of i plus length of P minus 1, we write i plus length of P. Because we again want it to be equal to the first equation.

The summation goes of the same terms. So these are equal. So, the only thing which breaks the equality and we want this equality to be true, is that we added one more term in the end, and we removed one term in the beginning. So we need to add back the term that we removed.

This is the term for j equal to i, we didn't sum it here. So we need to add it back. And it was T of j which is j equal to i, which is T of i times x to the power of zero, which is just T of i. And also, we need to subtract the term that wasn't initially here.

So, we only summed up to here in the first equation, but we sum up to i plus length of P in the second equation. So we need to subtract the corresponding term, and this is our subtraction. And of course we are subtracting T of i plus length of P, times x to the power of j minus i, where j is equal to i plus length of P. And we subtract i, and we get exactly length of P.

So, this is why we have length of P here. So now we added what we missed, and we subtracted what we added in excess. And so, this equality is indeed true. Now let's see what it gives us.

It gives us the following. If we just take this part and move it here, we don't change anything in this part. And regarding this part, we want to put x outside the brackets, and then we just decrease each degree of x by 1, exactly by 1 in the formula. So, this doesn't actually change anything because we added x before the bracket, and then we decreased each degree of each summant of x by 1.

So, this is indeed also equality. But this and the briquettes is actually exactly big H of i plus 1. So this already gives us the following recurrence equation. That big H of i is equal to x times H of i plus 1, which is this term, plus T of i minus T of i plus length of P, times x to the bar of length of p.

And everything module of p. So, this is the recurrent situation. What does this recurrent situation give us? So, we just rewrite it here too.

It will be easier to remember it. And we see that x to the power of length of P can be computed once in the beginning of the Reagan Carbs algorithm. And just saved. Of course, we're going to compute it module of P, because we don't need the x to the length of the P itself.

We just need the remainder module of p. And using this recurrence situation then H of i can be computed in constant time given H of i plus 1, and the same value of x to the power of length of P. Because we need only to multiply numbers module of P, and then add the number of module P, then subtract the number of module of p. And those are all constant time operations.

And so, using this recurrence equation, we can optimize the whole computation of the hash values of the sub strings of the text T. And in the end, we're going to optimize and improve the running time of the whole Raven Card Algorithm. To see how we do that, see in the next video.
