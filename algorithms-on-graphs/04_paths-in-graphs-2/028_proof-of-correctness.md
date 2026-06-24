# Proof of Correctness

- **Course:** Algorithms On
- **Module 4:** Paths in Graphs 2
- **Lecture #:** 28
- **URL:** https://www.coursera.org/learn/algorithms-on-graphs/lecture/txk8R/proof-of-correctness
- **Extracted:** 2026-06-21 21:27:32

---

Hi. In this video, we're going to prove that Bellman-Ford's algorithm returns correct distances for the case where there are no negative weight cycles. More specifically, this lemma states that for any k, after k iterations of relaxations of the Bellman-Ford algorithm, for any node u, its dist value is less than or equal to the smallest length of a path from S to u that contains at most k edges. It is less than or equal to not the shortest possible path from S to u, but to the shortest out of all of those that contain at most k edges.

We're going to prove this using mathematical induction. The base case is k equal to 0. At this iteration, the dist value for the starting node is 0 and all the other values are infinity. This corresponds to the lemma statement because the shortest path containing 0 edges from S to S, has length 0, and for all the other nodes, there is no such path which contains 0 edges and goes from S to those nodes.

The dist values are infinity, but the shortest paths can be considered to be infinity, so everything is okay at iteration number 0. Now, we need to prove the induction step, from k to k plus 1. Before iteration number k plus 1, dist value of u is already less than or equal to the smallest length of the path from S to u containing at most k edges. This is the assumption of the induction, and each path from S to u goes through one of the incoming edges into u.

These are the edges of the form (v, u). Relaxing the edge (v,u) is basically comparing it with the smallest length of a path from S to u through v containing at most k plus 1 edge. For any path from S to u, which is of at most k edges, dist value of u is already less than or equal to the length of this path even before k plus 1 iteration. On the k plus 1 iteration, for any incoming edge (v,u) and any path to v containing at most k edges, dist value of v is less than or equal to the length of the smallest path from S to v containing at most k edges.

Dist value of v plus the length of the edge (v,u) is an estimate of the smallest path going from S to u and having at most k plus 1 edges. Actually, as we try all the incoming edges from v to u, then we try all the possible paths of length exactly k plus 1 edges that go from S to u, and we try to relax by the dist value of u with the best possible such paths. After the iteration k plus 1, as we try to relax all such edges, the dist value of you will be not more than the shortest path out of all paths from S to u containing at most k plus 1 edges. We prove the induction step and lemma.

The corollary from this lemma is that in a graph without negative weight cycles, Bellman-Ford algorithm correctly finds all distances from the starting node S. Why is that? That is because for any path with at least v edges, it will contain a cycle because any graph that doesn't contain a cycle with v nodes, contains at most v minus 1 edges. It must be a tree or something like a subset of a tree.

Any path with at least v edges will contain a cycle, and this cycle can be removed from this path without making the path longer because any cycle is non-negative. Actually, any shortest path contains at most v minus 1 edges, and so it will be found after at most v minus 1 iterations. Bellman-Ford's algorithm will find correct shortest paths in this case. Another corollary which is stronger than the previous one, is actually that if there is no negative weight cycle, which is both reachable from S and such that vertex u is reachable from this negative weight cycle, then Bellman-Ford algorithm correctly finds dist value of u equal to the distance from S to u.

Even if there are some negative weight cycles in the graph, but node u is such that it is not reachable from a negative cycle, which is also reachable from the starting vertex, then the dist value for this node will still be correctly computed and will be equal to the distance from S to u. Why is that? Because anywhere in our proofs, we didn't actually use that there are no negative cycles at all. We just used that for any shortest path from S to u, if it contains a cycle, then we can just remove the cycle and the path will become shorter or of the same length.

This is true if u is not reachable from any negative weight cycle, which is also reachable from S. The Bellman-Ford algorithm works even for some graphs with negative weight cycles but only for those nodes which are not reachable from negative cycles, which are reachable from the starting node. In the next videos, we will deal with the negative weight cycles in a more general way so that our algorithm works always, although in some cases of course it will return that the distance from S to u is minus infinity because you can go from S to the negative cycle, then look through it for many, many times, and then when you want to get out of it and get to the node u. In this case, we just need to return that the distance from S to u is as small as you want.

Basically, it is minus infinity.
