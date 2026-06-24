# Implementation and Analysis

- **Course:** Algorithmic Toolbox
- **Module 3:** Greedy Algorithms
- **Lecture #:** 22
- **URL:** https://www.coursera.org/learn/algorithmic-toolbox/lecture/1nFS5/implementation-and-analysis
- **Extracted:** 2026-06-20 19:12:47

---

Hi, in the previous video we came up with a greedy algorithm for arranging patients optimally in a cube. And we proved that this greedy algorithm works correctly. In this video we're going to implement this algorithm and analyze its performance. Here is the pseudo code for this algorithm function MinTotalWaitingTime which takes as input the treatment times for all the patients in an array t.

And also the number of the patients n. It is going to return the total waiting time for all the patients. And if needed, it can be easily changed to also output the order in which to treat the patients. I just permitted that for simplicity of the code.

So we start with initializing the value which we're going to return, the waiting time which is the total waiting time for all the patients with zero, because nobody has waited yet. Also, we'll need this auxiliary array treated which is an array of n zeros initially. And in position i, it has a zero if patient i has not yet been treated and it will have one as soon as patient i is treated. Now we're going to go through this external for loop which has n iterations because we need to treat exactly n patients.

And first we're going to find the minimum treatment time of all the patient because you remember we need to treat the patient with the minimum treatment time first but not the patient with the minimum treatment time of all the patients. Just the patient with the minimum treatment time of all the patients which are not yet treated. So we initialize this total treatment minimum treatment time with plus infinity. Tmin is equal to plus infinity.

We also initialize the index of the patient we're going to treat with zero and we're going to update it as soon as we find the patient with the minimum treatment time. And now we have this internal for loop for j from one to n which is going through all the patients. And we first test whether this patient was treated before. So if treated of j is equal to zero, this means that patient number j hasn't yet been treated so we can consider this patient.

And if also the treatment time for this patient is less than the current value for the minimum treatment time, then we need to update both the minimum treatment time to be equal to this treatment time of this patient. And also the index of the patient with the minimum treatment time needs to be updated to j. And in the end when this inner for loop finishes we will have the minimum treatment time of all the remaining patients in the variable tmin. And the index of the patient with the minimum treatment time in the variable min index.

Now we need to update the total waiting time for all the patients. By this time, we have already made i iterations of the for loop. It means that we have treated first i patients and n minus i remaining patients are going to wait for the treatment of the patient with the treatment time tmin. So n minus i patients are going to wait for this patient with minimum treatment time tmin.

It means that the total waiting time for these patients increases by n minus i number of patients times tmin, the time for which all of them are going to wait. We only account for them waiting for this particular patient because afterwards in the next situations we're going to also account for them waiting to some of the remaining patients. But for now when we account for all of them waiting for the patient we are currently choosing to treat the patient with the minimum treatment time tmin. So we update waiting time by adding n minus i times tmin.

And also we should not forget to write down that the patient number mean index is now treated. And so we assign one to the array treated of mean index. And in the end when all n iterations of the external for loops are finished, it means that we have treated all the patients. We have updated the waiting time to be the total waiting time of all the patients.

And we can return the waiting time variable which contains the total waiting time. If we also wanted to output the order in which we need to treat the patients, it would be very easy. We would just need to add printing out the variable mean index in the end of the external for loop at each iteration. And that would be exactly the order in which we decided to treat the patients.

So this is the whole algorithm. Now let's analyze its performance. The lemma states that the running time of MinTotalWaitingTime is big O of n squared. Let's prove that.

So in the external for loop, variable i changes from one to n. We have just n iterations and in the internal for loop for each value of i, j changes from one to n. So it also has n iteration. So this gives us big O of n squared and everything else is just less than that.

There are some constant time operations inside the external for loop but that just adds another linear time. So all in all, this is n squared time for the old algorithm. Actually this problem can be solved faster in time big O of n log n. And to do that we need to notice that instead of choosing the patient with the minimum treatment time each time out of the remaining ones, and doing that for n times, we could just sort patients by increasing treatment time beforehand.

And then if we sorted all the patients by increasing treatment time, this sort of arrangement is already optimal. And then on each step we just need to select the patient number i for i from one to n, we just select the patient number i in order and treat this patient and update the waiting time. And so we can avoid this internal for loop with variable j to select the patient with the minimum treatment time because I already know who is the patient with the minimum treatment time out of all the remaining ones. And so our remaining algorithm after sorting would be just linear which is linearly go through each of the patients.

And we update the total waiting time and we print the number of this patient, that's all. So it is possible actually to sort those n patient in time big O of n log n, and you will learn how to do that in the next module. And if we assume that we can already to do that, then we just need n log n time to sort the patient, an additional linear time to solve the problem after sorting them. So all in all, n log n is bigger than linear time.

So all in all we'll have complexity big O of n log n. And in the next module you're going to study sorting algorithms and you will know how to sort the patients. But before that we're going to continue studying greedy algorithms. And in the next video we'll just review some of the concepts we've just learned and how they generalize into the concept of greedy algorithm.
