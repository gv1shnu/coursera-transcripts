# Fastest Route

- **Course:** Algorithms On
- **Module 4:** Paths in Graphs 2
- **Lecture #:** 18
- **URL:** https://www.coursera.org/learn/algorithms-on-graphs/lecture/2kwZj/fastest-route
- **Extracted:** 2026-06-21 21:25:44

---

Hi. In this lecture, we're going to study Dijkstra's algorithm. It is a general algorithm for finding the shortest paths in weighted graphs in the case when all the weights of all the edges are non-negative. It can help you find the shortest way home, either in terms of distance or in terms of time to travel given the traffic conditions.

It can also help you to find the optimal route to send the network packet through the Internet so that it comes to the destination as fast as possible and has many more applications. We are going to start it on the example of finding the shortest route home from work or vice versa. The question is, what is the fastest route to get home from work? There are many services that help you to solve that problem.

For example, Yandex [inaudible] or Google Maps. These services can either find you the shortest path in terms of distance or the shortest path in terms of time to travel, given that they know the traffic conditions and the typical speeds that you can travel through different routes. How to solve this problem and how is it different from the previous problem of minimizing the number of transfers when you are traveling by a plane? Let's consider a very simple example where we need to get from point A to point B and there is a direct edge from A to B.

For the previous problem of minimizing the number of transfers, this is already the fastest route possible because this is the direct route. However, in terms of distance, for example, if the distance from A to B is five, then this could be not the shortest path, actually. There could be some node C so that the distance from A to C is two and the distance from C to B is also two. Then it's more optimal to go through point C from A to C and then from C to B and we will spend in total two plus two, only four, for example, kilometers.

If we go directly from A to B, it could be five kilometers. Of course, on this picture, it doesn't look like it's a true situation. However, it could be just that the road from A to B has a lot of turns and the roads from A to C and from C to B are very straight. That's why actually going from A to C and then from C to B is more optimal than going directly from A to B.

You see that, in this case, the solution is very different from the solution of the previous case when we needed to find the most direct route. One could think maybe the goal is not to find the most direct route now, it is actually to find the least direct route. That is also not true because if we change the length of the edge from A to B from five to three, then it immediately becomes the optimal route to go directly from A to B because from A to B directly is three and from A to B through C is two plus two, which is four, which is bigger than three. It depends really on the weights on the edges whether it is optimal to go directly or through some node C.

Of course, these are not the only options. In the general situation, our optimal route may contain a lot of intermediate edges and nodes. We want to solve this general situation and find really the shortest or the fastest route home. Let's get some intuition about how this works.

Remember that all the distances and all the times to travel from any point A to any point B, all those numbers are non-negative. Actually, they are positive because there is no such thing as negative distance from point A to point B or negative time to travel from point B to point C. This is the case of the graph where edges have non-negative weights. In our graph, nodes are some intermediate points where we can be and edges connect points, and the weights of the edges correspond to the distances or the times to travel from some nodes to some other node.

Let's look at a particular example of a graph where we know that the length of the edge from A to B or the weight of the edge from a to B. I will use those terms interchangeably, weight and length. Weight is three and weight of the edge from A to C is five, and all the other weights are actually unknown to us yet. We didn't look at them yet.

Now let's answer questions like, can we be sure that the distance from A to C is equal to five? We know that there is a path of length five from A to C and that is a direct path. Can we be sure that there is no shorter path from A to C? Well, actually, no, because the weight of the edge from B to C, which exists, we just don't know this weight yet, this weight might be equal to one, for example, and then the path from A to B and then from B to C, will have total weight of three plus one, which is four, which is less than the weight of the path from a to C directly.

So we cannot be sure that the distance from A to C is five. It could be smaller. By the way, in the case of weighted graph, by distance, we mean not the number of edges, as in the previous lecture, but the sum of the weights of the edges, as if you traveled from A to B and you spend three minutes and then from B to C you spend one minute then, totally, you spend four minutes to get from A to C through B. This is what we will mean by distance in this lecture.

In case of A and C, we cannot be sure that the distance is equal to five. What about A and B? Can we be sure that the distance from A to B is three given that we know the same information, that the weight of the edge from A to B is three and the weight of the edge from A to C is five, and we don't know all the other edges? The only thing we know about them is that they are all non-negative.

Well, in this case, yes, we can be sure because B is the closest out of the nodes for which we know distance from A and there are no other ways to get out from A rather than either go directly to B or go from A to C. If we go from A directly to B, that already takes us three, so we cannot get to B faster. If you go from A to C, then it already takes five minutes just to get from A to C. Even if we travel further from C somewhere, we know that all the other weights are non-negative, so the time will go and will increase and we cannot be in B less than in five minutes after leaving A.

Actually, as we have the path of length three from A to B directly and we cannot get there quicker by going through C and using some other intermediate nodes maybe, so we can be sure that the shortest path from A to B is indeed three. You see the difference? When we discover some nodes which are adjacent to A and we take the closest out of them, we can be sure that we know already exactly the distance to the closest node out of the neighbors of A. But for all the other nodes, it might be the case that we don't know the exact distance to them because it can be improved by going through the node which is closest to A and then using some shortcut to get to the node which we need.

This is the general intuition, and in the next videos, we will use it to come up with a good algorithm to find all the correct distances from A to all other nodes.
