# Chaining Implementation and Analysis

- **Course:** Data Structures
- **Module 4:** Hash Tables
- **Lecture #:** 33
- **URL:** https://www.coursera.org/learn/data-structures/lecture/dWNAc/chaining-implementation-and-analysis
- **Extracted:** 2026-06-20 21:39:40

---

In this video we're going to implement the changes scheme we've learned in the previous video and also analyze time complexity and number of consumption. To implement the chain scheme means to implement a map and that means to grant three methods HasKey, Get and Set. So we assume that chain is our array, which consists of chains or downloading links. So each chain is a list of pairs, object value.

So in terms of phonebook problem, object is a phone number and value is the name. So to implement the version HasKey given the object, we assume that we already have these very chains. And so first we assign the chain position cache of object at index, cache of objects in very chains we assign it to variable change. So now chain contains this double increase of pairs of objects and value.

And then we go through this list for all pairs key value in this chain. Remember that the objects are also called keys in the map. So for each pair of key and value in this chain. If the key is equal to the object.

For example, if the key is equal to the phone number in case of the phonebook problem. Then we understand that this pair is actually the contact corresponding to this phone number or the despair of key value indeed corresponds to this object. And in this case we return true because we know that indeed our map contains a pair of key and value corresponding to this subject. And so it is possible to reduce the value corresponding to this object.

Otherwise, if we went through the whole list chain, and we didn't find any key which is equal to object, we return false because we know that it is impossible that there is a very corresponding to this object. Because if there was a very responded to this object, it has to be in the chain at in this hash of the object, and we didn't find it there. So there is no very corresponding to the subject in the net. The next function in the method is Get object.

It should return the value corresponding to this object in the map. So we start again by retrieving the chain corresponding to this object by index, which is equal to the hash of the object. Then we go through the whole chain, and we go through all the pairs, key value in this chain. And if some key is equal to our object, then we know that the value corresponding to the subject is the value in this particular pair, so we return this value.

Otherwise, if we went through the gold chain, and we didn't find any key which is equal to or object, then we know that there is no value corresponding to the subject in the map. So we returned the special value and a not applicable, which means basically that there is no value corresponding to the subject in this map. And the final function that we need to implement is Set object, value. It needs to write down that the value corresponding to this object should be valued.

Again, we start with retrieving of the chain in there a chains by position which is equal to hash of the object. And then we go through all the pairs in this chain. And if for some pair, the key in this pair is equal to the object. Then we set the value of this pair to the value that we got as the arguments of our function.

So we overwrite the value that was in this pair with the new value, and so this pair in the double in key corresponding to the object is now the new value. And if we manage to debt, we just returned from the function, and we don't do anything else. Otherwise, if we went through the whole chain and there was no value corresponding to this object. Previously, it means that we need to add a new pair to the corresponding chain with both the object and the corresponding value.

And this is what we do. So this is the end of the implementation of the map based on chaining. Now, let's analyze its ascent topics. So the Lemma states that if C is the length of the longest chain in the chains, then the running time of all these three functions HasKey, Get and Set is Terra of C plus one.

Well, basically if the chain corresponding to the object is not empty, but the object is not found in the chain, we will need to scan all the C items. And that's why we will need to do at least C operations and that of C is equal to that of C plus one in case one, C is more than zero when C is positive. And if C is zero, we still need a constant time to implement all those functions because they still do something and that's why we need the plus one, not just that of C, but C plus one in the asymptotic. Another Lemma, let n be the number of different objects currently on the map and m be the cardinality of the hash function.

And the memory consumption for chaining is Terra of n+m. And that is really easy to see because we need Terra of n to store and bears object value, which are actually stored in the map. And also we need Terra of m anyway to store the array chains of size some of the least in this array, some of the chains can be empty. But we still need the array with pointers to the heads of these arrays, and that would require us to have additional big all of m memory.

So all in all that is the Terra of n+m to store both the bears the context that we need in the phonebook. Or are there pairs for some general map n Terra of m for the array itself, in this video, we've learned how to implement map using chaining. We've analyzed its time complexity and memory consumption. And in the next video, we're going to learn what are the hash tables?

What are the sets and how to implement sets using hash tables?
