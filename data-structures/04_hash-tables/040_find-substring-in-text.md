# Find Substring in Text

- **Course:** Data Structures
- **Module 4:** Hash Tables
- **Lecture #:** 40
- **URL:** https://www.coursera.org/learn/data-structures/lecture/tAfHI/find-substring-in-text
- **Extracted:** 2026-06-20 21:40:57

---

Hi. In this lecture, we're going to apply hashing to a completely different problem called substring search or finding substring in text. What is this problem? The problem is given a text T, for example, text of the website, text of a book, or Amazon product page text, and a string P, for example, a word or a phrase or a whole sentence, find all the occurrences of string P in the text T.

Examples are numerous. For example, you could search with your browser for a specific term inside a long Wikipedia article to quickly get to the parts of the article that you need or a biologist could search for a gene occurrence in a genome or we could try to detect files infected by a computer virus using code patterns that are specific to the virus. There are many more examples of this problem in practice. To solve this problem first, let's introduce some notation.

Denote by S from i to j, the substring of string S starting in position i and ending in position j, including both position i and position j. For example, if S a string hashing that S of 0-3 is just hash, S of 4-6 is ing, and S of 2-5 is shin. Note that we're indexing the positions from zero. Formally, the problem to find substring in string gets us input strings T as text, the long string, and P as pattern, the short string.

The output is, we need all search positions i in the string T such that 0 is less than or equal to i and i is less than or equal to length of T minus length of P such that the substring of T starting in position i which has length equal to the length of P so T from i to i plus length of P minus 1, this substring of T is equal to the pattern P. The naive algorithm to solve this problem just tries for each position i from 0 to length of T minus length of P check whether this substring is equal to P or not. If yes you just append this position i to the result. Let's see how we can implement this algorithm.

First, we implement the algorithm that checks whether two strings are equal or not. First, it checks the length. If the length of two strings are different then they are different and not equal, so we return false. Otherwise, we go with index i from 0 to the length of the first string minus one, and the length of the second string is of course the same and we check if the corresponding characters are different then the strings are different, so we return false.

Otherwise, if we went from beginning to the end of both strings and we didn't find any difference, it means that the strings are equal and we return true. Now, the main procedure of the naive algorithm finds substring naive takes as input two strings, T and P, we initialize the resulting list of positions with an empty list. Then for each index i from 0 to length of T minus length of P, this is the last position where pattern P still can fit into the text T completely, if the substring T of i from i to i plus length of P minus one and string P are equal, then we just append i to the resulting list of positions and in the end, we return the resulting list of positions that we found. Let's analyze this algorithm running time.

Turns out that is O of length of T times length of P. It is really easy to see because each goal of procedure AreEqual is O of length of P because we need to compare two strings of length exactly equal to the length of P and this function AreEqual just go through each position in each of the strings once and that just happens in one four-loop of length of P. Then each time we consider some position i, in the worst case, we'll need to go AreEqual and in the worst case it will have to go through all the characters in both strings if they're equal and so we will have length of T minus length of P plus one calls to AreEqual. This gives us O of length of T minus length of P plus 1 times P and this is equal to O of length of T times length of P because we assume that length of T is much bigger than the length of P.

This is the estimate from the top. Let's see whether this estimate is actually tight or not. It turns out that it is in the tight and there is a bad example where we indeed mean on the order of length of T times length of P operations to solve problem using this naive algorithm. Take as a text T very long string which contains only one character a, million as.

As a P, we consider a much shorter string which consists of many letters a and one letter b in the end, like 999 letters a and then b. What will happen for each position i in T from zero to length of T minus length of P, which is like 999,000, the call to AreEqual has to make all 1,000 comparisons up to the end of the string P because it is only on the last character that we will see that the substring of T is not equal actually to string P. We'll have to make all 1,000 comparisons on each step and all in all, we'll have to do that for every possible position i in T. In the end, in this case, the naive algorithm runs in time Theta of length of T times length of P, which is bad because for very long strings, for example, if T is genome and P is a gene that could be billions and millions multiplied and that will run forever so we need some faster algorithm to solve this problem.

In the next few videos, I'll show you how to apply hashing to solve this problem much faster.
