# Queue of Patients

- **Course:** Algorithmic Toolbox
- **Module 3:** Greedy Algorithms
- **Lecture #:** 21
- **URL:** https://www.coursera.org/learn/algorithmic-toolbox/lecture/ixvcz/queue-of-patients
- **Extracted:** 2026-06-20 19:12:35

---

Hi, in this video we're going to solve one more problem using a greedy algorithm. Imagine the following situation, you're an administrator in the doctor's office and a lot of patients have just come at the same time and they're all ill and angry and they don't want to wait. And you need to somehow arranged them in the queue so that the total waiting time for them is minimized. More formally, n patients have come to the doctor's office at the same time let's say 9:AM and they can be treated in any order because they just came all at the same time.

For the patient number i the time needed for treatment you know beforehand and it is equal to ti. We just assume that you can estimate the treatment time for any patient after just looking at the patient. So you need to arrange all the patients in such a queue that the total waiting time is minimized. The queue is organized because the doctor is just a single doctor and can treat patients one by one, one after another and then the first patient doesn't wait at all.

The second patient waits for the treatment of the first patient, the third patient waits for the treatment of the 1st and 2nd patients and so on. There are no delays, so, the doctor works all the day through but the patients are waiting for the previous patients and for not anything else. So, you need to make the total waiting time. That is the sum of waiting times for all the patients to be the minimum possible.

So for example, if you have just three patients waiting the first one with treatment time of 15 minutes, the second one with treatment time t2, which is called 20 minutes and the third one with waiting time of 10 minutes. And for example you arrange them in the same order, they already in range 1, 2, 3. Then the first patient doesn't wait long, the second patient waits for the first patient which is 15 minutes treatment time and the third patient waits for both the first patient for 15 minutes and then the second patient for 20 minutes. And that's waiting time of 35 minutes.

Then the total waiting time is zero plus 15 minutes for the second patients plus 35 minutes for the third patient which is total waiting time of 50 minutes. Now, let's look at another arrangement example. If you first put the third patient then the first patient which is now number three doesn't wait at all, the second patient which is number one waits for 10 minutes because the treatment time for the third patient t3 is 10 minutes. And the second patient in the queue waits only for the first patient in the queue which is the third one with 10 minutes waiting time.

So, it's 10 minutes waiting time for the second patient in the queue and the third patient in the queue is number two. So he waits for the first patient in the queue with 10 minutes treatment time, then he also waits for another 15 minutes for the second patient in the queue which is the patient number one. And the total waiting time for the third patient is 10 plus 15 which is 25 minutes. And then the total waiting time is zero plus 10 minutes for the second patient in the queue, plus 25 minutes for the third patient in the queue, which is the total waiting time of 35 minutes and 35 minutes is less than 50 minutes in the first example.

So, this arrangement is better. So, what to do in the general case. Well, we want to apply some greedy strategy. And greedy strategy works like following you just make some greedy choice and then you reduce your problem to a smaller problem of the same kind and then you iterate until your problem reduces or increases and there is nothing left to solve.

So, in this case for example, greedy choice could be one of the following like first treat the patient with the maximum treatment time of all the patients. Another choice could be first treat the patient with the minimum treatment time of all the patients. And the third option could be just take some average patient, just the patient with the treatment time, which is the closest to the average treatment time of all the patients. So, what do you think would be a good choice in this problem?

Well, in this problem we're going to apply the following greedy algorithms. So, we are going to first treat the patient with the minimum treatment time. And we're going to prove just in a few minutes that this is the optimal choice. So we first treat the patient with the minimum treatment time and then we remove this patient from the queue.

And then we treat all the remaining patients in the queue in such order. So that to minimize their total waiting time as if there was no first patient. So, this is the greedy strategy. So we first treat the patient with the minimum treatment time and we reduce the problem to the problem where we have one patient less and then we treat all the remaining patients also in the same way in the greedy manner.

So, the definition of a sub problem that sub problem is a similar problem of smaller size. For example if we have 10 patients in the beginning and we need to arrange them in the queue and we somehow choose the first one and treat him. Then we are left with only nine patients and we need to arrange them so that to minimize their total waiting time. This is a similar problem but just a smaller size because we have less patients, nine instead of 10.

So, examples of some problem for the previous problem we're solving in the previous video maximizing their salary you're given five digits 1, 9, 8,9 and 6, and you need to maximize the salary which consists of these numbers. And to do that you first make a greedy choice. You take the the maximum digit 9 and put it first and then you append to it the solution of the problem with digits 1, 8, 9 and 6 which are left when you remove this maximum digit. So, this is one kind of sub problem.

Find the maximum salary consisting of a small number of digits. Another kind is this problem, so, you need to minimize the total waiting time for and patients. So, you first consider the patient with the minimum treatment time tmin and then you put this patient first. And when you put this patient first it means that all other patients are going to wait for this patient.

So, n -1 patient is going to wait for this first patient. So, n -1 times tmin is the total waiting time of all other patients for this patient. Apart from this waiting time they're going to wait some more. But this is already a sub problem, similar problem because now you're going to arrange all the other patients in some way so that they're waiting time for each other is the minimum possible.

But it is already not accounting for all of them waiting for the patient with the minimum treatment time. We just forget about this patient after we accounted for n -1 patients waiting for him already. So, this is a sub problem, now we need to arrange all the other patients in such a way that each of them waits for all previous ones as small time as possible. And we forget that all of them have already waited for the first one.

So, another definition of safe choice. A greedy choice like treat the patient with the minimum treatment time first or with the maximum treatment time first or something else. So any greedy choice is called a safe choice if there is an optimal solution of the problem which is consistent with this first choice. So for example, if we prove that there exists an optimal solution which starts with treating a patient with the minimum treatment time, then choosing such a patient is a safe choice.

If however, we choose a patient with a maximum treatment time and then there could be no optimal solution which starts with treating such a patient. So, this will not be a safe choice. Now, we're going to prove the following lemma that to treat the patient with minimum treatment time, tmin is a safe choice in our arrangement problem. The proof idea is the following.

So, what do you think? Is it possible for an optimal arrangement of patients in the queue to have two consecutive patient in order with treatment times t1 and t2? So, that t1 is bigger than t2, so that the patient with bigger treatment time is going to be treated before a patient with smaller treatment time. And the answer is this is impossible.

And to prove that, assume that there is such optimal arrangement and consider what happens if we just swap these two patients and don't touch any of the other patients, what happens? So if we swap these two consecutive patients with written times t1 and t2 or t1 is bigger than t2, then the waiting time for all the previous patients before the first one of them doesn't change. The waiting time for all the patients after the second one also doesn't change. The only thing that changes the waiting time for the first and the second of these two consecutive patients.

So for the first one of them, the one which was first after we swap them, he now needs to also wait for the second patient for additional t2 minutes. And for the second patient which was second initially after we swap them, now, he doesn't need to wait for the first patient. So, he's waiting time is decreased by t1. And so, the total waiting time doesn't change for the patients before and after these two and it changes by t2 minus t1.

It increases by t2 for the first one and decreases by t1 for the second one. So actually, t2 minus t1 is less than zero because t1 is bigger than t2. So, actually the total waiting time decreases. But this is a contradiction to the assumption that this was an optimal arrangement of patients in a queue.

So, it cannot happen. So, we just proved dilemma that in any optimal arrangement of the patients, first of any two consecutive patients has smaller treatment time of the two. And so, we can now prove that to treat the patient with the minimum treatment time is the safe choice. So, assume that this is not the case and assume that in some optimal arrangement the patient with treatment time tmin is not the first.

Now, let i which is the index bigger than one being the position of the first patient with treatment time equal to tmin in the optimal arrangement. So, we know that i is strictly bigger than one because the first patient is not with the minimum treatment time, we assume that. Then the patient at position i -1 right before that has bigger treatment time because that position i will have the minimum treatment time. And this is the first position with the minimum treatment time.

So, any previous position has strictly bigger treatment time. And this is a contradiction with dilemma was just proved, so, we get the contribution. And so, our assumption is wrong that the patient with minimum treatment time is not the first is wrong, so, we've proved our lemma. And now, in conclusion we know that the following greedy algorithm actually works correctly.

So, we first treat the patient with the minimum treatment time, we remove this patient from the queue and then we solve the sub problem. We treat all the remaining patients in such order as to minimize their total waiting time, forgetting about this first patient, which we have already treated. And in the next video we're going to implement and analyze this algorithm.
