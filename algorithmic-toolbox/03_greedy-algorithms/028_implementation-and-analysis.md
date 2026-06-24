# Implementation and Analysis

- **Course:** Algorithmic Toolbox
- **Module 3:** Greedy Algorithms
- **Lecture #:** 28
- **URL:** https://www.coursera.org/learn/algorithmic-toolbox/lecture/3Ywc9/implementation-and-analysis
- **Extracted:** 2026-06-20 19:13:55

---

Hi. In the previous video, we've came up with a greedy algorithm for maximizing dilute problem or for the fractional knapsack problem. In this video, we're going to implement this algorithm and analyze its running time. The algorithm itself, just to recall, while the knapsack is not full, we choose the best item in terms of the maximum value per unit of weight.

If this item fits into the knapsack, holy, we take all of it. Otherwise, we take so much of this item has to fill the knapsack to the n and we stop at this point. We may do a few iterations. We may first state the most valuable item and put all of it in the knapsack.

Then take the second most valuable item in terms of value per unit of weight, and take all of our knapsack, and then at some point we come to the station when we look at the most valuable item, it doesn't fit wholly into the remaining part of the knapsack. Then we take just part of this item, feel our knapsack to the end and we stop. Another suggestion is that we take all the items in the knapsack and it is still not full but, well, then we also stop our algorithm. In annual return, the total value of the items in the knapsack, and the amounts of the items taken.

Now, let's look as the following pseudocode. Before implementing the greedy algorithm itself, it is useful to implement an auxiliary method to select the best item in terms of the maximum value per weight. It is pretty simple, but it makes the code for the algorithm itself simpler. The function best item takes as input the weights and the values of n items and returns the index of the best item in terms of value per unit of weight.

It also accounts for the fact that some of the items may be already taken. In this case, we expect the weight of the corresponding item to be zero. If the wave is zero, we don't consider this item at all. We start with initializing the value of the maximum value per weight with zero.

This is definitely less than the optimal value among the items. We'll also initialize the index of the best item with zero. We will update it in the course of the external for-loop. For I from 1-n, we just go through all the items.

If there is still some amount of this item and the weight left is strictly bigger than zero so that i is bigger than zero, then we consider the value per unit of weight for this particular item number i, vi over wi. If this value per unit weight is more than the current maximum value per weight, then we update both the maximum value per weight and the index of the item to be equal to number i. In the end, when we went through all the items from 1-n, we just returned the index of the best item. Now, we move to the greedy algorithm itself, algorithm knapsack, which takes us input the total capacity of the knapsack, W, and also the weights and the values of n items.

We'll start with initializing the array of amounts we are going to take for each item, which is an array of n zeros, because initially we didn't take any items. Also, the total value of the items in the knapsack is zero. Then we're going to repeat n times because there are only n items and we either take or not take each of them, at least part of each of them. If at some point we see that there is no capacity to the left, we just return the total value of items taken by this time and the amounts of items taken by this time.

In the variable W will always store the remaining capacity. Initially, it is the total capacity of the knapsack, but as soon as we take some item, we reduce the remaining capacity. At some point, if the knapsack is full, then the W will be equal to zero. This is the easy case if there is no place in the knapsack we just stop and return.

Otherwise, we'll initialize the value of variable i with the index of the best item among the remaining items from one to n. To do that, we use the function we have just implemented on the previous slide, best item. Now we have the index of the best item. Now we need to compute how much to take of this item.

This is done on the next slide. A gets the value of minimum of the weight of this item, that will be i and the remaining capacity of the knapsack. Either the whole item number i fits into the knapsack and then we take wi. This is in the case when wi is less than W or the whole item doesn't fit and then we need to fill the knapsack of that.

Then we need to take W. What is left of space in the Knapsack? This is in the case when W is less than w_i. We need to take the minimum of w_i and W.

Now, we know that we need to take exactly a of the item number i, in terms of weight, and so the total value increases by a times the value per unit of weight because we take a units of weight and the variable of weight is v_i or w_i to increase the value by a times v_i or w_i. Also, we need to remember to update the remaining quantities. The weight of the item i decreases by a. We should also actually update the value of the item.

It decreased because we took some of it, but we won't bother about that because for every item we either take the whole item into the Knapsack and then W_i becomes 0, and we don't consider this item at all. Or if we take only a part of this item, then we stop at the same time because it means that we failed the Knapsack up to the end and we need to stop and return. We don't update the value, we just update the weight. We say that we decrease the weight of item number i by a.

Also, we increase the corresponding position in the array amounts to reflect the fact that we took a unit of weight of item number i. Also remember to update the remaining capacity of the Knapsack, which has just decreased by a units of weight. In the end, after we either repeated this whole loop n times and took all the items in our Knapsack, or we stopped before that because of the capacity of the Knapsack became equal to 0, after that, we return the totalValue and the amounts taken of each item. This is the whole greedy algorithm for the maximizing load or fractional Knapsack problem.

Now, let's analyze the running time. The lemma states that the running time of this Knapsack function is O of n squared. Indeed, first, we analyze the running time of the BestItem function. It uses just one for loop with n iterations, so it is obviously O of n, linear time.

The main loop of the Knapsack function is executed at most n times, and BestItem is called once per iteration, and everything else is just constant time operations. All in all, it's n times O of n, which is O of n squared. We can also optimize this algorithm. It is possible to improve the asymptotics.

To do that, we first sort the items by decreasing value per unit of weight. Then if we assume that all the items are sorted by decreasing v_i over w_i, then we have this function, KnapsackFast, which takes the same input. Actually, the code is almost the same. The first part of the code is the same, we just initialize the arrays and we have the external for loop, and if the Knapsack is full, we just return.

Then the only difference is that instead of finding the best item and calling the function BestItem to find it, we just know that at any point, the best item is the first one which is still not taken, which is that item number i, because all the previous ones are already taken because they're even better than the item number i, and they were considered before. We just compute how much of this item we need to take the same way, minimum of w_i and W. Then the second part of the code is also the same. Just update the totalValue, the amounts left of the items, the amounts taken of the items, and the remaining capacity, and then we return the totalValue and amounts taken of all the items.

The algorithm is basically the same, it just avoids calling the costly function BestItem which takes O of n time. We see that now this algorithm works just in linear time because there is only external for loop of n iterations, and everything inside it is just constant time. The asymptotics for this is again, now each iteration is constant time, so Knapsack after sorting is O of n, and so sorting and then Knapsack sorted is just O of n log n because you already know that sorting can be done in time n log n, you just don't know how yet, but you will learn this soon. In the end, we managed to solve our maximizing the root problem in time n log n.

In the next video, we will review the main ingredients and all the concepts of greedy algorithms, and the approaches of how to solve problems using greedy algorithms.
