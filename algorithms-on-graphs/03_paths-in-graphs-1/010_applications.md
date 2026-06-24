# Applications

- **Course:** Algorithms On
- **Module 3:** Paths in Graphs 1
- **Lecture #:** 10
- **URL:** https://www.coursera.org/learn/algorithms-on-graphs/lecture/aFOY9/applications
- **Extracted:** 2026-06-21 21:24:18

---

Hi. I'm Mike Levin and through the next few lectures we're going to study the algorithms for finding optimal paths in graphs. There's a huge number of applications for these algorithms, and we're going to study some of these applications in detail. The first one is when you need to go to a very faraway place, for example, for your vacation and you need to take a plane.

Ideally, you'd like to have a direct flight there, or at least to minimize the number of transfers that you need to make. This corresponds to the problem of finding the most direct route in a graph that is the route that uses the least possible number of edges to get from node A to node B. Next example is when you need to get to some point in the city and you're going to get there by car and you need the fastest possible route, for example, from home to work or back and that corresponds to finding the shortest possible path in a graph where edges have weights. The last example is probably a little bit surprising, it is about currency exchange.

The problems there include how to optimally exchange currencies from, for example, US dollar to Russian rubles. Is it actually possible to create arbitrage? That is to get more money that you had initially by making several currency exchanges and returning to the initial currency that you had. Is it possible or not and how to make them?

If we can make that, we can actually become billionaires. So that is a very interesting problem and we're going to consider it in the third lecture. In this lecture, we're going to focus on the first problem of getting to some faraway place with a plane flight or several plane flights. An example problem would be, what is the minimum number of transfers to get from London to Perth?

Here in the picture, we have an example network of plane flights offered by some air travel company. In this case, to get from London to Perth it'll take, for example, about 5-7 flights. Of course, that would be very painful and you would prefer that there existed some direct flight from London to Perth and you wouldn't need to do any transfers and there would be zero transfers. In terms of graphs, this problem can be reformulated as following.

We have a graph where cities are nodes and the available flights are edges, directed edges between those nodes. The route from London to Perth could be, for example, London to Paris to Las Palmas to Luanda to Johannesburg to Mauritius to Cocos Islands and then to Perth, and that is a very big number of transfers. Another path that is in this graph is from London directly to Johannesburg and then from Johannesburg directly to Perth, just one transfer and you're at your destination. Actually in this graph, there is a direct path from London to Perth.

If it exists, of course you want this path. The problem is in arbitrary graph, what is the path that contains the least possible number of transfers to get from some city to another. In the next video we're going to introduce the formal notion of paths and distances so that we can then formulate our problem in terms of algorithms.
