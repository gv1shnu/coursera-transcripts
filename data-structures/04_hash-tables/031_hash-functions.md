# Hash Functions

- **Course:** Data Structures
- **Module 4:** Hash Tables
- **Lecture #:** 31
- **URL:** https://www.coursera.org/learn/data-structures/lecture/vOqnE/hash-functions
- **Extracted:** 2026-06-20 21:39:18

---

Hi, in this video, you're going to learn what are the hash functions, which are the base for hashing. In the previous problem, we would like to somehow encode international phone numbers with small numbers. Small integers, for example, numbers from 0 to 999. because then, we could use direct addressing with just numbers from 0 to 999.

But we would need that there would be different codes for the phone numbers in the phone book. And all those are between zero and 999. Of course that would only work if you have less than 1000 contacts in your phone. But typically, you would have less than 10,000 contacts in your phonebook.

So numbers from 0 to 9, 999 would do it. The only question is, how do we encode those long international phone numbers with small integers. And hash functions are the answer to that. So, hash function in general, is such a function that it maps some set of objects as to set of integers from zero to m minus 1 for some integer m bigger than zero.

So any such function is called a hash function. And m, in this definition, is called the cardinality of hash functions. So m is the number of different values of the hash function. We have several desirable properties that we want from our hash function.

First, hash functions should be of course fast to compute, otherwise it would be useless. Also, we wanted to have different values for different object. Different values for all the phone numbers in your phone book. And then, if these two properties were true, we could just use direct addressing with big O of m memory, where m is the cardinality of the hash function.

And so, we want small cardinality m. Unfortunately, all of these at the same time are usually impossible. Because it is impossible to have all different values if the number of objects, the size of the set S, is more than m. By pigeonhole principle, if you have more objects than the codes, then at least some pair of objects will have the same code.

And as it is possible for two different objects to have the same value of the hash function, we call this situation a collision. Now let's reformulate the desirable properties of a hash function so that it is at least possible to satisfy all of them. We don't change the first property. Hash function should still be fast to compute.

We change the second property. Instead of requiring them to have different values for all different objects, we're required to have a small probability of collision. Just a small probability of situation when two different objects have the same value of the hash function. And again, we want a small enough cardinality act.

So assume we're successful with all those properties, we cannot use the direct addressing scheme with an area of size m, because it is still possible, although the probability is small. But it is possible that there will be a collision, and we cannot write two different contact names in the same cell corresponding to two different phone numbers, which have the same value of the hash function. So, it is impossible to use the exact direct addressing scheme from the previous videos. And in the next video, we're going to learn how we can solve this problem when there are some collisions, but the probability of collisions is small.
