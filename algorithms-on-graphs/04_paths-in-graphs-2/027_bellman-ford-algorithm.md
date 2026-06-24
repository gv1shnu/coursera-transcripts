# Bellman-Ford Algorithm

- **Course:** Algorithms On
- **Module 4:** Paths in Graphs 2
- **Lecture #:** 27
- **URL:** https://www.coursera.org/learn/algorithms-on-graphs/lecture/22cu6/bellman-ford-algorithm
- **Extracted:** 2026-06-21 21:27:21

---

Hi. In this video, we're going to introduce Bellman-Ford algorithm that will find shortest paths in graphs with negative weighted edges, but in the case where there are no negative weight cycles. You saw in the previous video that negative weight cycles are very nested theme. Because of them, the distances can be minus infinity, so we want to avoid this case for awhile and we'll introduce an algorithm that works even in the case when there are negative edges in the graph, but there are no negative weight cycles.

This is called Bellman-Ford algorithm. Remember the naive algorithm from the lesson about Dijkstra's algorithm and the shortest path for graphs with weighted edges with non-negative weight? It turns out that this naive algorithm would just relaxes edges while at least one dist really changes. It actually works even when there are edges with negative weights, at least in the case when there are no negative cycles.

This is the relaxation procedure. It's a standard. If we can improve the dist value of E by dist value of u and the weight of the edge connecting u and v, we do update it and also update the previous node for v to become u. Here is the code of the Bellman-Ford algorithm.

It is pretty simple. Again, assumes that there are no negative weight cycles in the graph G. For all nodes u, we initialize the dist values with infinity as usual and the prev values with the pointer new nowhere as usual, and then we initialized the dist value of the starting node to zero. This is also as usual, and then we do V minus 1 iterations, where V is the number of nodes in the graph.

On each iteration, we just try to relax all the edges in some order. We'll just call this procedure relax. It tries to relax an edge. If it succeeds, it updates something.

If it doesn't succeed, it doesn't update something, it doesn't matter. We just make sure that we go through the list of all edges, V minus 1 times. That's all. For now, we're not going to prove that this algorithm returns correct values.

We're going to analyze its running time and show the example of how it works. The running time of Bellman-Ford algorithm is V times E, where V is the number of nodes and E is the number of edges. This is very intuitive because to initialize the dist values, the prev values we just need big O of V and later we do V minus 1 iterations. Each of them is big O of E, so total time is V times E.

Now let's look at an example of how this will work out for this graph. We start with a graph where only the distance to the subject node is zero and all the other nodes have dist values of infinity. We have some directed edges with weights. Some of the weights are actually negative.

You see that there is no negative weight cycle, ABC in this case, because ABC is actually not a cycle because the edge doesn't go from C to A, it goes from A to C. There are no other negative weight cycles, so it is actually possible to find the shortest paths from S to every other node. Let's see how this algorithm will do that. First iteration, it tries to update all the edges to relax all the edges.

Start, for example, with the edge from S to A and it doesn't have to be solved, but let's assume it starts with this edge. Then 0 plus 4 is less than infinity, so update the dist value for A. It is now four. Next, this edge.

0 plus 3 is less than infinity, so we update the dist value from B to three. Then with this edge 4 plus minus 2 is 2, which is less than three, so we again update the dist value from B to two. With this edge, 4 plus 4 is less than infinity, so update dist value of C to eight. Then this edge, 2 plus minus 3 is minus 1, which is less than eight, so update C to minus 1.

This edge, 2 plus 1 is 3 less than infinity, so update D to three. Last edge from C minus 1 plus 2 is just 1, which is less than three, so we again update dist value for D. With this, our first iteration is finished. We tried to relax all the edges.

Some of them did relax, some of them didn't. At this one more iteration actually we have five nodes, so we need to do four iterations. But of course, if at some iteration nothing changes, it won't change on the next iteration. Let's see when this process actually stops.

We tried to relax this edge. 0 plus 4 is 4. It is the same as the dist value of A, so no need to relax. 0 plus 3 is bigger than two, so no need to relax.

4 plus minus 2 is equal to 2, so no need to relax. 4 plus 4 is 8 bigger than minus 1, no relaxation. 2 plus minus 3 is minus 1, no relaxation. 2 plus 1 is 3 bigger than one, no relaxation.

Minus 1 plus 2 is 1, again no relaxation. In this case, after the first iteration, we do the second iteration and nothing changes, and so we'll do of course the third iteration, the fourth iteration, but still nothing will change. In the end, we will get these distances. The distance from S to itself is zero, to A is four, to B is two, and to C it is minus 1.

This is because our edges can be negative, so even the shortest paths can be negative. The distance to node D is one. This is an example of how Bellman-Ford algorithm works. In the next video, we're going to prove that it works correctly in the absence of negative cycles.
