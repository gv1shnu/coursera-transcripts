# Design Don'ts

- **Course:** Pearson System Design Fundamentals Livelesson Video Training
- **Module 1:** System Design Fundamentals
- **Lecture #:** 25
- **URL:** https://www.coursera.org/learn/pearson-system-design-fundamentals-livelesson-video-training-n1kdi/lecture/lfYDX/design-don-ts
- **Extracted:** 2026-06-20 11:04:28

---

Now, like I told you, I've taught these ideas to thousands of people all over the world and when I later on would see what they've done, they've done things that were completely obvious to me should not be done. And as a result, I had to conclude it wasn't obvious after all. So I've compiled a list of design don't. These are things that if you do, you simply would leave to regret.

Now, the problem is, people are very good at explaining and making excuses why it's a good idea to do something which is actually bad. And the number one reason why you have to make those excuses is because you still have some flavor of functional decomposition where you've convinced yourself that it's actually volatility-based decomposition. And so, you have to convince yourself that it's actually volatility-based decomposition. And so, this list is incredibly useful because if you find yourself deviating from what this list is saying, it simply means you have some functional decomposition, go and investigate what did you get wrong.

So in no particular order, here's the list. Clients should not call multiple managers in a single use case. Now note, I didn't say clients should not call multiple managers. You can absolutely call that manager for this use case.

Turn around, call that manager for that use case. That's just fine. The problem is calling two managers in the same use case, in which case the client is the one stitching the managers. The number one reason you find yourself needing to do it is if you have functional managers, in which case somebody has to orchestrate them and that somebody is the client.

A moment ago, I told you that managers can queue up calls to other managers. I'm now about to almost take it away. Managers should not queue up calls to more than one manager. And the reason is, it's something I call, it's called the law of zero-one-infinite.

In software engineering, the law of zero-one-infinite states that either something is impossible, meaning there's no ways of doing it, zero, or there's exactly one way of doing it, or there's infinite ways of doing it, meaning there's no seven in software engineering. There's no seven way of doing something, it's an infinite way of doing something. So it's zero-one-infinite. Now, if you don't call any other manager, that's zero, that's fine.

If you call a manager queued, it should be one, meaning not just one, but even the same one and always, meaning everybody always calls the same manager. And the reason is, most people, when they call up a manager, you're calling the other manager or you're calling all other remaining managers. What does it mean? Suppose we have only one manager, then obviously you don't need to call anybody else because it's just one.

But suppose we have two managers. Well, one can call another, but typically A is calling B, but you're never going to have B as calling A. So that's actually okay. But what if you have three managers, A, B, C, and manager A is calling B, but not C?

Immediately it's a red flag. Why is C different? Why C doesn't need to know about this? Immediately you have to go and investigate.

And so, almost always, you will find that the initial queued call was because there was just one other manager, and then when you added the other manager, nobody bothered to actually go and add the queued call. Almost always what you will find is that when you call a queued call from one manager to another, you're not calling that manager, you're basically calling all other managers. In this case, it was just one. In which case, you should use a PubSub service, and the manager's queuing up a call to the PubSub service, and the PubSub service is queuing up the call to all remaining managers.

As a result, adding all of a sudden another manager to the system is trivial because you just added a subscriber to the PubSub, and the notifying managers are completely unaffected. Other points. Never queue up a call to an engine. A queued call, by definition, exists in isolation.

It's outside the timeline. Sometimes later, maybe much later, the queued call is going to take place. On the other hand, engines exist to service managers. They are utilitarian.

They have no existence on their own. A queued call happened in isolation. So, why would you want to do the activity of the engine in isolation from anything else in the system? It doesn't make any sense.

Don't queue up a call to resource access. Resource access is also utilitarian. It exists to service engines and managers. A queued call exists in isolation.

Why would you want to go and access the database? What are you going to do with the data? Nobody. Just go.

Accessing for accessing's sake doesn't make any sense. Engines don't publish events. Publishing event is a highly managerial decision. Something has changed in the state of the system.

Some required behavior requires you to publish that event. Well, that's what managers do. The engines have no way of knowing what the activities they do actually imply, what are the allowed values and so on. They're just utilitarian.

So, they don't. Clients don't publish events. Publishing an event requires intimate knowledge about the making of the system. Clients should never have that knowledge.

When a client publishes the event, the client knows about what's going on in the back end, almost always because the client is the one stitching all the functional services that you have. Resource access and publish events, the same thing. The resource access has no way of knowing what does the value actually mean and what are the, it just goes and does the access. Nobody should change the underlying resources without the resource access doing it.

Same goes with resource itself. Resources do not publish events. Now, you will find the need for a resource-defined event when you have a calcified system that is basically dead on top of the resource and you still need to accommodate changes. So, what developers are forced to do now, they go and they put a trigger or write some SQL CLR that actually goes and basically start putting business logic inside the resource.

Oh, my God. I have a simple observation here. Who changed the resource? Who touched it?

The system? The system should publish the event, not the resource, unless you believe in gremlins. If gremlins can come at night and change the resource, then you need to publish an event. But short of that, don't do it.

Engines don't subscribe to events. The act of subscribing to an event is almost always the trigger for processing some kind of a use case. So, definitely managers can subscribe to events and absolutely clients can subscribe because part of the use case can be done by the user or another system, but not engines. Engines never call each other.

First of all, it's a violation of the closed principle because it shouldn't go sideways. But this engine is already doing everything there was to do with that activity. All of a sudden, if you need to call another engine, then kind of like your volatility is leaking to the other engine. It's a really bad smell.

Resource access never call each other. First of all, it's a violation of the closed principle. Second, if a resource access is an atomic business verb, how can you actually need another atomic business verb from another resource? That doesn't make any sense.

So, your resource access is not atomic at all. Now, the need you will find for that is when people need to join information across multiple resources and they made a mistake of thinking that resource access are mapped one-to-one to resources, in which case they have to do it. But you can absolutely interact with multiple resources inside the same resource access. Remember, you expose a business verb.

You don't expose the crowds. The mapping to the crowds is completely independent from the atomic business verbs. So, again, perform the architecture and then scrub this list, make sure you're not violating these design don'ts. If you violate a design don't, you will live to regret it.
