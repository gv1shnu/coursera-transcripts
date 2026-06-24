# Paths and Distances

- **Course:** Algorithms On
- **Module 3:** Paths in Graphs 1
- **Lecture #:** 11
- **URL:** https://www.coursera.org/learn/algorithms-on-graphs/lecture/rns9h/paths-and-distances
- **Extracted:** 2026-06-21 21:24:29

---

Hi. In this video, we are going to study paths in graphs and distances between nodes in the graphs. First, let's define the length of the path as the number of edges that this path goes through. For example, the green path on the slide has length of four because it goes through four edges, BC, CF, FE, and ED.

This another path has length of three because it goes just through three edges, BA, AF, and FD. Although these paths connect the same two nodes, B and D to each other, they have different lengths and the second path is shorter. So it is better for us if B and D were cities and the edges were the direct flight between those cities. The distance between two nodes in a graph is the length of the shortest possible path between these nodes in this graph.

For example, the distance between B and D in this graph is three because there is a green path of length 3, B to C to F to D, and you can check that there is no path that is shorter. That is, it has only one edge or only two edges. The distance between A and C is two because there is a path of length 2, for example, A to B to C or A to F to C, and there is no direct route from A to C so the distance cannot be one because there's no edge from A to C directed. Everything changes a little bit when the graph is directed instead of undirected.

For example, the distance from B to D in this graph is already not three. It is actually four because there is this path B to A to F to E to D, and this path has length 4. The path that we had in the previous example that is going through node F, for example, B to C to F to D, is no longer possible because the edge from F to D goes in the opposite direction, and it doesn't go in the direction from F to D so we cannot use this edge in the path. The distance from A to C in this graph becomes infinity.

Because actually, it is impossible to get from A to C. If we try to get from A through the edge from A to F, then it is not possible to get from F to C because the edge from C to F goes in the wrong direction. It is actually not possible to get from A through B because the edge from A to B goes in the opposite direction from B to A. There is no way we can get from A to C using any path.

In this case, we consider the length of the paths infinity and the distance from A to C also infinity. Now let's see what happens if we consider a single node in the graph and all the distances from this node to all the other nodes. In this case, it's convenient to place all nodes into several distance layers. We number these layers from zero and the node itself A is in the level number 0, and this is the only node that is in this level because this is the only node for which the distance from A equals to 0.

Then go all the nodes, which are at distance 1 from node A. Those are the cities to which we can get with a direct flight from A. Those are B and F because there are edges AB and AF. Then go all the nodes at distance 2 from A.

Actually, all the other nodes are at distance 2 because there are paths of length 2 from A to them. This is the same graph, we just repositioned all the nodes. Nodes are going from top to bottom with increasing distance from A. There are some other properties when we represent a graph in this way with several distance layers.

Let's consider what happens if we add a new node, for example, a node G, which is connected only to node C. In this case, the distance to the node G is three, going with the path A, B, C, G. This makes us create a new distance layer number 3. What other edges are possible when we have the structure of several distance layers?

For example, it is not possible that we have an edge from node B to node G in this structure. Why is that? Well, that is because if there was such node, then the distance from A to G would become just two because there is a path A to B to G, which has length 2. Then G couldn't be in the level 3, it should be in layer 2.

If G was in layer 3 and that is fixed, then there cannot exist an edge from B to G, which is marked with red. Now let's consider some other edge. For example, from A to G. This edge is actually also not possible, because if there existed such edge, then G should be in the layer 1 right there.

But G is in the layer 3, so this red edge cannot exist. In general, only the edges which go between nodes inside somewhere or the edges which go from a layer to the adjustment layer, those are the only edges which are possible if we have an undirected graph and we fix all the nodes at some distance layers from some starting node A. Now, what happens if the graph is directed? Then again, everything changes a bit.

For example, can we have an edge from G to D? Well, yes. That's possible because the edge from G to D doesn't make node D closer to A and doesn't make node G closer to A, so everything is okay. Actually, can we have an edge between nodes which are not in the adjustment layers?

We couldn't have that for the undirected graph, but we can do that in a directed graph. For example, an edge from G to F can exist because this doesn't make node F any closer, it's already at distance 1. It also doesn't make the node G any closer because this edge goes from G, not to G. It doesn't make node G closer, so this edge can actually exist without breaking the structure of distance layers in the directed graph.

What else? There can be an edge from B to F that doesn't make node F any closer because it's already at distance 1. But actually some edges are still not possible. For example, the edge from B to G can be in the graph because if it was in the graph, then the distance to G would be just two, not three.

We would have a path A to B to G, and then G would be at the layer 2. In the directed graphs, many more edges are possible. Basically, not only the edges between the nodes in the same layer or in adjustment layer are possible, but also any edges from a layer to any of the previous layers is possible. However, edges from a layer to layers more than one forward are not possible because that would make nodes in those forward layers closer to the node A than their distance layer.

The structure of distance layers is very inconvenient if you want to find the shortest path from A to any node. Basically, you know that the distance is the number of the layer where the node lies, and to find the path, you just go back through layers. You always select any edge that goes into this node from some node from the previous layer. There always exists such a node.

Then if you go every time one layer up, one layer up, one layer up, then you will get the path of exactly the needed length. If we had some algorithm that could represent our graph in this form in the form of several distance layers, then we could use this algorithm to find the shortest paths and the distances from a single node to all the other nodes in the graph, and this is what we're going to do in the next video.
