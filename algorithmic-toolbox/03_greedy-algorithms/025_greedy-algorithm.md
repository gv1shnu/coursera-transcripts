# Greedy Algorithm

- **Course:** Algorithmic Toolbox
- **Module 3:** Greedy Algorithms
- **Lecture #:** 25
- **URL:** https://www.coursera.org/learn/algorithmic-toolbox/lecture/Z3tPJ/greedy-algorithm
- **Extracted:** 2026-06-20 19:13:22

---

Hi. In the previous video, we've considered a celebration party problem. We came up with a naive algorithm, but it turned out to be too slow. I promised you that we are going to overcome this with a greedy algorithm, but first we're going to consider a seemingly unrelated problem.

Covering points by segments. You're given a set of n points on a line with coordinates X_1, X_2, up to X_n and you need to find the minimum number of segments with each segment of length at most 2, which are needed to cover all those points. For example, this is the line and a few points are marked on it. Above it there are a few segments which cover all these points.

All the segments have Length 2, so every point is under some segment. Another example to cover these points is below the line. There are just three segments to cover all these points. The solution above is not optimal because there are four segments and we can do better, we can do with just three segments.

The solution below is actually optimal, we cannot do with less than three segments to cover these points. What is the connection? The connection is actually quite simple. If we consider those points and their are coordinates X_1, X_2 and up to X_n as age of the corresponding child than points X_1 up to X_n correspond to the children's ages.

The segments will correspond to groups. Actually any two children within the same segment, if two children correspond to points and those points are within the segment of Length 2, then the ages of any two children inside the segment different by at most two years of age because the segment has Length 2, so any two children inside this segment cannot differ by more than two. Any valid group of children and group in which any two children differ by at most two years of age can be put into a segment of Length 2 from the minimum age of the child, for example, in this group to the middle age plus two. All other children will get into this segment of Length 2.

This is the connection that means to group the children into the minimum possible number of vetted groups is equivalent to covering the corresponding points with the minimum possible number of segments of length at most 2. Now we're going to solve the problem about points and segments, instead of the celebration party problem itself. We're going to solve it with a greedy algorithm using the following greedy choice. We are going to cover the leftmost point with a segment of Length 2 which starts in this point, so that the left end of this segment is in the leftmost point.

We're going to prove that this is actually a safe choice, so that we can use it in our greedy algorithm and it will work correctly. To prove that, we need to show that there is an optimal solution which is consistent with this safe choice. To prevent consider some optimal solution. Assume that the solution below with the points and the segments is optimal and the minimal number of segments of length at most two to cover these points is four in this case.

Consider the leftmost point marked with green now and consider the segment that covers it. This is a solution, so there is some segment that covers it. It's right above it, and it's in red. If this segment doesn't start at this point, if it's left end is not the same as the leftmost point, then we can just move this segment to the right until it's left and coincides with the leftmost point.

While we're moving this silent to the right, we don't lose any of the points because the green point is the leftmost point. While we're moving, there are no points below the left end of the segment. When we move this segment to the position where it's left end is directly above the leftmost point, we have an optimal solution with the same number of segments, so it is still optimal. All the points are still covered, so this is still a solution.

In this solution, the first segment has the left end coinciding with the leftmost point. There is an optimal solution which is consistent with our choice, so this is indeed a safe choice. This gives us the following greedy algorithm. First, cover the leftmost point with a segment of Length 2, which starts in this leftmost point.

Second, we now don't need to cover any of the points which lie within this first segment. They are all already covered, so we can just remove them. Now we can solve the same problem, which is the same problem with the remaining points which we do and remove which are not yet covered. This is our greedy algorithm.

We prove that the choice of the leftmost point and the starting segment of Length 2 with the left end in this point is a safe choice. This greedy algorithm is actually correct. In the next video, we're going to implement it and analyze its running time and show that it is actually much faster than the naive algorithm we've came up with in the previous video.
