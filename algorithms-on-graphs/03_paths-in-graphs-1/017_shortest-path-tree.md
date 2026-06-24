# Shortest Path Tree

- **Course:** Algorithms On
- **Module 3:** Paths in Graphs 1
- **Lecture #:** 17
- **URL:** https://www.coursera.org/learn/algorithms-on-graphs/lecture/X7NUe/shortest-path-tree
- **Extracted:** 2026-06-21 21:25:34

---

Hi. In the previous videos, we've implemented the BFS algorithm, analyze its running time, and proved its correctness. Now we have an algorithm to answer questions like, what is the minimum number of transfers to get from London to Paris? To do that, we just select a node for London as the starting node, launch BFS algorithm starting from the starting node, and find the distances from London to all the other cities.

Those distances will be exactly the minimum number of transfers to get from London to this or that city. If we choose Paris as the second city, then we will know the minimum number of transfers to get from London to Paris. However, it is funny because we could be in the situation where we know that the minimum number of transfers from one to Paris is two but we don't know which two flights we could take to get actually from London to Paris. That's unfortunate.

We want to know not only the minimum number of transfers, but actually the exact flights to fly from London to Paris using minimum possible number of transfers. In this video, we're going to augment our BFS algorithm to be able to also answer this question. To do that, we will introduce shortest-path tree. On the left, we have an example graph for which we could take node A as the starting node and find all the distances from A to all the other nodes.

On the right, we have all the nodes of this graph positioned according to their distance layers from node A. Node A is on the topmost layer zero, then B, D, E, and F are a distance one from A, so they're at the Layer 1 and so on. Also, the graph on the right has directed edges and it has less edges than the initial graph. This is because this is a new graph which we are going to call shortest-path tree.

To build it we first arrange all the nodes into the distance layers as of the nodes of the initial graph. But then we only draw an edge from node B to node A, for example. If node a is the previous node for node B, and when I say previous, it means that node B was discovered while we were processing node A, then A is the previous node for B. If node C was discovered while we're processing node B, then B is the previous node for node C.

So for every node, but for the node A, there is a previous node. For node A, there is no previous node because it was discovered first. We draw an edge from any node to the previous node and we get some graph. This graph is going to be a connected graph if we made it undirected by removing the arrows.

Because for any node in this graph, there will be a path from this node to node A by going to the previous node, then to the previous node, and so on. At some point the previous node will be node A because this is the starting node. If there is a path from any node to node A, it means that there is a path from node A to any other node, and it means that the graph is connected. To prove that it is indeed a tree, we just need to prove that there are no cycles in this graph.

The Lemma states exactly that the shortest path tree is indeed a tree because it doesn't contain cycles. Now we're going to prove this Lemma, and we're going to assume that there is a cycle in the graph we just built. For example, this is a cycle B, C, D, E, F. Now let's analyze what happens here.

We know that in the graph we've built, there is at most one outgoing edge from each node. Actually exactly one edge for all nodes but for the starting node A and node B can be previous for the node F, and node F can be previous for node E. Node E is previous for node D, and so on. This is how this cycle could be formed.

Then we should also note that when we look at any edge, the distance from node A decreases if we go through this edge. Because this is an edge from a node to the previous node, and it means that when the node was discovered, the previous node was being processed. It means that the distance to the discovered node was assigned to the distance to the node B in process plus one. When we go through an edge, the distance decreases exactly by one.

Assume that the distance to the node F is some number D. Then if we go through the edge from F to B, it means that the distance to the node B is D minus one. Then if we go from B to C, it means that the distance to C is d minus 2 and so on, d minus 3, d minus 4. At some point as this is the cycle, we are going to return to the node F.

But then the number will be strictly less. D is not equal to d minus 5 or d minus any other length of the cycle. This cannot happen because distance to F cannot be simultaneously D and some numbers strictly less than D. This is a contradiction with the assumption that there is a cycle in our graph.

Our graph is indeed a tree. Now, why do we call it a shortest path tree? Well, because for every node, there is a previous node in this tree. This previous node is exactly one edge closer to the starting node.

If we follow the route from the node to its previous node and then to its previous node and so on, we at some point will come to A, because A is the starting node. We'll come to A using exactly so many edges as is the distance from A to the initial node, because at each step we'll decrease distance exactly by once. If we do d steps, we decrease the distance by d and we come to node A at distance 0. Our path will contain exactly D edges and it will be a shortest path from node A to the initial node.

We went in the different order. We went from node to the previous node to the previous node. This is actually in the opposite directions to the edges of the initial graph. To get the shortest path, we will need to reverse the path and starts from A, then go to some node, and so on up to previous node of our node and then to our node.

This is the way to build the reverse shortest path. Then we just need to reverse it again to get the actual shortest path from A to any node in the graph. To do that, we first need to construct the shortest path tree itself. We're introducing array prev to store the previous node for any node.

Initially, we initialize prev of you with nil, which is a pointer to nowhere, basically. As soon as we discover some node v in the last line, apart from putting it in the Q and assigning distance value for it, also assign the previous node for node v to the node u, because node v was discovered while we're processing node u. This way we will construct the whole shortest-path tree. For every node, but for the starting node A, there will be a previous node for this node.

Then to reconstruct the shortest path from node A to some node u using array prev is to do the following. This is the procedure reconstruct path which will return that path itself from A to u, and this will be the shortest path. We initialize the result of this procedure with an empty list of nodes. Then we are starting with the node u.

While this node u is still not back to the node 8, we add this node to the result and we go to the previous node, and then we repeat until we go to the previous node until we come to the node A. That means that we have the whole reverse shortest path from A to u. The only thing we need to do to return actually the shortest path from A to u is to reverse this result again. We return the reverse of the result.

This is the way to reconstruct the shortest path from A to any node u. Now we have the BFS algorithm augmented with the construction of the shortest path tree. The procedure reconstruct path to actually reconstruct the shortest path from A to any node in the graph. This allows us to not only find the minimum number of transfers to get from London to Perth, but actually to find the exact way to get from London to Perth using this minimum possible number of transfers.

To conclude, now we can find minimum number of flight segments to get from one city to another. That, of course, applies not only to flights but also to trains or bus changes and things like that. We can reconstruct the optimal path, not only know its length, but actually find some optimal paths, some shortest path. We can build the whole tree of shortest paths from one origin.

We not only find the distance from one node to some other node, but actually, we know all the distances from one node to all the other nodes and we can quickly reconstruct the shortest path from this node to any other node. It works in time proportional to sum of the number of edges plus number of the nodes in the graph. In the next lecture, we're going to solve a similar problem. But when edges have weights, like when you want to go from home to work, you need to optimize not the number of streets you go through or turns you take, but actually the time that it takes you to get from A to B.

Then you can estimate how long does it take to get from this point to this point on some road. Then you can find the path to minimize the sum of the times. This is what our next lecture will be about.
