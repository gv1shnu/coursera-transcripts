# Problems with Functional Decomposition

- **Course:** Pearson System Design Fundamentals Livelesson Video Training
- **Module 1:** System Design Fundamentals
- **Lecture #:** 4
- **URL:** https://www.coursera.org/learn/pearson-system-design-fundamentals-livelesson-video-training-n1kdi/lecture/hGZIs/problems-with-functional-decomposition
- **Extracted:** 2026-06-20 11:01:57

---

In a more abstract way, here's what's happening. The moment you have the client stitching up the services, you always pollute the client and you bloat the client with business logic. Now, that starts a runaway reaction where you don't wish to maintain the business logic both at the client and across the services. Now since you have to do it in the client, you dumb down the services to be just these pass through good for nothing building blocks, and the whole system becomes the client.

Now you could say, I know how to fix that. I'm going to do this. I will keep the client as a pretty face, an empty conduit just to the system. I'll have A call the B, and B is going to call the C.

That is true. That would solve the problem of bloating the client. The problem is, it never looks like this. It always ends up looking like this.

And the reason is, A can never be A. In the first case I showed you, where the client is the one stitching the services, something like this. A is just doing A. But in this scenario, A has to know about the B.

At the very least, A has to receive enough parameters to be able to call the B. And what if B fails? Where all the logic of undoing the B, all the internals of B are now inside A. Now B is no B.

B has to know about C. At the very least, B has to receive enough parameters to call the C. In fact, A is inflated because of C, because A has to receive enough parameters to enable the B to call the C. B has to know about C.

B has to know about what happens with the failure of C. And what if B calls C asynchronously? And so now C fails. How would B detect it?

And so we have enormous coupling and pollution of B because of C. And this is already bad, except it never looks like this. And the reason is, it always ends up looking like this. Think about what happens when you're all the way inside C, and then you have a failure.

Well, somebody has to undo the A and the B, but who is that somebody? Maybe A and B are long gone because C was done asynchronously, or maybe over queues. So all the logic of A and B, of what it takes to undo the A and the B, has to reside inside the C as well. B is no longer B.

B has to know about undoing the A. And B and C have to coordinate who is undoing the A. Is it B or is it C? And what if B fails to undo the A?

Should C do something about it? And isn't the recovery of the business of B depends on the success or failure of undoing the A? And how would C know about that? And so do we really have three services or do we have one giant click of doom?

And think about how complex these things is with only three services. What if you have 13 or 30? This added accrued complexity is not linear. Meaning it's 2 plus 3 plus 4 plus 5 is not a linear sum.

It's a runaway reaction. And we've all seen it before with horrendously complex technical debt and systems that nobody can actually make sense of. Here's a terminal state of such a system. Look at all the interconnection between these building blocks.

And this is only five big things. And can you imagine what happens if you have 15?
