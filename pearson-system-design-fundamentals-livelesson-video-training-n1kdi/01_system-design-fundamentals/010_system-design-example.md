# System Design Example

- **Course:** Pearson System Design Fundamentals Livelesson Video Training
- **Module 1:** System Design Fundamentals
- **Lecture #:** 10
- **URL:** https://www.coursera.org/learn/pearson-system-design-fundamentals-livelesson-video-training-n1kdi/lecture/8djkz/system-design-example
- **Extracted:** 2026-06-20 11:02:42

---

The first act of wisdom before you jump into architecture, before you start drawing lines, is to simply prepare a list of areas of volatility. This is a normal part of required gathering and analysis. Now note, I never said requirements are something you should completely ignore. Requirements are very important.

I said, don't design against them. Don't do functional decomposition. You need to take the requirements and analyze them to identify the areas of volatility. That is the essence of requirement analysis.

Ask what could change along the axis of volatility. Try to identify solution masquerading as requirements, and so on. So let's go back to the stock trading system and identify the areas of volatility. You had a requirement to enable traders to buy and sell stocks.

Now, do traders buy and sell for their own money, or do they do it for end customers? Well, it could be that they do it for themselves, but by and large, they do it for end customers. Now, it turns out that most people care a lot about their money and their investments. And so those people, the end customers, are going to be bombarding the traders with questions, how much money I have, how much money I have, did it change?

So very quickly, even though you were not given today a requirement for it, you will have requirements to allow end customers to interact with the system. Now, they may not be able to do any kind of trading, but to be able to see how much money they have, of course. They may sit there all day long hitting F5, F5, F5, F5, refreshing the screen, trying to review their portfolio. And so what we have identified here is volatility in who is the user.

Now, volatility in who is the user almost always has other volatilities that it implies. For example, the type of client application. For a casual user that just needs to see the value of their portfolio, a web page is just fine. And indeed, you had a requirement for a web page.

However, if you're going to try and give a web page to a professional trader, they're going to laugh at you. Traders need a rich six monitor desktop application. On one monitor, they have the stock tickers. On the other one, they have Excel.

On the other one, they have the portfolio. On the other one, they have some projection. On the other one, they have news feed and so on. How are you going to do that in a web page?

It's a completely different user experience. And so we've identified volatility in a type of client application, simply because of the different audiences that we have, different types of users. Now, volatility in user implies volatility in how you authenticate and authorize. How many traders are you going to have?

One, ten, a hundred? Several hundreds, probably not a thousand. Now, if you only have several hundred traders, you can absolutely authenticate them using account on your local domain, on your local network. But you could have millions of end customers, and you're not going to give accounts on your domain to people coming from a jungle called the Internet.

So for those, you're going to have different credentials. It could be username and password. It could be biometrics. It could be some kind of a single sign on federated.

You're going to use the Google or Facebook credentials. I don't know how you're going to resolve it, but I do know that how you authenticate is very volatile. Same goes with how you authorize. You need to decide on what is the user allowed to do.

Maybe not all traders can trade all amounts of money on all kinds of stocks. Maybe some can do more than others. And certainly, we've already identified that end customers cannot do trading, but traders can trade. And so how do you authorize?

Do you look at roles on your machines, roles in the domain, roles in the database? Maybe use claim-based security. I don't know how you do it, and nor do we have to actually decide on it. All we have to do is to identify that authorization is volatile.

We had a requirement for the system that after everything we do, we send an email about what we did. And then we said, what if the customer comes to you and says, can you send me a text message? And what if some customer says, look, email is nice, but can you please send me a paper letter? I'll pay for the stamp, but I need a hard copy as well.

Maybe a customer wants a fax. So even though the requirement was for an email, that was, again, a solution masquerading as a requirement. The fundamental requirement here is to notify the customer. Notification has enormous volatility in the transport.

It can be email, paper mail, text messages, carrier pigeons. If you think about it, the transport is volatile, but the payload is not. The message itself doesn't change, but the transport over which you send it is volatile. Now, there's also volatility in who sends a notification.

Literally, any box in the system can send it. It's not just one box. And as you add boxes, perhaps you're going to have more publishers. But the same is true with who receives the information.

A customer can say, can I please get an email, but could you also send an email to my accountant so that at the end of the year I have everything, I don't have to actually send anything? So now we have volatility in who receives it. But there's another volatility here, which is, all of a sudden, we're not doing a unicast, we're doing a broadcast. We're sending the message to multiple recipients.

And you could say, I want the paper letter to me, and I want an email to my accountant, and I also want it to my lawyer, and you maybe also need it to send it to the government. So now we have enormous volatility in who receives the information over which transport, by the way. Now, we don't have to discuss any of these things. All we have to point out is that the transport is volatile, the publishers are volatile, the subscribers are volatile.

You have a requirement to store the data in a database. Okay, but we also know that the bulk of the traffic for the system is going to come from the end customers who are going to sit there doing F5 all day long. And that means that the bulk of the traffic is going to be read-only in nature. If the bulk of the traffic is read-only, perhaps we should use a cache as opposed to a database.

So all of a sudden, the system is using a cache. And we already discussed a whole separate volatility, which is perhaps moving to the cloud. So what we actually recognize here is that the requirement to store it in a database was also a solution masquerading the requirement. The fundamental requirement here is you're required to store the data.

And whether you store it in a cache, in a cloud, in a local database, that's implementation detail. But the fundamental volatility here is the storage. Now, as you keep analyzing the requirements, you have to also look at the persona of the users. And the traders themselves, their persona is a persona of somebody that likes to make a lot of money.

Nobody in finance is there because they hate making money. Now, if the nature of their job is simply picking up the phone or reading emails and entering stock numbers and account numbers, that job is a hair shy from data entry. And data entry is a hair shy for minimum wage. And they're going to try and stay away from such a job as much as possible.

So traders can only make the big bucks when they add value. And they can only add value when they make complicated trades. And these trades are going to hedge the risk. So if you ask them to buy a particular stock, it means it's going to say, well, what if the stock goes down?

Well, what are the terms under which this actually goes down? For example, if you ask them to buy, say, Exxon Mobil, which is an oil company, that sounds like a subtle investment, okay? But what if there's war? If there's war, then oil companies don't do very well because their assets are on fire.

But on that case, defense stocks are going to do very well. So now you start looking at the conditions, and how you hedge, and how you spread the risk. And unfortunately, doing any one of these things is not quick, and it's not fast, and it takes time to do it. Now imagine, all of a sudden, that the trader is working on such a very complex trade.

Unfortunately, it's five minutes to five. And if you don't go home right now, you're going to miss the last train going home. Well, you can either spend the night in the office and finish the trade, or go home and start all over tomorrow. So how about the following interaction?

Mid-trade, you jump out, run to the train station. You have an hour to kill, you take your mobile device, keep working on it. You get home, you have dinner, put the kids to bed. And then 10 PM, you go into the den and VPN to the office and finish the trade.

Show me one trader that would not want to work this way. But now what we've discovered is enormous volatility in the duration of the interaction. Interaction can be short, fill up a form, submit. Or it can last several hours, for that matter, several days.

It can come over multiple devices, and some of them are connected, some of them are disconnected. So there's enormous volatility in the interaction. And if you think about it, the connectivity is its own separate volatility. I could fill up a form, connect, submit, and that's it.

Or I could issue a bunch of calls. Now those calls, I can put them asynchronous if I'm absolutely convinced that there's no issue with the order. Or I could still issue them asynchronous, but restore the order on the side of the system. And besides, if I have future orders next Wednesday by me, Johnson & Johnson, why insist on doing it right now?

Insist on doing it right now would needlessly increase the stress on the system. Such a request, you would actually go into a queue. And then during the downtime, you would dequeue future trades and execute them. So what we have here is volatility in the connectivity and the synchronicity of the calls.

We discussed volatility in the trade item. Most people are not going to trade just stocks. They're going to want to diversify the risk, and they're going to go for bonds, and they're going to go for currencies, or maybe commodities. And so the trade item is volatile.

Now, that kind of volatility implies additional volatility. For example, the system needs to connect to the outside world to process some kind of a market feed. Well, maybe stocks can change once per second. But if you're changing currencies, there's about 150 tradable currencies, each changes several times per second compared to all the others.

All of a sudden, you have a torrent of data flooding your system. In addition, the steps or the workflow of buying and selling stocks are very different than buying and selling currencies, commodities, bonds. And so the workflow is volatile. Same goes with the analysis.

It's not the same analysis for stocks and bonds. Why? Because stocks are riskier, so I actually expect a higher return. So if I make the same return on bonds and stocks, then my bonds is fine, but my stocks are not so fine, and so the analysis is different.

We discussed volatility in the locale. Once a locale is different, it will have implication on the trading rules. The acts of buying and selling stocks are different in New York versus London. And they're going to be different volatility in localization.

It's not just language. Different locales have different population of users, and those users could very much differ in the level of sophistication. It doesn't get any more sophisticated than the city of London or Wall Street. But maybe if you're going into some backwater market, you want to go for ease of use as opposed to sophistication.

And different locales are going to have different trade items. Maybe in New York, it's okay to have bonds and commodities in the same portfolio, but it's not okay in California, and on and on and on. We also have volatility in the feed. The system needs to go and connect to some kind of a provider, such as Bloomberg, and receive market feed.

Suppose you want to switch to another provider, such as Reuters. Do you think Reuters and Bloomberg use the same communication protocol? Well, we know the answer is probably not. Even if you use the same protocol, do you think the content of the message is going to be the same?

Meaning maybe Bloomberg give you stocks and currencies, and Reuters give you stocks and bonds. Could be. And even if it's just stocks and stocks, if you were to look at Bloomberg and Reuters at the same moment in time, are you going to see the same value of the stock? And the answer is probably not.

It's going to be close, but not quite, which means at least one of them is wrong. If at least one of them is wrong, maybe both of them are wrong. Maybe the truth is somewhere else. Maybe if you take 20% Reuters, 80% Bloomberg, or maybe it's a third, third, and a third is some kind of a secret sauce that you add on top.

I don't know what it is. I know that the content is volatile. And think about the format of the messages, which keeps changing. And maybe one feed ticks at 20 times per second, the other ticks at 20,000 times per second.

Now, you could have external feeds, you can also have internal feed. What does it mean? What if you do have that secret sauce? Well, you monitor the world, and then the real feed is actually internal.

Now, the feed can be real or simulated. Suppose you have a new trading algorithm, which you think is going to be very worthwhile. So you could actually deploy it and see if, in hindsight, you made more money, but you can also bankrupt the company. So a prudent way of solving it is let's make a recording of the last three years of data, feed it to the new algorithm, and see if, in hindsight, it would have made more money.

That's probably a better way of doing it, but now we're talking about simulating the feed and coming, in this case, from an internal that pretends to be external. And on and on and on. We don't have to discuss any of these things just to realize the feed is volatile. The key observation of the last few slides is that this is not an exhaustive list of all the possible areas of volatility in a stock trading system.

You could, in fact you should, spend several days doing what I just did, itemizing the volatility. My objective here was to really get you to think about what could change, and most importantly, what is the mindset you need to have as you go about hunting for areas of volatility. Sometimes, some areas of volatility are out of scopes. Mostly because they pertain too much to the nature of the business.

This is such an important point, we're going to discuss it in a separate slide. But in a nutshell, the nature of the business hardly ever changes. If you identify volatility that is unrelated to the nature of the business, or is too related, then anything that forces a change in the nature of the business, you actually don't encapsulate. For example, what if this system indeed must only trade stocks?

It can never go into, say, commodities. Its call to fame is, indeed, its ability to trade stocks. Well, you know what? Then the volatility in the trade item doesn't matter here, because going outside stocks would contradict the nature of the business.

On the other hand, if the nature of the business is just trading, and it's not specific just to stocks, then, of course, the volatility in the trade item matters a lot. Now, it's vital to call out the areas of volatility as soon as possible. And the reason is, drawing a box in your architecture costs you nothing. It's just digital ink.

It's pixels. It doesn't cost you anything. Nobody says you have to go and drill down and figure out all the details and assign developers and testers and deploy it. No.

Maybe you will never get to it. Maybe you have some kind of a stage delivery strategy that, over time, you will get to it. It doesn't matter. You need to call it out.

Your architecture has to be valid till the end of time, a point we're going to discuss later on. It should not be invalidated when things change. If things change, there is a box for it, and here it is. Once you settle on the area of volatility, those encapsulate in components of the architecture.

Now, here's the architecture we are going to use for the stock trading system. I'm going to keep coming back to it, so now just move on. The transition from the areas of volatility to service is hardly ever one-to-one. As a gross approximation, it is one-to-one.

But the important thing is to encapsulate the volatility, not necessarily to map it one-to-one to boxes on the architecture. Why? You could have a single service or a component encapsulate several volatilities. And sometimes you can have a volatility that is mapped to an operational concept rather than a component.

For example, if you have high volatility in throughput, 20 calls per second, 20,000 calls per second, the best way of mitigating that volatility is to introduce a queue in front of your system. And the reason is you could enqueue at whichever rate and dequeue at another rate. And now your system doesn't care about the frequency of the incoming messages, or put it differently, you've encapsulated it by the use of a queue. Now, technically speaking, I guess a queue is a component of the architecture, but it's not the same component as we talk about decomposition and boxes and so on.

Sometimes there's an area of volatility, but a third-party component or a vendor is taking care of it, in which case it's their problem. It's not a component in your architecture. Some mapping is straightforward. I always advise, start with the most obvious things that are clearly going to be components in your architecture.

For example, we discussed the data storage volatility. Now, the storage volatility implies a secondary volatility, which is access volatility. Even if I stick just to databases, how many ways do you have of accessing a database? And certainly, if I switch from a database to a file, to a cache, to a distributed hash table, whatever it is, the way I access the resource changes, irrespective of the resource.

We have two volatilities here. We have access volatility and the storage itself. So if you look at this architecture, you see at the bottom, these barrels, those are the storage. And note the sleight of hand.

It doesn't say database anymore. It says storage. The storage can be a database, a file, a queue, a hash table, a cache, and so on. On top of that, we have, in gray, components that encapsulate how you access those resources.

Now, this is fairly straightforward. And you can see they're actually mapped almost one-to-one, except all of a sudden, we have this feed access. So in this architecture, the external feed is actually a resource or some kind of a virtual store for your system. It's not even in your system.

But still, how you access it needs to be encapsulated. And you can see that with that gray feed access. We discussed notification volatility. And as a result, there is a box here called Notification that encapsulates all the elements of the notification volatility.

And those would be how you notify over which transport, who is the publisher, who is the subscriber, and so on. Now, the notion that your system may have volatility in the publisher, the subscribers, and even the transport is not unique, of course, to the stock trading system. Not exactly the pattern that the PubSub service is designed to solve. The PubSub service encapsulates the volatility of the publisher, the subscribers, and the transport.

In fact, a great exercise after this presentation, make a list of all the design patterns you're familiar with. And ask yourself, what is the key volatility that this design pattern encapsulates? So if you think about it, volatility-based decomposition is the master, most abstract design pattern there is. And all the other things are just variation of it.

And so you could, in this system, use just a general purpose PubSub. However, this is not the case in this stock trading system. Because the decision, whether or not to send an email or a fax, and maybe there's some regulation it should be in writing, and so on, these are business logic decisions. And therefore, we actually have a component in the architecture called notification.

Now, it may use underneath some off-the-shelf PubSub system, but that is an implementation detail to the notification box. We also identify volatility in the workflow of the trade. There's different steps in buying and selling stocks compared to currencies, different steps, different on locales, and over time, and so on. Since the workflow itself is volatile, we need to encapsulate it.

And you can see in the architecture a trade workflow, which, as the name implies, encapsulates the volatility in the workflow of the trade. We also have discussed the volatility in the duration of the session and the number of devices. And we have here an operational concept to handle it. And the operational concept is the use of a workflow storage.

So imagine that each workflow is actually stored, and there's even a workflow access component that encapsulates how you access it. What the trade workflow needs to do, every time it executes a stock trading workflow, it picks up the stock trading workflow for that particular locale, or even that particular user, by the way, picks it up, advances a step, and saves it back. Now, the advantage of doing it this way is that as the trader is making subsequent calls, and those calls can come two seconds apart or two days apart, and they can come from different devices, and they can come from different locations, all of that doesn't really matter to the trade workflow because it simply picks up the workflow, advances the next step, and saves it. So this operational concept of persisting the workflow encapsulates the volatility in the duration of the session, in the location, in the number of physical connections, and the type of device.

Exactly the same applies for the analysis workflows. Whether or not it's stock analysis, currency analysis, on this locale or that locale, is all specific for the analysis workflow, and therefore we have a separate box for the analysis. We also have volatility and security. All of that is encapsulated in the security box.

You can see upper right corner. So there is no security smeared across all components. When you need something with security, such as a good user or a bad user, they go to the purple box, and the purple box makes a decision for them about security. Then we have the volatility in the different client application.

You can see that we have different client application. You can have even different trader application, a customer portal, and so on. They're also encapsulated from each other their own volatility so that now the webpage can change independently from the desktop. I really mean it when I say decompose based on volatility.

I didn't say decompose based on what you're used to. I didn't say decompose based on what you already have. Decompose based on what the customer wants to see. No, you decompose based on volatility.

If something is not volatile, there is no need for a box in the architecture for it. In fact, if it's not volatile, hard code it, you'll get away with it. And so, for example, suppose that in the stock trading system, reports are not volatile. You are required by law to always respond and report this way and that's it.

As a result, the architecture doesn't have a reporting block. Now, of course, if reporting is volatile, there is a block, but in this case, there isn't. And this is going to be hard to come to terms with because you're so used for having a reporting block because every system has a reporting block and you always had a reporting block. But that's not volatility-based decomposition.

You could be doing functional decomposition in that case. And people that have been developing software incorrectly for a long time will hear an irresistible sign song of their bad habits calling them, pleading them to do it wrong again. So what is this analogy for the sign song? In Homer's Odyssey, after 10 years in the Trojan War, Odysseus is sailing home to his wife, Penelope.

So after the famous story with the Trojan horse, that was also Odysseus' idea. Why he didn't have that idea sooner, Homer doesn't say, but I guess better late than never. The Trojan horse, of course, was the world's first hack. Odysseus is sailing home.

And as he's sailing home, he has to clear the straits of the Siren. What are the Siren? The Siren are beautiful winged fairies that have the voice and face of angels and they sing a song no man can resist. The sailors would jump into their arms, the Siren would take them under the sea, drown them, and eat them.

And there's no not sailing through the straits of the Siren. And this situation is depicted on this vase from 2,500 years ago. This vase is in the British Museum. And so how is Odysseus overcoming the Siren song?

The first thing he does, he plugs the ears of his sailors with beeswax. In this analogy, the sailors are your developers. The sailors' job is to row. They're not at liberty of listening to the Siren.

They're supposed to write code. Unfortunately, he is the leader. As the leader, he doesn't have the liberty of plugging his ears. Maybe you do need that reporting block.

So he instead is tied to the mast of the boat. The sailors sail into the Siren, into the strait of the Siren, and the Siren appear. And they sing this song. And it sounds like this.

Add a reporting block. You need a reporting block. Everybody has a reporting block. We always had a reporting block.

And Odysseus is tied to the mast. And he is dying to free himself. And he says, well, free me. I want to add that reporting block.

Except the mast, he is tied to his volatility-based decomposition. And the mast says, well, if it's not volatile, there is no block. If it's not volatile, there is no block. And they sail through, and the crisis is over.
