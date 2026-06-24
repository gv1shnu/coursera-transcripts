# Intro to Deno and Deno KV

- **Course:** Database Architecture Scale Nosql Elasticsearch Postgresql
- **Module 3:** DenoKV
- **Lecture #:** 13
- **URL:** https://www.coursera.org/learn/database-architecture-scale-nosql-elasticsearch-postgresql/lecture/1G3Mm/intro-to-deno-and-deno-kv
- **Extracted:** 2026-06-22 20:48:27

---

Hello, and welcome to my lecture on the Deno Key Value Store. My name is Charles Severance. I'm a professor at the University of Michigan School of Information. So Deno emerged from the Node.js server project.

Node.js was a tremendous new opportunity when it made it possible for JavaScript to really be a server for web applications. The nice thing about JavaScript in the server and the client is the browser does JavaScript, and if the server does JavaScript, they can kind of share code, and execution can move back and forth. Node was founded in 2009 by a fellow named Ryan Dahl, and it was very, very successful. But in 2018, Ryan Dahl founded Deno, which is Node spelled backwards.

And that's not just random. He wanted a fresh start. The problem is that Node came on very early, and some things got locked in early days that you might want to have changed as an architect for a piece of software, and you couldn't just change it. And it became a really big business, and the stakes became really high.

And so Ryan, who was trying to do cool, innovative, next-generation stuff, found himself kind of limited in the innovation. And every time he wanted to do something, a bunch of people yelled at him because they had millions, if not billions, of dollars invested in that product. A number of things kind of manifested themselves as part of the pain of Node after 10 years. First off, there was a typing.

There was a JavaScript dialect battle, whether JavaScript pure or TypeScript was going to win. And TypeScript, a lot of people like it. It adds types to JavaScript. And the hope was, and this was a battle that raged for a while, that TypeScript would become not just a preprocessor, but it would just become the new JavaScript.

And that didn't happen. And so there was some large falling out between the TypeScript and JavaScript. It's gotten a little better now, but Node sort of just bounced through that whole thing. Supportive TypeScript, not supportive TypeScript.

The libraries would support TypeScript or not support. And it was just kind of a frustrating thing. Node started as a really kind of empty technology base. It was an interpreter for JavaScript that could run in the server.

And it wasn't opinionated. It was just kind of you could, it's like a language, like Python's a language, like Ruby is on a language. And so Node started out as not particularly opinionated. It could just run code.

And so to do anything useful with Node, you had to add a series of modules that almost became independent projects of their own right. And this led to the fact that there was kind of nothing really built into Node. And then you had all these dependencies. And there's all this sort of funny, funny jokes about how dependencies are hard to maintain.

And you're always getting new versions of stuff. And you could end up with hundreds, many hundreds of dependencies in a large project. And that is kind of a risk. And it just became difficult to maintain and improve Node, as I said before.

The other thing that happened was over that same past time period, the notion of distributed web architectures really came to the fore. And it's kind of silly. You're going to go to Amazon and rent a server and pay for bandwidth for that server, and then put all your CSS files and your image files and all that stuff from some one server sitting in a giant warehouse in Ohio in the United States of America. Well, it's slow, because all the connections in the whole world are coming there.

And the farther away you are, the slower the connection is. And the bandwidth outgoing is expensive. And it's not good for web architectures, because if you have to go across the Pacific Ocean, say from the United States to Korea, that takes a while and uses extremely scarce under-ocean cables. And so it's expensive.

It's slow. And so from the beginning, there was this notion that we would want to cache static assets like images, et cetera, JavaScript files near the edge, meaning not going underneath the Atlantic or Pacific Ocean, but somewhere on the other end. And so there's a company called Akamai very early on. Amazon CloudFront, CloudFlare, I'll talk about that more, and Fastly and Netlify.

And these are all organizations that put all around the world, put servers, and then for various amounts of money, let us put our static assets in. But then what happened was is it would be really smart about finding those assets at a server that is closer to the customer and not having to transfer them all the way from a single little virtual Linux environment running in Ohio. So I use the one right now called CloudFlare. And I'm not sure CloudFlare is the best.

I love it. And the thing I like about it is it's free. And a lot of those other ones, they try to get your money right away. So Akamai was very expensive and very awesome.

And really big folks who had lots of money used it right away. But I couldn't. I wasn't going to pay thousands of dollars for serving a small amount of static content near the edge. So whether I'm in Asia or Europe or South Africa, I would love to be able to put my static assets there.

The difference was CloudFlare was free. And the smart thing that CloudFlare did was they realized that they could convince these people in each of the countries not to fill up their under-ocean cables with a bunch of static stuff if they would just put a CloudFlare server. And then the CloudFlare would get a copy of my stuff and serve it within the country and not waste the precious trans-Atlantic, trans-Pacific, et cetera, bandwidth. And so the other thing that the CloudFlare did, for example, is because they have all these servers that are in all of these countries and on all these continents, if someone is doing what's called a distributed denial of service, which is they wake up a bunch of zombie computers and they attack your system, it's really hard to track them, except for the fact that CloudFlare had all of the traffic going through, let's just say, 150 different servers.

And if one zombie popped up in one country and the same zombie popped up in another country, CloudFlare could see that it was happening, where we could never see what was happening. So they had distributed denial of service protection, and it was free. I mean, seriously free. Amazing.

And so the actual server is a single EC2 server that cost me like $14 a month in Amazon, backed by a single database, MySQL database. And my server is kind of behind a VPN, and it only accepts network connections from CloudFlare servers, which means it's really difficult to give me a denial of service, because you're attacking CloudFlare, you're not attacking me. And if you look at the domain name, depending where you are in the world, you will see on a domain name lookup, CloudFlare will give you a different IP address. So depending on where you are in the world, with hundreds of servers all over the world on every major continent, CloudFlare has a presence.

And it gives you the domain that points to its local system. And then those servers forward your data to me in Ohio, in the United States of America, a $14 a month server. And so you cannot connect to my server. I can connect to it for maintenance, but you cannot connect to it no matter how you try.

I can even tell you what the IP address of that server is, and you won't be able to connect to it because of kind of an incoming VPN that CloudFlare gives me. So I can think of CloudFlare as this big thing. It's not. It's many little things geographically distributed.

It caches my static asset. It handles my DNS. It handles my termination and my HTTPS certificates, meaning that I don't need to have a certificate because CloudFlare in their servers generates certificates for me and handles all the HTTPS processing and DDoS, or distributed denial of service, my mitigation with thousands of servers and large amounts of disks, all geographically distributed. So in 2018, Coursera added this concept.

We've got all these servers sitting out there. They're not too busy. So how about if we make it so that people like me can install a little bit of JavaScript, not maybe our whole application, but what they call JavaScript workers. And it had to do with as web applications were evolving from static HTML in the browser to JavaScript in the browser.

And then web services on the back end. I mean, that's pretty cool, except there are some things that you want to share with your application, like secrets or connection strings or something. You don't want to put that in the user's browser where they can view source and see it. And so you could take parts of your application that you wanted to keep protected and sensitive and put that in the JavaScript workers running on CloudFlare hardware and then make the connections.

And so you didn't have to share sensitive information. And so that's pretty cool. And it seemed like it made a lot of sense. JavaScript, because of the work that Node has done in the last decade, JavaScript has become pretty adept at running inside of server code.

And it's got all this beautiful isolation, the sandboxing, et cetera, that makes it easy for it to have a quick cold start, run a little bit, be isolated from many other JavaScript workers, and then go away. And if you had a heavy duty site, you might have 3,000 JavaScript workers available and talking to one another as well. The JavaScript workers could talk to one another. So this seemed pretty cool.

My applications are PHP and then some JavaScript in the front end and CSS and HTML. And so the thing that's going back and forth between my servers and CloudFlare is HTML. And the thing that's going back and forth through short, quick connections between CloudFlare and you is also HTML. So I never really wrote much code for CloudFlare Workers.

It felt to me like CloudFlare Workers was kind of the first one that I saw. And I'm like, I kind of scratched my head. And I'm like, OK, how could I use this? I really can't convert my whole application to it.

And it just felt like it was too emergent. And it just didn't seem like it was going to be a standard in any way. And so they were playing with it and releasing new versions. And so I just like step back when I see something like that.

And I had no idea how the cost might scale. And so I just kind of stayed away. And what I really want to do is find an opportunity to experiment with a small part of a production application that I could back off. And I still never ran into that.

I teach more classes rather than build new technology that would make use of CloudFlare. So last year or so, I've been hearing more and more about Deno. It's like a modern Node.js. I never liked Node.js.

It turns out it wasn't that I didn't like Node.js. I didn't like Express. Express is the thing that turns Node.js into a web server. And I just didn't like Express.

And I didn't like all the promises. I didn't like all of the ways that you wrote code. It looked ugly to me. But then again, over the past few years, we got async await.

And the promises are not as scary looking. And for an old mainframe person like me, I can read and write JavaScript. I just need to know when to put async and when to put await. And that's cool.

And I'm beginning to learn that. And so the JavaScript has gotten better. And Deno is based on modern JavaScript. Now, the thing that I like about Deno is Deno has in-sourced a lot of the little dependencies for basic JavaScript capabilities, like signing a Java web token.

If you're doing that in Node, you've got some dependency. And there's some open source project of eight or nine people. And it probably is important. But you're depending on that.

But what Deno does is it pulls the basic stuff in. It also has chosen to support both JavaScript and TypeScript out of the box, which means it has enough built-in stuff so that if you write TypeScript, it works. And if you write JavaScript, it works. So it's not making a choice.

But it also means that all those standard libraries that Deno has also work in JavaScript and TypeScript, which gives the market, i.e. me, the choice to use JavaScript when we feel like it and TypeScript when we feel like it. And so Node becomes like Django. Django turns Python into a web server because it has a bunch of stuff built in.

It's got some batteries included. And it's opinionated. Now, I haven't rewrote all my code because Deno 2 just came out a few months before I'm recording this lecture. But the thing that got my interest related to this course is it's more than a server.

And this is something that Ryan Dahl has realized. And that is he just built Node.js and let everybody else make all the money on it. And that left his open source project not well-supported. And so he wants to make money off the hosting of Deno by giving us a commercial service that is a distributed hosting.

Cloudflare is a commercial service. And so you can write a Deno application. And you can go to deno.com. And you can distribute it.

Matter of fact, you will in this course. And it's cool. And it's a way of supporting open source. Now, what's cool is they release it all.

So if you just want to go get a bunch of Amazon things in Hong Kong, in Ohio, in Amsterdam, you can make Deno deploy work for you. And so it's not like it's live. Lock-in, Cloudflare is more lock-in to me. So DenoDeploy means if I really feel like it and I don't want to pay for their hosting, I can pay for the underlying hardware and do my own hosting.

And that's really cool. But the thing that really got me going as a teacher is it's free, permanently free for low-volume developer sites. And that's really important, because now I can have you do things and not make you pay. Then the other thing that I really love about Deno is it has this built-in JSON database, like a MongoDB.

That's every deploy instance. And so when you create the server code, it co-creates a database for you. Now, it's not an SQL database. That's the point.

We are in a non-ACID situation here. And so we're going to have a distributed database. It's not going to be ACID. It's going to be eventual consistency.

But it comes. And then you also don't have to build a messaging infrastructure, because DenoKV includes its own messaging infrastructure, publish, subscribe, and worldwide notifications. It's kind of like a Redis. So you've kind of got a simple database.

You've got a simple notification server. And you've got free commercial hosting all around the world. And so it's a cool idea. And just for completeness, I should note that there are other products in this space.

Cloudflare Workers. Cloudflare Workers now has a key value database. Cloudflare Workers has notifications. So I think Cloudflare is kind of playing catch-up with Deno, because Cloudflare is a very mature company.

And Deno is an upstart to some degree. And Cloudflare doesn't want to lose all the people that have invested in workers to Deno. There's other things like Upstash and Amazon's DynamoDB and Google's Firestore and Firebase that have similar kinds of distributed computing, distributed data environments. And the folks that I know from big companies that I say, what do you guys use?

Those folks that use this stuff at scale say, it is wonderful. But you have to have deep pockets, meaning that it's great to delegate to all these companies, to all the scaling and the distribution of it all. It's wonderful, because then you can focus on your application. But you better be ready to write checks that are four figures, five figures, and low six figures, potentially per month, to build and support large-scale applications.

Now, you might think six figures is expensive. But six figures is also the cost of a developer. And so you might say to yourself, OK, I've got a developer team of 10. And Deno is my 11th developer.

That's a way to think about it. Or I've got a developer team of 10. And Deno is my four more developers for $400,000. I'm just approximating here.

So the point is, we still don't know, or people like me, who are not big companies making lots of money, we don't know how well this is going to scale from a spending place. But that's where starting with a simple free developer version and seeing how it goes is a great way to get started. So if we review my architecture, I've got Cloudflare with static assets, distributed domain names, HTTPS, and DDoS mitigation. I've not yet used workers yet.

And it talks HTML through a VPN to my server in Ohio, my $20 a month server in Ohio. And that sends HTML back to Cloudflare. And Cloudflare sends it back to you. So when it's going across an ocean, that middle Cloudflare to Amazon, that's the cross-ocean link.

And the Cloudflare to your browser, three to five hops. And if you do a trace route, you can see that you going from your computer to www.pyfree.com, it has a very few hops. This might be eight or nine. But they're all short hops, fast hops, and low latency hops.

So this is my current architecture. And so I've been spending time thinking, is it time for me to do something different? So because I like Deno, because Deno seems like it might be more standard than other things like Netlify, and it just seems like it's because a lot of those things are based on Node. But this is the new Node.

And so Deno is going to deal with my DNS, my DDoS, my static asset, and JavaScript workers, and my distributed database. Now, I still expect that I am going to need a Amazon instance that has a Linux and SQL. Because the KV database, key value database, is not really great for permanent data. It's really great for live data, caching data, and data that's in the process of being changed.

And so you still kind of need a sort of old school Postgres or MySQL back end. But I also want to re-architect my application to use web services, both between the browser and DenoKV, and then between DenoKV and my sort of traditional relational back end. And so I like it. Why I like it?

Well, it's got so much built in. I love the standard JS library, so I don't have to have 40 dependencies just to say hello world. DenoKV as a built in database is great. And DenoKV watch is a built in messaging system.

Some of these other things, they kind of have one kind of database and one kind of messaging. And it feels like Deno is just starting fresh and looking at all these patterns, and trying to make it as easy as possible for me as a developer. And again, because I can deploy the open source DenoDeploy, don't have to use their hardware infrastructure, I love that. That gives me a little less fear of paying the only choice for hosting is them.

And also the free account for you and for me. And KV and KV watch are built in. I already said that. And I just think that in the future, as we build applications that move from kind of traditional seemingly classic web request response cycle applications to little notification based things, especially in education, I think that the notifications KV watch will be a very important.

So that's kind of where I feel, how I see KV fitting into the marketplace, and why I am intrigued enough to teach you about it. And so up next, we're going to talk about kind of high level architecture issues, and why perhaps DenoKV has the database patterns that it has.
