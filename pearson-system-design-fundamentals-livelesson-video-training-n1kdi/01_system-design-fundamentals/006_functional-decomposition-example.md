# Functional Decomposition Example

- **Course:** Pearson System Design Fundamentals Livelesson Video Training
- **Module 1:** System Design Fundamentals
- **Lecture #:** 6
- **URL:** https://www.coursera.org/learn/pearson-system-design-fundamentals-livelesson-video-training-n1kdi/lecture/X6KXo/functional-decomposition-example
- **Extracted:** 2026-06-20 11:02:12

---

Now, you could be saying, okay, I understand it with houses and with jumbo jets, but we're designing and developing a software system, and it's so different in software, okay? Let's look at the software system. Let's talk about the stock trading system. Here's the requirements pack for a stock trading system.

It's a simple system, one-page requirements. The system should enable traders to buy and sell stocks, such as buy Johnson & Johnson. But you should also enable the traders to schedule trades, such as next Wednesday, buy me Johnson & Johnson. The system should issue reports, I bought you these stocks, analyze the trade, it was a good deal to buy those stocks, and so on.

Let's keep it simple. The client is a browser. The browser, you fill up a form, you press submit, it's a connected session, nothing too fancy. After every activity, such as trade, you need to send an email confirming what you did, and you're required to store it in a database.

Okay, this is a simple example, an example you've seen in every book on architecture, in every webcast, or an article, or a blog post. It's a classic example. Well, let's look at the architecture for that system. Most people will do some form of a naive functional decomposition that will look something like this.

You have a client here in green, and yellow boxes correspond to the requirements. Actually, every bullet has a corresponding building block in the architecture. We have buying stocks, we have selling stocks, scheduling, analyzing, reporting, and so on. At the bottom, we have a database, and we're done.

Most developers wouldn't give such a design a second thought. Now, this is so bad, I really hope you're not doing something as bad as this. Let's start poking holes through it. Who is saying to the system, buy and sell stocks?

Well, it's the client. Buy and sell. Okay. Now, suppose I'm trying to fund the trade by selling other stocks, which means first I'm going to do a sell, and then I'm going to do a buy.

Now, you're saying, no problem, here, sell, buy. The problem is, suppose by the time you execute this, the price of what you sold dropped, and the price of what you're about to buy has risen. That is actually likely to happen. The reason you sell stocks is because you think they're going to go down in value, and the reason you buy stocks is because you think they're going to go up in value, and now you can't fulfill the order.

And the question is, what are you going to do? Well, first option is not do anything, but you already sold stocks, what do you do? Buy them at a lower price? You could maybe just fulfill as much of the order as you can, or maybe you go to the cash account behind the trading account, and you fulfill the rest with cash, or maybe you sell other stocks to fulfill the order, or maybe you ask the user for instructions.

Now, I don't know quite how you're going to solve it, and nor is it relevant that much. My point is that how you resolve it is a business logic decision, which now resides in the client, and so now the client has to have business logic. Now, you were required to just do a web portal. Suppose marketing comes to you and says, we need to add a mobile device for this system.

The problem is, a mobile device is not just another green box in this system, because it's another system. All the business logic now has to reside in the mobile device, just like it resides in the web portal, and then you have to add a desktop, and maybe a HoloLens, and on and on and on. At some point, you will just throw your hand in the air, and you will say, we can't take it anymore, we cannot add more of these clients. And now you're impeding the business.

The business wants to grow, the business wants to go into different segments, different categories of users, and developers are saying, no, we cannot do it. And from that perspective, they are correct, because they cannot scale up with these clients. Every additional client means doubling up and doubling up of the entire development team. This is such a level of complexity, and nobody can actually keep up with it.

Now you had a requirement to send an email after everything that you do. In fact, every one of the yellow boxes, and of course the green box as well, sends an email. And the customer comes to you and says, email is so 90s, maybe you can send me a text message? And you say, well, we'd love to do it, except that is a very expensive sweeping change.

We have to go to every box and say not an email, a text, not an email, a text, not an email, a text, which is a horrendously expensive change. Now you had a requirement to store it in a database. Now suppose you need to move to the cloud. And the cloud vendors offer you amazing deals, and they say, we'll host your data for free for three years, just move your logic to us.

Well, out of the gate, this is also a sweeping expensive change, because it means you have to visit every yellow box and say the following, not local database, cloud, not local database, cloud. And that's a very expensive change. That is just the beginning of your trouble. Whenever you consume a local database, you typically pay for the license just once, and then you just go and party on it.

But when you go to the cloud, eventually they would nickel and dime you for the number of connections, the number of messages, the size of the messages, the bandwidth, the time of day. And that is a false function to go and make the calls very chubby. Now when you have a local database, the calls tend to be fairly chatty. So now we need to go to every one of those yellow boxes and say to them, don't be chatty, be chubby.

So that's a totally different way of thinking about how you access the data. But there's more. Most local databases tend to be relational databases. Now we can have a separate discussion, was that a good choice or not?

Most cloud out there offer a tabular and an object worth looking at the database. And so the very way you think about representing the data is completely different. And so now it's a complete rewrite of every box in the system just because you wanted to move the database to the cloud. And now you go back to the CTO or the CEO and say, no, this system cannot move to the cloud.

But the business wants to move to the cloud and the CTO is looking at the bottom line and the cost of doing the operation on site. And now you again, you're impeding the correct flow of the business. And more issues. We had a requirement here to do connected sessions in the browser.

And so this flow is the following. You fill up the form, submit it. You block the client. It executes the request to the system and you come back.

Unfortunately, most traders are not going to like it. And the reason they're not going to like it is because how much money the traders make is directly proportional to how many trades they do. If the form is blocking and basically have some kind of a lockstep execution, then that immediately gates how much money they can actually make. And now they're going to resent it.

They're going to want to push the calls asynchronously. Okay. Now you could just sprinkle some pixie dust on top of the green box and make the calls be asynchronous. And there's async and script and there's all the techniques for making it fairly easy.

The problem is the moment you go asynchronous, the calls start getting out of order. And so if you were to try and do that sell and then buy, even if you can fulfill by the virtue of how much stocks you actually sold, if you go asynchronous, perhaps the buy is going to happen before the sell. Now you can fulfill the order. And what if you're issuing a bunch of orders and they have a certain volume that actually moves the needle?

Because if you buy a hundred stocks, then you don't change the value of the stock. But if you buy a hundred million stocks and the value of what you buy actually goes up, and now that tends to change the legality of what's happening. Because if you know this is happening, you can buy some of that stock before and then sell it after and basically front run the system. There could be horrendous such problems just because of the order of the system.

And so the moment you go asynchronous, you lose the order of the calls. But this system is very much dependent on the order of the calls. So now what? Well, the only way to fix it is to restore the order of the calls on the yellow boxes, which means you have to start tagging the calls.

You don't just do A, B, C, because if you do A, B, C, they may get their B, C, A. So you say A is one out of three and B is two out of three and C is three out of three. And so if you just get them B, C, A, you say B, well, I never got an A because I got two out of three. I never got one out of three.

You put B in the buffer. And then you get the C and you say C, well, put it in the buffer after B. I got an A, okay, so now I execute the A and then I execute the B out of the buffer and I get the C and now I restore the order of the calls on the back end of the system. Now you can actually do it and lots of people actually solve it, except it's no longer the same yellow boxes because in the synchronous case, the yellow boxes did not care about the order.

Now they absolutely have to care about the order and they're internally coupled as well against the notion of implementing the sequencing. Most systems or most financial portfolios don't have just stocks in them. A well-balanced portfolio would need to have currencies and bonds and stocks simply to diversify the risk. Except if you look at this system, it says buying stocks and selling stocks and the acts of buying and selling stocks are very different than buying and selling commodities or currencies or bonds and there's different rules and different sequences.

Now over time, people are going to want to add different financial instruments to the system, different trade items, except this system was designed to buying and selling stocks. And so as the business evolves, as the traders come to you and say, we want to buy and sell currencies and bonds and commodities, you're going to have to keep duplicating components here because the user doesn't want to actually use different systems while they're all feeding from the same trading account. And so every time you add a different trade item, you're going to have to have a massive change in the system. Then we have globalization.

Globalization is not just about having the UI in German, in English and Korean. That's a list of your concern. Different locales are going to have different trading rules. For example, there are things and activities which are considered fraudulent in Wall Street but are legal in the city of London.

And even inside the same country, there's different trading rules in California versus New York, different compliance, different reporting. Unfortunately in this system, all of that is actually baked into the client and the interaction between the components, which means as you go to different locales, you're going to have to have the version of the system for New York and for London and for Singapore and for Frankfurt. As the business grows, the business would want to go to different locales, but you cannot afford to scale this way because you cannot double up and double up and double up the development team. And you're going to have your fingers in the dike in multiple places and at some point you say, we cannot take it anymore.

No more new businesses, no more new markets. And the business wants to go there. So now again, you're impeding your business. And this is the direct result of the functional decomposition you have in front of you here.
