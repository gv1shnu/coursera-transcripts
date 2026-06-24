# Chaining

- **Course:** Data Structures
- **Module 4:** Hash Tables
- **Lecture #:** 32
- **URL:** https://www.coursera.org/learn/data-structures/lecture/2yY2h/chaining
- **Extracted:** 2026-06-20 21:39:29

---

Hi. In this and a few following videos, we're going to assume that we've somehow managed to create a good hash function with all the desirable properties from the previous video. Still, however, it can generate some collisions. In this video, we're going to learn how to go around those collisions and still solve the phone book problem.

But first, let's introduce some definitions. Often, we need to store mapping from some objects of one kind to objects of another kind. For example, a mapping from a filename to its physical location on the disk, a mapping from a phone number to name in the phone book problem, or a mapping from name to phone number in your smartphone. When you need to call Maria, you want to just find her by name and then let the phone call her by her phone number.

To do that, it needs to retrieve her phone number given just her name. A map from a set of objects S to another set of objects V is a data structure with methods HasKey, which just returns whether there is some value in the map corresponding to this particular object or not, function Get, which returns the value corresponding to this object if there is one in the map, and function Set which takes two arguments, objects and value, and it sets the value corresponding to this object in the map. If there is a map from a set S to V, objects from the set S are usually called keys of the map and objects from the set V are usually called values of the map. Now, to solve our phone book problem, we actually need to implement a map from phone numbers to names.

Now you'll learn the technique called chaining, which allows to create such a map from phone numbers to names for our phone book problem. We assume that we came up with a hash function, for example, with cardinality eight. It maps phone numbers to integers from 0-7. Then we are going to create an array of size eight with cells indexed from 0-7 and we're going to use this array to add contacts to our phone book.

First, there comes a contact with this phone number. We compute its hash function and it turns out to be four. So we go to the cell with Index 4 in the array and we add the contact to this cell, like name Maria, and this phone number. Now there goes another contact with another phone number, and the hash value for this phone number turns out to be one.

We go to the cell with Index 1 and we add the corresponding contact to the cell, name Sasha, and this phone number. Now let's see what happens when there is a collision. We add a new 3rd contact. It has a distinct phone number, but the hash value is the same as the hash value of the first phone number, so there is a collision.

Then we want to also put the corresponding contact in the cell with Index 4, but we don't want to erase the contact that is already there. We want to keep the old contact and also keep the new contact. What we want to do is basically to widen this cell of the array and put more contacts into it. For example, put a new contact in the end of the cell, so to say.

How can we do that? Actually, we can do that by creating an array which consists not just of names or pairs of names and then phone numbers. We can create an array which consists of lists. This array has size corresponding to the cardinality of the hash function, eight.

Its cells with the indexes correspond to the values of the hash functions, so the cell within this four corresponds to the value four of the hash function, and each cell contains a doubly linked list of contacts, where each contact is a pair of name and the phone number. When we need to add a new contact, we first compute the hash value of the phone number, we go to the corresponding cell in the array, we take this doubly linked list, and we append the new contact pair of name and the phone number to the end of this list. If you want to change the name corresponding to some phone number, we again compute the hash function of this phone number. It is four, so we go to the cell with Index 4.

We go through the whole doubly-linked list with the contacts corresponding to the cell, we find the one which corresponds to this particular phone number, and then we can change the name. We can change Helen to Elena. Now our phone book reflects the change of the name that we wanted. If we want to remove some contact, we can again compute the hash value of this corresponding phone number.

This one has hash value of one, so we go to the cell with Index 1 and we take the doubly-linked list there. We see that there is only one element there and it indeed corresponds to this phone number, and we just remove this item from the doubly-linked list. This is how we're going to work with our phone book. In general, we select a hash function of some cardinality m, which should be small enough so that our array is not too big, is not a huge array like in the case of direct addressing for international phone numbers.

We create array chains of size m, and each element of the array chains is a doubly-linked list of pairs: name, phone number. This doubly-linked list is usually called chain. This is where the technique gets its name for, chaining. Because of chains in each cell of the array.

Pair, name, phone number goes into Chain at position hash value corresponding to the phone number in the array chain. Typically, it first converts phone number in some standard way to an integer, then we compute the hash function based on that integer, and then we find the corresponding index and the corresponding cell in the array chains. Actually, we could just apply some other hash function from phone numbers directly to indexes. That doesn't matter too much, but in practice, we'll probably convert the phone number first to some integer in a standard way and then use a hash function from integers to the indexes in the array chains.

To look up name by phone number, we just go to the chain corresponding to the phone number by hash function value and look through all the pairs. To add a contact, we create a pair, name, phone number, and insert it into the corresponding chain. To remove a contact, we go to the corresponding chain, find the pair in the doubly-linked list, and remove it from the chain. In the next lecture, we're going to see how all these can be implemented in pseudocode and analyze the time complexity and the memory requirements of this chaining scheme.
