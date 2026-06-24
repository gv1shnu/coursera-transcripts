# The Design Mission

- **Course:** Pearson System Design Fundamentals Livelesson Video Training
- **Module 1:** System Design Fundamentals
- **Lecture #:** 18
- **URL:** https://www.coursera.org/learn/pearson-system-design-fundamentals-livelesson-video-training-n1kdi/lecture/h6aIg/the-design-mission
- **Extracted:** 2026-06-20 11:03:39

---

Let's define the real task. Your architecture must satisfy all use cases. All here means present and future, known and unknown. That is where the bar is set.

Nothing less will do. If in the future there could be use case your system cannot support, you have failed as an architect. The use case has now invalidated your architecture. And so that's where the bar is set.

You have to support all use cases, present and future, known and unknown. Now, on the face of it, it sounds like mission impossible. How could you possibly know the future? How could you possibly know what you don't know?

So what are you going to do about it? It's impossible. Well, I know it sounds harsh, but that's where the bar is set. And unless we agree this is where the bar is set, we cannot continue.

Nothing less will do. Now, to make it even worse, nobody has ever had the time at the beginning of any project of beautifully specing all the use cases up front. What does it mean? Suppose at the beginning of the project you show up and I give you a book with 300 use cases, all beautifully specced graphically in UML activity diagrams.

Can you actually trust it? And the answer is no. For the simple reason that nobody has ever had the time to beautifully spec 300 diagrams. If I did 300 diagrams, are you going to be surprised to learn that the real number is actually 330?

You missed a few. And if the number is 300, are you going to be really surprised to learn that there's actually only 200 use cases there simply because lots of duplicates. So the marketing guys go and talk to a customer and they describe things and they put them in a document. And then they go and talk to another customer and describe something with their own vernacular.

They put that in a document too. All of a sudden you have duplicates. And you're going to be surprised to learn that those 300 diagrams are full of contradiction. Meaning we have cooking and feeding, but we also have going on a diet.

In the same diagram, well of course because they go and talk to one customer, they describe it in black, and they talk to another customer and describe it in white, and they put both black and white in the document. So if I give you a book with 300 use cases on day one of the project, you should reject it because it's full of holes. It's missing things, it's full of contradiction, and of course there's tons of solution masquerading as requirements. As a result, you cannot trust it.

Now, most people would simply commit the cardinal sin of designing against those requirements. They will do functional decomposition. Now, as we've just discussed, these requirements are full of holes because nobody has ever spec'd the requirements correctly. And now when they design against the requirements, the system implodes.

And they may call it different names. They may call it we have technical debt or whatever. But the net result is they have a broken system, broken promises, broken reputations, shredded reputation, no trust with the stakeholders, with the customers. It's just this spiral of negative consequences of designing against the requirements.

The solution is so simple, it has eluded most people their entire career. The solution is, never design against the requirements. And that's how we actually started this session, I already told you. Do not do functional decomposition.

In other words, stating it is, never design against the requirements. And this simple truth has eluded people their entire career. Don't design against the requirements. Why should you do something that inflicts so much pain on everybody involved?

Inflicts pain on you, on your colleagues, on your future colleagues, on your customers, on your users. Don't do it. Never design against the requirements. And yet, this is exactly what most people do.

And it's absolutely amazing that they inflict this pain. The reason they do it is because when all you have is a hammer, everything looks like a nail. The only technique people know is to design against the requirements. That's the only thing they've been taught.

Everybody's doing it. They take it for granted that's the only way. It is the way of designing software. You know, when all you have is a hammer, everything looks like a nail, even if it's your toes.

They spend their entire career banging on their toes and their colleagues' toes, inflicting pain. Never stop for a second that maybe you shouldn't do it. Maybe it just doesn't work. So what's the solution?

I already told you. Don't do it. A guy goes to the doctor and say, doc, it hurts when I do this. What is the doctor going to say?

Don't do that. This is my solution as well. Do not design against the requirements. If there's nothing you learn from this presentation, it is a simple observation.

It is not okay to inflict pain, not on yourself, not on anybody else. Stop doing something that's bad for you. Do not design against the requirements. And we already discussed the futility of it.

Even if I give you, on day one of the project, a book with 300 use cases, I just gave you a steaming pile of manure. It is impossible to do anything with it. Now, since the dawn of time in software, we've known that if you feed garbage into a system, only garbage comes out. And this is not new to people watching this presentation.

And so what we have here is a cognitive dissonance. On one hand, in one track of your head, you knew about garbage in, garbage out. On the other hand, you absolutely knew that requirements that you were giving in any way, shape, or form is pure garbage. And yet, you treat it as gospel.

You transcribed it, and you tried to maximize adherence to it. And then you're surprised you get garbage out, while at the same time, you knew about garbage in and garbage out. This is purely a cognitive dissonance. It is a sign of insanity.

So what's the solution? I already told you, don't do it. So you say, okay, but what should I do? Well, there is a silver lining to this cloud.

If I do give you a book with 300 use cases, it's full of holes, there's duplicates, mutually exclusive, and of course, you're missing. And by the way, even if I gave you a book with 300 use cases, and they're all perfect, meaning there are no duplicates, there are no mutually exclusive, and everything is there, truly everything is there, it will be no good. Because what you have now will actually change. Over time, you're going to get new use cases.

Use cases you have are going to be illegal, and by regulation, you're going to have to remove it. It will change, and that is actually a wonderful thing. Change is what keeps all of us employed. You, me, we are all in business because requirement change.

And here's why. If requirements would not change, then somebody somehow, somewhere would write the code once, and it would be good. They wouldn't need us. We are here precisely because requirement change.

And arguably, the more requirement would change, the better off all of us are going to be. Why? Because there's so few of us and so many of everybody else. And as a result, the demand for our services would increase, and with it, the compensation and the benefits.

And that's, in my mind, a good thing. So requirement change is actually a wonderful thing. And yet, developers and architects spend their career resenting change because it is so painful. And that's also human nature.

Human beings always resent the hand that feeds them. The hand that feeds you is called change, and what do you do? You resent it. I've seen people even explain to customers why change that the customer want is not a good idea.

Why? Because the pain developers would have to actually suffer is unsufferable. So they don't want to do it. Don't fight the change.

Change is good. Change is excellent. Change is fantastic. So even if I were to give you a book with 300 use cases, it would be no good.

Why? Because it will change. And that would actually be a very good thing. So that's already sound like something which is very bad.

Because on one hand, the change in requirement is good. On the other hand, it's so painful. And this is also a form of a cognitive dissonance. You all know that change is good.

On the other hand, you have learned to resent it.
