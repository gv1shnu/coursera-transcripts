# Breadth-First Search

- **Course:** Algorithms On
- **Module 3:** Paths in Graphs 1
- **Lecture #:** 12
- **URL:** https://www.coursera.org/learn/algorithms-on-graphs/lecture/bxu5y/breadth-first-search
- **Extracted:** 2026-06-21 21:24:40

---

Hi. In this video, we're going to study the algorithm called breadth-first search. It is one of the most basic graph algorithms and it is used as a building block in many other graph algorithms. But also this algorithm alone will solve our problem of finding the minimum number of transfers to get from one city to another using plane flight.

In the previous lecture, we introduced the notion of distance layers for some fixed node A and all the other nodes and the distance to them from the node A. Let's see how it would work if we could come up with an algorithm that could just list nodes layer by layer. It would start with discovering the node A itself. When we discover a node, we color it with gray.

We've just discovered node A, and of course, we understand that this starting node A is at distance zero from itself. We put it in the distance layer number zero, and then we need to process this node to find all the other distance layers, all the other nodes. When we process a node, we color it with black. Now, to process the node, we just take all the edges outgoing from this node and discover the nodes to which these edges go.

We go to these four nodes from node A with direct edges. All the nodes are the nodes at the distance layer one because there is a direct edge from A to each of those nodes and there are no more such nodes. These four nodes are the only nodes at the distance layer one. We've just discovered them, and that's why we mark them with the color gray.

Then we need to process all of them. We color all of them into black. To process them again, we need to consider all the edges outgoing of these four nodes at the layer one, which we have just discovered, we continue to all the outgoing edges. Some of them are white-black edges, which lead to new nodes, which are not discovered yet.

And we discovered them and we color them with gray, so we discovered four more nodes. Also, there are edges colored with red. Those are the edges which are useless because they lead from black nodes to other black nodes which were already discovered and are now being processed. These edges give us no new information.

However, we didn't know that in advance, so we had to look through all those edges and we just mark them with red to distinguish them from the black edges, which give us new information. The black edges led us to four more nodes that are at the distance of layer two, because they are at the distance one from the nodes which are in the layer one, and they are not in the layer one themselves, so they are at the distance layer two. We've just discovered them. Now we need to process them, to process them we color them with black and we consider all the edges outgoing from those four nodes.

It turns out that all of those edges are red, they are useless. We cannot discover any more nodes because we've already discovered and processed all the nodes. All these edges are red and this is when our algorithm actually stops. It has discovered all the distance layers.

Now we can mark the nodes with the number of their distance layer. The node A is the distance layer zero. The next four nodes are in the distance layer one and the outer four nodes are in the distance layer two. Actually if we had some far away node which is not connected to any of these nodes, then it will have distance infinity from node A and so it would be in a separate layer with distance infinity.

Now let's see what happens when the graph is undirected. Node a is again initially marked with blue, just to mark that this is the single node from which we are going to build all the distances. Now first, this node is undiscovered and we discover it by marking it with gray, and we put it into layer zero. This is the only node in the layer zero.

Now we start processing this node. We consider all the edges outgoing from this node. In this case, we discover five nodes. All of these nodes are in the distance layer one and only these nodes are in the distance layer one.

So we discovered them and now we need to process them. To do that, I consider All the edges outgoing from these five nodes. Some of them are red because they lead to other black nodes which are already discovered. Some of them are black because they lead to new nodes which are yet undiscovered.

We discover them. Three more nodes are discovered and they are at the distance layer two. Now we need to also process those nodes. We color them with black.

All the edges outgoing from those nodes are red because they lead to other nodes which are already black. Now again, we can mark every node with the distance layer which lies in node A's in the distance layer zero. These five nodes which are discovered in the first step are in the distance layer one. These three nodes are in the distance layer two.

Again, if we had a faraway node which is not connected with any of these, then it would have distance infinity from A and it would be in a separate distance layer infinity. This is how we would like our algorithm to work. However, something happens that cannot happen in the real algorithm. We're just covering several nodes at the same time with our algorithm.

This cannot happen. We can only discover nodes one-by-one because we cannot do actions in parallel. We need to change our algorithm a little bit so that it discovers all nodes in the same order, more or less but out of the nodes which are in the same distance layer. It doesn't matter in which order we actually discovered them.

We just need some orders. That node in the layer zero goes first, then go all the nodes in the layer one, then all the nodes in the layer two and so on. To do that, we're going to use a data structure called queue, which you could have learned in one of our previous courses.
