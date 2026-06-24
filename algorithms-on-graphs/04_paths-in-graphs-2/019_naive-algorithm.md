# Naive Algorithm

- **Course:** Algorithms On
- **Module 4:** Paths in Graphs 2
- **Lecture #:** 19
- **URL:** https://www.coursera.org/learn/algorithms-on-graphs/lecture/BVj0X/naive-algorithm
- **Extracted:** 2026-06-21 21:25:55

---

Hi, in this video we're going to come up with an algorithm to find the shortest paths from a single node to all the nodes in the graph with weighted edges for the case when all the weights are non negative. This won't be an optimal algorithm, and we will improve it later, and that will become dextrous algorithm. However, let's start with this naive algorithm. There is a very important observation to make before we can come up with an algorithm.

This is about optimal substructure, the llama states that, any subpath of any optimal path is also optimal. That means that any set path of the shortest path, and terminal distance is also shortest path between the points that it connects. And any subpath of the fastest route from A to B is also the fastest route between the nodes it connects, and so on. And it is really easy to prove that, because we can just assume for the sake of contradiction that, that is not true.

Consider any optimal path from A to B. And any two nodes U and V on this path, and assume that there is a better, more optimal path from U to V. But then we can substitute this current path between u and v which is the part of path from A to B, with a better path between U and V. And construct a new path from A to B.

And this path will be better than the optimal path from A to B, with which we started, which contradicts the assumption that it is the optimal path. So it is a contradiction, and that cannot happen. It means that for any two nodes on the optimal path, the side path connecting them is also optimal. There is an important corollary from that, that if any path from a through some nodes to b which has the previous to last node u.

If it is a shortest path from A to B, then the distance from A to B, the distance from A to U, plus the weight of the edge from U to B. Why is that? Because the path from A to U is a subpath, and also has to be optimal. And so the distance from A to U is equal to the length of the path from A to U, which is a subpath of the path from A to B.

And then the second path is also optimal, and its length is the weight of the last edge from U to B. Now we will introduce the procedure of edge relaxation, and with that also introduced the disk values. So the disk values will be basically an array where we will have for any node, V. An upper bound on the actual distance from this tragic node A to V.

And initially this array will contain only values plus infinity, and then will improve, and improve these upper bounds. And those upper bounds will not be just any upper bounds, those B will be actually substantiated by some paths. So at any point this stuff V will be the length of some path that we already found from A to V. In this sense, this is not just an upper bound, this has some path that implements this upper bound.

So there is a path with this distance, and it means that the shortest path is at most this distance. So, this value is indeed an upper bound. So, the edge relaxation procedure for an edge from U to V basically just checks whether it is possible to improve the upper bound dist of V using the upper bound dist of U. Or whether it is possible to improve our knowledge about the best path to V using the best path we know from A to U.

And the edge from U to V, appending this edge to the end of the bathroom to U, and getting to V this way. So basically this procedure relax. It checks whether this V is bigger than this of you, plus the weight of the edge from U to V. If that is the case, it means that we can improve dist of V.

Because we can first get from A to U with a path of flying this U, because this U is substantiated with some specific pathroom A to U. And then we can augment this path with the edge from U to V. And the total length will be just a few plus weight of the edge from U to V. So would you like the, this value for V, and assign it actually to the some of the sum of u, and weight of the edge from U to V.

And also as you remember from the previous lecture, we need to construct the shortest path tree, in this case it is very similar. We just remember that the node from which we know, the best current estimate of the distance from A to V is the node U. So we will always remember the previous node on the current best known path to V. And in the end it will allow us to reconstruct the shortest path from A to B.

So the naive algorithm works like following. We start by initializing the dist values with plus infinity, and the prep values with pointers to know where we initialize the dist to the node A which is the starting node with zero. And then we just go, and look trying to relax all the edges, and we do that until at least one this value actually changes. And if at some point we see that no matter how, and when we try to relax any edge, nothing changes, then we stop.

So basically we relax everything we can until we cannot relax anything else. And the lama states that after the call to the naive algorithm, all the distances will be said correctly. That is the dist values will contain actually the correct distances from A to all the nodes. And to prove that, we will assume for the sake of contradiction that although knowledge can be relaxed, there is a vertex V, for which the distance is smaller than the upper bound dist of V.

We remember that dist of V is always an upper bound, so it is either equal to the correct distance, or strictly bigger. So suppose it is strictly bigger, now, consider a shortest path from A to V, there is some shortest path from A to B. And let U be the first vertex on the path with the same property, that dist value of U, is strictly bigger than the actual distance from A to u. And let B be the vertex right before U, note that there is a vertex right before U because U is not equal to A.

Because for a actually the disk value is set to zero in the first step of the algorithm. And so is not strictly bigger than the distance from A to a. It is equal so you is different from A. So there is some previous verdicts P on the shortest path from A to you.

So what happens with this node, B? We know that this not be doesn't have this property that it's this value is incorrect, it is closer to A than you and you is the first verdict for which our property is broken. So actually for P that this value is equal to the actual distance from A to B. So then the distance from A two U.

Is equal to distance from A to B plus the weight of the edge from P. T. You. Because of the property that the optimal sub path the path of an optimal path is also optimal.

So distance from H e U. Is equal to distance from HP plus weight of the edge. And that is in turn equal to this value of P plus weight of the edge from me to you. And we know that this value of you is strictly bigger than the distance from A to you.

And that we know that it is equal to this value of people as the weight of the age from P to you. And now we see that actually the HP you can be relaxed because this is exactly the property that we check when we try to relax the edge. And this contradicts the assumption that no edges can be realized. And as we reached contradiction with our assumption that some this value is incorrect, it means that all the values are actually correct.

And when the naive algorithm stops all the dist values are equal to the correspondent distances from the starting node to all the other nodes in the network. We won't analyze. How long does this algorithm run because it is definitely not optimal. And in the next video we will come up with a better algorithm which also gives correct distances
