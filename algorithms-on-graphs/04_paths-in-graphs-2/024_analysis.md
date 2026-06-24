# Analysis

- **Course:** Algorithms On
- **Module 4:** Paths in Graphs 2
- **Lecture #:** 24
- **URL:** https://www.coursera.org/learn/algorithms-on-graphs/lecture/oyJiN/analysis
- **Extracted:** 2026-06-21 21:26:49

---

Hi. In this video, we are going to analyze the running time of Dijkstra's algorithm. Let's look at the pseudocode. There are four blocks that determine the running time.

First is the initialization, which runs in time proportional to the number of nodes. Next is the make queue operation, which depends on the implementation of the priority queue. Next is the Extractmin operation, which is called v times, where v is the number of nodes in the graph. There is the ChangePriority operation, which is called for every edge that is relaxed.

These four things are the main parts which determine the running time because everything else is either constant time or at least faster than these parts. The total running time is the big of v for the initialization plus the time to build the priority queue out of v nodes plus number of durations of the main loop, which is number of nodes, v times the time to implement ExtractMin plus the number of edges times the time to call ChangePriority. Why it is the number of edges times ChangePriority because we relax each edge at most once so this is an estimate from the top. Now we need to decide which implementation to use and we know two implementation of the Priority queue.

First one is based on the array and in this case, the first part doesn't change. It's Big O of number of nodes in the graph. To make hue out of array, we just need to look through this array once and it also takes linear time in terms of number of nodes. To extract the minimum value in an array takes time equal to the size of the array, which is number of nodes.

Number of nodes V times number of nodes is V squared. The time to change the key in the array is just constant time because we can just go there by index and change the key. So E times ChangePriority is just E. We see that both v is less than v squared and the number of edges in any graph is less than v squared.

So all in all, this is Big O of V squared. If we implement our priority queue is at array. Another way to implement priority queue is binary heap, and typically it is more efficient. But actually, you will see that it depends on the graph we are working with.

The first v doesn't change, the time to make queue from array into binary heap is actually also linear. The time to extract the minimum key from a binary heap is logarithmic so we add V of V and the time to change priority in a binary heap is also rhythmic so we add E log V, and we see that the first two sums are small compared to the two others and the final estimate is V plus E log V. In the case when the number of edges is much smaller than the v squared, this is actually better than the previous estimate of V squared. But if the graph is full, if the number of edges is close to V squared then this is close to V squared times log V and so this is actually worse.

This is why I told you the algorithm in a more general way because depending on the structure of the graph whether is a lot of fascist or only a few edges it can be better to either use the binary heap implementation or an array implementation. Now you know the running time for both options. To conclude, we now can find the minimum time to get from work to home. We can find the fastest route from work to home, not just the time but the route itself.

We can solve, of course, a more general problem to find the shortest paths from a single node to all the nodes in any weight to graph where all the weights are non-negative. It works either in the time proportional to the square of the number of nodes or in time V plus e log V depending on the implementation. The first one is for the array-based implementation of priority queue, and the second one is for the binary heap based implementation.
