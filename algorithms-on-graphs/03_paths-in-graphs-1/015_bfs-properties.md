# BFS Properties

- **Course:** Algorithms On
- **Module 3:** Paths in Graphs 1
- **Lecture #:** 15
- **URL:** https://www.coursera.org/learn/algorithms-on-graphs/lecture/8aYP7/bfs-properties
- **Extracted:** 2026-06-21 21:25:13

---

Hi, in the previous video we've implemented the BFS algorithm and analyze its running time. So it runs fast but doesn't return correct values. We don't know yet because we haven't proved its correctness yet. And to do that, you will first prove some of the properties of how this breadth first search algorithm works.

What is the order in which the nodes are discovered and processed? And these properties will be useful both for proving the correctness of the algorithm and for the different applications of this algorithm in other situations. So, first, let's define the rich duty node u is reachable from note A if there is a path from A to u and the Lemma states that all the writable notes are discovered at some point during the breadth first search algorithm. So they get a finite distance estimated at that point and the unreachable nodes are not discovered at any point.

And so the distance to them stays infinite. First, let's prove that every note that is reachable from a will be discovered. And assume for the sake of contradiction that there are reachable nodes which are not discovered during BFFs. Then let's consider u which is the closest node to A which is reachable and undiscovered.

We know that u is not equal to A because A is definitely discovered in the first step of the algorithm. So u is the closest known to A which is reachable but undiscovered. Now, let's consider the shortest path from A to u there is some path from A to u because u is reachable. So there is some shortest path and then the node vk is reachable from A and it is closer to A and u is the closest reachable and discovered notes.

So vk must be discovered because it's reachable and closer than u. So at some point vk is discovered and then you actually is discovered while processing vk because if the k is discovered then at some point it will be processed. So we first discovered in the process a discovered the process, if you want discovering process with u and so on. And at some point we discover and process the k and one would process the k and the outgoing edge from k to u.

We're going to discover all of you. So we get a contradiction and it means that every note which is reachable from A will be discovered by BFS. Now, let's prove that any unreachable node won't be discovered again, assume for the sake of contradiction that there is some nodes u which is unreachable. But it is discovered, u is definitely different from a because A is reachable from A so it can be unreachable and let's find u as the node which was discovered first out of all the unreachable notes.

So you was discovered while processing some other node v and that means that actually u is reachable because vi was processed. And it is also reachable book because u is the first unreachable that was discovered and then u is reachable through v. So there is a path from A to v because v is reachable and there is an edge from v to u because you was discovered while processing v. So there is a path from A to u, going from A to v and then from v to u and thus u is actually reachable, which is a contradiction.

And so it means that actually no unreachable nodes will be discovered during the BFS algorithm. Now the most important lama which is intuitively what we tried to do with the breadth first search algorithm but now we need to actually prove that the nodes are processed in the order of increasing distance in some sense. So the Lemma states that by the time node u at some distance de from node is the cute that is processed, started to be processing all the nodes at distance at most. They have already been discovered by the time I discovered, that means that they were already put in the queue.

So by the time some notes, the distance d is being processed all the nodes at distances less than the and exactly the have already been discovered, this is what we want to prove. And from this, it follows that nodes cannot be processed in the wrong order. So to prove this Lemma, let's again assume for the sake of contradiction that it is wrong and then consider the first time that the order was broken. So that there is a notes u which is already being processed, it is black, it is a distance d.

And there is some other nodes v which is not yet discovered, it is a distance d prime and g prime is less than or equal to d. So this is the first time that the order was broken. Now, let's consider the note u prime. Such that naught u was discovered while processing naught u prime there exists such nodes.

And the distance to this note is at least the minus one because when u was discovered, it was assigned distance d. So it could have assigned this distance only if the distance to u prime was the -1. So also let's consider the node v prime such that naught v is a distance d prime and g prime is a distance d prime minus 1. There is such nodes with prime because there is some shortest path from A to v and the length of this path is the prime.

And there is the previous node before we on this path and this is the note v prime and the distance to this naught would be the prime -1. So what do we know about nonsense u prime and g prime, we know that d prime minus one is less than or equal to d minus one. And it means that the node v prime was discovered before naught u prime was the queue. This is because the first time that the condition of the Lemma was broken was with the node u and v.

So with the nodes u prime and g prime which were discovered before that the Lemma still stays correct. And so it means that the prime was discovered before u prime was the cute. Now let's see at the sequence of events the first v prime was discovered at some point. And then after that at some point u prime was du and processed after u prime was du and processed, u was discovered.

So it means that the v prime was discovered before u was discovered. And that means that the v prime would be processed before u would be processed. Because everything that goes into the queue earlier, we'll get out of the q earlier also. So v prime is processed before u is processed and during the processing of v prime, we would definitely discover v if it was not discovered before and it means that v would be discovered before u is processed.

But this is a contradiction with our assumption that by the time u was already processed, v was not yet discovered. So we came to a contradiction and this proves our order level. Well now let's prove the q property that we initially had in mind, basically intuition is that at any moment of time we only have nodes at distance d. And distance d plus one for somebody in the queue and no other distances are present in the queue and all the nodes of distance d are before all the notes at distance d plus one in the queue.

This is what our Lemma states, well, let's prove this Lemma. First all nodes of distance d. We're in queue before first sketch node is d queue. So they go before nodes at distance d plus one because nodes at distance d plus one can be in queue.

Only one side node the distance d is q queue and by the time all the nodes at distance d. We're already in queued so they are earlier in the queue. Also nodes at distance d-1 were include before nodes at distance d. So they are not in the queue anymore.

If the first node in the queue is already a distance d. It means that all the nodes that distance d might as well we're d queue before that. And the nodes the distance more than d plus one can be discovered only when all the nodes at distance d are gone because they are before the nodes at distance d plus one in the queue. And while we d queue nodes at distance d, we cannot get any nodes of distance d plus two or more because when we process note the distance d.

We only discover nodes at distance d plus one. So these three items show that indeed when the first node in the queue is a distance deep that we only have notes of distance d or d plus one in the queue, and all the nodes of distance d go in the queue before the nodes at distance d plus one. So this is the main property of the breadth first search algorithm that we intuitively build the algorithm around, but now we have proven that this is true. And in the next video we'll use these properties to prove that actually the offense finds correct distances to all the nodes in the graph from the starting node A.
