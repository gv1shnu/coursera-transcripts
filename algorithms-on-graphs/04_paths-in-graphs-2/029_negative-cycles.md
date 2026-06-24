# Negative Cycles

- **Course:** Algorithms On
- **Module 4:** Paths in Graphs 2
- **Lecture #:** 29
- **URL:** https://www.coursera.org/learn/algorithms-on-graphs/lecture/8DRLn/negative-cycles
- **Extracted:** 2026-06-21 21:27:42

---

Hi. In this video, we will deal with negative cycles. We'll augment Bellman-Ford algorithm such that it will allow to detect whether a graph contains a negative cycle or not. If yes, it will also allow to find at least one negative cycle.

The idea is pretty simple, we will need to add one more iteration of relaxation of all edges. But this time, we will need to also notice whether anything changed on the situation or not. This lemma states that basically, anything will change on the additional iteration if and only if there is a negative weight cycle in the graph. Let's prove this lemma in both directions.

First, we prove that if there are no negative cycles, then nothing will be changed on iteration number V. Indeed, if there are no negative cycles, then all shortest paths from S contain at most, V minus 1 edges. That is because if you have at least V edges, then you have a cycle on your path, and you can remove the cycle, and the path will become shorter or will remain the same. All the shortest paths, we can consider that they contain, at most, V minus 1 edges.

Now, dist-value can be updated on iteration number V, because already by iteration number V minus 1, all the distances to all the nodes are correct. To prove in another direction, let's assume that there is a negative weight cycle. Let's say it's a cycle of length 3, a to b to c to a. Assume that there is a negative weight cycle, but there is no relaxation on the additional iteration.

Then it means that for all three edges ab, bc, and ca, we couldn't actually relax them. This means in turn, that dist-value of b is less than or equal to dist-value of a plus the weight of the edge ab, and so on. We have these three inequalities. Now, let's look what happens if we sum the left and the right parts of these inequalities.

On the left, we will have dist b plus dist c plus dist a, and on the right, we'll have dist a plus weight of ab plus dist b plus a weight of bc plus dist c plus weight of ca. But you can notice that in both left and right part, we have sums of dist a, dist b, and dist c. We can subtract them from both parts, and we'll get that weight of edge ab plus weight of edge bc plus weight of ca's greater than or equal to 0. But this is a contradiction with the assumption that a, b, c, a is a negative cycle.

This is just for the case when the length of the cycle is three. But of course, if we had more edges, it would be the same contradiction. If there is a negative cycle, something we will definitely change on iteration number V, and if there are no negative weight cycles, then nothing will change on iteration number V. This is the algorithm to detect whether there is a negative cycle in the graph or not.

Again, the algorithm for finding negative cycle, you just run V iterations of Bellman-Ford algorithm. To find the negative cycle itself, you also need to save the node V, which was actually successfully relaxed on the last iteration such that its dist-value changed. V is reachable from a negative cycle because if it wasn't reachable from a negative cycle, its dist-value couldn't be relaxed in the last iteration. Because the fact that its dist-value relaxed on this iteration means that there is a path of length which contains at least v edges, which is shorter than any path which contains fewer edges.

This path with at least V edges contains a cycle, and if we remove the cycle, the path must become longer, otherwise, we wouldn't be able to relax on this iteration number V. This is a negative cycle. V is reachable via this path from a negative cycle. Now, we can use our prep array to actually find the negative cycle.

We're going to start with assigning some node x to node v. Then we're going to follow the prev link until we come to the cycle. Actually, if we follow the prev link for at least V times, we will definitely be on the cycle because we will return, return, return. Our last relaxation improved the path to V with a path of, at most, V edges.

After we go back, the edges will definitely be on the cycle. We can't go away from the cycle because this is the cycle, and we will go indefinitely through the cycle if we follow the prev links. After V times we follow the prev link, we will definitely be on the sum vertex of the cycle. Let's denote now this vertex as y.

We just saved this vertex another variable. Now, go once again, through prev links until we come to the same node. This way, we'll go through the whole cycle. If we save all the nodes that we visited on this way, we will just write down the whole negative cycle.

This is the way to find at least one negative cycle if we detected that there is one with Bellman-Ford algorithm augmented with additional iteration. Now that we've learned to deal with negative cycles, to detect them, and to find one, and to resist one, can we finally get as many rubles as we want from $1,000 if we detected that our currency exchange graph contains a negative cycle? Well, unfortunately, it turns out that not always. Even if that there is a negative cycle, it can be not possible to get as many rubles as you want from the $1,000 US that you have initially.

Because for example, in this graph, you can exchange from US dollars to Euros and from rubles to Euros. There is a negative cycle between euros, British pounds, and Norwegian crowns. You can check that the product of exchange rates on these three edges from Euros to pounds to crowns is more than one, but still, you cannot actually use this negative weight cycle to exchange dollars to rubles. Because you can exchange from dollars to Euros, then you can use this negative weight cycle to get as many euros as you want.

But for some reason, there is no exchange rate from Euros to rubles, and so you can't get rubles at all. This is not sufficient to detect a negative cycle to exchange from US dollars to as many Russian rubles as you want. Any negative cycle doesn't work. In the next video, we'll actually deal with this problem, and we'll answer definitely whether it is possible for a given graph to get as many Russian rubles as you want from $1,000 US, or is it possible to get as many US dollars as you want from $1,000 US, and so on.
