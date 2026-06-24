# Implementation

- **Course:** Algorithms On
- **Module 4:** Paths in Graphs 2
- **Lecture #:** 22
- **URL:** https://www.coursera.org/learn/algorithms-on-graphs/lecture/cgiHK/implementation
- **Extracted:** 2026-06-21 21:26:27

---

Hi, in this video we're going to study the implementation of Dijkstra's algorithm. Here is the pseudocode for the algorithm but before we dive into it, let's remember the data structure that we started in the previous course about data structures, it is called a priority queue. So from a priority queue we need only the following three things. First, we need to be able to build a priority queue out of a set of keys.

Second, we need for this particular to be able to extract the element with the minimum key, say the value of the ski and remove it from the particular. This is called extract minimum. So you both get the value of the minimum key and you remove it from the particular at that moment. And the third thing is which would be able to change the key of any element of the priority queue at any time.

These are the three things that we will need. There are different ways to implement this priority cube and the running time of Dijkstra algorithm will depend greatly on the way we implement priority queue. But we'll discuss that later when we analyze the running time of this algorithm and for now we'll just assume that there is some data structure based on priority queue that is available for us and we will use it in our algorithm. So we'll start with initializing the disks values to infinity for all the notdes and also the prep values.

Two pointers to nowhere and the dist values will be the estimates of the distance. And in the end they will be equal to the correct distances to the corresponding notes from the static node A. And the prep values will always point to the previous node on the best known that from the starting node to the current node. But initially we don't know any previous notes, so we initialize them with pointers to nowhere.

We initialize the distance to the starting node with zero because we know this distance and now we create a priority queue out of the disc values of all the nodes. So basically we create a priority queue where one key is equal to zero and all the other keys that are equal to plus infinity. And then we'll proceed by extracting the minimum key from disparate eq until it becomes empty. It corresponds to the action in the Dijkstra algorithm where we find the note with the minimum current this value out of the known region, adding it to the non region and processing it by relaxing all its outgoing edges.

So our priority queue will lead us to select the note with the minimum this value out of all the notes in the priority cube. And all the nodes in the priority queue will be all the notes which are outside of the non region. So initially all the notes are outside of the known region. But we will extract the minimum node, which is the starting node because it has a key of zero and we'll add it to the non region and we will process all the outgoing edges.

And then we will extract the next note with the this value medium of all the other nodes. And then process it and relax all of its outgoing edges and so on. So this goes is following, we take our priority queue and we extract the note with the minimum key with the minimum value from this priority queue. So it is no longer in the priority queue and you is the note with the minimum value.

So now we're sure that the distance to the snout is equal to the value of this note. And then we go through all the outgoing edges from you and we look at the endpoint V of this outgoing edge from U to V. And if it is possible to relax the edge UV then we do that we relax the edge. We assigned the prep value of the to you because now if we manage to relax the edge it means that you is the previous to last verdicts on the best known path from A to B.

And also we need to make a very important action to change the key of the node V in the priority queue. Because the key of the note must always be equal to its disk value and the value of the node V has just changed. And we want the property that the key of any note is always equal to its this value because basically what we do on each iteration is we select the note with the minimum key and we wanted to be the note with the minimum disk value out of all the notes in the priority queue. So we should always maintain the property that the keys of all the notes in the priority queue, are there just values?

So in the last line we changed the key with the change priority procedure is called like that because H is a priority queue. And we change the key of node V in the priority queue age to the key list. And when we finish this wild loop, it will go for exactly a number of nodes in the graph number of iterations because we will process notes one by one and add them to the known region and proceed with relaxing all their outgoing edges. So when we get out of this loop, I state that the values of all the notes will contain the correct distances from starting notes to the corresponding note and the prep values will contain the previous note on the shortest path from starting note to this note.

But we're going to prove this in the next video
