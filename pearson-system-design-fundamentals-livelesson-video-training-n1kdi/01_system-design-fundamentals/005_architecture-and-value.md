# Architecture and Value

- **Course:** Pearson System Design Fundamentals Livelesson Video Training
- **Module 1:** System Design Fundamentals
- **Lecture #:** 5
- **URL:** https://www.coursera.org/learn/pearson-system-design-fundamentals-livelesson-video-training-n1kdi/lecture/UlbfZ/architecture-and-value
- **Extracted:** 2026-06-20 11:02:05

---

Now, I can prove that functional decomposition is the wrong way of designing software systems without using a single software argument. I'm going to defer to the first law of thermodynamics. The first law of thermodynamics simply states that you cannot add value without sweating. And that's a layman interpretation.

I don't want to get into the calculus behind it. Now, we don't quite know why this is the first law of thermodynamics, but we know that on this side of the Big Bang, that's just the way things are. You cannot add value without sweating. Now, before the Big Bang, we're not quite sure.

But by the way, the only way physicists know to define the moment of creation is when the first law of thermodynamics kicks in. So on this side of the Big Bang, that's the way things are. Now, architecture, by its very nature, is a high added value activity. It's not intense in effort, but it has to be all-encompassing, and it basically dictates what the system is going to look like till the end of time.

And tiny mistakes in architecture has enormous consequences down below, enormous future pain. And so it's very high added value. On the other hand, if I give you a requirement spec, and it reads 1.2.3, system should do A. 4.5.6, system should do B.

You say, no sweat, A block, B block, C block. And that's a problem. You said no sweat. Now you endeavor to cheat the first law of thermodynamics.

Now you endeavor to add value without sweating. And according to the first law of thermodynamics, that is simply not going to happen. So by the very nature of this universe, functional decomposition is precluded from ever working. And yet, this is what everybody's doing.

Examine your past project. Examine your current project. Look at what your colleagues are doing. They're all doing some variation of functional decomposition.

By now I'm convinced this is because of human nature. Human beings are always in perpetual search for the free lunch. Unfortunately, there is no free lunch in the universe. For thousands of years, people tried to do alchemy, turning lead into gold.

The alchemists, for thousands of years, commanded the king's ransom. They were very expensive. They were the smartest people in any kingdom. They've produced zero results, meaning it has never, ever worked.

And yet, for thousands of years, they kept trying. People spent money on it. Why? Human nature.

The allure of the free lunch is irresistible. And you have to understand this has nothing to do with intelligence. The greatest alchemist of all time was Isaac Newton. Isaac Newton spent more time trying to figure out the philosopher's stone than he did trying to write Principia Mathematica and inventing calculus, and the age of reason, and the modern age, basically.

There's nothing in eternal physics that says that functional decomposition cannot work. Now, I can talk about functional decomposition and its futility till I'm blue in the face, and yet people are still going to try and do it. The technique that we've been practicing at iDesign of driving home the message about the futility of functional decomposition is what we call the anti-design effort. Announce to the team that you're doing a design contest for the next generation system.

Split the team in two halves and put them in two separate rooms. Say to the first half, your goal is to come up with the next generation architecture. Say to the second half, your goal is to come up with the worst possible architecture. A designer would maximize our inability to extend it, to maintain it, to use it.

Let them work on it for one afternoon, and then we can bring them together, and you see they did the same. It's not going to be exactly the same because the labels are going to differ, but if you scrub away the labels, it will be exactly the same. Only now you come clean and you say, guys, you weren't really working on the same objective. What does it mean that those that did the worst did the same as those that did the best?

What does it mean? Now you're going to get some embarrassed there. Now the mind could be open for a better way of doing something. The fact you shouldn't do functional decomposition has nothing to do with software.

It's a universal observation about the design of things. For example, let's talk about designing and building a house the same way you build a software system. Now, of course, that would be a functional house, so let's talk about a functional house. Suppose I give you a requirement spec that has all the required functionalities of a house, such as cooking, resting, sleeping.

One possible architecture for a house would be something like this. You reflect the architecture, and the architecture reflects the functionality. Every unit of functionality has a corresponding building block in your system. And so I look at the requirements for the house, and I have a building block for each.

Now this is already an absurd way of building a house, and you could be already smiling at this, but the true insanity only becomes evident when we talk about what does it take to build this house. So let's build the first building block. It's built cooking. Now, you have nothing in the house.

You have dirt under your feet and sky above you. What do you do? Well, maybe you take a microwave out of the box, and what? You hold it in midair.

So you build a little scaffolding to hold the microwave in midair. You connect just the microwave to the power grid. You put a little roof on top to protect it from the elements, and you announce to the customer, sprint 1.0 is done. Cooking is done.

Now, I can only hear you in my mind already laughing. This is so absurd. I know. I know it's absurd, but why are you building software systems this way?

And by the way, is cooking actually done? Cooking is not going to be done this way, not just because of cooking on the stove or cooking on the microwave. Think about all the sub-scenarios of cooking. Think about all the combination.

Done this way, is cooking ever going to be done? Why are you lying to the customer when you are saying the feature is done? Now, you could be saying, hold on a second. The architecture you just showed us is a contrived example.

In my house, I do cooking in the kitchen. Very well. Let's examine this house. This is what literature calls domain decomposition.

This is also death. Domain decomposition is still a failure, and the reason is it is still functional decomposition except it's in disguise. Now, it's not straightforward, but look at it. Kitchen is where you do cooking.

Bedroom is where you do sleeping. Garage is where you do parking. So it is still functional decomposition in disguise. Since a rose by any other name is still a rose, this is still functional decomposition, and by the nature of the universe, we know that this design is precluded from ever working, from ever adding value.

The true insanity of this house only becomes evident when we talk about what does it take to build this house. Let us build this house the same way most people would build a sofa system. Let's build a kitchen. So we're standing on dirt.

We've got nothing. So we dig a trench to have the foundation for the kitchen. We pour cement into that trench. We put some bolts in it.

We allow it to cure. We erect the walls on top of the foundation. We tighten the bolts connecting the walls to the foundation. We connect the kitchen to the power supply, the water supply, the gas supply, the sewer discharge.

We put all the wires in the walls and the heating and cooling ducts. We put stucco on the outside. We put drywall on the inside. We hang cabinets.

We put the roof on top. We paint the whole thing, and we announce to the customer milestone 1.0 is done. Kitchen is done. Now, we need to add bedroom one for the house.

The first thing we do, we take a hammer, and we bust the stucco around the perimeter of the house, exposing the bolts connecting the kitchen to the foundation. We unbolt the kitchen from the foundation. We take very expensive hydraulic jacks, and we lift the kitchen off the foundation. We disconnect the kitchen from the sewer discharge, from the gas, from the water, from the power, and we shift it to the side.

We take jack hammers, and we bust the foundation. We dig it all out, and we dispose of it in a dump, which is very expensive. Now we dig a new trench, which contains continuous foundation for the kitchen and the bedroom. We put the bolts inside that new foundation.

We pour cement inside that. We allow it to cure. We move the kitchen on top of the new old foundation. We very carefully lower it on top of the foundation, and make sure all the holes, of course, align, meaning the holes in the kitchen align with the new bolts in the foundation, which is very tricky, but suppose we can do it.

We bolt the whole thing. We erect walls for the bedroom. We tear the cabinets of the kitchen. We tear the drywall of the kitchen so we can expose the wires and the ducts in the walls.

We connect the wires in the kitchen and the bedroom. We put, again, drywall in the kitchen and the bedroom. We hang the cabinets in the kitchen, the closets in the bedroom. We take a hammer, and we bust now all the stucco that coated the kitchen so we can have a new uniform coat of stucco on the kitchen and the bedroom.

Nobody wants to see a big crack in the middle of the stucco. We tear the roof of the kitchen, put continuous roof on the kitchen and the bedroom. We paint the whole thing. Oh, by the way, at least one of the walls that used to be an external wall is now an internal wall, so you have to have a way of fixing it, and there's some issues with security perhaps and safety.

We tidy it all up, and we say to the customer, bedroom one is done. The fact that you had to rebuild the kitchen is not mentioned to the customer. The fact that rebuilding the kitchen a second time around was way more expensive than building it first time around is not disclosed to the customer. What will it take to add another bedroom to this house?

If anybody tries to build your house this way, you're going to fire them on the spot because they're clearly insane. So why is it acceptable to build software system this way? This is just the beginning of your travel of how bad these ideas really are. Any composition, especially the way I just showed you, always leads to duplication of functionality across different areas.

For example, in my house, at the end of every party, all the guests end up in the kitchen. So apparently in my house, I have to duplicate entertaining guests from the living room into the kitchen. Now, what happens if you fall asleep in front of the television in the living room? They duplicate sleeping in the living room and the bedroom.

What if you have to do some cooking in the garage? And so very quickly, every domain ends up duplicating every other domain. In addition, there's a long list of things domain decomposition cannot do. For example, in this architecture, why would you do barbecue?

Can you do barbecue in the kitchen? So now you start proclaiming things which are actually impossible and are mutually exclusive and on and on and on. Now, this is not even how bad it's going to be in real life, simply because we started the scenario by saying you're standing on clean dirt, you've got sky above. Most people have an existing system with existing data and existing logic and existing customers.

Now, the number one motivating factor for doing a new system is because the previous system has reached end of life. Nobody can maintain it anymore. Nobody can extend it. It's too complex.

Human beings cannot make sense of that level of complexity. You throw your hand in the air. You say, we cannot take it anymore. We have to do a new architecture.

We have to do a new system. Now, between you and me, this is a paradox. Why would you let the same people that did not know how to do a good job in the first place do a good job in the second place? To me, it doesn't make any sense.

But suppose that your boss relents and the customer agrees and you're going to do a new system. Well, most people, of course, are going to do it functionally, either this crooked way or this crooked way. Now, suppose you have three things you need to do in your system. You need to do A and B and C.

Well, of course, you're going to do it functionally because that's how everybody's doing it. And so what you're going to try and do is build just the A in the new system. Unfortunately, that is not going to work. And the reason is there's no business value for just deploying the A.

You need to do A and B and C. There's no business value just doing billing. There's no business value of just doing invoicing. You need to do invoicing and billing and shipping.

The whole sequence needs to be there. And yet, you're still going to try and add value early, often, and soon by deploying just the feature. But we've just agreed. On its own, it doesn't make any sense.

If you're just going to deploy the A in the new, it's not going to work because the B and the C are in the old system. And every validation rule in the old system is going to say we cannot just do B and C. Where's the A? The old does not know about the new.

Now, of course, you could do the A in the new and the old. The users are going to revolt. Why should they do double the work and not receive double the value? What is the solution?

How do you solve this? And so the way most people actually solve it is they do try and do the A in the new and the B and C in the old. And the way they're doing it is they're reconciling the A in the new and the B and C in the old. The problem is this reconciliation is a problem of complexity which far exceeds just the challenge of doing an A.

Recall that the motivation for doing a new system was because the old system has reached end of life. You cannot go in there anymore. You cannot maintain it, extend it, reuse it. It's too complex.

So we are talking about a system which is very calcified. You cannot change anything there. And so in such a system, you are going to try and do a significant surgery of extracting the A and putting it in a new system. This problem far exceeds in difficulty, in complexity, in challenge the problem of just doing an A.

And so you'll be solving a far worse problem. And so think about it. The allure of the free lunch of just doing the A ends up paying so much more. It always ends up in tears because the problem we're trying to solve is so horrendously complex.

Another problem with domain decomposition and the previous garden variety functional decomposition has to do with testing. Most developers are infatuated with unit testing. I'm not saying you should do unit testing. However, unit testing is borderline useless.

And I can prove it to you. Examine for example a jumbo jet. A jumbo jet could have several hundreds of internal components such as servos, actuators, gears, turbines, computers, and so on. Now suppose we are building a jumbo jet the following way.

We do unit testing for each component and each component passes unit testing flawlessly and then we assemble the jumbo jet. My question to you is if this is the only kind of testing we do. are you ever going to fly it? And the answer, of course, is no.

No sane person would be willing to set foot in that jumbo jet. And the reason is, we all know that defects are probably going to be in the interaction between the components, not in any one component. So even if the individual components are completely flawless, the whole can be defective. For example, look at the subsystem of fuel in the jumbo jet.

We have a fuel tank. We have a pipe leading to a pump, another pipe leading to the engine, and so on. Now suppose the jumbo jet is flying, and then it's turning, and that applies excess g-force on the fuel in the tank, which creates sub-pressure in the pipe leading to the pump, which creates a tiny cavitation bubble to appear. And that bubble makes its way to the engine, and the injectors misfire.

And the problem is, no amount of unit testing can actually figure out this kind of a defect. The kind of testing you need to do to address this kind of defect is called regression testing, where you need to look at the system as a whole across all its subsystems, and then you need to test individual subsystems, and then individual subsystems in interaction with other subsystems. And then you need to go inside the subsystem and test subcomponents inside the subsystem and interaction there, and eventually you may get to a component. So it's a massive spiral of tests and combination of all the components.

The problem is that in a functionally composed system, the level of internal complexity is so high where everything is connected to everything else, you simply cannot delineate it in a way that will be conducive for regression testing. And as a result, you cannot do regression testing. Now, whenever you cannot do regression testing, that's another way of saying your system is untestable. When you have untestable system, you will always have system rife with defects.

So now I understand why most systems out there are rife with defects. It's unavoidable, you simply cannot test it. And in such an environment, developers, the only kind of testing they can actually do is testing individual units. And so the focus on that test, but it doesn't mean that unit testing is valuable.

It is simply searching under the streetlight. Searching under the streetlight is a cognitive bias that most humans have, which you focus on things you can do, not on the things you should do. And it's called after a joke where somebody's walking down the street, see a friend of his walking on all four on the pavement, saying, what are you doing? He says, well, I'm looking for my car keys.

So the friend says, where did you drop your keys? And the guy says, near my car. But he says, where's your car? It's around the curve.

So what are you doing here? The streetlight is here, I'm searching here. That's basically unit testing.
