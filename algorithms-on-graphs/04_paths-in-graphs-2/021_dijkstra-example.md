# Dijkstra Example

- **Course:** Algorithms On
- **Module 4:** Paths in Graphs 2
- **Lecture #:** 21
- **URL:** https://www.coursera.org/learn/algorithms-on-graphs/lecture/ZS5pm/dijkstra-example
- **Extracted:** 2026-06-21 21:26:15

---

Hi. In this video, I will show you an example of how Dijkstra's algorithm works on a specific graph. This is our graph. We have all the edges with their weights.

We have the starting node on the left. We already set the distance to this node to zero because we know this is the starting node, and for all the other nodes we set distances to plus infinity. Dijkstra's algorithm will process vertices one by one, and when the vertex is about to be processed, we will color it with black. We'll start with coloring our first vertex with black, and also we recolor the number zero into green, because we're sure that this is already the correct distance to this node.

When we process the node, we consider all the outgoing edges in some order, and we'll try to relax those edges. For example, first we consider this edge of length three, zero plus three is three so we can improve the current estimate for the end nodes of this edge from plus infinity to three, and we do that. Now we consider the second edge outgoing from the starting vertex. It has length 10, zero plus 10 is 10, which is less than plus infinity, and so we'll relax this edge and set the distance estimate to 10.

Now, we need to select the next node to process, because we've processed all the outgoing edges from our starting node, and so we're going to take the node with the smallest dist value out of all the nodes which are not in the known region yet. There is only the node with distance zero in the known region now, so now we're going to take this node with distance three as the next node into the known region. We color it with black, we color the distance to it with green, because now we're sure that the distance to this node is three and it won't decrease anymore. Now we need to process this node.

We go through all the outgoing edges. First, this edge of length eight, three plus eight is 11. Eleven is bigger than 10 so we cannot actually relax this edge, so we ignore it. Next edge has length three, three plus three is six, six is less than plus infinity so we update the dist value to six and the next edge has length of five, three plus five is eight.

Eight is less than infinity so we update plus infinity to eight. Now we have processed this node and we need to select the next one to include in the known region and of course this is the node with the distance estimate of six, which is the minimum of all the left nodes. We color it with black, color the distance with green, now we're sure that the distance of six and represses the outgoing edges first goes the edge of length two, and it updates the dist value of the corresponding node from infinity to eight. Second edge is one, six plus one is seven.

Seven is less than eight so update eight to seven and the next edge is this one of minus three, six plus three is nine. Nine is less than 10, so we update the distance estimate of this node to nine. Now we have processed all the outgoing edges and we need to again select the next node, to include in the known region. This is the node with the dist value of seven, so we go with black, we color the distance with green because we're sure it is seven and 21 degrees and we process the outgoing edges.

There is only one outgoing edge of length zero here, so we update the node because seven plus zero is seven. Seven is less than eight and so the distance decreases. It is now seven. Now we select the rightmost node as the next to include in the northern region because the dist value is seven, seven is less than nine, so we color it with black.

We color the distance with green because it is now the final distance. We don't need to process any outgoing edges, because there are no outgoing edges. Now we select the last node as the node to include in the known region and we color it with black and the distance to this node is nine, and it is now the final distance. But actually we need to process this node too because who knows maybe we'll find more nodes.

We first process this edge. Nine plus five is 14 bigger than seven, so we ignore this edge, and now this edge of length two, nine plus two is bigger than three, so again ignore this edge and now actually we can finish because we have processed all the nodes and we know all the distances to all these nodes, and we process all the edges. There won't be any new nodes for which we actually knew to estimate the distance. This was the example, and in the next video we're going to implement Dijkstra's algorithm in the general case.
