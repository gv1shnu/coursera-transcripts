# Taxonomy in Layers

- **Course:** Pearson System Design Fundamentals Livelesson Video Training
- **Module 1:** System Design Fundamentals
- **Lecture #:** 14
- **URL:** https://www.coursera.org/learn/pearson-system-design-fundamentals-livelesson-video-training-n1kdi/lecture/0JYMr/taxonomy-in-layers
- **Extracted:** 2026-06-20 11:03:10

---

My methodology calls for the following four layers. The top layer, I call it the client layer. Now, sometimes people call it the presentation layer. I don't like the word presentation because presentation implies there's a human in the loop, some grids are being filled and buttons are being clicked.

And that could very well be the case. But what if the consumer of your system is another system? Nothing is being presented. It's just another system.

And you actually want to equalize all your clients into this level of abstraction. I don't care if it's a mobile device, or a web page, or a desktop, or another system consuming my system. They're all clients of my system. Now, you can absolutely have a whole enormous volatility in the kind of client technology.

And typically, clients tend to be very volatile as how they evolve. And so the clients encapsulate the volatility of how they present information, how they forward it to their system, and so on. By equalizing all your clients as to just a client, at least there's hope for a single point of entry. So this kind of an approach advocates a single point of entry.

It doesn't guarantee it, but at least there's hope. Underneath that, we have the business layer. The business layer encapsulates the volatility in changes in the required behavior of the system. So there's a lot going on in that sentence.

So let's start parsing it. First, I didn't say requirement. I said required behavior. Most people capture incorrectly the requirement for the system.

Most people capture the requirement in a functional way. And if there is a requirement spec, it reads 1.2.3, system should do A. 4.5.6, system should do B. This is not a good way of capturing requirements.

A good requirement is always behavioral and not functional. You need to capture how the system is required to behave, not the required functionality. For example, if I give you a requirement for the system should open a file, you're saying, well, what's wrong with that? I've seen it a million times before.

Well, here's the same thing from a behavioral perspective. The system should present the user with a standard open file dialog or an application-specific open file dialog. The filter and dialog would be star dot blah. The system is only going to allow the user to navigate to portion of the drive where they have NTFS permission to go to.

The system will maintain a write-exclusive read, non-exclusive lock on the file. If the user has not released the file in three hours, the system would force a release of the file, a log that the file was abandoned by the user, and so on. As developers, which would you rather receive? System should open a file or the full behavior?

Well, obviously, we know that the behavior is actually better. And the reason is the behavior is not open for interpretation, or it's a lot less open for interpretation. You should not leave the required behavior as something the developers should interpret, because Murphy says they're always going to get it wrong. So what I just described, the required behavior, has a technical term.

It's called a use case. Note it's not called a user case. It's called a use case. And the reason is it may not be a user.

In most systems today, what the users see is the tip of the iceberg, and the bulk of the system is below the waterline. Case in point, Google. Is Google just a search box and a button? Probably not.

Most of Google is below the waterline. So you need to capture use cases, which are nothing but a series of required behaviors. Now that I understand that, the job of the business tier is to provide that required behavior. Now, we also know that things are going to change.

And that means the use cases are going to change. Over time, and across customers, of course, the required behavior will change. The key observation is there's only two ways that required behaviors could possibly change. A use case is always some sequencing of activities.

And there's only two ways a use case could change. Either the sequence would change, or the activity would change. For example, let's look at these four sequences. All four sequences perform the same three activities, A, B, C.

But look at the enormous volatility in the sequence. They can be sequential. They can be in parallel. They could be conditional.

They can be staggered. There can be repetitions, and so on. And so there's enormous volatility in the sequence. Since in volatility-based decomposition, we encapsulate something which is volatile, managers are the type of components that encapsulate the volatility in the sequence.

Each manager, in fact, encapsulates a family of logically related use cases. Now, the other type of volatility you could actually have is in the activities themselves, irrespective of the sequence. For example, look at these two sequences. The two sequences are identical, except the activities that perform are not.

So the volatility in the activity is separate volatility in the sequence. Engines encapsulate volatility in activities, in business rules. Managers encapsulate the sequence. Engines encapsulate the activities.

There are two different types of volatilities here. Now, in theory, I could change the sequence without ever changing the activities. At least the managers may use zero or more engines. Engines may be shared between managers.

There's nothing wrong with doing this activity over here in that family of use cases for that manager, and then exactly the same activity for a completely different manager. And in this dot, we have resource access. Resource access encapsulates the volatility of how to access the resources the system actually consumes. The resource itself, by the way, may be part of the system, may be outside the system.

And all of that is encapsulated inside the resource access. Now, the need to encapsulate the resource access is, of course, not new. And many systems have tried to do it. However, a classic mistake is to expose on the resource access, on the interfaces, the contracts, the CRUDs.

So people write resource access that sounds like Insert, Select, Delete. The problem with it is that it betrays the fact that the underlying resource is a database. It is just as bad if you were to call it Open, Close, Read, Write, Seek, which now implies the underlying resource is a file. So now what happens, if that's the kind of contract or interface you expose on the resource access, then as you move from a file, to a cache, to a hash table, to a database, anybody upstairs that used the old interface detonates because you force a massive change on them.

So never expose the actual CRUDs. Good resource access exposes what we call atomic business verbs. What does it mean? If you look at any acquired behavior, it's always a sequence of activities.

Now, those activities can in turn be sequencing of other activities. And you can keep going like this, but at some point you will discover a set of business verbs that are so atomic they cannot be expressed using any other business verbs. For example, if I have a bank, transferring money between two accounts means I'm crediting one account and I'm debiting another account. So transferring is not an atomic business verb.

Banks do it all the time, but it's not atomic. On the other hand, credit and debit an account is an atomic business verb. You cannot express them using any other verb. Now, here's a beautiful thing.

Atomic business verbs pertain to the nature of the business. The nature of the business hardly ever changes. Since the time of the Medici, banks did credit and debit. So for the last 500 years, credit and debit was good enough for capturing banking activities as atomic operations.

What your resource access needs to do is to expose these atomic business verbs. And then internally, they act as a transformation function on the business verb to actually go and access some resources. Now, here's a beautiful thing. Since the atomic business verbs never change, you can completely swap the underlying resource without ever affecting anybody on top of the resource access.

Underneath the resource access, we have the physical resources, databases, queues, other systems. To the side, we have utilities, common infrastructure everybody needs to consume. So the template for a system looks like this. At the top, we have clients.

Underneath that, we have business logic in the form of managers and engines. Underneath that, we have resource access. And underneath that, we have resources. Note that in this particular case, resource C is even outside the system.

To the side, we have utilities, common infrastructure, security, diagnostic, logging, hosting, pub-sub, message bus, instrumentation, and so on, things that every system needs to actually have, infrastructure. So note how, on one hand, generic and abstract this approach is. On the other hand, how it can well describe literally any software system. Any software system will have a need for clients, utilities, managers, engine, resource access, and so on.

It is a wonderful starting point as you start designing your system to ask the question, what are the areas of volatility for the managers, the engines, the utilities, and so on? Now note, we are elegantly here avoiding the question of detailed design. We are purely focusing on the decomposition, on the building blocks of the system. The hallmark of a good architecture is precisely the ability to talk at this level on the system.

For example, a mouse and an elephant have exactly the same architecture. A mouse and a grasshopper do not have the same architecture. Now note that I can actually talk about the common architecture of a mouse and an elephant. Well, of course, these designs are drastically different.
