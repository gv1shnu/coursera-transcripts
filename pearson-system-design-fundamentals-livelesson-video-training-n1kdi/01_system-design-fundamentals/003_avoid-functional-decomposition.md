# Avoid Functional Decomposition

- **Course:** Pearson System Design Fundamentals Livelesson Video Training
- **Module 1:** System Design Fundamentals
- **Lecture #:** 3
- **URL:** https://www.coursera.org/learn/pearson-system-design-fundamentals-livelesson-video-training-n1kdi/lecture/nO96P/avoid-functional-decomposition
- **Extracted:** 2026-06-20 11:01:49

---

You must avoid functional decomposition. Functional decomposition simply means that you do the decomposition of the system based on the functionality. So let's pass that sentence. Architecture is always an act of decomposition.

You take a big nebulous idea and you break it down into small building blocks, components, modules, services, even classes, whatever the unit of modularity is. So architecture is always an act of decomposition. Functional decomposition is doing the decomposition based on the required functionality, meaning if I give you a requirement spec and you need to do A, you need to do B, you need to do C, you will have an A block, a B block, a C block, such as billing, shipping, invoicing. If that is your architecture, the project has already failed in past tense.

The project is already dead. And it's already dead before anybody wrote the first line of code. Now, I know it sounds funny when I'm saying that because functional decomposition is so simple, it's so easy, and everybody's doing it. Yes, I know everybody's doing it.

It doesn't make it right. I'm going to start driving nails in the coffin of functional decomposition. Every one of these nails is going to be enough to kill it. I'm going to save the best nail for last.

The reason why this is so detrimental to success would only become clear once we actually discuss the right way of doing something. Then, functional decomposition will become clear in its full horror. So let's start. Functional decomposition is always time decomposition as well.

You don't just do A and B and C. You do A, and then you do a B, and then you do a C. So built into the very fabric of B is a notion it's called after an A and before a C. Now suppose I have another system that needs to do B as well, shipping and billing and invoicing.

Suppose I need to do B in another system. So I'd like to pick up the B from one system and drop it to another system. Well, you can't actually do it because the moment you lift up the B, the A is hanging off it and the C is hanging after it because in the other system, nobody is doing the A before it or the C after it. Put differently, you cannot reuse components.

Now you understand why likely none of you have ever seen or have done reuse, meaning you take a component written for one business context in one system, lift it, shift it, and drop it in another system. That never works simply because in the other system, nobody is doing the steps before it and the steps after it. As a result, functional decomposition always leads to enormous duplication of functionality across system and subsystem. Everybody is reinventing the wheel all the time.

In addition, you're not going to have just three things to do. A decent system could have 300 functionalities. So one possible design is a design with 300 building blocks. The problem with a design with 300 building blocks or for that matter even 100 is that while each building block is simple, there is an enormous nonlinear cost to integrating those systems, those components together across the system.

So you'll be solving a far worse problem as far as complexity. Well, the other edge that functional decomposition may lead you to is taking those functionalities and pumping and bloating building blocks. So you're going to get the A and the B and the C and start pumping into a giant monolith of doom, a giant service, a god service. And the problem is that while you have not much to worry about the integration cost, the internal complexity of such services is diabolical.

And again, you'll be facing a nonlinearly worse level of complexity. Now, if the system is to do some functionalities, an A, a B, a C, who is telling the system do the A and the B and the C? Well, that somebody is the client. And so now business logic has to reside in the client, meaning the client has to know that after an A you do a B and if B fails, here's how you undo the A.

And for that customer over there, we're only doing B prime and we skip the D and so on. Now, every developer out there knows do not pollute the client with business logic. Every developer out there is doing it simply because functional decomposition forces the clients to be polluted with business logic. There's no other way of doing it.

You have to do the sequencing of those components inside the clients. As those sequences change over time or across customers, your clients are going to have to change. And this is why every developer out there knows do not pollute the client with business logic. Every developer is simply doing it because functional decomposition forces them to pollute the client with business logic.

Another problem is if you expose these functionalities, the client has to enter the system in multiple places. You enter it for the A, back, for the B, back, for the C, back. And that means there's multiple places to worry about security, scalability, availability, responsiveness, performance. An attribute of a good design is that it minimizes a number of points of entry, ideally even a single point of entry.

But functional decomposition will tend to maximize the points of entry. I mentioned that functional decomposition leads you to either an explosion of services or one or a few bloated services. I often say it side by side. Here's an example.

A big company asked me to go and do due diligence on a small company they wanted to purchase. I cannot get into the details, but the sum of money on the table had eight zeros in it, meaning some leading digits and then eight zeros. So, it wasn't a trivial sum of money. One of the things I'm doing when I'm doing due diligence or design review, I'm doing cyclomatic complexity analysis of the entire code base.

And here's what I saw. I scrubbed all the specifics and I kept three of the labels in the diagram. Now, in this analysis, big and dark is complex. Now, look at the component in the bottom left called main form.

In my mind, a form should be just a simple conduit from the client to the back end, a pretty face, nothing more. But look at this system. Is main form just a pretty face? Is it just a form or is it the system?

If the whole thing is eight zeros, how many zeros are in main form? Would anybody watching this like to be the developer charged with maintaining main form? Of course, the answer is no, and we all know main form is mortally wounded with business logic. It's so inflated.

In fact, all the system migrates into the client at that point. On top of it, we see form setup. Main form is so big and so complex, it can't even set itself. And so, you see this form setup on top.

This is what it takes to even stand up this beast. Over there to the right, we see resources. Resources should be complexity of one, just a long list of strings and images. But think about what it takes to change one string inside main form.

It takes the monstrosity of resources. And then everywhere in between, we see this explosion of building blocks, of tiny little things. So, in this particular system, they got to enjoy the best of both. Few big, horrendously internally complex components and explosion of little things with horrendous integration cost.

And so, I look at the architect in the room and I ask him, I think you have functional decomposition on your hands. Now, he did some reading about me before I showed up. And so, he sighs and he says to me, I don't think so. I know so.
