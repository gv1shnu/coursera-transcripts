# Rabin-Karp's Algorithm

- **Course:** Data Structures
- **Module 4:** Hash Tables
- **Lecture #:** 41
- **URL:** https://www.coursera.org/learn/data-structures/lecture/c0Qkw/rabin-karps-algorithm
- **Extracted:** 2026-06-20 21:41:07

---

Hi, in this video, we will start learning the Rabin-Karp's algorithm which uses hashing to solve the sub-string search problem more efficiently. The idea of Rabin-Karp's curves algorithm is that, of course, we need to compare pattern P will all the sub-strings S of t of length P. But we could use hashing to make the comparisons faster. Suppose we chose some hash function h.

Then if the hash of pattern P is not equal to the hash of a sub-string S, then definitely P is not equal to S. If, however, the hash values are the same and we can call the function AreEqual to check whether P is equal to S or not. We can use polynomial hash family P within this small p with some prime number p small. The main idea is that if P is not equal to S, then the probability of collision is at the most length of P or small p for polynomial hashing.

This probability can be made very small by choosing a very large prime number p. That we will only need to compare the strings themselves, only when the strings are really equal or when there is a collision, but then would happen very rarely because of the small probability of collision. That is the main idea. Now let's see how we can proceed.

This is the initial implementation of Rabin-Karp's algorithm. This is not yet optimized, but it gives you the general idea of how it works. Firstly, select P has a very big prime and number x as a random number between 1 and p minus 1. X is an integer.

This is an X to select a random hash function from the polynomial hash family. Now we initialize the resulting list of positions as an empty list. Also, compute just once the polynomial hash of the pattern because it won't change. It is just fixed and we can compute it before comparing it to any of the hashes of the sub-strings of the text.

Now it goes through all the sub-strings of the text, which can respond to D. We can view the hash of the corresponding sub-string using the PolyHash procedure from the previous video and we compare the hash values. Those are just integers. If they're not equal, we can be sure that the pattern is not equal to the corresponding sub-string.

We continue, get out of the loop. Otherwise, we need to check whether strings are equal or not because their hashes are equal and so probably P is equal to the sub-string or there was a collision. We need to check using AreEqual procedure. If there are actually equal, we append position I to the resulting list and in the end, we just return the list of all positions we found.

This is the general way this algorithm works and the main thing here is what we call false alarms. A false alarm is the event when P is compared with the sub-string S of T. But P is actually not equal to S. That's why it's called a false alarm.

Their hashes are the same, but the strings are actually different. The probability of a false alarm is the same as the probability of collision. It is not more than the length of the pattern over the big prime number P. On average, the total number of false alarms will be the number of iterations of the for loop, which is the length of T minus the length of P plus 1 times this probability, which is the length of P or small p.

This whole number can be made very small by selecting big prime number p much bigger than the product of the length of the text and the better. We can select arbitrarily large prime number p as we want. It can easily be made bigger than this product, even if the length of the text is in billions and the length of the pattern is millions. We will just select P on the order of 10_18 and that will work for us.

We still can compute numbers on the order of 10_18 in constant time. Let's analyze the running time of Rabin-Karp's algorithm, but let's analyze it separately. First, everything but for calls to AreEqual and then separately all the calls to AreEqual. First without the AreEqual, hash function on the pattern is computed in time proportional to the length of the pattern.

The hash function of the sub-strings of T is computed also at the same time, but it is computed for each iteration of the for loop. It is computed length of T minus the length of P plus 1 times. This already gives us the length of P plus length of T minus length of P plus 1 times the length of P, which is equal to big O of the length of T times length of P. Now that this is already the same as the estimate for the name algorithm.

This is already jumped too bad, but actually, we know that this part can be optimized and I will show you in the next part how to do that. These can be made much, much faster if we compute the hash values for the sub-strings of the text T much more intelligently. We're actually interested more in the second part. The second part is the total time spent inside the AreEqual call.

Each AreEqual call is computed in time proportional to the length of the tangent. However, AreEqual is called only when the hash value of the pattern is equal to the hash value of the corresponding sub-string. Means that either we found an occurrence of P, of pattern in the text, or a false alarm happened. By selecting a very large prime number p, make the number of false alarms negligible, very small.

Total running time can be estimated as follows. If the pattern P is found q times in the text T, the total time spent in AreEqual is on average, big O of q plus the number of false alarms, which we estimated from the top and all that times length of P and that is equal to big O of q times length of P. For the case when the big number, prime P, is much bigger than a product of the lengths of the text and the pattern. This is on average q times the length of P.

Total running time is an average big O of the length of T times length of P plus q times P and this is, again, big O of the length of t times the length of P. Because of course q, the number of occurrences of the pattern in the text, is less than or equal to the length of T. The running time of the current implementation of the Rabin-Karp curves algorithm is the same as the random time of the Naive algorithm, so it can actually be greatly improved. The second summand, big O of q times length of P is unavoidable because for every occurrence of the pattern in the text, we need to actually check whether this is an occurrence and to do that, you need to go AreEqual and this call to AreEqual will run for the exact length of P iterations because all the characters will be equal.

This is unavoidable and we can not improve. But in practice, the number of times that pattern occurs in the text is usually very small. If you're looking for a gene in the genome into may occur 1, 2 or 3 times, if you're looking for a word in a Wikipedia article, maybe it'll occure 10 or 100 times, but not like thousands or millions of times. This summand actually will be very small in brackets.

The first summand, big O of the length of T times length of P is so big because we compute the hash of each sub-string of T separately and this actually can be optimized a lot. To see how, see the next video.
