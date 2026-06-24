# Open and Closed Architectures

- **Course:** Pearson System Design Fundamentals Livelesson Video Training
- **Module 1:** System Design Fundamentals
- **Lecture #:** 24
- **URL:** https://www.coursera.org/learn/pearson-system-design-fundamentals-livelesson-video-training-n1kdi/lecture/xraH1/open-and-closed-architectures
- **Extracted:** 2026-06-20 11:04:21

---

Since the methodology I showed you advocates using layers. We also have to discuss two schools of thoughts of how it is to design a system using layers. And I'll discuss the two schools of thought, but in fact there's only one. So only once we discuss both of them, we discuss which one not to use.

So I'm specifically referring to the open and close architecture. In an open architecture, anybody can call anybody else. So you can call up, down, sideways, across all the layers. As a result, open architecture is by far the most flexible, gives you the most options.

But it has enormous amount of potential for coupling. For example, if we were to look at the methodology and the taxonomy we have here. If I'm allowing the engines to call directly to the resource, that would compile. Except now what happen if you want to change the way you access a resource?

Immediately the engines detonates. Or how about the clients calling the resource access? Well, if the clients call the resource access, then all the business logic must be in the clients. And now when the business logic changes, the clients will have to change.

And we know that's a bad idea. So yes, it's flexible, but potential for coupling. How about managers calling the clients, calling up? Well, that would work, except think about what happens.

Suppose the manager wants to update something in the client. If the layout of the GUI changes or the API changes, the manager would have to change. So now you have imported a higher level of volatility to a lower level in your architecture. And now volatility is absolutely not going to decrease going down the layers.

So open architecture on one hand is the most flexible, but has enormous potential for coupling and bad things happening. A closed architecture tries to minimize the potential here. And if you're looking at the scenes of open architecture, calling up down sideways, they're not equally weighted. Calling up is by far the worst thing, because it imports high level volatility to low levels.

And that's really bad, so let's not call up. Calling sideways is also a really bad idea. If you think about when a client calling a client, is that a good idea? What happens when a manager is calling a manager?

Is that manager or the second manager really a manager or just an activity in the other managers? So it's really a bad sign. So calling sideways is a bad idea. I wish we could also ban calling down, in which case you're going to have a very decoupled design, but also a dead system because you can't do anything.

So in the closed architecture, you open a chink in the armor and you're saying, I'm allowing to call exactly one layer down. As a result, you maximize the benefit of the layers, because now layers lay encapsulation. Everybody can call exactly one layer below, no more. The downside of a closed architecture is that you lose flexibility, and sometimes you have some additional indirection that you may not actually want.

But by and large, you should actually opt for a closed architecture. A semi-closed, semi-open architecture says, look, calling up is really bad, calling sideways is really bad, but how about calling more than one layer down? If you're allowed to call more than one layer down, you incur the problem we discussed before, but you get some flexibility. So this is clearly a trade of encapsulation for flexibility.

Not as bad as calling up or sideways, but you do lose some encapsulation, such as clients calling directly the resource access and so on. The two classic cases for a semi-closed, semi-open architecture are, imagine you have a piece of infrastructure that is so critical, you decide to squeeze every ounce of performance out of it and sacrifice some encapsulation. For example, if you look at the TCP stack in Windows, the TCP stack in Windows supposedly implement the OSI seven layer model, all the way from the applications to physical level. On the other hand, if you're going to look inside the code of the TCP stack, you're not going to find seven layers there, because that would just kill performance.

And so, in the case of infrastructure, you may forgive it. The other case where semi-closed, semi-open makes sense is a piece of code that you rarely maintain. If you rarely maintain it, then why do you care if it's coupled? You'll get away with it.

And indeed, something like the TCP stack is a good idea. Over the last decade, how many times it changed? Not that many. So yes, I can make a case for a semi-closed, semi-open, but you should always strive for a closed architecture.

I explain an open architecture just so you can see what not to do. Now, there are some things you can actually allow that will let you have your cake and eat it too. Meaning you could reduce the complexity and the overhead of a closed system, while not compromising on the decoupling and gain some flexibility. The first escape hatch is utilities.

If you look at the structure presented to you before, utilities present a problem. There's no good place for them. If you put them, say, at the resource access layer, then sure, the engine, maybe the manager can do logging, but then not the client. And the client couldn't use security.

If you put it at the level of the manager, then the managers can't use it, but the clients use it. And so there's no good place for utilities. So what you could do is you can say utilities are in a vertical bar to the side, where it cuts across all the layers, and everybody can use it. Now, the downside of doing that, the moment you allow this, people may try and abuse it.

I've seen cases where developers took a component that they wanted to short-circuit everywhere, they call it utility, put it in utility bar, and then they said everybody can use it. Well, while I'm sure you can actually do it, this is not a good idea. To pass as a utility, there's a simple litmus test the utility must pass, which is explain to me how you're going to use it in a cappuccino machine. Yes, a cappuccino machine.

For example, security. I can make up a story why you need to use security in a cappuccino machine. Are you allowed to drink coffee? Logging, how much coffee is the office workers drinking?

Diagnostic, what is clogged in it? Pub sub, I'm running low on coffee, replenish me, and so on. So I can make up a story, a plausible story why you want to use a utility in a cappuccino machine. I cannot make up a story why you want to calculate interest on a mortgage in a cappuccino machine.

And so whenever you catch something in utility bar that shouldn't be there, you ask, can you please explain how you would use it in a cappuccino machine? The other escape hatch is managers can queue up a call to other managers. And that looks like a violation of the close principle. If you look at the diagram, calling sideways, obviously a violation of the close principle.

Well, it's actually allowed as long as you do it in a queued way. And there's two reasons why, one technical, one semantical. Let's actually start with the technical reason. When you're actually calling on a queued call, like manager A calling a queued call to manager B, or not actually calling manager B.

In this kind of an architecture, the queue acts as a resource. And there's a kind of a proxy to the manager B, which acts as a resource access. So manager A actually calls down to the resource access and then deposit a message in the queue. With any queued system, you have a queued listener or monitor, and that's actually a client in your system.

It picks up the message and give it to manager B. So you actually didn't call sideways. Now you can logically represent it as a sideways call, queued one, but you actually called down, that's a technical reason. There's also semantical explanation.

And that is, the reason we really don't like calling synchronous manager to manager is because at that point, the called manager become just an activity in the calling manager use case. And which voice, is it really a manager or is it really an engine? And you find yourself needing to do it, when you have function decomposition in disguise. Meaning you still have functional managers, but you call it managers and engine and so on, just to pretend that you're actually doing a good job.

And then you need managers of managers that actually stitch and sequence those functional managers. That's really not a good idea. On the other hand, it's quite common in a business scenario, where you have one use case triggering the latent, much deferred execution of another use case. So suppose manager is doing some kind of a use case over here.

And then based on what's going on, there's another business rule that says, you need to remember at the end of the month, when you reconcile the batch, to remember to do something. So what you could do is queue up a call to the batch manager to do something a month from now. So it's all part of your use case, it's kind of like FYI, and that's it. And so managers can queue up call to other managers.

Now, time and time during design review or code review, you will find developers trying to open up your system. Don't brush it aside, don't say no, it's not okay, you shouldn't do it. Always go for the underlying need, try and understand what makes them want to violate your architecture guideline. Why do they try and open up the system and then resolve it correctly?

For example, suppose you see manager A calling client A, which is a gross violation of the clause principle you're calling up. And you're saying, why are you doing that? And the developer may say, look, in the requirements, it clearly states that we need to notify the client about this. And you say, okay, but tell me something, if we have another client, should we notify that client too?

And the answer is yes, but we don't have that as a client. I know, but suppose we would. Okay, so apparently there's volatility in who needs to be notified. What do we do with things which are volatile?

We encapsulate them. How about you use a PubSub? How about you have manager A call the PubSub, which is utility, and the PubSub will call client A? Now, I know it looks kind of weird to do it this way, but now what does it take to add another client to the system?

Manager A is completely unaffected by it. What does it take to add another manager that needs to notify client A and B? Nothing, it also goes to the PubSub. So you resolve it by actually publishing an event that's kind of calling up.

Maybe we'll see a developer calling directly another manager, and he will say, why are you doing this? And they will point, look, requirement 4.5.6, we need to do it. And you will say, okay, we need to do it, but what does it say we need to do it now? Does it make sense to maybe defer it on a timeline?

Maybe you should use queued calls here. So don't just cancel the need to open up. The need to open up indicates something is going on, you have to address it correctly according to the allowed behaviors. The other escape hatch here is that both managers and engines can call resource access.

And what does it mean? We have no problem with engine calling resource access, it's one layer below, but what about managers? It looks like you're calling more than one layer down. But first of all, the real layer boundary is the dotted line between the engine and the resource access.

Managers and engines are actually in the same layer. The engines are really just a strategy pattern with respect to the manager, and so it's actually okay. But another explanation is that the engines are in another plane orthogonal to the regular architecture, and they call one layer down and the managers call one layer down, which says the architecture is two dimensional. And so managers and engine can call resource access.

Another design attribute is that sharing engine resource access across managers is not just permitted, it's actually encouraged. You must design the engine and the resource access for use.
