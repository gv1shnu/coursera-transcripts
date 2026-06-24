# Managers and Engines

- **Course:** Pearson System Design Fundamentals Livelesson Video Training
- **Module 1:** System Design Fundamentals
- **Lecture #:** 23
- **URL:** https://www.coursera.org/learn/pearson-system-design-fundamentals-livelesson-video-training-n1kdi/lecture/ucWlR/managers-and-engines
- **Extracted:** 2026-06-20 11:04:14

---

One of the things people struggle with initially is what exactly is a merger, what exactly is an engine? Now, I gave you the definition. Merger encapsulates the sequence, engine encapsulates the activities. But I can give you some additional guidelines.

Merger names tend to be nouns. And if the merger name is verb or not verb, that means you have functional decomposition. For example, bank manager is a good manager. But billing manager is a really bad manager.

The same is true with resource access. Engines tend to be verb-like, so calculating engine, validating engine, matching engine, these are all good engines. But account engine means you have some kind of a functional decomposition. I can also tell you that engines are somewhat rare.

Over the years, we discovered empirically that there's a golden ratio between managers and engines in favor of managers. Meaning they follow some kind of a Fibonacci series. So if you have one manager, you may have zero engines, or you could have one engine. If you have two managers, you have one engine.

If you have three managers, you have two engines. If you have five managers, I already have serious question, but you're gonna have three engines. If you have eight managers, you've already failed because that system is way too complex. And so you have far fewer engines than you actually think.

And I have to caution about that, because quite often, the cardinality of engines, the number of engines, is the escape hatch for most people that still want to do functional decomposition. Because engines are the closest it gets to areas of functionality. Because activities and functionalities are fairly similar. As a result, when they try and still hide some functional decomposition in this kind of an architecture, you will see an explosion of engines, where each engine corresponds to some kind of functionality.

But in a well-designed system, you'll find that engines are somewhat rare. And the reason is, there has to be some fundamental volatility and open-ended number of ways of doing something to merit an engine. If there's only two or three ways of doing it and no more, then you need a switch statement. You don't need another block in your architecture.

I really mean it when I'm saying, decompose based on volatility. Don't confuse what is volatile with what is variable. You can absolutely have variability, and that's just code. A component in the architecture corresponds to a volatility.

And there's a lot less volatility in activities than there is, for example, in sequencing. Engines tend to do things. They aggregate and strategize and validate and calculate. They are very much in the do section.

Another interesting observation is that the four layers in the methodology I showed you correspond loosely with the English questions of who, what, how, and where. Client is who is doing something to your system. Manager is what you're doing. Engine is how you do it from the business perspective.

Resource access is how you're going to access. And resource is where you do the access. And I'm saying loosely because it's not perfect, meaning not every what would mature into a manager. And certainly, managers can encapsulate several what's.

But by and large, it's a good initial take. And it's very useful both for validation and initiation. Let's start with initiation. Suppose you know nothing about the system.

You may be given nothing, not even requirements. So what do you do now? You say, let me make a list of all the who. Let me make a list of all the what.

Let me make a list of all the hows. And you start in a very coarse way, toss into those bins the possible candidates. Now, it may not be that every who would be a client and every what would be a manager, but it's a starting point to start wrapping your brain around what you need to do. It's also good for validation.

Do the architecture, and then take a step back and reflect on it. Are all my clients who? There's not a smidgen of what. Are all my managers what?

There's not a smidgen of how, and so on. So it's a great validation technique.
