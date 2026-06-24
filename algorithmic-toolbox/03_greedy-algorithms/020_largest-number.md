# Largest Number

- **Course:** Algorithmic Toolbox
- **Module 3:** Greedy Algorithms
- **Lecture #:** 20
- **URL:** https://www.coursera.org/learn/algorithmic-toolbox/lecture/WOm2M/largest-number
- **Extracted:** 2026-06-20 19:12:22

---

Hi, I'm Michael Levin, and together we're going to study greedy algorithms in this module. Greedy algorithms are some of the simplest algorithms that exist, and they often seem to be a very natural thing to try when you're solving a problem. In this lecture, we're going to start with a few examples of problems that can be solved using greedy algorithms. And the first one is a very intriguing problem of how to maximize your own salary.

And you're going to come up with a greedy algorithm for this problem yourself because this is really a very natural thing to do with this problem. Next, we're going to consider a problem of how to arrange patients in the doctor's office in the queue so that the total waiting time for all the patients is the minimum possible. We're going to introduce the concepts of greedy choice, subproblem and safe choice which will help us to generalize our solutions to these problems, and you will understand what is a greedy algorithm in general. Let's start.

Imagine the situation, you're trying to get a job at a company, and you've already passed a few job interviews. And you are at the final interview with the boss and the boss tells you that he's going to give you a few digits like this. And your task will be to arrange all those digits in a line so that when you read the number from left to right in the line, that is going to be your salary. Of course, you want the maximum possible salary.

So, you're going to solve this toy problem. What is the largest number that consists of the given digits? For example, if you're given digits 9, 8, 9, 6 and 1, and you need to use all the digits. The examples of the numbers that you can get are 16899 or 69891 or 98961.

So what do you think is the correct answer for this particular problem? And probably most of you have guessed correctly that the correct answer is 99,861. And to get this answer you need to first take the maximum digit and put it first, which is 9 then you're going to take the second maximum digit which is again 9 and put it second, then take the third maximum digit 8 and so on. And in the end you get the number 99,861.

And in this number all the digits are in the descending order. Now let's consider the greedy strategy for solving this problem. So we start with a list of digits, 9, 8, 9, 6, 1, five digits. And in the end we're going to get a number which consists of exactly five digits because we need to use all the digits.

So there are five question marks on the right. So to solve this problem, we start with finding the maximum digit. In thiis case this is the first digit which is 9. Then we're going to append it to the end of the number.

The number is currently empty. So when we append digit 9 to the end we just get number 9. And then we should not forget to remove this digit from the list because we cannot use it again. So we remove this 9 from the list.

And we're left with the list of only four digits 8, 9, 6 and 1. And then we're going to repeat this whole process while there are some digits in the list. So we're going to find the maximum digit which is again 9. But in the second position now we appended to the end of the number to get 99 we remove this 9 from the list, repeat find the maximum digit 8 append removed from list.

Find the maximum digit 6 append removed from the list. And at the end we're left with a list of just single digit 1. We find it as a maximum appendage removed from the list. And this is success.

We've just built the number 99,861 which is the correct answer for this problem. So this greedy strategy worked. And in the next video we're going to consider the problem of how to arrange patients in the doctor's office in the queue, so that the total waiting time for all the patients is the minimum possible.
