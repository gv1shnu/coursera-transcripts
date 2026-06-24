# Breadth-First Search (continued)

- **Course:** Algorithms On
- **Module 3:** Paths in Graphs 1
- **Lecture #:** 13
- **URL:** https://www.coursera.org/learn/algorithms-on-graphs/lecture/WSyTa/breadth-first-search-continued
- **Extracted:** 2026-06-21 21:24:51

---

High in the previous video, we described how to process all the notes in the order of increasing distance from a layer by layer. And thus to find all the distances from a to all the nodes in the graph. However, there was a problem that we discovered several notes at once in that description and that cannot happen in a real algorithm. So we'll change the algorithm a little bit and it will discover all the notes one by one, so that all the notes at distance zero will go before all the notes at distance one and before all the notes that distance two and so one.

But all the notes in the same distance layer will be discovered in some order, which is not important. We will put our notes in the queue when we discover them. And we'll take them from the front of the queue to process them. So at first the queue is empty and then we discover the note A.

We set the distance to this note from A 20 and we put this single note into the queue. And then all we do is we consider what is on the top of the queue. We take the first note from the top of the queue and process it. So in this case the queue only contains note A.

So we'll take the note A from the top of the queue and we'll process it, we'll color it with black to mark that we're processing it already. And then we'll start to process all the edges out going from this note in some order. It doesn't matter what is the order. So let's see for example, this Is the 1st edge.

And we discovered a new note which was not discovered before one. We consider this first age from node A. We know that this note was not considered before because it's colored with white. And our algorithm knows that the note which is colored with white yet hasn't been discovered yet.

And as soon as our algorithm discovers a note, it colors it with gray and puts it in the queue. And also when we discover some notes, we know that the distance to the note from which we discovered it, we know this distance and the distance to the new note is bigger by one. So for example, if we're processing note A. Which is a distance zero than any note.

We discover while processing node A will be a distance one. And if we were processing some notes at distance, 10 for example than any note discovered while processing this note would be a distance allow. So in this case we set the distance to the note to one and we put it in the queue. Then we proceed to processing the next edge of going from node A.

And we discover one more note that distance one. We covered with gray and put it in the queue, discover one more note color with gray. Put it in the queue distance one and discover one more note colour with gray, put it in the queue. Now we've processed all the edges out, going from the note A.

And so we need to go to the Q. And take the top element from the queue and process it. Now the queue has four elements in it. And by the way, when I say that we take the top element, we not only look at this top element, we also get it out of the queue.

So the note A is no longer in the queue as soon as we started processing it. So the Q now contains only four notes which are marked with gray. And this is the general property only notes which are currently marked with gray are in the queue. So we take the top note from the Q.

And that would be the note to the right from A. Because this was the note that was discovered first. And so it got into the Q. The first.

And this means that it will take it out of the queue the first. So we start processing it and that's why the market with black and to process it will start processing all the outgoing edges from this note in any order. So first edge goes to another note which is already great. So this edge is useless.

We don't need to do anything with it and we just ignore it. The next edge however, goes to the note which was white and so we discover a new note at the end of this edge. And we know that the distance to this note is bigger by one than the distance to the note we're considering now it is one. So the new distances to and remarked the new note with distance to with color gray and we'll put it in the end of the cube.

We consider one more edge and we'll find one more note that distance two. We cover it with gray, set the distance and put it in the queue. Now we've processed all the edges out going from this node, the distance one, and we continue to the next top node in the queue. This is this note, we cover it with great, consider this edge, it is useless, consider this edge, it is also useless because it goes to the note which is already great.

Although the distances bigger still this note is already gray, so it is already in the queue. It was already discovered and we don't need to consider this edge. And this edge gives us a new noted distance to. We mark it with a great car and put it in the end of the queue.

Now we process the next no distance one. This edge is useless. This edge is useless and this edge gives us a new note of distance two and now I consider the last note that distance one and this edge is useless. This edge is also useless and all the edges from these notes are now to be useless.

So we don't put anything in the queue. And we finished processing this note and we start processing notes at distance to notice that we are processing all the nodes in the order of distance from A. We process notes at the same distance in any order, but we process first all the notes of distance one, then all the notes of distance two and so on. So when we process this note, the distance two obviously all the notes are already discovered.

All the notes are either gray or black so all the edges will be useless. This edge is useless. This one to this one, two. Now we consider actually the right bottom note because this note was discovered the next after the top right note.

If you remember how our algorithm went through the graph. So this is the note we're going to discover next. All the edges are going from this node are useless. Now we consider the top left note and all the edges are going from this node are useless.

And finally we process the bottom left node. Of course. Also all the edges are going from these notes are useless and now we have all the distances marked on the corresponding nodes. And so we know all the distances from the note A to all the nodes in the graph.

And this is how breadth first search works. It is called breadth. First search because it goes through distance layers, so it goes in the direction of breath. So first he discovers everything in the near vicinity of the starting note, and then it becomes broader and broader and broader.

But it doesn't discover far away notes before the notes, which are close to the starting note. So it gradually increases the breadth of the search. That's why its breadth first search, and in the next videos we're going to analyze the algorithm, proof that it is correct and also implemented.
