# Composable Design

- **Course:** Pearson System Design Fundamentals Livelesson Video Training
- **Module 1:** System Design Fundamentals
- **Lecture #:** 19
- **URL:** https://www.coursera.org/learn/pearson-system-design-fundamentals-livelesson-video-training-n1kdi/lecture/yBkCv/composable-design
- **Extracted:** 2026-06-20 11:03:45

---

We already told you there's a silver lining to this cloud. Even if I were to give you a book with 300 use cases, and all full of holes, are all of these use cases separate, distinct, and unique? And the answer is no. Most of them are variation of other use cases.

We have the main use case, we have the happy case, we have the incomplete case, we have the case we just did for that customer over there. So let's define two types of use cases, core use cases and fluff. Core use cases would bring the customer to the door. Core use cases present the essence of your business.

Now, because the essence of your business hardly ever changes, or it changes at a glacial pace, the core use cases hardly ever change. Now, you have to understand that because the core use case is the essence of your business, you are going to have them in the requirements spec. For example, suppose I were to give you a requirements spec with 200 use cases, and the real number is 300, are you going to miss a core use case? Probably not, simply because that's the essence of the business.

You're going to miss the fluff. And so, the first act of wisdom is when you're receiving even a horrendously flawed requirements spec, you need to analyze it to identify the core use cases. Now, hardly ever the core use cases are going to be explicitly present in the requirements spec. It's almost always the result of some obstruction of other use cases.

There won't be 1.2.3, this is a core use case. You have to look at 4.5.6 and 7.8.9 to actually see what is the core use case. Now, the next observation is how many core use cases we actually have. And what you can do is look at the system you're working on right now and count how many truly distinct core use cases you actually have.

And you can agree or even just on the order of magnitude. It's more like 1, 10, 100, 1,000, 10,000 core use cases. And if you were to try and count it on your fingers, you will find out the number is more or less one. And it's not exactly one, it could be two, it could be three.

But in order of magnitude, three is the same as one. Systems have a ridiculously low number of core use cases. Many systems have just one core use case. Sometimes some systems have two, sometimes three.

Four is a high number, and I've never seen more than six. What does it mean? I've lost count of how many systems we have designed that I design. It's in the many hundreds.

And I have never seen more than six. And the system that had six had the following attributes to it. It was a massive system with 40 services supporting the entire IT infrastructure of one of the largest companies in the world that catered to 120,000 users, 24 by 7 in four continents. You know what, then you get six core use cases.

Most systems are not going to get five or even four. And again, go in your mind and ask how many core use cases we actually have at the system back in the office. Yes, I'm waiting, how long? How many?

Two, three? It's not that many. Often, finding the core use case is an iterative process. If you're not familiar with the domain, work with somebody who is, such as a marketing product manager.

Ask the product manager, give me a book with hundreds of use cases. Suppose out of this entire book, I'm only doing one thing. Which one is it? And you may get some pushback and Michigan is saying, no, no, don't worry about it.

I'm going to do all of it and more. But suppose out of this entire set, I'm only doing one thing. Which one is it? And they're going to say, this one.

And you're going to say, okay, if I were to ask you one more thing, which one would it be? Which point, they give you something else, which is typically a variation of the first. The first is such a core use case, they're going to give you a variation. Say, no, no, no, don't waste a bullet on that one.

Give me something completely different. They will give you something else. By the time you're asking for the third, they're going to be stuttering. Well, I don't know, maybe this, maybe that.

You're not going to get a very large number here. So there could be near infinite number of fluff use cases, but core use cases, very simple, very few. Here's another way of looking at it. Suppose you're asking the same marketing person to come up with a one page brochure for the system.

How many bullets are going to be on the brochure? Well, if the marketing person's going to put ten bullets on the brochure, the marketing person's going to lose their job because we all know there needs to be three bullets on the brochure. And so, again, the number of core use cases is ridiculously small. And so, the first thing you do with requirements is identify the core set of use cases.

Separately from that, you need to identify the smallest set of building blocks that you can put together to satisfy each of the core use cases. That's the mission. Again, you have to identify the smallest set of building blocks that you can put together to satisfy each of the core use cases. Now here's the key idea.

Since all the other use cases are a variation of the core use cases, what they actually represent is a different interaction between your building blocks, not a different decomposition thereof. So now when the requirements change, your design does not. This is such a key observation, I'm going to say the whole thing again. Your mission as an architect is to identify the smallest set of building blocks that you can put together to satisfy each of the core use cases.

Since all the other use cases are a variation of the core use cases, what they actually represent is a different interaction between your building blocks, not a different decomposition thereof. So now when the requirements change, your design does not. And I call this idea composable design. Composable design never tries to satisfy any use case in particular.

It's an exercise in futility. The use cases will change. Over time you're going to get a new one, you're going to change, you're going to remove, it doesn't matter. Let go, stop yearning for this mythical unicorn project where somebody's going to give you finally all the requirements are never going to change.

First of all, it's not going to happen. And second, it's really a bad thing if it does happen because if the requirements will never change, you're not going to have a job. Composable design recognizes that. You try and find the smallest set of services.

Now, composing in a particular way supports a particular use case. Use case change, change the way you put them together. Now, I did say the smallest set of services. I didn't say a set of services.

Why smallest set? Well, first of all, if you can get by by doing less work, that's always good. Architects should always find a way of doing less, not more. And the reason is, as architects, you are high on the pendulum.

And in the pendulum effect, tiny, tiny changes upstream have enormous swings downstairs. You could have just another block for you, just a few pastel pixels, but it could be years of work for somebody else. So you want to minimize that. And so, the smallest set of services.

Suppose I do give you a book with 300 use cases. Well, the smallest possible set of services supporting all 300 use cases is one big service. So I'll take one big service and I'll just bloat it with this monster set of functionalities. And that's my system.

That is a smaller set. But we all know that's also not a good design. It's also not a design you can actually validate. Think about it.

You're only worth validating a big thing is because, because I say so, because it does everything. That's not an engineering approach. The other extreme end is if I give you 300 requirements, or 300 use cases, is have a component in the architecture for each use case. Now we know that's also not a good design because of the explosion in interaction.

Just like the one big thing is not a good design because of the inherent complexity inside that nobody can understand. So somewhere between 1 and 300 is your number, which on one hand is a smaller set, on the other hand is good enough. And let's try and agree on the order of magnitude. Is it more like 1, 10, or 100?

We've already established that 1 is too low, and 100 is too many. And so it has to be about 10. So as far as an order of magnitude, the number of components that you're going to require to satisfy all use cases is about 10. Now when I'm saying order of magnitude, it could be 12, could be 20.

It's not gonna be 100. So it's a relatively small number, a dozen or two components, that's it. And that's all you need. And the reason you don't need more than that is combinatorics.

The number of possible combination of 10 is roughly 10 factorial, which is bazillion. By the time you have 15 or 20, it's like the number of grains of sand on planet Earth. It's enough combination to do anything foreseeable. And if you look at the architecture structure I proposed to you so far, it has about a dozen or two components.

Typically, you're gonna have two or three clients, two or three managers, two, one or two, three engines, four or five resource access and resources, and half a dozen utilities. And that's already in the realm of about 10, it's not 100, it's closer to 10. And so doing volatility-based decomposition along the structure I described to you here will land you in that sweet spot of not too many and not too few. And you're gonna get that critical number of components.

And it turns out everything is designed this way. For example, how many components are in your car? If we were to look at your car as components, well, we have engine block, gearbox, radiator, fuel tank and so on, it's about 10. How many components are in this laptop right here?

Well, I have CPU, graphic card, bus, memory, hard drive, video card, about 10. How many components are here in this body? Well, I have two kidneys, one liver, one heart, one spleen, guts, about 10. Everywhere you look, you will find about 10, and that is not an accident.

It doesn't matter if it's natural evolution that produced our body or artificial evolution produced your car or your laptop, it's about economics. It doesn't make any economic sense to produce more components than what you actually need because then the car or the laptop is too expensive. And you can't go half-baked with too few components because then you're going to die. And so all of these systems have converged on the smallest set of building blocks that they can actually use to satisfy all the requirements.

And again, let's go back to the design of the human body. The design of the human body was put forward on the plains of Africa 160,000 years ago. Now 160,000 years ago, I'm pretty sure that being a software architect wasn't part of the spec at the time. If you're going to ask the average software developer to design somebody like me, they're going to design against the requirements.

They are going to have a box here corresponding to everything I need to do. It would be a box, write a book, conduct a session on software architecture, drive to the airport, more the loan. All the things I need to do, there would be a box here. Now, I actually do not have a box here called conduct a session.

Let me check. No. Therefore, how could I actually deliver this session? To make it even worse, how could I deliver this session using exactly the same components as a pre-Neolithic hunter-gatherer from 160,000 years ago?

For most people, that would not compute. Well, it is true I'm using the same components as a pre-Neolithic hunter-gatherer. The key here is that I'm putting them together in different ways. By the way, the core use case hasn't changed in 100,000 years.

You know what it is? Survive. We only have one core use case, survive. Everything else is fluff.

All systems are put together this way. You can observe something else that comes out of composable design. Composable design is all about recognizing that smaller set of building blocks that you can put together to satisfy all the requirements. Now, you still have to satisfy the requirements.

You still need to provide the features. But features are always and everywhere aspects of integration, not implementation. This is a universal design rule. It is such a fundamental observation, you need to read it again.

Features are always and everywhere aspects of integration, not implementation. For example, I'm giving you now a very valuable feature. I'm teaching you how to design software systems, okay? But how am I doing it?

Well, I have to integrate this laptop, this microphone, this desk, the camera, something that captures the HDMI feedback out of my laptop. All of that has to be integrated. You cannot point at anything in the room around me and say, aha, that's where the, no, no, this is where the presentation is. No, it's not in any one place.

It is the integration of these things. And by the way, I have to integrate internal components as well. I have to integrate my vocal cord, and my liver, and my heart. You take anything out of this, the whole thing is dead.

And so, it's the integration of my body, the laptop, the room, and so on, that provides the feature of this presentation. What is almost as impressive is that this observation that features are always in every aspect of integration is a fractal observation. For example, the overall feature we have here is this presentation. Now, each component here provides a different feature.

My heart provides pumping blood. The laptop provides projection. As far as the laptop is concerned, the laptop doesn't know about this session. It doesn't know about you or me.

The laptop only needs to do presentation. So if I look at this laptop as a system, its feature is sending the HDMI signal. That's all it needs to do. Okay, is there any one thing in this laptop that does the presentation?

And the answer is no. I have to integrate the CPU, the video card, the bus, the hard drive where the PowerPoint slides are actually stored. All of these things have to be integrated to provide the single feature of presentation. Okay, I mentioned the hard drive that stores the PowerPoint.

The hard drive actually doesn't know about the presentation. As far as it is concerned, there's only one feature, which is storage. That's it. Okay, if I look at the hard drive as a system, is there one thing in the hard drive that does the storage?

And the answer is no. It has lots of internal components. It has its own little processing unit. It has some media storage.

It has its own voltage regulator. It has its own clock. It has its own bus. And there's even a box that holds everything together with tiny screws.

And all of that, the integration of all of that, provides the feature of storage. Okay, let's look at the screws. So there's a little screw that holds one piece of the hard drive to another. The screw doesn't know about storage.

The screw provides one feature, which is fastening. Okay, so if I look at the screw, is the one thing that's doing the fastening? No. I have to integrate the thread of the screw, the stem of the screw, the head of the screw, plus some torque to provide the feature of fastening.

You can keep drilling this way all the way down to the quarks, and you will never see a feature. That is how the universe is put together.
