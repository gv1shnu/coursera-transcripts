# Volatility and Reuse

- **Course:** Pearson System Design Fundamentals Livelesson Video Training
- **Module 1:** System Design Fundamentals
- **Lecture #:** 22
- **URL:** https://www.coursera.org/learn/pearson-system-design-fundamentals-livelesson-video-training-n1kdi/lecture/EFsDl/volatility-and-reuse
- **Extracted:** 2026-06-20 11:04:07

---

So far we discussed structure as a way of accelerating the design of having a better starting point of recognizing the common areas of volatility in the relationship. But you can take it a step further by looking for certain design attributes or qualities in your design that will tell you if you are on the right track. Some key observations that you should look for in systems that are designed along this methodology. First is that volatility decreases top down.

What does it mean? The top layer, the clients, represent the most volatile entities. Clients have enormous amount of churn. Some clients want it in mobile, some want it in a webpage, some want it in blue, and some want vanilla.

And you're going to have all this churn on top of your system while in fact nothing really changes underneath. So clients are very volatile. Managers are also volatile. Not as much as clients, but every time there's a change in the required behavior of the system, you're going to have to change some of the managers.

Engines are not as volatile as managers. For an engine to change has to be a fundamental change in the way of doing a particular activity. And that's not that likely. How many ways you have of calculating this versus that, there's a finite set, and that's about it.

Resource access are even more stable than engines and less volatile. Why? Because they expose atomic business verbs that never change. So for the resource access to change, either you change the way you access a resource, which could happen, or you change the resource, which hardly ever happens.

And resources are incredibly stable. They hardly ever change. They're like sentinels. Sometimes the organization is okay with designing the next generation system, provided you use the existing database, because nobody wants to pay for data migration.

So volatility decreases top-down, and that's actually a very good thing, because if you have a layered architecture and volatility does not decrease top-down, then maybe it increases top-down. Now, the further down things are, the more the things above depend on them. So if the things you depend upon the most are also the most volatile, you have a recipe for disaster, because things detonate on top because of the compounding volatility. But if volatility decreases top-down, then you have stability.

The flip side is that reuse increases top-down. Clients are not reusable. This form, this client, this particular customer, and that's it. The managers are reusable.

You can reuse that manager for this client over here and that client over there. Engines are even more usable, because you can reuse them on behalf of this manager over here, and that manager over here, and that client, and this client, and that client. Resource action is even more reusable, because you can call it across all engines and all managers. And resources are so reusable, you can even reuse them across systems.

The other observation is that managers should be almost expendable. To discuss what almost expendable means, we have to use an example. If you're looking at, say, a paper cup or disposable forks and such, those are clearly expendable things. You don't quite do much when you lose one of these things.

But look, for example, at this laptop. I would definitely be upset if this laptop would die now on me. It would set me up to lose a pretty penny, because I paid for this laptop. But once I plug in a replacing laptop, nothing else in my life would actually change.

So, differently, this laptop is not expendable, but it is almost expendable. Managers should be almost expendable, meaning if there's a change in a manager and your response is, yeah, okay, whatever, that is not a good response. That means you have a pass-through manager, manager in name only. And it's not a good response.

If your response is, oh my God, what do we do? No, no, this would cost us so much to change that manager, that's not a good response. But if your response is, mm-hmm, mm-hmm, well, what I could do is I could go into the area. Okay, that's a very good response when it comes to a manager.

Now, people that follow my teaching tend to never do a pure functional decomposition ever again, at least that. But they don't practice enough. And sometimes what happens is that when they design a system, they encapsulate the most glaring, the most obvious volatilities, and the rest, they just do functional decomposition. And a very telltale sign is in such a half-baked system where you don't see these things, meaning volatility is absolutely not decreasing top-down, use doesn't increase top-down, and managers are not almost expendable.

So if you see these things, it's a red flag. It tells you, look, you're not quite there yet. You still have some functionality you need to scribe. You haven't identified all the volatilities.

Keep digging here.
