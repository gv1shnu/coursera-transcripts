# Hashing Names

- **Course:** Data Structures
- **Module 4:** Hash Tables
- **Lecture #:** 38
- **URL:** https://www.coursera.org/learn/data-structures/lecture/KKYUc/hashing-names
- **Extracted:** 2026-06-20 21:40:36

---

Hi. In the previous video, we finally completely solved the problem of mapping efficiently from phone numbers to names. Now it's the time to map efficiently from names to phone numbers. We're going to use chaining scheme again, but we need a hash function for names.

Actually, we're going to generalize it and to learn how to hash arbitrary strings of bounded length. Also, by the end of this video, you will learn how string hashing is implemented in Java. This is actually a function that is used probably trillions of times per day. First, let's introduce some notation.

For the length of the string, we denote by absolute value of S, the length of string S, for example, length of string edx is three because there are three characters, e, d, and x. Also, length of ucsd is four, and length of chaining is eight. Now, given a string, we need to compute its hash value. With phone numbers, we just converted them to integers first and then computed some function on the integers.

There is no such obvious way to convert a string to an integer. We're going to use actually the characters of the string to do that. If S is a string, then S of 0, S of one, and so on, up to S of length of S minus 1 are individual characters in the string S. We can imagine that the string is just array of characters.

We should use all the characters in the hash function. Otherwise, there will be a lot of collisions. For example, if we don't use the first character of the string, then for any of the strings, aa, ba, and so on, up to za, the hash value will be the same because it doesn't use the first character, and that is the only thing that changes between these streams. The hash value will definitely be the same.

That's bad because these guarantees us a lot of collisions. We need to somehow use all the characters when we're computing the hash function. Before computing hash function, we're going to convert each of the characters to integer. To do that, we can use some encoding of characters which is actually already built-in into the computer, like ASCII encoding or Unicode, depending on what our string consists of, which characters are those.

Then we're going to also choose a really big prime number B. We're going to compute something module of this number b, and that will be our hash function value. Now, we just present the following family of hash functions called polynomial family. Within this p is a prime number, consists of hash functions parameterized by one parameter x.

Where x is just the remainder modulo p between one and p minus 1, x is just the remainder. To compute the hash value for any string, S we compute a polynomial modulo p. This polynomial is the sum of character at ith position multiplied by x to the power of i, and all these with some modulo B. Let's consider the code to compute this hash function and an example.

The code to compute this function is really easy. It's called PolyHash and it takes string S, prime number p, and number x as inputs, and it returns the hash value of the hash function from this polynomial family parameterized by x. We start by assigning zero to the hash value. Now we go from the back of the string to the start of the string from index length of S minus 1 down to zero.

At each step, we multiply our hash by x and after that, we add the code of the character S of i, and we take the result modulo p. In the end, we return this result as a hash value. What will happen in practice if the length of the string is three? First, we start with assigning zero to the value of the hash, then we start from the end of the string, and the last character of the string is the character S of 2.

We're going to assign hash is equal to hash times 0 plus S of 2 modulo p. Hash times 0 is 0. Then we add S of 2 and take modulo p. The result is equal to S of 2 modulo p.

Now, we are going to make another iteration of the for loop. To do that, we multiply our current hash value, which is S of 2 modulo p. When multiplied by x, we get S of 2 times x. Then we add S of 1 and we get S of 1 plus 2 times x modulo p.

The last iteration, we're going to multiply the current value of hash by x again. We will get S of 1 times x plus S of 2 times x squared. We're also going to add S of zero to that. Then we got S of 0 plus S of 1 times x plus S of 2 times x squared modulo p.

This is the general way how our hash function looks like for the string of length three. If it was of length four, then the value would be also plus S of 3 times x to the power of 3, and so on, so forth. The method hashCode in the built-in Java class String is very similar to our PolyHash. It just uses constant x equals to 31, and for technical reason, it avoids the modulo p operator.

Everything else is the same. Now we know how the hashCode method of the String class in Java is implemented, and actually, a String is a very popular class and hash tables are a very popular data structure. This function is probably again executed trillions of times a day. Now you know how is it implemented.

Another question is why is it implemented this way? This is because the polynomial hash family is a really good family of hash functions for strings. In the next video, we're going to analyze why is that so and finally, solve the second part of our phone book data structured problem for mapping from names to phone numbers.
