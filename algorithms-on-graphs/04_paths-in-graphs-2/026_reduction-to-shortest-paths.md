# Reduction to Shortest Paths

- **Course:** Algorithms On
- **Module 4:** Paths in Graphs 2
- **Lecture #:** 26
- **URL:** https://www.coursera.org/learn/algorithms-on-graphs/lecture/cw8Tm/reduction-to-shortest-paths
- **Extracted:** 2026-06-21 21:27:10

---

Hi? In the previous video, we introduced the problem of currency exchange, optimal currency exchange, and we reduced it to some problem on a graph, but this was rather a strange problem. In this video, we're going to reduce it to a standard shortest path problem on a weighted graph. This is the problem we've finished with in the previous video, and basically it says that we need to maximize the product of weights of edges over all the paths from one node to another in the graph.

What is strange here is first that we need to maximize something instead of minimize something as in the shortest path problems. The most strange thing is that we need to maximize our products. While we can do something with the sums, we don't know how to do anything with products yet, so actually we want to do minimization instead of maximization and we want to do summation instead of multiplication. How to do that.

Actually, there are two standard approaches. First, to replace product with the sum, we just take logarithms. The second to solve minimization problem instead of maximization problem, we just negate the weights. To be more specific, let's see both approaches first, taking the logarithm.

On the left, we have the product of x and y. But you can rewrite this product as a product of two to the power of logarithm x base 2 and 2 to the power of logarithm of y base 2. Because these two multipliers are still equal to correspondingly x and y. This in turn is equal to 2 to the power of logarithm of x plus logarithm of y.

Thus, there is a correspondence between product of x and y and some of their add logarithms. More specifically, if we want to maximize the product of x and y, it is equivalent to maximizing the sum of the logarithms of x and y. On a specific example, if we are multiplying 4, 1 and 1/2, this is equal to 2 and this is equal to 2 to the power of 1. Now, if we take logarithms of all the three multipliers and do summation instead of multiplication, then we'll have logarithm of 4 base 2 plus logarithm of 1 base 2 plus logarithm of 1/2 base 2.

The first logarithm is equal to 2. The second logarithm is equal to 0, and the third logarithm is equal to minus 1 and the sum is 1. What do we get as the power of 2 in case of logarithms, we get this as the result of summation. Basically, our problem of maximizing the product of exchange rates over some paths is equivalent to maximizing the sum of logarithms of those exchange rates over the same paths.

Now, we can actually reduce our problem to maximize the total weight of the path from one node to another by replacing the initial weights, which were the exchange rates with their logarithms. Now, we have a maximization problem, but this is still not something we would like to solve because we only know how to solve the minimization problem and this is a maximization problem. To reduce this further to a minimization problem, you should know that to maximize the sum of logarithms is equivalent to minimize minus the sum of logarithms. This doesn't yet give us convenient reformulation though.

Instead, we'll say that to maximize the sum of logarithms is equivalent to minimize the sum of mean of minus logarithms. If we replace each logarithm with its negation, then we will need to solve the minimization problem. If we do both steps, then we basically need to replace the initial edge weights are corresponding to edge e_i, which are actually the exchange rates by minus logarithm of the initial weight. Then what we need to do is to find the path with the minimum sum of weights on the edges between the node corresponding to the US dollar and the node corresponding to the Russian ruble.

This is basically the shortest path problem. We just need to find the shortest path from US dollars to the Russian rubles, and we already know how to solve that problem. It seems we've solved the initial currency exchange problem now because we can create the currency exchange graph with weights r_e_i corresponding to the exchange rate. We can replace these initial weights with minus logarithms of these weights.

We can find the shortest path from the US dollars to Russian rubles by Dijkstra's algorithm. That will give us the optimal sequence of operations. Then we can take the initial exchange rates corresponding to the edges and just compute how many rubles we'll get. Looks like a solution.

Well, not so easy actually. Dijkstra's algorithm relies heavily on the fact that the shortest path from s to t goes only through vertices that are closer to s than t. Basically, it relies on the fact that all the edge weights are non-negative. But this is no longer the case for graphs with negative edges.

If we have some starting node s and an edge from S to A of length 5 and an edge from S to B of length 20, then Dijkstra's algorithm, after seeing that these two outgoing edges are all the edges going from the starting node will decide that we already know the shortest path from S to A, because A is the node with the shortest dist value of 5 out of all the nodes in the unknown region, and so Dijkstra's algorithm would declare that the distance to node A is exactly 5. However, in the case of graphs which can have negative weights on the edges, that will be just plain wrong because in this graph there is a path from S to A through B, which has the total weight of minus 10, because it's 10 plus minus 20, and because of this edge with negative weight, the distance to node A will be determined incorrectly by Dijkstra's algorithm. It won't be the optimal way to exchange currency. We need some other algorithm to solve our problem.

This was just theoretical example and a more practical example with some exchange rates close to what could be in the real world is the following. We have just three currencies, Russian rubles, Euros and US dollars. The exchange rate from Russian rubles to US dollars is 0.015, from Russian rubles to Euros is 0.013, and from Euros to US dollars, it's 1.16. If we multiply 0.013 by 1.16, it turns out that this is bigger than if we go directly from Russian rubles to US dollars.

When we take the minus logarithms of these exchange rates, here's what we get. We get the edge from Russian rubles to US dollars of length 6.05 something and from Russian rubles to Euros 6.26 something. Our Dijkstra's algorithm would decide that the edge from Russian rubles to US dollars determines the shortest path from rubles to dollars in this graph. But actually, there is a shorter path going through Euros and our Dijkstra's algorithm won't understand that and we'll give an incorrect answer.

Actually, there is even nastier problem when you allow negative edges, and this is negative weight cycles. In this example, the cycle A, B, C is negative cycle because from A to B is minus 2, from B to C is minus 3, and from C to A is 4. The sum is minus 1. If you want to get from S to any other node, either A, B, C, or D, you can go through this cycle as many times as you wish, and it will decrease the total weight as much as you can.

Actually the distance from S to any of the nodes or the other nodes in the graph is minus infinity because you can start with going from S to A, and that gives you weight of 4. Then you can go for like million times around the cycle A, B, C, and it will get you almost minus million. Then you can go to any other node in the graph. If you want to get to any node with distance minus medium, you can do if you want to get with minus billion, you can get and so on.

This is very nicely thing which is hard to go around. But actually in currency exchange, a negative cycle, if it exists, can make you a billionaire, so this is a very interesting problem to solve.
