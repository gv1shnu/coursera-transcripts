# Maximizing Loot

- **Course:** Algorithmic Toolbox
- **Module 3:** Greedy Algorithms
- **Lecture #:** 27
- **URL:** https://www.coursera.org/learn/algorithmic-toolbox/lecture/PvJnA/maximizing-loot
- **Extracted:** 2026-06-20 19:13:43

---

Hi. In this lecture, we're going to solve the burglars problem of maximizing loot. Imagine that a burglar has broken into the house of a merchant of different spices and he wants to take as much value with him as he can, but he only has a small knapsack which has capacity of only 15 kilograms and the burglar can take any amount of any spices in his knapsack so as the total weight of those biases doesn't exceed the 15 kilograms capacity of the knapsack. He can take only part of one spices and part of another one and all of them have different value.

One may be very expensive and another one may be very cheap. Of course, he can choose which to take and which to not take and he wants to maximize the total value of the spices he takes with him in his knapsack. Formally, the problem of fractional knapsack is formulated as following. We have n items with weights W_1, W_2 up to W_n and values V_1, V_2 up to V_n, and a knapsack of capacity, W.

We want to find the maximum total value of fractions of items that fit into a knapsack of capacity, W. For each of n items, we can take any fraction of this item, from 0-1, we can take just 1/3 or 1/2 or 0.4 of this item, or don't take it at all or take the whole item as we like, but the total capacity in terms of weight is restrained to W and we want to maximize the total value. Let's consider the following example. We have just three items.

First item has value of $30 and weight of five kilograms. Second item has value of $28 and weight of four kilograms. The third item has value of $24 and weight of three kilograms, and have a knapsack of capacity nine kilograms. There are a few ways that we can fill the whole knapsack.

The first way is to take the first two items and then the total value of the items will be 30 plus $28, which is $58, and the knapsack is full, because the total weight of those items, 5 kilograms plus 4 kilograms, which is 9 kilograms, which is equal to the capacity of the knapsack. More efficient way is to take the first item, the third item, and just one kilogram of the second item. That will give us 5 kilograms plus 3 kilograms plus 1 kilogram, which is 9 kilograms and the knapsack is full, but the total value is bigger because when we take $30 of the first item plus $24 of the second item and for the third item, we have just 1/4 of this item, so the total value is $28 for four kilograms and for one kilogram is $28/4, which is equal to $7. We take $30 plus $24, which is 54, plus $7, which is total of $61.

But there are even more efficient way to fill the knapsack. Let's take the third item, the second item, and just two kilograms of the first item. In this case, we will have $24 of value for the third item, additional $28 of value for the second item, which is $52 already, and for the first item, we have just two kilograms on this item, the total value is $30 per kilogram is $30/5, which is $6, and have two kilograms so it is $6*2, which is $12 for the total value of $64. This is even bigger than the previous option.

This is actually the optimal way to fill the knapsack. To come up with this optimal way, we should consider the value per unit. For the first item, the value per unit of weight per kilogram is six dollars. For the second item, it is seven dollars, and for the third item it is eight dollars.

It is intuitive that we should take as much as we can from the items which are the most valuable per unit of weight. That's why we take the whole most valuable third item, the whole next most valuable second item and normally what is left we fill with the first item, which is the least valuable per unit of weight, although it is the most valuable item in total, it is the least valuable in terms of value per unit of weight. Now, let us prove the following Lemma. That in this problem, the safe choice is to take as much as possible of an item with the maximum value per unit of weight.

To prove that this is a safe choice, we need to show that there exists an optimal solution that uses as much as possible of this item with the maximum value per unit of weight. Let's prove this. We'll show this proof on the same example with the same three items. Assume we have some optimal solution and in this solution, we don't have the full maximum possible value of the item with the maximum value per unit, which is the third item in this case.

For example, we have just the whole first item and the whole second item. Instead of taking the whole first item, we could separate it into two parts. First part corresponds to the total value and total volume of the third item, which is the most valuable and the rest. This first part, we could substitute with the whole third item, which is more valuable per unit of weight, and so these first three kilograms of weight of capacity would be used more efficiently because instead of having value of $6*3, which is $18 for these first three kilograms, we would get $24 because the third item is so much more valuable per unit of weight.

All the remaining six kilograms of the capacity of our knapsack will be filled exactly the same. We just remove the 3/5 of the first item and substituted it with the three kilograms of the third item, the most valuable, and we improved our solution. It cannot be so that the optimal solution doesn't have as much as possible of the most valuable item. Because if this is the case, then we can just substitute some of the other items with what's left of the most valuable item per unit of weight.

This is indeed a safe choice. Now we have a greedy algorithm to solve the fractional knapsack problem and to solve the maximizing loot problem. While the knapsack is not full, we choose the item number i with the maximum value of V_i over W_i, which is the value per unit of weight. If this item fits into knapsack, all of these items still fits into knapsack, take all of these items.

Otherwise, take so much just to feel the remaining part of the knapsack to that. In the end when this logical loop ends, we return the total value and amounts taken. We may do this iteration several times. Choose the item with the maximum value per unit of weight of this item, then take the next most valuable item per weight, use all this item and then at some point, we will consider the item with the maximum value per unit of weight, and it won't fit into the knapsack so we will take on the part of this item and then we will fill the knapsack up to that, and then we'll return the total value of the items in the knapsack and the amounts of each of the items we took, and that would be the correct solution.

It will be correct because we've proven that our greedy choice is a safe choice. In the next video, I will show you how to implement this algorithm and we'll analyze its running time.
