# Serial Versus Parallel Code and Flynn's Taxonomy

- **Course:** Introduction To Concurrent Programming
- **Module 2:** Earn credit towards a degree!
- **Lecture #:** 9
- **URL:** https://www.coursera.org/learn/introduction-to-concurrent-programming/lecture/qL2g8/serial-versus-parallel-code-and-flynns-taxonomy
- **Extracted:** 2026-06-19 21:36:14

---

we are onto the video discussion of cereal versus parallel code in the main way of describing how you can develop code for all situations to show how you can create code to search for value in a data set with serial and parallel means. We will use some pseudo code to illustrate how this can be done. Searches one of the most canonical challenges of computing. So understanding good and bad ways to perform it can help define other analogous processes using sequential or concurrent programming.

Also, as a means of breaking down what happens and what types of programming work for what type of data. We will investigate Flynn's taxonomy. In this code, you will recognize a very simple sequential algorithm for finding the index of a search value in a data set, simply stated iterate through all values in the set. If the search value is equal to the value that you are looking at, return the index otherwise return.

Negative one were not found will be returned. So the good things are that is pretty much the simplest implementation that you can imagine. There is no need to sort the data ahead of time, which can be costly. The negative is that define the index based on the data and the value passed.

You may need to search through all values of the data set. Linear search is not great, especially if to do a lot of search. That is why the cost of sort along with a good algorithm, is preferred. We're hoping to get log arrhythmic Lee computed search based on data set size even if there is a large initial cost to it, especially if the days that can be updated efficiently.

This is one of the more common implementations of search and it is using a divide and conquer solution. We will presume that no matter what data is is always sorted or this will not work. The code divides and conquers the search by picking mid points which are tested to see if they are equal to larger or smaller than the search value. If not equal, the function calls itself with the left or right subsets each one being smaller than the calling function dataset.

If nothing is found, return negative one. The positive aspects of this implementation are that search becomes algorithmic and the cost of search is low. relative to the following usage a search than it is worth the up front cost. If the sort doesn't update efficiently or the data and or computation is distributed, this becomes a very negative cost.

The first thing you will notice about the parallel search said it is more complex since you need to assign correct data to each threat. In this case, that is by uniformly slicing of the data into subsets to evenly distribute the load to each thread. Each thread only searches a small subset of data, and if it finds X that needs to kill the other threats, probably indirectly and return the index. Good parts of this are that no sorting is required and scaling can be managed by increasing the number of threats.

The negatives are that if the number of threads is order of magnitude smaller than the J s eyes, this is just slightly more efficient than the inefficient serial search. Thread management isn't easy, and killing off other threads would be either dangerous or require well thought out logic. This can be improved with pre sorting and binary search, but then it inherits the issues with Ryker version where this shines as if you have lots of threads, and that is where GPS coming more on that later. But if each thread just needs to do a single comparison and only update shared variable if it is found, then you have a constant search time better than log arrhythmic.

So let's take a look at Flynn's tax on. Okay, the first two characters can either be S I or am I single or multiple instruction? Which means do you perform the same logic or different logic on all data? The second two characters can either be SD or ND single or multiple data.

Which means is the data complex or is it numerous and simple in the top left or sequential programs working on a single complex state? Think of it as a program that executes a chess or non trivial game between two humans. Lots of parts. But the game probably can be decomposed.

This isn't about searching for the next move. Just managing state the bottom right of problems. Multiple different processes are doing different things to lots of small pieces of data. This is similar to running multiple filters on pixels in an image or images in a video or something similar.

Each operation may be completely independent of the other. It may not need context, like previous images, the sequence or values for nearby pixels. Most CPU based sequential programs are misty, since there have different processing steps that are meant to work on a single or few complex objects. GPS and other distributed programming solutions are often Cindy, since they aim to use numerous threads and processes running the same logic.

A large amounts of data uses taxonomy to look at your data and what you're trying to do. And then when you determine which of the four is your category, look at applicable languages, frameworks, hardware, etcetera.
