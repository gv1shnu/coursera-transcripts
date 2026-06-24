# Optional: Hungry Chickens Problem

- **Course:** Introduction To Concurrent Programming
- **Module 2:** Earn credit towards a degree!
- **Lecture #:** 7
- **URL:** https://www.coursera.org/learn/introduction-to-concurrent-programming/lecture/BfYPH/optional-hungry-chickens-problem
- **Extracted:** 2026-06-19 21:35:51

---

The first thing we'll see here is a food that I'm going to give the two big donkeys, which one you can see here. These two donkeys act as if there are two large processes in a CPU or alternating or they're getting their food from sometimes come over and bug you for resources. But the point being that there are two cores and two donkeys. There should be enough processing power to have them do what they need to do.

Unfortunately, sometimes the donkeys and the CPU processes may end up trying to take more than they have. But thankfully, the scheduler will keep it such that most of the time they are always active doing what they need. This is a little bit different than what we'll see with the chickens, where there are many chickens and there are more constrained resources. Here we see the chicken feed on the left and the chicken scratch on the right.

The chickens need a feed to live, but literally they like a very sugary scratch. It is used to distract them and keep them from damaging each other. Here is a collection of chickens, I mean processes waiting to get some resources. While I go around, you will see different types of feeders or access points for resources and the water.

What I'm doing now is only giving a few resources in specified slots in the feeder. Each chicken acting as a process is trying its best to get the resource at once. Some chickens are waiting around for more resources to come seeing that the main feeder is not worth their effort. Now I will place resources in one of the slots in the red feeder and close its top.

Chickens will then attempt to get resources from any of the slots. They will start to actually come into resource contention with each other as you see the one packing on the other. Now I've placed resources in each of the slots of the feeder. You would imagine that there will be more opportunity feed, but there isn't.

There isn't enough resources from prospective of the chickens. We need to divide up the feed even more such that the chickens are looking at each other less and fighting over resources. They will continue to fish around looking for an open slot, in this case, the green feeders or the red feeders. Note that they have to be closer to each other because the resources are more readily available.

But at this point, we've avoided deadlock. Now to avoid livelock or over contention for resources or even suboptimal use of processes, I will put scratch on the ground, which further separates the chickens and puts them even in less contact with each other and it gives them the thing they want the most. Thank you and I hope that my chickens and donkeys have helped you think about multiprocessing in a new way.
