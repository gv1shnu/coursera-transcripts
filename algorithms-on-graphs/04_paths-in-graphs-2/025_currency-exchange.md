# Currency Exchange

- **Course:** Algorithms On
- **Module 4:** Paths in Graphs 2
- **Lecture #:** 25
- **URL:** https://www.coursera.org/learn/algorithms-on-graphs/lecture/m2p4u/currency-exchange
- **Extracted:** 2026-06-21 21:27:00

---

Hi in this lecture we're going to study the Bellman Ford algorithm. Remember that in the previous lecture, we studied Dykstra's algorithm and it is a general algorithm for finding shortest path in any way to graphs, but where all the edges have no negative ways. So Bellman Ford algorithm doesn't have this restriction. It is a general algorithm for finding shortest spots in any weighted graphs, without any restriction on the weights of the edges.

But we'll start studying it with a very interesting application of this algorithm, which is to currency exchange, which is somewhat unexpected. So the problem is just following, you can convert between some of the currencies you have a convertation between dollar and euro and back. In some cases you can convert from one currency to another but you cannot convert it back because no one wants to convert in this direction. And you start with $1,000 and in the end you want to get as many Russian rubles as you can.

So the question is, is it possible to get as many Russian rubles as you want? So any sufficiently large amount, is it possible to get as many U.S. dollars as you want in the process? And what is actually the maximum amount of Russian rubles or U.S.

dollars that you can get? So this is the set of questions we want to answer. One of the reasons were asking those questions is the possibility of arbitrage and an example of arbitrage is depicted below by John Shendy on the example of three currencies for U.S. dollars, euros and British pounds and three banks with different exchange rates.

So you start with $5 million dollars and it turns out that the conversion rate from dollars to euro in Dutch Bank is 0.8171. And if you compute then you'll get 4,085,500 euros out of your initial $5 million if you do the exchange. Next, you can go to another bank credit Agricole and exchange euros to pounds and £1 is €1.1910. So out of your € 4,085, 500 you get 3,430,000, 311 British pounds.

And then to complete the deal, you go to the third bank, Barclays, and the conversion rate from pounds to U.S. dollar is 1.4650. So when you convert your pounds, you get $5,025,406. So we started with just five million and you turned a profit of 25,406.

This is called arbitrage. Typically these situations don't happen in practice, but if at some point the rates allow for that, we definitely want to know how to use that to extract some profit. So this is why we're going to approach this problem. And even if arbitrage is not possible, many of us still often need to exchange one currency and get another currency and if there is some more optimal way to do that rather than just exchanging directly, it is also good to know if that's possible and how to do that.

So a typical exchange if you exchange not directly but you do several exchanges like in the previous example makes the following. You start with some amount of for example U.S. dollars, it doesn't actually matter with which amount you start, if the exchange rates don't depend on the amount and we will assume that. So let's say you start with $1.

If the exchange rate from dollar to euro is 0.88 then you will multiply your one U.S. dollar by 0.88 and you will get the corresponding amount of euros. If then the exchange rate from euros to British pounds is 0.84, then you need to multiply that further by 0.84 so on. And in the end for the last age you get 8.8 rubles for the unit of the previous currency, then you need to multiply all that by 8.08.

And the number we should get after multiplying all those numbers on the edges, the exchange rates will be the amount in rubles that you will get. So what you want is to maximize this number. And in a general situation, you could have some graph with for example five currencies and some of them are connected with directed edges and these edges are weighted. And there is an edge from one currency to another if it is possible to exchange first currency and to get back another one, it could be not possible in the opposite direction, in the general case and the weight on the edge is the rate of exchange.

And what you want to do is to compute the maximum possible product over all the paths from one currency to another. If in the case we want to exchange U.S. dollars, two rubles, you need to find the path with the maximum possible product of exchange rates or all the paths from us dollars to Russian rubles in the graph. So this is the problem we want to solve and in the next video we'll reduce this problem to a problem about shortest paths in weighted graphs.
