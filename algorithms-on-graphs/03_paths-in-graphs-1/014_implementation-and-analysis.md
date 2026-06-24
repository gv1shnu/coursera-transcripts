# Implementation and Analysis

- **Course:** Algorithms On
- **Module 3:** Paths in Graphs 1
- **Lecture #:** 14
- **URL:** https://www.coursera.org/learn/algorithms-on-graphs/lecture/gAXPb/implementation-and-analysis
- **Extracted:** 2026-06-21 21:25:02

---

Hi, in this video we're going to implement the breadth first search algorithm described in the previous video and to analyze its running time. The breadth first search algorithm is often called BFS in the literature or for brevity. And the BFS procedure here is implementing this algorithm. It takes us input graph G and node A.

Node A is the starting node and the algorithm will find all the distances from A of all the nodes in the graph, including not A. Also assume that we know the set of nodes V and the set of edges E in the graph G. We start by assigning distance of infinity to all the nodes from the node A because we didn't find any beds from A to any of the nodes yet. And for the nodes for which we won't find any beds, the distance will stay infinity.

And those will be the nodes which are not reachable from A. Also initialize the distance to node A itself with zero because we know that this node is in the layer zero. And then we initialize our Q. We put a single node there, that is the starting node A.

And then starts the main loop of our algorithm. Basically what happens is we look at the Q and if there is something in it, if it's not empty, then we take the top element of the queue and process it. The top element of the Q is some node and we process it by processing all the edges out going from this node. So we start by taking the top node from the queue, we remove it from the queue, and we save it to node u.

And then we go through all the edges outgoing from u. Those are edges of the type of uv which are in the side of the edges of the graph, which is E. So we consider all those outgoing edges. And we need to detect whether this node v in the end of this edge is a new node which was not discovered before or is it a node which was previously discovered.

In our case, it is easy to determine that. Because if the node was not discovered before, then the distance to this node is infinity. And as soon as the node is discovered, the distance to this node will be updated. So we just compare the current dist of v to infinity.

If it is equal to infinity, then this node is yet white. In terms of description from the previous video, we haven't discovered this node yet. So we need to be add it to the queue to color it with gray. Which is the same as added to the queue and to update the distance to this node.

So on the next line we add the node v to the queue, that way it becomes discovered and gray. And also we update the distance to this node v to distance to node u plus 1 because we know that we've just discovered this node v. And so it is in the next distance layer from the layer of the node u. And then all this happens for several generations until we process all the nodes which are in the queue.

Note that sometimes we add nodes to the queue, sometimes we remove nodes from the queue. So we need to prove that this algorithm will stop because maybe this while loop will go forever. And we also need to prove that it will stop after some reasonable number of iterations. And this is what we're going to do in the analysis.

So, actually, the lemma states that the running time of breadth first search is big O of size of the set of edges plus the size of the set of nodes of the graph. And this implies that the algorithm stops and stops in the time proportional to the sum of those sizes. So to prove that we need to notice that each vertex is enqueued, so put in the queue, at most once. Why is that?

Because as soon as this node is put in the queue, its distance is updated and it becomes from infinity to some finite number. And after the node is marked with some finite distance, it cannot go into the queue for the second time. Because before putting a node into the queue we compare its distance to infinity. And if it's not equal to infinity, we'll just ignore this node.

So each vertex is enqueued at most one. So each vertex will be processed at most once. And so it means that each edge examined either only once for the case of directed graphs or at most twice for the undirected graph. Because for the undirected graphs the same edge from u to v can be considered both when you process node u and when you process node v.

And if the graph is directed, then the edge uv can be only considered when we process node you. And as we process each node at most once, no edge can be processed more than two times. And so basically everything we do is we process either a node or an edge. We know that we process each node and each edge at most constant number of times.

And this proves that the running time of the breadth first search is proportional to the number of edges plus number of nodes.
