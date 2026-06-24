# Review

- **Course:** Algorithmic Toolbox
- **Module 3:** Greedy Algorithms
- **Lecture #:** 29
- **URL:** https://www.coursera.org/learn/algorithmic-toolbox/lecture/xR5jz/review
- **Extracted:** 2026-06-20 19:14:07

---

Hi, in this last video of the module we're going to review the concepts of greedy algorithms. So the main ingredients of greedy algorithms are greedy choice. A safe greedy choice for which we can prove safety, and the sub problem which is a smaller problem of the same kind, which will reduce your problem after making the safe choice. And then you need to solve this problem.

And if you have all that you just need to estimate the running time effort algorithm to make sure it is fast enough for you. So there are many different greedy choices and safe choices in the first problem. But maximizing our salary, the safe choice was to put the maximum digit first and to put minimum digit first for example was a greedy choice but not a safe one. In the second problem about optimal patient Q arrangement to choose patient with the minimum treatment time was a safe choice, and to choose a patient with a maximum treatment time or average treatment time was not a safe choice.

And the third problem about grouping children or covering points with segments. A safe choice was to cover the leftmost point with the segment which starts in this point. And in the last problem we consider about maximizing the loot or fractional knapsack, to take an item with the maximum value per unit of weight is the safe choice for that problem. And after you've came up with a safe choice you've proven that it is safe and reduce your problem.

It's a problem and estimated the running time for algorithm, there is still a possibility that you could optimize your greedy algorithm. And usually as you saw in many of the problems we've considered in this module. If you assume that something is that everything is somehow sorted in a very convenient way in terms of your greedy procedure. And then it could be that the greedy move can be done faster than if you don't assume that everything is sorted.

So you just have to think what is the sort order which is convenient, and typically it is very connected with the type of greedy choice that you're making. For example, if you take the maximum digit then you probably have to just sort the digits in decreasing order. If you take the patient with the minimum treatment time first, then you should sort the patients by increasing treatment time and so on. So what is a safe choice?

A choice is called safe if there is an optimal solution consistent with this first choice, and you can show that there exists an optimal solution which is consistent with this choice. Because in this case you can just make this choice, their existing solution which starts like that. Then you can just solve the remaining problem, and to solve the remaining subproblem, you do the same. Just make a safe choice.

And again, there is an optimal solution which starts with this safe choice and so on. So this is the main concept to prove the correctness of your algorithm. And not all first choices are safe, I already made some examples before. So greedy choices are even often unsafe.

So before actually implementing your greedy algorithm, you have to make sure that it will be correct. And you need to prove that the choice is safe for that, because if you don't do that, it is very likely that you're going to implement your algorithm and it won't work of course. But you are going to debug it and find a lot of bugs in your initial implementation every time you hope that finally after fixing this bug, your algorithm will work. But in the end you will only understand that you've spent a lot of time implementing and fixing the bugs, and everything for nothing, because your algorithm was incorrect in the first place.

And the greedy algorithm doesn't work in this problem. And you will see some problems in this course, where it is intuitive that maybe greedy algorithm will work but actually it won't. And what to do in this case also just take in mind that you always need to prove that your greedy algorithm works before even trying to implement it. Otherwise you risk spending a lot of time for nothing.

So the general greedy strategy for solving a problem is first coming up with some greedy choice then proving that this greedy choice is actually a safe choice. Then the safe choice lets you to reduce the problem to the subproblem, which is a similar problem of the same kind. And then you just solve this problem as the initial problem. So you have this loop from problem to safe choice, to subproblem, back to problem.

And on each iteration of this loop, you decrease and decrease the size of your problem until there is no problem left. And then you're done. This is the general strategy for solving problems with greedy algorithms.
