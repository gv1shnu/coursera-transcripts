# Phone Book Data Structure

- **Course:** Data Structures
- **Module 4:** Hash Tables
- **Lecture #:** 35
- **URL:** https://www.coursera.org/learn/data-structures/lecture/NYZZP/phone-book-data-structure
- **Extracted:** 2026-06-20 21:40:03

---

Hi. In the previous lecture we've learned how to implement maps and sets using hash tables and how to store a phone book efficiently using hash functions, but we've left out one important question. How to actually come up with good hash functions so that these hash tables consume not too much memory and all the operations are working really fast. In this lecture, we're going to learn how to do that.

At first, we're going to widen the scope of our initial phone book problem. So we want to design a data structure to store your contacts and to do everything that you actually need with your contact book on your smartphone. You need to store names of people and their phone numbers and the following operations should be really fast: to add and to delete contacts, to call a person given only person's name without the phone number, and to determine who is calling given their phone number. We need two maps to do that.

We need a map from phone numbers to names and a map from names to phone numbers, and both maps should be efficient and not consume too much memory. We can implement those maps as hash tables, and first, we will focus on the map from phone numbers to names. To do this using chain, we first select hash function of cardinality m then create array chains of size m, and each element of this array is a doubly-linked list called a chain, which contains pairs of name and phone number. The pair, name, and phone number goes into chain or the position hash function of the phone number converted to integer.

This is for the map from phone numbers to names. This is how it could look like if you had just three contacts and the cardinality of the hash function was eight. The array had Size 8 and indexed from 0-7, and you had just three contacts and there was a collision between two of the phone numbers of Maria and Helen. Now, remember the parameters.

You want to store n contacts and m is the cardinality of the hash function, and the hash table size for chaining them should be equal to m, to the cardinality of the hash function. I could refer to m both as the cardinality of the hash function and as the hash table side. Now c is the length of the longest chain in the hash table, and then the memory consumption is Theta of n plus m and the operations run in time Theta of c plus 1. What we want is we want both small enough m and c, but there is a fundamental restriction that in any way c will be greater than or equal to n over m by the pigeonhole principle, so it is not possible to have arbitrary m and c.

But still, we want reasonably m and reasonably c. So how to do that. Well first, let's consider good and bad examples. This is a good example.

We have cardinality of eight, we have eight objects, so c couldn't be less than one. In this case, it is two. It could be actually exactly one, but that would be the best case. This is still a good case and two longest chains are marked, and their lines are two and all the other chains have length just one.

Here is a bad example. We have Cardinality 8 and we have eight objects, but the length of the longest chain is eight. In general, the worst case is when you have n objects and the length of the longest chain is again n. In this case, the operations will run in time Theta of n, and that is too long.

We could do that without chaining, with just the least, and we're not content with such slow operations. Let's try to come up with hash functions that will give us both reasonably m and c, the length of the longest chain. For example, let's consider a map from phone numbers to names, and let's select cardinality of the hash function as m equal to 1,000. Then we can use as our hash function the first three digits of the phone number.

For example, for this phone number the hash value would be run just 800 because the first three digits are 8, 0, and 0, but there will be a problem with this approach because we have area code and area code is often the first three digits of the phone number. For all the phone numbers from the same area code, you will have the same hash value and that will generate a lot of collisions and that will generate a really long longest chain because all of those numbers would go in the same cell of the hash table. That is the best solution. Let's try another one.

Select again cardinality of 1,000, but use the three last digits of the phone number as the hash function. For example, for this number the hash value would be 567 because the last three digits in order are 5, 6, and 7. But again, there could be a problem if many phone numbers end with the same three digits. For example, a lot of phone numbers end with three zeros and that could happen.

In this case, we again will have a problem with a lot of collisions and a long longest chain in the hash table. Another attempt. Select the same cardinality m equals to 1,000 and hash function would just return a random number between zero and 999. Well, then we will have uniform distribution of hash values and we will get the best case possible probably because the keys will be almost evenly distributed among the cells.

We cannot really distribute the keys much better than random function does if we don't know in advance what would be the phone numbers to be stored. This seems like the solution, but the problem is that this hash function will take different value when we're calling it again. When we first store some phone number in the hash table, we will store it at one index, and when we then want to retrieve this phone number from the hash table, the hash function will return a different value almost with Probability 1 and so we won't find actually our phone number in the hash table which is bad. Actually, we won't be able to find anything with high probability, and so hash function actually must be deterministic, it cannot be random.

So this solution doesn't work again. The good hash functions have to have the following properties. They have to be deterministic, they have to be fast to compute, they have to distribute keys well into different cells or in other words, they should have few collisions. Actually, it turns out that there is no such universal hash function.

This lemma states that if the number of possible keys is very big and also much bigger than the cardinality of the hash function that for any hash function of such cardinality there exists a bad input resulting in many collisions. To prove that, let's consider some arbitrary set of all possible keys; all possible phone numbers for example, and let's consider the case of cardinality m equal to 3. Actually, the argument is the same for any cardinality, it's just easier to draw the example with the small cardinality. If we have this set S of all possible keys, we can group all these keys into three groups in case of Cardinality 3.

In general case, we can group them into n groups. Each group corresponds to a particular value of the hash function, so all the keys for which the hash value is zero go into Group 0. All the keys with the hash value of one go into Group 1 and so on. Now, let's select the biggest of these groups.

For example in this case, it is the Group 1. It turns out that it contains 42 percent of the keys in the set of all possible keys. If we're unlucky and we need to store all these keys in our phone book and we use this hash function, then we will have lots of collisions. Every key will actually go into the same cell, and the length of the longest chain rule will just be equal to the number of keys that we need to store.

This number of keys is very big because it's more than 1/3 of all the possible keys. In the general case, it will be more than 1 over m part of all the possible keys. For any hash function with any cardinality m if the size of the set of the keys is much bigger than m, there is a bad input of all keys in the biggest chunk responding to the same hash value which is definitely of the size more than size of the whole set of all possible keys over m, which could be very big. It seems like our problem is unsolvable.

We don't have any universal hash function. Actually, is it right? We will learn in the next video. It turns out that there is a solution to our problem.
