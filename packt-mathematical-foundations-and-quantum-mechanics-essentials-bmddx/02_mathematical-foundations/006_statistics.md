# Statistics

- **Course:** Mathematical Foundations And Quantum Mechanics Essentials
- **Module 2:** Mathematical Foundations
- **Lecture #:** 6
- **URL:** https://www.coursera.org/learn/packt-mathematical-foundations-and-quantum-mechanics-essentials-bmddx/lecture/PUYmH/statistics
- **Extracted:** 2026-06-22 14:44:35

---

Hi. Within this lecture, we're going to see another topic in the Math fundamentals for the quantum computing, which is a very easy topic, by the way, it's statistics, and we're going to see the very fundamentals of the statistics, at least we got to know about the terms, like Mean or Median or Min or Max. And obviously, you know all of this stuff from high school, I believe, but again, we need to make sure so that you understand the calculations in a better way when we go into the next lectures. So, consider this list, we have 15, 22, and so on.

So if we want to have a Mean, it's actually the average of all these numbers, okay. If you add all these numbers up, and if you divide them by the 7, that is the length of this array, well, we have 7 numbers over here. If you add them all together, and divide it by 7, we're going to have 43.57 average. So this is the Mean.

Median means that it's the middle number in the sorted array. So it starts with 15 and goes up till 79, and if they are not sorted, we should sort them out, and we can get the middle number which is 40, 40, okay, so this is the Median that I'm talking about. Of course, you already know what a Min is and Max is, so it's very easy to understand about this concepts. By the way, we're not going to be directly dealing with Medians or Means, but know that Median is a good reference point, because sometimes there can be different numbers in a given array that can actually diverge the Mean, or increase the Mean in an unwanted way, like outliers, so Median can be a good reference point to understand whether you're doing the right thing by looking at the Mean or the average of that array.

So, that's it for all the terms. But, of course, we need to go a little bit deeper. So, consider this scenario. We have the Mean, right, it's 43.57.

So maybe I want to know, how many Variance or how many different points that I have in a given array. So, for example, over here it's very easy to understand, the numbers are not very far away from each other, and we have only 7 numbers. But consider that you have 1 million points, you have 1 million numbers to analyze, and you don't even have a clue in order to understand if they're, like, very close to each other, or if they are very far away from each other, if it start with 0, and if it all goes all the way up to the 1 billion, you don't know. So, how do you get a measure for that?

So we know the Mean, then you get every number and you subtract it from the Mean, like this, okay, I just go on and on and on and subtract it from the Mean. Of course, some of them will give us kind of negative numbers, because they are less than average, and some of them will be positive numbers. So if we sum all of those things together, it will just converge to the 0, and it won't do good. So rather than that, we actually take a square of this things, okay, we take the square of this differences, and we add them together.

So it's called variance, we have 515 variance in that given list. Okay, so this is a good point in order to understand whether this is a varied, or like it has a big variance or something in a given array, but it doesn't make sense, because we squared everything, okay, we don't even have a number, like 500, or here, the maximum is 79. So 500 number by itself doesn't mean a thing. We call it variance, and it's good to compare with other variances may be some time, but there is a better measure that we can use it, called standard deviation.

If we take square root of this variance, it gives us the standard deviation. Now you can easily intuitively understand what it means. It's the standard deviation of this given list. So we have this Mean between 40 and 55 and the standard deviation from the Mean itself is 22.

So, you can compare this with the given numbers, or the average, or the Median, in order to understand whether you have too much big of a variance inside of a given array, or they are close to each other. So I don't know how you're going to use this information in your analysis, but, of course, this can be very helpful or useful, right? Maybe you may want to get rid of the outliers or some kind of broken data, and just compare your standard deviation later on, in order to understand if you get a better result or something like that. But we are not interested in the data analysis or kind of machine learning at this point, we are only interested in taking these squares of this variations and just adding of them together and taking the square root of this variance in order to go into the standard deviation, because that's kind of very similar what we're going to do in the quantum computing sections as well.

So far so good. Let's stop here and continue within the next one.
