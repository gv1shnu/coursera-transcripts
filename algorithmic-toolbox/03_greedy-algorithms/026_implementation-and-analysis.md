# Implementation and Analysis

- **Course:** Algorithmic Toolbox
- **Module 3:** Greedy Algorithms
- **Lecture #:** 26
- **URL:** https://www.coursera.org/learn/algorithmic-toolbox/lecture/aqwAa/implementation-and-analysis
- **Extracted:** 2026-06-20 19:13:32

---

Hi. In the previous video, we came up with a greedy algorithm to solve the problem about covering points with segments and that in turn gives us a greedy algorithm to solve the celebration party problem. In this video, we're going to implement this algorithm and analyze its running time to show that it is indeed much faster than the naive algorithm that we've came up with first. Let's start with this pseudocode.

We assume that the points are given to us in the ascending order. So x_1 is less than or equal to x_2 and so on up to x_n. The function PointsCoverSorted takes and input the points sorted by coordinate, and outputs the list of segments which covers all these points. All the segments are of length two and there is the minimum possible number of segments in the solution.

We start with initializing the variable segments, which will contain the answer in the end as an empty list. We also initialize the variable left with one, where left will be the index of the current leftmost point, the leftmost of all the remaining points which are still not covered. So while left is less than or equal to n, it means that there are some uncovered points. In this case, we take the leftmost point with coordinate x left and we create a segment with left n equal to x left and the right n is equal to x left plus 2, because the length of this segment should be equal to 2 and we'll append this new segment to the solution.

Then we see that the leftmost point is now covered. So we need to move left one position to the right, so we increase left by one and also we need to check maybe some next points are also covered by the same segment. All the points to the right from the leftmost point we've just covered are to the right from the left end of this new segment. If they're also to the left from the right end of this segment, then they're covered so while left is less than or equal to n, and the coordinate of the point is less than or equal to r it means that this point x left is actually covered and so we need to increase variable left by 1 again so we move this left by 1 until we find the point which is not covered, or until we go to the end of the array of points.

Then we'll repeat this external while loop if there's some uncovered point left, we create one more segment and so on. When this external while-loop finishes, all the points are covered by segments. All those segments are in the list segments, which is the solution and we just return this list of segments as our solution. This is the implementation of the greedy algorithm we've come up with in the previous video.

Now let's analyze. The Lemma states that the running time of this algorithm is linear. Indeed, the variable left changes from 1 to m as soon as it becomes more than n our algorithm stops. Although there is this external while loop and also an internal while loop with the same variable left you could think that this leads to n squared running time, but actually variable left just increases at each step and so is increased, abolished and times.

For each value of variable left we appends at most 1 new segment to the solution so everything we do is just to increase the variable left and add segments. We increase the value left at most n times and for each of the values from 1 to n, we append at most 1 new segment to the solution. Overall we do at most 2n actions that is big O of n o overall, the running time of our algorithm is linear. Now let's compute the total running time.

Remember that when we implemented PointsCoverSorted we assumed that the points are given to us in the sorted order. PointsCoverSorted itself works in linear time, but also need to sort the points before calling this PointsCoverSorted function and soon you will learn next module to sort in time, big O of n log n. Then the total running time, if you're given points in unsorted order will be sort plus PointsCoverSorted is n log n plus linear time, linear time is less than m again so the total running time will be n again. Now we see that the straightforward solution from the first video of this lecture is Omega of 2 of power n is at least exponential.

This is very long even for n equal to 50, 50 children is too much to wait for computation on your laptop. Sort plus greedy is just big O of n log n so it will be fast even for n equal to 10 million, probably you won't have 10 million children at any celebration party but even if you have, your laptop, will compute the solution for this celebration party in under a second, probably so this is a huge improvement. In conclusion, straightforward solution is exponential and to improve it, it was important to first reformulate problem in mathematical terms and we switched the problem from grouping children to covering points with segments that came out to cover the leftmost point with a segment to the left and coinciding with this leftmost point and prove that this is a safe choice. Our final solution is sort all the points in time n log n, and then launch a greedy algorithm in linear time.

In the next lecture, we're going to consider the problem from burglar, how to maximize the loot that you can put into his knapsack before running.
