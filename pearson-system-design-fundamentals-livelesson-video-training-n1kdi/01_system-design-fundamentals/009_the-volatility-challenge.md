# The Volatility Challenge

- **Course:** Pearson System Design Fundamentals Livelesson Video Training
- **Module 1:** System Design Fundamentals
- **Lecture #:** 9
- **URL:** https://www.coursera.org/learn/pearson-system-design-fundamentals-livelesson-video-training-n1kdi/lecture/thnjl/the-volatility-challenge
- **Extracted:** 2026-06-20 11:02:34

---

So now, I'm going to start giving you a series of techniques and ideas of how to go about identifying those areas of volatility. Now the fact that you have to sweat on it doesn't mean that you don't want to minimize the sweat. The first law of thermodynamics doesn't state you have to sweat a lot on it, you just have to sweat. So you need to come into this battle armed with techniques and ideas that will make it quick and efficient, and of course effective.

And I will start giving you techniques. The first technique, I call it the axis of volatility. There's only two ways anything could possibly change in your system. The first way is at the same customer all the time.

Suppose you were to give this piece of code to a customer, are they going to be happy with it for now to the end of time? Perhaps today, but in the future, they're going to want to do that thing this way. Perhaps that thing that will change at the customer all the time is volatile. But the other way something could change is, suppose you're freezing time and you're looking at all your customers, are all your customers using the system exactly the same way right now?

Well, no, because these guys are doing it like this, and those guys are doing that like that, and perhaps this is volatile. You can always, always ask these two questions in any project. So you never actually ask about the requirement, you ask about what could change. And this is an iterative process.

Your first iteration can be just one big thing. Look at this big blob, there's no if, there's no else, there's no decomposition, one giant tissue of code. Suppose I give this to a customer, are they going to be happy with it forever? And you say, no, no, no, because today they're going to do it like this, but we know in the future they're going to, aha, that perhaps this is actually volatile.

Okay, now give this to all your customers right now, are they going to be happy? No, no, no, because those guys are doing that like this, and those are going to, aha, that perhaps this is volatile. And you keep going like this. I also note that the axes tend to be independent.

Something that changes at one axis is hardly ever the same thing that changes at the other axis. When something hits both axes at the same time, it's probably an indication that that something is actually functional decomposition. Let's look at the example of using these axes on a house. Let's use volatility-based decomposition on a house.

So I will ask the first question, a house changes over time. All I have to do is look at my house and ask, how does my house change over time? And for example, furniture. The furniture in my house is not constant.

As time goes by, the furniture's come and go. So you know what? Furniture is volatile. How about appliances?

Fifteen years ago, we didn't have a flat screen TV. Today, I don't think you can actually buy an old tube. Our kids are not going to know why YouTube is called YouTube. Now 15 years from now, do you think televisions are going to be a flat thing on the wall?

Now I don't know what television is going to look like 15 years from now, but I'm willing to bet the one thing it's not going to be is a flat thing on the wall. Maybe it's going to be some three-dimensional holograms beamed directly into a visual cortex. I don't know. What about other appliances?

Is the price of power the way it is? You're going to replace the appliances with more power-efficient appliances. The occupancy is volatile. I'm not in my house right now, and what if the kids have a sleepover?

And what if you have a baby? That's a big change. The appearance is volatile. You can change the landscape, the drapery.

You can paint. The utility is volatile. I already mentioned the power volatility, that there's enormous volatility in power in the house. But how about other things?

How about internet? Today, I'm getting the internet to my house on the cable system. Before that, we had DSL. Before that, we had dial-up.

But I could also use a satellite connection or my cell phone. These are completely different systems. If I'm using a satellite, the email leaves my laptop, goes 20,000 miles up, and comes back. If I'm using the cable, then it goes under the floorboards and disappears somewhere.

Now, while it's very, very different ways of connecting to the internet, all of that volatility is encapsulated behind the network jack. I have a mailbox, and I can get delivery from the USPS, from Federal Express, from UPS, from DHL, from custom carriers. I don't care. It's encapsulated behind the mailbox, and so on.

So utilities in my house are actually volatile. Over time, I could have different utilities. Now, that is one axis of volatility. Let's look at the other axis, which is, at the same time, across customers.

Suppose I take my house from the Bay Area in California and cut and paste it into Los Angeles, five hours to the south. And my question to you, would it be the same house? So imagine I did a perfect cut and paste. Every atom of the house is pasted in Los Angeles.

Would it be the same house? And the answer, it won't be. And the reason it won't be is because in a different city, I will have different regulation, different building code, different taxation. Since I didn't copy and paste the neighbors, I'm also going to have different neighbors and different interaction, making it a completely different house.

And besides, at this moment in time, my house doesn't have the same structure as any other house in the world. It has a different structure. So at the same customer over time, we see different volatilities. We see structure, neighbor, city.

Now, note the independence of the axis. Let's talk about neighbor's volatility. If I compare my house to another house, I instantly see the volatility in the neighbors. Now, when I asked you about cutting and pasting my house in Los Angeles, is it actually guaranteed that I will have different neighbors?

And the answer is no, because there's non-zero probability that all my neighbors are going to relocate with me and occupy all the houses next to me, so I will actually have the same neighbors in Los Angeles. It's highly unprobable, but it could happen. In addition, even at my house over time, I could actually have different neighbors. And so my point is that the neighbor's volatility is much more accentuated on this axis, the same customer over time, than it is at the same customer over time.

I mean, neighbors do change over time, but very, very slowly and very infrequently. And so the actual volatility, it's more like a question of relative probability as opposed to absolute exclusion. Now, by asking about a different axis of volatility, it is a lot easier to discern the network volatility than it is on this axis. On this axis, it's not so obvious that neighbors are also potentially volatile.

On this axis, it's instant. Now, once I have a box in my architecture for neighbor's volatility, it handles equally well at the same customer over time or at the same time across customers. But the important thing is, as an analysis tool, is using these two axes to identify the different boxes. Another observation here is, I want to go back to the question about function decomposition of a house, either this crazy way or the other one.

Let's talk about cooking. Suppose we have a house where the most important requirement is cooking. Now, the house needs to do all the other things, like cleaning and fixing and learning and all those things. But to the customer, the number one requirement is cooking.

Why? Because we have Mr. and Mrs. Jones.

They were avid chefs, but they always lived in tiny rental places. They never liked it. They want to build a dream house all around their dream cooking. As a result, every conversation with the customer is about cooking.

Do you do cooking? And what about cooking? Every conversation is marketing. Every conversation with the manager is about cooking, because that's the most important requirement.

If there is a requirement spec, cooking is in bold with underscore, and it's 1.0.0.0. It's that important requirement. But I have a different question. My question to you is, is cooking actually a requirement?

Now, you could say, what do you mean? You just told us it's the most important requirement. Yes, I know. Suppose it's the only thing the customer talks about, and it's the most important thing in the document.

My question to you is, is cooking really a requirement? Well, suppose you implement cooking this crooked way or this crooked way. And then, a year later, the customer comes to you and says, can we order a pizza? And you say, why didn't you say so a year ago?

And they say, look, a year ago, all we could think about was cooking. But after a year of home cooking, we're dying for some change. We're dying for some fat. Can we order some pizza?

You're looking at the architecture. There's no box for pizza. What do you do? You add another box for pizza.

And six months later, they come, and they say, can we order Chinese? And so you put a box for ordering Chinese. And then how about going out for dinner? You put a box going out for dinner.

What we see here is that every time there was a change in the user domain, there was a reflecting change in the system domain. And that is the hallmark of a bad design. A good design should be resilient to changes in the user domain. The root evil here is that cooking was not a requirement.

I know that's what the customer talked about. I know that's what the requirement spec said. Cooking was not a requirement. Cooking was a solution masquerading as a requirement.

The real requirement here is feeding. Now, feeding has enormous volatility. It's all the way from cooking a home dinner to ordering pizza or going out for dinner. So the fundamental volatility here is actually feeding.

It's not cooking. So you take a marker, and you cross cooking, and you put feeding instead. So now you identify the volatility. Okay, is feeding a requirement?

Well, what if in the interest of diet, everybody in the house should go to bed hungry tonight? Well, if you had a requirement called feeding, it's mutually exclusive with going on a diet. And every day at 6 PM, a big funnel shows up, and you feed them. And now you throw your hand in the air, and you say, we cannot do this new requirement.

It's mutually exclusive with the other requirement you gave us. And so now you claim the customer gave you mutually exclusive requirements. The root evil here is that feeding is still a solution masquerading as a requirement. Now, it's better than just cooking, that's no doubt, but it's still not good.

The fundamental requirement of a house is not cooking or feeding. The fundamental requirement of a house is to take care of the well-being of the occupants. Now, well-being has enormous volatility. It's all the way from eating a pizza to going on a diet.

But well-being also has temperature. The house can't be too cold, or too warm, or too humid, or too dry. And now we're done with the games. The real requirement here is well-being.

And so only by identifying these things and trying to understand what is the true underlying volatility will you actually get the real requirements. Unfortunately, almost every requirement spec or board with sticky notes you will ever see has almost nothing but solution masquerading as requirements. If you do function decomposition, you will never, ever, ever be done. There will be a never-ending parade of these tiny things masquerading as requirements, different variation of things.

You will never, ever be done. But if you're doing volatility-based decomposition, that is absolutely the correct way of handling solutions masquerading as requirements.
