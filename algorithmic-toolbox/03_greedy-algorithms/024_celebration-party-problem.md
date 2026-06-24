# Celebration Party Problem

- **Course:** Algorithmic Toolbox
- **Module 3:** Greedy Algorithms
- **Lecture #:** 24
- **URL:** https://www.coursera.org/learn/algorithmic-toolbox/lecture/I5iH1/celebration-party-problem
- **Extracted:** 2026-06-20 19:13:10

---

Hi. In this lecture, we're going to solve another problem using greedy algorithms, celebration party problem. Imagine the following situation. Many children came to a celebration party and you need to organize them into groups.

But you want them to play nicely with each other, so you want the groups to be pre-homogeneous. For that, you wish that any two children in the same group should differ by at most two years of age no more. You want to organize them in the minimum possible number of groups because for each group, you need to supervise this group and you want to minimize the number of adults that have to be doing that. I'll know the problem is to organize the children into the minimum possible number of groups such that any two children in the same group differ by at most two years of age.

We could try to solve this problem with a naive algorithm. Just try all possible distributions of children into one or more groups and see which one is valid and which one is also with the minimum possible number of groups. Just for each distribution, check whether any two children in any of the groups differ by at most two years of age, and if that's true, then consider this distribution valid. Then return the minimal number of groups among all the valid distributions in the groups.

This algorithm obviously will work because it will consider all the possible distributions of children to groups. But there's no problem with this algorithm. It's running time. The Lemma states that the running time of the naive algorithm is at least 2^n, at least exponential, where n is the number of children, and that is bad.

But we will see in a few minutes why it is bad. To prove that this algorithm is at least exponential in complex table, we should notice that this algorithm is going to consider at least all possible distribution of children into exactly two groups. It will also consider distributions into one group and more than one group probably, but at least all the distributions into two groups it will consider. If you are going to distribute all children into two groups, the first of these two groups corresponds to any subset of children.

You can just group any subset of children to the first group and then all the other children in the second group. There are 2^n different subsets of the set of n children. There will be 2^n different distributions into two groups. First group is a subset and second group is all the adult children.

As our naive algorithm is going to consider all those distributions and there are 2^n of them, their running time is at least 2^n, and actually it is much more than that. This is not a very good algorithm. Nave algorithm works in time Omega of 2^n, which means that it works in time at least 2^n. For n equal to just 50 children, it is at least 2^50, which is this huge number of operations.

You're probably not going to wait until your laptop computes the result for this algorithm. You won't be able to wait for that. We're going to do much better than that. We will improve this significantly using greedy algorithm, and we're going to do that right in the next video.
