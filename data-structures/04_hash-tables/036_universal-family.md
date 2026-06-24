# Universal Family

- **Course:** Data Structures
- **Module 4:** Hash Tables
- **Lecture #:** 36
- **URL:** https://www.coursera.org/learn/data-structures/lecture/xbw9u/universal-family
- **Extracted:** 2026-06-20 21:40:15

---

Hi. In the previous video, we proved that there is no universal hash function and so our problem seems unsolvable. It seems that it is not possible to come up with a good hash function, hash function that has all the desirable properties. However, it turns out that there is such a thing as universal family of hash functions.

This family is going to help us solve our problem as usual. The idea is, remember QuickSort? At first, the algorithm was pretty slow. It works in time that of n squared but then we came up with an idea to choose a random pivot instead of a fixed pivot and it helped.

The idea is to use randomization. Actually, if you remember from the previous video, the closest we came to a good hash function was a random hash function. It distributed keys into cells really well. The problem is that we cannot use a fully random hash function because it will return different values at each call and so we won't be able to find anything in our hash table.

Instead, we want to first define a family or a set of hash functions, and then to choose a random hash function from the family. This is the way we're going to use randomization. Now, forward to the universal family. The definition is a little bit complex, so we'll introduce it part by part.

Let U be the universe or the set of all possible keys that we need to put in our hash table. Maybe not all of them will actually go into the hash table but this is the universe of all possible keys. For example, all phone numbers or all names that can be potentially in your phone book. Now, a set of hash functions H with the same cardinality m, so we fix first the cardinality m, and then we consider some set of hash functions with the same cardinality, and all these hash functions from this universe to the set of integers from 0 to m minus one.

Such a set of hash functions is called a universal family if, for any two different keys in the universe, the probability of collision between them is less than 1 over m. What does it mean that the probability of collision is less than or equal to 1 over m. It means that a collision for any fixed pair of different keys x and y happens for no more than 1 over m part of all hash functions in the family. So that if we select a random hash function from the family with probability equal among all the hash functions in the family, then the probability that this particular hash function would give a collision on this particular pair of keys is no more than 1 over m.

However, this hash function could give lots of different collisions on different keys, but we're only interested in some fixed pair. For any fixed pair of different keys, collision between them happens for no more than 1 over m of all hash functions in the family. This is true for any fixed pair of different keys. Then how randomization will work in our algorithm if we have some universal family.

The random hash function gives probability of collision exactly 1 over m but it is not deterministic, so we cannot use it. Instead, we can see that all hash functions in H are deterministic. Those are some hash functions and those are deterministic. We select a random hash function from this family and the only place where we use randomization is this selection of the hash function.

The hash function itself is fully deterministic, now the random step is selection of this hash function from the family. Then this fixed hash function is used throughout the algorithm to put keys into the hash table, to search for keys in the hash table, and to remove the keys from the hash table. Now let me introduce one more very important parameter of the hash table called load factor. It is the ratio of the number of keys stored in the hash table to the size of the hash table.

It is important because if it is very small, then we can be sure that a load of the cells of the hash table are empty and so we're wasting space. If it is bigger than one, then we can be sure that there is at least one collision and if it is big, then we can be sure that there are a lot of collisions and the longest chain length is too long and the operations will be too slow. We want to keep the load factor in some medium range. The lemma states that if hash function is chosen randomly from a universal family, then the average length of the longest chain in the hash table is big O of 1 plus Alpha, where Alpha is the load factor of the hash table.

The corollary from that is that if h is chosen randomly from the universal family, then operations with a hash table will run on average in time O of 1 plus Alpha, because they run in time O of 1 plus c, where c is the longest chain then c is O of 1 plus Alpha. So O of 1 plus c is the same as O of one plus Alpha. It means that load factor actually determines the speed with which operations are going to run. Not only on average, actually, there are theorems, they are much more complex called probability concentration theorems, from which it falls that not only the average running diagonally O of 1 plus Alpha, but the probability that the longest chain will be much longer than that, and so the running time will be much slower than that.

This probability is very small. Now, how to choose the size for the hash table? We can control the amount of memory used with m. Ideally, we want the load factor to be in the medium range from 0.5-1.

Because if it's bigger than one, we will have collisions. Definitely, if it's less than 0.5, it means at least half of the hash table is just wasted without any chains in it. We're going to use m side stat. O of m is equal to O of n over Alpha by definition of Alpha and that will be equal to O of n memory to store n keys because Alpha is constant, so n over Alpha is only a constant times bigger than n.

Operations will run in time O of 1 plus Alpha on average, which is equal to O of 1 on average because Alpha is between 0.5-1, so 1 plus Alpha is between 1.5-2. This leads to good hash table size. We don't waste too much memory. We don't use too much memory and operations run almost in constant time on average.

What if the number of keys is unknown in advance? One solution could be just to start with very big hash table, so that load factor is definitely below one in the end. But this time, this way we'll waste a lot of memory while the hash table is still very small. Another way is to copy the idea of dynamic arrays.

That is, we will gradually increase the size of our hash table and we'll resize the hash table when the load factor becomes too large. We can adjust resize the hash table because the size of the table and the positions of the items in the table are dependent. Because hash function has to be different if it has to choose positions within hash table of size m or of size m plus 10. There should be different hash functions to do that.

We not only need to resize the hash table, we'll need to copy all the keys from the current hash table to the new hash table. We choose new hash function and then rehash all the objects. How does the rehashing work? Suppose we want to keep load factor below 0.9, just for example, we want to keep it in general below one.

Let's try to keep it exactly below 0.9. The rehash operation first computes the current load factor, which is the ratio of the number of keys already stored in the table over the size of the table. If the load factor has just become more than 0.9, it means that we need to increase the hash table. So we create a new hash table of size twice the current size of the hash table, we choose new hash function with the corresponding cardinality.

Then for each object which is currently in our hash table, we insert this object in the new hash table using the new hash function. then we just substitute our current hash table and our current hash function with the new hash table and new hash function. This is the rehash procedure. We need to call rehash procedure after if each operation with the hash table, because after any insert hash table could become too loaded, the load factor could become more than 0.9 when we don't want to miss that moment.

So we need to call rehash after each operation. Similarly to dynamic arrays, although single rehashing takes linear time and that is a lot of time but amortized running time of each operation with hash table still constant on average because rehashing will be rare, we need to insert n more keys into the hash table of size n until we will again have to double the size of the hash table. On average, we will just spend O of 1 per each insertion. So this idea from the dynamic arrays also applies to the hash tables.

In the next video, we're going to find out what is an example of universal family, which can be used for hashing format.
