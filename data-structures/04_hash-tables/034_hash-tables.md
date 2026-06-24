# Hash Tables

- **Course:** Data Structures
- **Module 4:** Hash Tables
- **Lecture #:** 34
- **URL:** https://www.coursera.org/learn/data-structures/lecture/5e8QH/hash-tables
- **Extracted:** 2026-06-20 21:39:51

---

Hi. In this video, we're going to study hash tables. We've just studied maps and how to implement them using chaining in the previous videos, another very natural data structure is called set. Set is a data structure with methods to add an object, to remove an object from the set, and to find an object in the set.

Examples of the sets are like students on campus. Whether a student with this particular name was on campus or not, phone numbers in your phone book. You might just want to know whether your phone book contains this particular phone number or not, or keywords in a programming language. When you've typed something in your program, the compiler needs to know whether this is a keyword of the programming language or it is just an identifier that you decided to use.

It is possible to implement a set also using chaining and there are two ways. One is just to see the set is actually equivalent to a map from Set S to the Set V of just one value true. We just store a mapping from objects to values from the Set V, which has just one value true. If there is a value true corresponding to some object in the map, it is just the same as if the object is in the set, and if there is no value corresponding to this object, then the object is not in the set.

This is costly and strange way to implement the set, would need to store pairs of objects and values true in the map. We don't need to do that, we can actually just store objects instead of pairs object value in the chains of the chaining scheme, and then do everything more or less the same way. Now we're going to implement it into the code. Assume again that we have an array chains which consists of doubly linked lists, which are called chains and each chain contains a double linked list of object, not just pairs of objects variable, just objects.

To find an object in such a set, we first retrieve the chain corresponding to this object by computing the hash of this object and taking the chain at the index, which is equal to hash of the object. Then we'll go through this chain, go through all the keys in this chain, and if some key is equal to the object, then we know that this object is in the set and return true. Otherwise, if we didn't find the object in the chain we'll return false because it cannot be in any other chain, it can be only in this chain and we checked it is not there, so it is not in the set. The second method is add.

To add an object into the set or again retrieve the chain corresponding to this object by its hash, then we first need to check whether this object is already in the set. Because if it is, we don't want to store the same object in the set twice. We go through the chain and if some key in the chain is equal to the object, it means that the object is already in the set so we don't do anything, we just return from return function, because to add an object which is already in the set to the set means to do nothing. Otherwise, if we didn't find this object in the chain, we just append this object to this corresponding chain.

This is when our object wasn't in the set, but we've actually added it to the set. The last function is to remove an object from the set. We'll start by determining whether this object is even in the set or not. If it's not in the set, then we don't need to do anything, we just return.

Otherwise, we retrieve the chain corresponding to this object by index equal to the hash of this object, and then we erase this object from this chain. We know already that this chain contains this object because our method find return true, we know that the object is in the set. If the object is in the set then it is definitely in this particular chain in the set, because it can be only in the chain corresponding to the hash of this object and so we can safely erase this object from the chain using erase from the double linked list. This is the end of the implementation.

What is a hash table? A hash table is just an implementation of either a set or a map which uses hashing. Any implementation of set or map using some hashing like direct erasing, or chaining, or some of the other techniques that exist, anything like that is called a hash table. The examples of hash table implementations in different programming languages are unordered set in C plus plus, HashSet in Java, and set in Python, those are the implementations of set.

Implementations of map, are unordered map in C plus plus, HashMap in Java, and dict in Python. All those implementations are based on hashing so those are all hash tables. There are also implementations of sets and maps in these languages based on different techniques which we are going to study later in this course. But these particular implementations are based on hashing and so they have the properties of hash tables.

Meaning that they have the time complexity operations and the memory consumption of the table corresponding to what I've just told you about chaining. In conclusion, we learn chaining, which is a technique to implement a hash table with parameters like n is number of objects, hash function cardinality m, and the length of the longest chain in the hash table c. We know that the memory consumption of chaining scheme is Theta of n plus m, and the operations work in time Theta of c plus 1. We want memory consumption to be low and actually Theta of n is what we cannot avoid because we need to store that object, but additional Theta of m is an overhead and we want to minimize this overhead.

Also we want everything to work in constant time or nearly constant time, so that Theta of c additional in the time complexity is overhead. So we want both m and c to be as small as possible. It is not easy to achieve that, we're going to learn how to do that in the next lecture.
