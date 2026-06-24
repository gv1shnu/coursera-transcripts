# Call Chain Diagrams

- **Course:** Pearson System Design Fundamentals Livelesson Video Training
- **Module 1:** System Design Fundamentals
- **Lecture #:** 17
- **URL:** https://www.coursera.org/learn/pearson-system-design-fundamentals-livelesson-video-training-n1kdi/lecture/0Rz0l/call-chain-diagrams
- **Extracted:** 2026-06-20 11:03:31

---

One way of validating your design is using call chain diagrams. Call chain diagrams are a simple graphic representation of interaction between your components. And it may look something like this. You can use straight and black arrows for synchronous connected calls, and dashed and gray for queued calls.

And you basically now show, just by using the components of your architecture, how some interaction between the client, the manager, the engine, and so on satisfies a particular use case. Arguably, if you can generate such a call chain diagram for every use case in your system, you have a valid design. It doesn't mean it's a great design. It just means it's a valid design.

It supports the required behavior. Now, the need to validate architecture this way is not new. And in fact, for many years, we've had other sequence diagrams that actually enable you to capture the same idea, the interaction, but in the form of a sequence. And you can do something that looks like this.

This is a sequence diagram. Now, the advantage of a sequence diagram is that it captures time and order. You can see here the order of the call, because time flows from the top to the bottom. And the length of the bars represent the lifetime of the individual components.

You can capture here duration and order. The problem with sequence diagrams like this, it's very time-consuming to actually produce them. And it may subvert your need to produce the architecture very quickly. And so in most cases, this kind of call chain diagram is good enough for the validation of the design.

However, if you suspect that you're going to need to talk about order and such, then sequence diagrams are actually better. So this is a very simple way to, a priori, before anybody wrote the first line of code, to validate your design, to know that this design is going to hold water. So it's incredibly valuable. However, this is not good enough.
