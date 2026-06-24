# Decompose Based on Volatility

- **Course:** Pearson System Design Fundamentals Livelesson Video Training
- **Module 1:** System Design Fundamentals
- **Lecture #:** 8
- **URL:** https://www.coursera.org/learn/pearson-system-design-fundamentals-livelesson-video-training-n1kdi/lecture/Q6ZIp/decompose-based-on-volatility
- **Extracted:** 2026-06-20 11:02:27

---

Now that we have discussed the what not to do, let's transition into discussing the what to do. The only way to do software architecture is to decompose based on volatility. Decomposition based on volatility simply means that as an architect, what you need to do is to identify areas of change, areas of volatility. Those encapsulate in services or modules or building blocks of your architecture.

And then you implement the required behavior as interactions between these building blocks. These four simple words, decompose based on volatility, is everything you actually need to know about software design. The idea behind volatility based decomposition is that the building blocks of your architecture each encapsulate an area of change, an area of volatility. As such, you start thinking about your architecture as a series of vaults.

Each vault encapsulates some area of potential change. Now when a change happens, the change is always very dangerous. It's like a hand grenade. Well, you open up the door of the appropriate vault, toss the hand grenade inside, and close the door of the vault.

And the vault may go, boof. Now whatever was inside the vault may be completely destroyed. However, there's no shrapnel flying all over the place, destroying everything else in the system. And now you've contained the change, and you didn't maximize its effort.

Now, it turns out that this idea is how all good systems are actually designed. This is a universal principle of a good design. For example, let's look at power in your house. Power in the house is very volatile.

You can have AC or DC, 110, 220 volts. You can have different 50 hertz, 60 hertz. You can have different gauges of wires in the walls. The power could come from the power grid, solar panels on the roof, generators, batteries.

And yet, you don't care. Why? Because all of that volatility is encapsulated behind the receptacle. And you just plug in.

You say, give me power. Crazy volatility on the other side of the receptacle, but you don't actually care. Imagine what it would be like to live in a house where the power of volatility was not encapsulated. We have to worry about, before you plug any appliance to any receptacle, if it can actually work, and if so, under which conditions and such.

It's true also with biological systems. For example, your body has a collection of volatility-based decomposition components. There's enormous volatility in pumping blood. You can have high blood pressure, low blood pressure, high pulse, low pulse, running or sleeping with adrenaline, without adrenaline.

And yet, all of that volatility is encapsulated inside your heart. You could not run your day-to-day activities if you had to also worry about the volatility of pumping blood. Your liver encapsulates the volatility of metabolism. The breakfast I had this morning is unlike any breakfast I've ever had before, nor will I ever have that breakfast again.

This exact combination of amino acids and proteins and carbohydrate ingested in that particular time, over that particular period of time, with respect to all the other things going in my body, is completely and utterly unique. And yet, I don't care because that volatility is encapsulated in my liver. I could not conduct this session if I had to worry about metabolism. I can drive my car, but you can actually go into my car and drive it as well.

And yet, my car is completely different from your car. Well, the reason it works is because all the differences between our cars is encapsulated behind the steering wheel and the gas pedal and the brake. As long as you encapsulate the volatility, you can start interchange and reuse things. So this is a universal principle of a good design.

And what actually happens is change will always happen. But if you have volatility-based decomposition, you encapsulate it, and you don't resonate with the change. Whatever happened inside the component could be completely destroyed. But beyond that, there won't be any other differences.

Look at this laptop I'm doing this presentation on. I have a cup of tea over here. I like tea. Now, if I were to spill tea on the laptop, that would be unfortunate.

And I would have to plug in a different laptop. But the only difference between that laptop and the other, there's tons of differences between the two laptops, except it's encapsulated behind the HDMI plug. Enormous volatility on this side of the HDMI plug, but I don't actually care. Put differently, you don't resonate with the change.

Now, let's examine functional decomposition. With functional decomposition, you did the decomposition, the breaking down into components based on functionality. As a result, any change is, by definition, not in any one place. And Murphy says the change is going to be in all places.

So now when a change happens, you have maximized the impact of the change. It is like throwing a hand grenade into your system. And that is the ultimate nail in the coffin of functional decomposition. All the other reasons I said not to use functional decomposition was just to weight your appetite.

The real killer here is the inability to handle change. The fact that functional decomposition maximizes the impact of the change is the kiss of death in all systems. Now, this is actually very good news. Think about it.

I gave you here four words. That's it. Decomposed based on volatility is all you ever need to know about software architecture. There's no need to read books.

There's no need to listen to webcasts or blogs or anything. Truth often comes in such a very distilled form. For example, there's lots of books and articles and webcasts on architecture. But fundamentally, you don't need more than those four words.

So that's actually very good news. Again, truth often comes in such a very distilled form. Think about, say, the laws of Newton versus the complexity of the laws of Aristotle and the spheres within spheres and so on. Truth tends to be simple and easy to grasp.

And this is very good news. The problem is that volatility is not self-evident. How many of you were in a project where the very first conversation with a customer sounded like this? We're going to change this.

We're going to change that. We're not going to change this. We're definitely going to change that. That is not the typical flow of interaction with customers or with managers.

Customers and managers talk about features and functionalities. And as a result, nobody's ever going to give you the areas of volatility on a silver plateau. You have to sweat on it. And that is actually very good news, because now you're given a chance to comply with the first law of thermodynamics, because you have to sweat on it.

Now, it doesn't mean that if you sweat on it, you will add value. The first law of thermodynamics doesn't state that if you sweat on something, you add value. You can absolutely sweat on something and add no value. But if you want to add value, you have to sweat on it.

So volatility-based decomposition at least gives you an option of success. As a result, it takes longer than functional decomposition. That's actually a very good thing, the fact you have to sweat on it. The fact that it takes effort is fantastic, because that means you have a chance.

The challenge in doing it is not in actually doing it. Doing it is liberating. Doing it is creative and it's fun. And I will spend the rest of the day giving you techniques and ideas so you can do it effectively and relatively quickly.

The challenge in volatility-based decomposition is getting management support. Time and time the manager will come to you and say, I don't understand why this is taking so long. Do the A, do the B, do the C. You'll literally be fighting insanity here.

The smartest man that ever lived said that doing things more of the same, but expecting better results, is the essence of insanity. I want to believe your manager wants you to do things better than the last time. Well, given how things ended last time to the point that you have to do a new system, that means things did not work very well. And so obviously the manager would like you to do better than that.

But according to Einstein, doing functional decomposition again, that would be insane. And you need to fight that insanity. The software industry is like an insane asylum where the lunatics have taken over the asylum, and everybody expected to do something which is horrendously detrimental and insane. And they simply do not understand how horrible functional decomposition is.

On the other hand, you shouldn't expect them to understand. And the reason is something called the Dunning-Kruger effect. The Dunning-Kruger effect is a cognitive bias all human beings are afflicted with. And it basically means that whenever somebody encounters something that they know nothing about, they always think it's less complex than what it is, and never think it's more complex than what it is.

And only once you become an expert in something, you see how deep it can go, and you've practiced it, and you know what it takes to master it. When the manager is saying, I don't understand why this is taking so long. Give me the A, give me the B. The manager really doesn't understand.

You're fighting Dunning-Kruger effect here. By the time the manager does understand, the manager is already an expert architect. And that is simply not going to happen. And so you need to actually fight this insanity, and I will give you some techniques of doing it.

Now, you could actually confront the manager on this, but that's typically not a good idea. It's a lot easier to do than it is to argue. You need to get to the point that you can do it so quickly and effectively, nobody's going to argue about doing it, because by the time they finish arguing, you've already done it. That is the ultimate cue.

Now, the fact that this is going to be an uphill struggle, that doing the right thing, which I hope you agree by now, is self-evidently true, the fact that it's going to be hard is actually another piece of good news, because that is the essence of progress. Most people's mental model of progress is wrong. They think that we are here, and then we improve a lot, and everybody's coming along into everlasting prosperity. That has never happened in the history of our species.

Progress is always made in the face of lunatics, in the face of people sticking sticks in your wheels. A classic example is doctors of old. Up until about 130 years ago, every doctor, every physician, was a serial killer. Every physician has murdered thousands of people in his career.

For the simple reason that doctors did not wash their hands or sanitize their tools. They would do things like chopping off a gandering leg, and then while having necrotic flesh on their fingertips, go and touch another patient. If you're going to allow a 19th century doctor to touch you to be the kiss of death from the angel of death, just to tell you how bad it is, or how bad it was, in the early 20th century, women in labor will say to the coach driver, slow down, slow down, not so fast, because they prefer giving birth in the coach than giving birth in the hospital. Because if you allow a doctor to touch you, that will be the end of it.

Hospitals were places people went to die at. Now all that almost changed in the early 19th century in Vienna, when young doctor Ignace Semmelweis discovered that washing hands is a good idea. Now I couldn't explain why. This was before the discovery of germ theory by Louis Pasteur with a microscope, and microbes, and viruses, and bacterias.

Semmelweis simply knew that it worked, and he started pleading with all his colleagues to wash hands. Now how do you think his colleagues responded to that message? Did they say, thank you, Dr. Semmelweis, for telling me that I've been killing every patient attached since the day I graduated from medical school, from now on I'm going to start washing hands and behave properly?

Or did they ridicule him, and then they shunned him, and then they fired him, and then they banned him from practicing medicine, and then they involuntarily committed him to mental distitution, and then they forced him to commit suicide? Which one of these things actually happened? The reality is that hardly ever people actually want to hear the truth. They don't want to hear that they've been destroying every system they touched since the days they graduated because they did function on the composition.

Nobody wants to hear the truth. It's a lot healthier, it's a lot more constructive to just do it right, not to ask permission for doing the right thing, just do it right, than it is to try and educate the world. Fix yourself, fix your system, the rest of the world may or may not follow, but then it's not really a problem anymore.
