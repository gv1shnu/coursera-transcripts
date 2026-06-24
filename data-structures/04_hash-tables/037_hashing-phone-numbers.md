# Hashing Phone Numbers

- **Course:** Data Structures
- **Module 4:** Hash Tables
- **Lecture #:** 37
- **URL:** https://www.coursera.org/learn/data-structures/lecture/mW2wn/hashing-phone-numbers
- **Extracted:** 2026-06-20 21:40:25

---

Hi, in the previous video we've introduced the notion of universal family of hash function, and we showed that if there is a universal family of hash functions for some cellar project, then it is possible to create efficient hash tables using the training scheme using these universal family. However, we didn't show any examples of universal family of hash functions. Doesn't even exist in the first video of this part will prove that there is no universal hash functions. So maybe there is no universal family of hash functions.

Well, it turns out that for any finite set of integers there is a universal family of hash functions. And I'm going to demonstrate it to you in this video. Also using this, we will be able to solve the first part of our phone book data structure problem to map from phone numbers to names efficiently to hash phone numbers. We first can convert phone numbers to integers who already did that.

And as a result any phone number will be converted to an integer strictly less than 10 to the power of 15. If we come up with the universal family for integers up to 10 to the power of 15, we will be able to map phone numbers to name sufficiently using chain. We know that from the previous video. Now I stayed with this llama that there exists such a universal family age within the XP for any prime number P.

And this family consists of a set of hash functions parameter. Rised by two parameters A and B. So for any pair A B. Such that a is between one and p minus one integer number and B is between zero and B minus one.

Also an integer for any such pair? There is 1 # function in this family. And this hash function takes the key X, which is An integer between zero and B minus one. It multiplies it by A S B, then takes the result module api And finally takes the result modular M.

Where M is the cardinality of the hashtag. So I state that this is a universal family for the set of integers between zero and B -1. If B is any prime integer number. This is a pretty complex example, but this is needed to make a really universal family which has the property that we need for hash tables to work really fast and consume not too much memory.

Also, actually, the functions are really simple. It's very easy to compute function A X plus B. It's just a linear function. And then we just need to take module A P where P is the fixed number and then module M where M is also a fixed number.

So it just takes only a constant number of operations. So all the hash functions in this family are really very fast to compute, which is a desirable property for a hash function. Now, what could be an example of such family and such a hash function from this family. But first We need to select the prime number P and in this case I selected B to be equal to 10 million and 19.

Why did they select such a big prime number? Because this prime number needs to be bigger than the numbers Corresponding to the phone numbers that we're going to consider. And for a moment we're going to consider only local phone numbers with at most seven digits and they are all less than 10 million. And so I selected piece slightly bigger than 10 million, Which guarantees that all the phone numbers are between zero and B -1.

Now we can select any aid Between one and P -1. So let's just select a equal to 34 and B should be any Number between zero and B -1. So let's just select b equal to two. Let's consider as a key number 1,482,567, which corresponds to the phone number one for eight 25 67.

So what will happen with this key When we choose this particular hash function with parameters A and B. From this particular universal family with brian B. first we're going to multiply it by 34 and add to and then we're going to take it modular P which is equal to 10 million and 19. And the result that we're going to get is 407,185.

You can check that with your computer. Now, this is not the end. You also need to take this result 407,185 modular are cardinality. So let's select for example, Cardinality of 1000.

Then The result of taking model of 1000. Just the last three digits, it will be equal to one 185. So in this case H of X is equal to 100 and 85. This is the mapping from our integer to one of the industries between 10 and 999.

Because the cardinality of our hash function in the end is 1000. Because the last operation we take model of 1000. So how to prove that actually for any prime number, P such a family is a universal family. I'm not going to give you a full proof that I am going to give you the main ideas of the proof.

It turns out that for any pair of different keys, X and Y. So remember in the definition of the universal family, the key is that for any fixed pair of different keys? The probability of collision when choosing a random hash function, the probability of collision on these two keys is less than or equal to one or M where M is the chosen personality. So it turns out that for any pair of different keys, X and y.

Any of the hash functions in the family. Hp By the way there are exactly p times p minus one different hash functions in this family because there are P choices for the parameter B and t minus one, choices for parameter A. Those choices are independent. So there are in total p times p -1 different hash functions.

So it turns out that each of these hash functions, hashes this fixed pair of keys xy into different bears are s of different reminders module B and there are exactly p times p minus one. Different pairs are s of different tremendous module Api because the first remainder can be any remainder from 0 to P -1. So there are options and the second remainder should be different than our but otherwise it should be any number between zero and b minus one. So there are t minus one options for the second remaining.

So there are exactly Peter is P -1 different pairs. It means that the fixed pair xy is mapped to every possible pair of different tremendous module api by all the hash functions in the family and it happens with the same probability. So any pair R, s of different tremendous module Api has equal probability one hour, Peter and Schema and so on. And so the probability that x and y will have a collision is now the probability that some pair of different remainders module api will have the same remainder module M or it means that the probability is the ratio of all bears are as of different remainders must be such that their remainders module M are the same.

And it turns out that the ratio of pairs of different tremendous module piece such that they are the same module M is less Than one over M. And this is the end of the informal proof that this family is indeed universal. Now, let's finally use this universal family of hash functions to solve the first part of our phone book data structure problems to map efficiently From phone numbers to names. First define the maximum possible length of a phone number.

In practice, L will be equal to 15. Then convert all the following numbers to integers from 0 to 10 to the power of L -1 just digit by digit. Then choose any prime number P which is bigger than 10 to the power of such prime numbers always exists. Then choose the size of the hash table M which is also the cardinality of the hash function.

And then choose random hash function from the universal family HP. Which basically means that we need to choose two parameters, integer A between one and p minus one uniformly and integer B from zero to p minus one also uniformity. This is very easy to do. And this already results in a hash function eight times X plus B module P module M.

Now we have a hash function and a hash table size. And we can use chaining to store the correspondence between the phone number and the name. And this solves our problem of mapping efficiently from phone numbers to names. Because this is a universal family, which means that the operations will run fast and the memory consumption will be good.

It will be linear in terms of the number of contacts we need to store in the next video. We're Going to solve the opposite problem of mapping from names two phone numbers.
