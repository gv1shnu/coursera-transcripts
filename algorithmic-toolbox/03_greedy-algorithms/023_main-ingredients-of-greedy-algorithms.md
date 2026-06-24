# Main Ingredients of Greedy Algorithms

- **Course:** Algorithmic Toolbox
- **Module 3:** Greedy Algorithms
- **Lecture #:** 23
- **URL:** https://www.coursera.org/learn/algorithmic-toolbox/lecture/JuqUg/main-ingredients-of-greedy-algorithms
- **Extracted:** 2026-06-20 19:12:59

---

Hi, in this video we're going to review the main ingredients of greedy algorithms. So the main thing, the main idea is reduction to some problem. If you want to apply a greedy algorithm, you make some first choice and then you solve a problem of the same kind but smaller. Like there are fewer digits left or fewer patients left.

And this smaller problem of the same kind is called the sub problem. So the concept of safe choice is critical. A choice is called safe if there is an optimal solution which is consistent with this first choice. And not all first choices are safe and often greedy choices are not safe.

And so if you want to solve a problem with the greedy algorithm, you need to prove that the greedy choice you came up with is really a safe choice and only after that you can apply it. So the general strategy to solve a problem using greedy algorithms. First, you need to come up with some greedy choice and then critically you need to prove that this is indeed a safe choice. Then using this safe choice, you can reduce your initial problem to a sub problem, just smaller.

And then as the sub problems similar to the initial problem, you just solve this problem the same way as a problem. And so you get the slope, you have a problem, you come up with a greedy choice and this is a safe choice. You reduce your problem to a sub problem using the safe choice and then you solve this sub problem. And at each iteration of this loop, your problem decreases and decreases until there is no problem to solve.

And then you're done. So this is the general greedy strategy. And in the next several lectures, we're going to solve some more problems using this general strategy using greedy algorithms.
