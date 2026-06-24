# Improving Running Time

- **Course:** Data Structures
- **Module 4:** Hash Tables
- **Lecture #:** 43
- **URL:** https://www.coursera.org/learn/data-structures/lecture/h4ZLc/improving-running-time
- **Extracted:** 2026-06-20 21:41:29

---

Hi? In the previous video, we came up with a recurrence equation for the hashes of the substrings of the text. Now, we're going to use this recurrence equation to greatly improve the running time of Rabin-Karp's algorithm. The idea is to use precomputation.

First, we use the recurrence equation to precompute all hashes of all substrings of the text T of length equal to the length of the pattern, and then we proceed the same way as the original Rabin-Karp algorithm. Instead of just computing hashes of substrings on the way of the Rabin-Karp's algorithm, we first precompute them, save them, and then use them to compare to the hash of the pattern. Let's see how the pre-computation works. This is the function precompute hashes, which takes as input to the text T.

The length of the pattern P doesn't even need the pattern itself, the prime P, and some number x, which is the generator of the polynomial hash function. We initialize the array H, which will contain the hash values of the substrings. It will be having length of T minus length of P plus 1 because this is the number of substrings of T which have the same length as the pattern P, and we initialize string S with the last substring of the text, which has length equal to the length of the pattern, and then we just compute the hash value for this particular substring of the text directly using our polyhash procedure. We know that the polyhash procedure needs time proportional to the length of the string S, which is equal to the length of the pattern.

This part of the algorithm works in time with O of length of the pattern. In the next few lines, we're going to compute x to the power of length of the P of the pattern modular prime number P. We initialize y to be equal to one, and then we run a simple for loop. In each line of this for loop, we just multiply y again by x modular P, and so by the end of this P for loop, we will have that y is equal to x to the power of length of P, modular prime number P.

This for loop has exactly length of P iterations and each operation is done in constant time, so it adds another length of P iterations. The last for loop just uses our recurrence relation. In each line of this for loop, we just apply our recurrence equation to compute H of I, given H of I plus 1, and the value of y, which is equal to x to the power of length of P modular P. We compute this line in constant time.

There are exactly length of T minus length of P iterations of this last for loop, so it gives us an additional length of T minus length of P operations. In the end, we just return the array H and we've computed it all in time proportional to length of the text plus length of the pattern. Compare that to the previous estimate of how we computed hashes of all the substrings in time proportional to length of T times length of P. This is much better instead of multiplication, we have some measurement here.

To recall that precomputing H, first we compute polyhash just once in time length of P. Then x to the power of length of P is computed also in time proportional to length of the pattern and then all the rest values of array H are computed in time length of text minus length of pattern. Total computation time, precomputation time is proportional to length of the text plus length of the pattern instead of length of the text times length of the pattern which we had before we came up with this recurrence equation and precomputation area. Now, suppose that we've launched our precomputation, how should the Rabin-Karp's algorithm proceed?

This is the final pseudocode for the first Rabin-Karp's algorithm. You text in the text and the pattern only, it generates a big prime number P and generates a random x integer between one and P minus 1. It initializes the list of positions with an empty list. It precomputes the hash of the pattern in time proportional to the length of the pattern.

It precomputes all the hash values of all the substrings of the text, which have the same length as the pattern in time proportional to some of the length of the text and the pattern, and then the final loop, we go through all the possible positions where pattern could occur in the text and we compare the hash of the pattern with the corresponding saved hash value of the substring. If they are different then definitely better, B doesn't occur at this position in the text so we continue, we go out of this for loop at this time and return to the next iteration. If the hash values are equal procedure on the corresponding substring of the text and the pattern to check whether they are actually equal or not. Because their hashes are equal, so with hyper mobility, the substring is equal to the pattern.

If this is the case, we add this position i to the resulting list of positions, and in the end, after the for loop, we just return this list of results in positions where pattern occurs in the text. The algorithm is pretty much the same. Just instead of computing here, the hash value of the substring, we just take the saved precomputed value being H of i, and that's mainly the difference. This difference makes a huge difference because hash value of the pattern is computed once in time proportional to the length of the pattern.

Precompute hashes, run some time proportional to some of the length of the text and the pattern and the total time spent in are equal is on average proportional to q times length of the pattern for large enough prime P, where q is the number of actual occurrences of the pattern and the text. We know that this part is unavoidable because for each occurrence of the pattern and the text, we actually need to check whether this is a real occurrence or a false alarm. In practice, the value of q will be very small because if you are looking for a gene and a genome or a word in a Wikipedia article, the number of occurrences will be probably small. That's why this algorithm can be used in practice very successfully.

The total running time on average is proportional to the length of the text plus q plus 1 times length of the pattern q plus 1. Because in theory, the pattern could occur zero times in the text. It couldn't occur at all. Then we still need to compute its hash and so on, so that's why we need q plus 1 multiplier before the length of the pattern.

This is the final running time of the Rabin-Karp's algorithm. Usually q is small, and this is much less than the running time of the algorithm, which was length of the text times length of the pattern. If length of the text is for example in billions, as in the case of genome and length of the pattern is in the order of millions, then the running time of Rabin-Karp would be on the order of 10 to the power of nine and the running time of the F algorithm will be on the order of 10 to the power of 15. It will be million times slower.

This is a great improvement indeed. To conclude our main section of the hashing, hash tables are useful for storing sets and maps. It is possible to search and modify hash tables in constant time on average. To do that, we must use good hash families and randomization to take random functions from those good hash families.

Also, hashes are useful while working with strings and texts to compare them quickly. There are many more applications, including the blockchain and if you're interested, you can see the next optional set of videos describing how blockchain works.
