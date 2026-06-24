# Decomposition and Business

- **Course:** Pearson System Design Fundamentals Livelesson Video Training
- **Module 1:** System Design Fundamentals
- **Lecture #:** 11
- **URL:** https://www.coursera.org/learn/pearson-system-design-fundamentals-livelesson-video-training-n1kdi/lecture/g3lnq/decomposition-and-business
- **Extracted:** 2026-06-20 11:02:49

---

There's another thing that I've noticed over the years. I've taught these ideas to probably thousands of people by now. And I've noticed that there's a saying that the most zealous with any new idea are the new converts. And the reason the new converts are the most zealous is because if you spent years doing it wrong and then you recognize you did it wrong, it will heave on you to be an irresistible burden.

And you are going to try to undo the sins of the past by overdoing the present. And what does it mean? You're going to say, well, this could change and this could change and this could change and this could change. Encapsulate, encapsulate, encapsulate.

All of a sudden, you will have an explosion of building blocks in your architecture. And we know that's not going to be a good design. And so the question is, what do you have to do here? And the guideline here is very simple.

You must avoid encapsulating changes to the nature of the business. The nature of the business hardly ever changes. And it doesn't mean it can't change. It just means you don't encapsulate it.

For example, supposing to build a single family home, is it impossible that in the future the house owner is going to have an irresistible urge to extend the building into 30 floors skyscraper? No, it's possible. So you need to encapsulate the changes. OK, let's talk about foundation.

Can you put a 30 floor skyscraper on a single family home foundation? No, because it will fall to the bottom of the earth at this point. Which means you have to fortify the foundation by driving into the earth friction pylon foundation, basically these long tubes that go down 300 foot into the earth. And then they add so much friction, it carries the weight of the building.

And by the way, I need maybe 200 of them. So you add those. So now the foundation can support a skyscraper. What kind of a power panel you need with a single family home versus a 30 floor skyscraper?

With a 30 floor skyscraper, you probably need your own transformer. So you put a transformer. Well what about water? The local water company can probably get water to the building, no problem.

But 30 floors up, that's on you. OK, so you put a pump. And you keep doing all of these things, and now you're ready for having a transition from a single family home to a 30 floor skyscraper. The problem is now you're violating this guideline, because now you try to encapsulate the changes in each of the business.

No longer is the house in the business of housing a family, now it's in the business of being an office building or a hotel, which is a different business. And I told you, don't encapsulate that. So you could be saying, well, how do I know? Well, the problem is that whenever you try and encapsulate a change in the nature of the business, you're no longer designing, you're speculating.

So I'll give you two hints that will tell you that you have fallen into the speculative design trap. The first hint is that changes in the nature of the business are incredibly rare. If I were to ask you not, is it impossible that the house owner is going to want to extend it in the future to a 30 floor skyscraper? But if I were to ask you, how likely is it, you would tell me, not very likely.

Let's look, for example, at the California Bay Area. As far as order of magnitude, there's probably a million homes in the California Bay Area. Once a year, how many of them are converted to a skyscraper? Probably not even one.

Over a decade, maybe one. So we're talking about a change that's one in 10 million. It's a ridiculously rare change. The other hint I can give you is that whenever you try and encapsulate a change in the nature of the business, you always find yourself doing a poor job.

What does it mean? Do you have enough money for those friction pylon foundations? One pylon costs more than a single family home. Do you have enough muscle to negotiate with the power company to get your own transformer?

Probably not. Will you sacrifice a whole bedroom for the pump? Probably not. So as you try and put in place the mitigation that encapsulates a change in the nature of the business, you always find yourself doing a poor job.

You know what? When you do a poor job, it's an indication you probably shouldn't do it in the first place. Now you're no longer designing, now you're speculating. Here's a visualization of speculative design.

Let's examine this entity. Suppose the lady is going to dance on the ballroom floor, and then is it impossible that she's going to get an urge to walk out the balcony, put on scuba gear, and dive into the reef? Is it impossible? Well, the answer is no.

It could happen. But how likely is it? It's not very likely. And also, are these things as elegant as regular high-heeled shoes?

Are these things as comfortable to walk over sharp coral as regular flippers? The answer is no. Anything these things try and do, they are poor at. Why?

This is speculative design. And the reason it's speculative design is because it tried to encapsulate a change to the nature of the business. No longer it's in the business of being a fashion accessory, now it's in the business of being a scuba accessory, which is a completely different business. Do not engage in speculative design.

Another technique is to adopt a posture that you never design for yourself, you only design for your competitors, for your arch-nemesis. For example, suppose you're the architect for Federal Express, and you design a system. Let's do the following mental experiment. Suppose we take a mental experiment.

We're taking a magic wand, we're waving it in the air, and we're lifting all the code off the servers of Federal Express. And then we're going to do a massive search and replace. We're going to replace every string with Federal Express, with the string UPS, we're going to paint all the trucks from white to brown, we're going to change all the tracking from grids to strings, but definitely we're going to do all the cosmetics. You got it?

We're going to do all the cosmetics, and then we're going to take the magic wand, go to the server room of UPS, dump the code on the servers. My question to you, is it going to work? Well, on the face of it, there's no reason why this mental exercise is not going to work. These guys have white trucks, these guys have brown trucks, these guys ship packages, these guys ship packages, these guys have tracking, these guys have tracking, so why would it not work?

And the reason it's not going to work is the following. Suppose you need to issue insurance for the packages. Suppose Federal Express, when you want to insure a package, goes to Lloyd's in London and buys a policy for you. But maybe UPS says, our internal tracking is so good, we are not going to lose your package.

And so we're basically going to self-insure. You want to insure it, you're making a bet with us that we are going to lose it, we make a bet we're not going to lose it, we're just going to pocket the money. Or maybe the route planning, Federal Express, say, plans the route for quickest delivery, but maybe UPS plans the track for least amount of fuel spent. Or maybe they minimize the number of left turns so that they're going to have the safest route.

And there are going to be a million such differences. So while they're in the same business, the way they go about doing that business is totally different. And the result is lift and shift with the magic wand is never going to work. And this is a wonderful design tool.

Why? Because if you need to design a system for Federal Express, you start by asking, why can't we use the UPS system? Well, it's because we insure it like this and they insure it like that. Uh-huh, then perhaps insurance is volatile.

How is DHL doing it? Is there a third way of doing it? Well, it's definitely volatile. How about route planning?

And on and on and on. And so by designing for your competitor, you very quickly identify the components that are actually the areas of volatility to put inside components of your architecture. Now suppose you identify something that you and your competitor are doing exactly the same way. This is typically a strong indication it's pertaining to the nature of the business.

And as a result, you should not encapsulate it. That is actually not going to change. What does it mean? Federal Express could, in theory, at some point in the future, move into ballistic missile control.

There's some probability of that happening, but how likely is it? And what's the likelihood of it happening any time soon in the life of the system? And the answer is not very likely. It's just not going to happen.

Why? Because the processes don't change their nature very quickly. Now I mentioned to you that doing volatility-based decomposition is not going to be easy. And the reason is nobody understands what we've discussed so far.

Everybody is going to be hell-bent on doing it the worst possible way, which is functional decomposition. Now if you think that every few years you can actually waltz to a whiteboard, draw a few lines, and nail it, you're kidding yourself. Being good at anything requires patience and practice. In fact, there's an old adage that says to be really good at something, you need 10,000 hours, which is about 10 years of work.

And in software architecture, it's even worse. Think about it. How often do you actually get to do architecture? You get to do architecture only in major revolutions when it's a new system.

And how often is that? Well, it typically happens every few years, maybe once a decade. And companies try and avoid doing it because software is getting so complex and so expensive, they try and amortize the cost of developing the system over the longest possible cycle. And how much time you're actually going to get to actually even do the architecture in the first place?

You may get a few days, maybe a week, but you're not going to get more than a few weeks. It's just not going to happen. Now, if it's a week versus years, it's roughly 2% of the time, which means whenever you spend 2% of the time on something, you're never actually going to be good at it. This has nothing to do with how smart you are.

It has everything to do with dedication and focus and practice, which means in a few years from now, maybe tomorrow, when you will get that chance to design a system, you have to go to the whiteboard and completely nail it. You're not going to get more than a few days to a week to do the architecture. And the architecture has to be good for the next 10 years in spite of all the changes that are going to happen. That is the essence of a good design.

And so you have to do it in near zero time. And this would also avoid the need to argue and educate and pontificate with everybody about getting to do it right. Never ask for permission for doing anything right. You do the right things because they're the right things to do, not because somebody gave you permission for doing it.

And so that means you need to practice and practice and practice. Any professional out there spends an enormous amount of time practicing. Think about doctors. Doctors don't just study from anatomy books and then start cutting up patients.

Doctors spend an enormous amount of time chopping up cadavers. And even when they have patients that are closely supervised for several years. Think about pilots. Professional pilots spend years, plural, years in simulators.

And they practice every conceivable emergency. And even when they are in the cockpit flying, the reason that there is a senior pilot in the cockpit because the co-pilot who's actually flying the plane is actually under training. Any professional, we expect to actually practice their trade. You need to do the same.

You need to acquire the self-respect and the discipline to practice. So you need to practice on everyday systems. Look at your past projects. Past projects are your reservoir of cadavers.

The reason doctors practice on cadavers is because they don't complain if they make a mistake. You need to practice on your past projects. And past projects in software are fantastic because in hindsight, you already know where the pain was. Oh, they changed this, and then they changed that, and oh, OK, maybe that was volatile.

Imagine we had a box for it. And then we changed this, and oh, well, that was definitely volatile. We put another component, and so on. So examine all your past projects.

Look at your current project. First of all, you may be able to save it from the clutches of functional decomposition. But even if it's already doomed, you can actually, purely from a deductive perspective, practice on your current project. You are already experiencing the pain today.

Ask yourself, if I were to do it differently, what would that look like? Imagine designing a non-software system, design a laptop this way, a house, a bicycle. These ideas are universal, and you need to develop the muscles in your head for getting to do it conclusively, decisively, and quickly. And you have to practice and practice.

Some tasks you simply cannot learn by reading a book or watching a YouTube clip. You need to get the muscle memory for doing it.
