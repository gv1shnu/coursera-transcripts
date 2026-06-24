# Welcome to the Course

- **Course:** Database Architecture Scale Nosql Elasticsearch Postgresql
- **Module 1:** Scaling Databases
- **Lecture #:** 1
- **URL:** https://www.coursera.org/learn/database-architecture-scale-nosql-elasticsearch-postgresql/lecture/Cq7UV/welcome-to-the-course
- **Extracted:** 2026-06-22 20:46:12

---

Welcome to Course 4 in Postgres for Everybody. Now we're going to finally talk about how things work, and sort of some of the meta issues around databases. And you might say to yourself, why didn't I talk about this at the beginning? In some ways, I did start with history.

I started to talk about how standards happen. And really, databases have been a big part of every application that we've built. How they've changed as we and the market and the world has changed. How the Internet changed, how the Cloud happened.

And so we're going to start with how they work, how relational databases work. And then we'll talk about what the strengths and the weaknesses are of relational databases and how we build and deploy relational databases and how we make them run at scale. And then again, that scale has changed over the years from 1000 users, hundreds of users to thousands of users to millions of users and on up, billions of users. The NoSQL movement is kind of part of that story.

And you might think that the NoSQL movement and the relational database movement are like at odds with one another. And the answer is they're in some ways very complimentary. There are so many moments where the relational databases needed to step up, to up their game a little bit. And NoSQL was a good example of showing a weakness in relational databases.

We will talk about deployment. We'll talk about scalability. We'll talk about words like master-master and master-slave replication, etcetera. And how that works and how that impacts performance and what works and what doesn't work.

And we'll finish up by actually using a NoSQL database. I've chosen to show you Elasticsearch. It's one of many NoSQL databases where you pretty much talk to it in JSON. The reason I picked Elasticsearch is that it is really common, and has been common for quite some time, to have a hybrid application that uses Elasticsearch to support its search, and then uses a relational database like mySQL or Postgres to do the rest of its application.

And so even if you work with relational databases for kind of the rest of your career, it won't be, you shouldn't be surprised if you eventually run into Elasticsearch. So there's a lot of really nice stuff going on in this, and I hope you enjoy the class.
