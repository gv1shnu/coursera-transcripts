# Dijkstra's Algorithm

- **Course:** Algorithms On
- **Module 4:** Paths in Graphs 2
- **Lecture #:** 20
- **URL:** https://www.coursera.org/learn/algorithms-on-graphs/lecture/oL85Y/dijkstras-algorithm
- **Extracted:** 2026-06-21 21:26:05

---

Hi. In this video, we will study Dijkstra's algorithm for finding shortest paths from a single node to all the nodes in the graph. Let's remember our intuition. We start with a node A and we want to find all the shortest distances from A to all the other nodes.

We know that the distance from A to itself is zero. Now on the next step let's just take all the edges outgoing from A and relax those edges. For A we know the exact distance. We take all the outgoing edges from A.

It turns out that there are only two outgoing edges. We relax them. We now have estimates that the distance from A to B is at most five, and the distance from A to C is at most 10. As we discussed in the first video of this lecture, now, we can be sure that the distance from A to B is equal to 5.

We cannot be sure that the distance from A to C is equal to 10. It can decrease later. But for B we can be sure that the distance is five. Now that we know the distance for B, we mark it with a color and we are going to relax all the edges outgoing from B now.

First we find that there is an edge from B to C with weight three, and this edge actually updates the estimate dist of C because our best estimate with the distance from A to C is 10. But now we see the path of length eight from A to C through B. We update dist of C with value eight. Also we find more outgoing edges from B.

They lead to nodes D and E. Now we have an estimate for the node D that the distance is at most 12. For node E, that the distance is at most 6, and for node C that the distance is at most eight. Now, what is the next vertex for which we already know the correct distance?

Well of course it is the vertex E because this is the vertex with the minimum known estimate. For any other vertex, if we go through it, then we'll already spend more than the path we know to E. We cannot get to E faster than through the best currently known path, because either we go to E directly from B and we get exactly the estimate of six. Or we go from B and then to C or to D, and then we will spend already at least path of length eight and all the future edges will be non-negative.

So we can spend less than six. For E we can be sure that the distance is six. For C and D, we cannot be sure what are the distances to them. We only they have the upper bounds of eight and 12 respectively.

The main idea for the Dijkstra's algorithm, in general, is that we maintain a set R of vertices for which the dist value is already set correctly to the correct distance. This is the known region. Initially, we only add the starting vertex A to the known region R because for the starting vertex, we know that the distance to this vertex is exactly zero. We can add it to the known region.

Then we are going to include more and more nodes to the known region one by one. Basically on each step, we will take the vertex which is not in the known region, but with the minimum dist value out of all those vertexes. We'll add it to the known region. We'll say that again, the dist value for this vertex is already correct and we can add it to the known region.

Then we're going to relax all the edges outgoing from this vertex to update some of the dist values for other nodes which are outside of the known region. We will proceed until all the nodes are in the known region. This is how the algorithm works. In the next few videos, we will see the example of how it works.

We will implement it, prove its correctness, and analyze its running time.
