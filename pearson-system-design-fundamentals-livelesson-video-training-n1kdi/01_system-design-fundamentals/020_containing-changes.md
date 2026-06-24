# Containing Changes

- **Course:** Pearson System Design Fundamentals Livelesson Video Training
- **Module 1:** System Design Fundamentals
- **Lecture #:** 20
- **URL:** https://www.coursera.org/learn/pearson-system-design-fundamentals-livelesson-video-training-n1kdi/lecture/zeA42/containing-changes
- **Extracted:** 2026-06-20 11:03:53

---

So let's go back to what we discussed before about structure. Change is good, change is wonderful, change is what keeps all of us employed. Now let's define a live system versus a dead system. A live system is a system people use, and a dead system is a system people don't use.

Okay, I think that's a good definition. Now, most systems are designed against the requirements, functional decomposition. In such a system, by definition, the change is not in any one place, and so it's horrendously expensive. It is incredibly painful to change anything in a functionally decomposed system.

Since people don't like pain, even when it's self-inflicted, I mean, the customer didn't insist on doing it the worst possible way, so that's totally on you. They will try and punt the pain, they will take future pain over present pain. And they will say, I will add it to the semi-annual release. Why?

I'll take future pain over present pain. But I have news for you. The customer doesn't want the feature six months from now. The customer wants the feature now.

Part and parcel of responding to change is responding quickly, even if it's not stated. And so your system must respond to change and must respond quickly. The trick is not in fighting the change. Anybody can fight the change.

The trick is in minimizing its impact. There's always going to be impact for the change, but you want to get away with the least amount of impact, not the most amount of impact. Functional decomposition maximizes the impact. Because it's decomposed based on functionality, not based on change or based on volatility, by definition, the change is spread across multiple places.

And Murphy says, it's on all places. And if you do things like domain decomposition, you have to change it to multiple places because every domain duplicates all other domains. Now let's look at a system design according to the methodology I offered you in this presentation. The change in the use case means a change to the required behavior, to the workflow.

And that means a change to the manager. The manager may be gravely impacted by the change. Maybe everything inside the manager is completely toast. You have to write the manager again.

However, none of the underlying services are impacted by the change. If you do the correct system structure, where is the bulk of the effort of building the system? Think about everything that goes into building engines. All the ways of doing particular activities.

That's a ton of effort to get right. Think about doing resource access and not just talking, writing some stored procedure. Truly identifying the atomic business verbs and then mapping those to resource access. Well, that's a lot of work.

Think about all the effort that goes into designing a resource. And I'm not talking about just having a silly table somewhere. What does it take to design a resource to be infinitely scalable and to be just as useful on-premise and on the cloud? And to be indexable and scalable and all of that.

My God, that's a ton of effort. Think about what it takes to do good clients. I'm not talking about just some buttons and forms. How about the user experience?

How about looking at all the ways the clients are trying to do something, be it flesh and blood or APIs, and say, what is the least amount of effort we can possibly do? Meaning, let me try and see what they are trying to do and provide them the most bang for the buck. There's typically some 80-20 pareto distribution where 80% of the time they're doing 20% of the features. Say, you know what?

Look at those 20%, streamline those, automate those, and so on. Well, you know what? That's a superior user experience. Takes a lot of time to do.

How about designing APIs? Most people don't understand how to design an API. An API is a statement of vanity. Look how clever I am.

Look how complex my system is. This is not a good API because if you put yourself in the shoes of those consuming the APIs, you will realize they don't want to use the API. They want to have used the APIs. They want to get away with the least amount of effort interacting with your system and move along, okay?

So what is the correct API? A correct API offers the least amount of chinks in the armor, the least amount of cross-section, and gives them the most work. How about doing utilities, infrastructure, automated build, regression testing, diagnostic, message bus, pub-sub, logbook, security? All of it is a ton of work.

But think about it. None of the items on the list I just said has anything to do with a change to the workflow, to the required behavior. That change is contained inside the manager. So that means you have salvaged the bulk of the effort that goes into implementing the system, and you contain it inside the manager, and you can quickly respond to change.

Now think about it. The ability to quickly respond to changes in required behavior, is that not the essence of agility? Most people have said the word agile hundreds of thousands of times in their life and had no idea what it actually means. Most people when they say agile refers to the ritual, to the artifacts.

That has nothing to do with agility. If you need to be agile, not to do agile, to be agile, you have to do what we discussed so far. What I propose to you in this presentation is how to offer the agility that every business craves and what most developers have denied. Because they did functional decomposition.

When you do functional decomposition, you guarantee the lack of agility. Now, of course, you did something else. You did the artifacts, the process, the voodoo, and called yourself agile. But that's not the essence of it.

You were doing agile, you weren't being agile. The essence of agility is the ability to respond quickly to changes in the business, that's it. How to do that to contain change? How to do that?

Volatility-based decomposition. What does it mean? Everything we discussed so far and what you see in front of you is also almost a mathematical proof how you can actually do it.
