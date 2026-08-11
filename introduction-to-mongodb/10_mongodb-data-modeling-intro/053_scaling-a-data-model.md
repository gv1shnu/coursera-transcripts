# Scaling a Data Model

- **Course:** Introduction To Mongodb
- **Module 10:** MongoDB Data Modeling Intro
- **Lecture #:** 53
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/LjG2P/scaling-a-data-model
- **Extracted:** 2026-08-11 10:01:10

---

In this video, you will learn about the problems that arise when we create data models that aren't scalable and how to avoid them. MongoDBs first-principle of data that is accessed together, should be stored together as mostly because your query pattern, how you access your data, needs to align with your data model in order to have optimum efficiency of query result time, memory usage, CPU usage, and storage. This is a very complex topic. In this lesson, we will teach you some of the basics.

First, when creating a data model, we want to avoid documents that are unbounded. Unbounded means that the document size grows infinitely. This can happen when we use document embedding. Here's an example.

Let's examine the sample document model of a blog post and it's comments. Currently, all the comments on one blog post or in an array and the blog post document. This looks okay. But what if we get a lot of comments on this post?

What if we had thousands of comments on a post? This model allows us to easily retrieve all the blog posts comments in a single read. But problems will arise as the comments array grows larger. For example if we get thousands of comments, the document will get larger and take up more space in memory.

Also, this data model may have an impact on write performance. As comments are added to each document, the entire document is rewritten into MongoDB data storage. Furthermore, it will be difficult to perform pagination of the comments. Comments can't be easily filtered from a single post, so all comments will have to be retrieved and then filtered in the application.

Also, there's a maximum document size of 16 megabytes, so we'll eventually have storage problems. The benefit of this model is that we can retrieve all the documents in a single read, but that's probably not functionality you will need. The model creates problems without providing any real benefit. In this case, embedding comments probably isn't a good idea.

Instead, we can break our data up into multiple collections and use references to keep frequently accessed data together. For example here are two collections called blog posts and comments. We can use a blog entry ID field as a reference between the two collections. I hope this lesson helped to explain how our data model has a scale and how it has to match our query pattern.

Ultimately, you don't want more than the document size limit of 16 megabytes, poor query performance, poor write performance, too much memory being used. Effective data modeling will help prevent all those things. Great work.


<details><summary>Timestamped transcript</summary>

```
In this video, you will learn about the problems that arise when we create data models that aren't scalable and how to avoid them. MongoDBs first-principle of data that is accessed together, should be stored together as mostly because your query pattern, how you access your data, needs to align with your data model in order to have optimum efficiency of query result time, memory usage, CPU usage, and storage. This is a very complex topic. In this lesson, we will teach you some of the basics. First, when creating a data model, we want to avoid documents that are unbounded. Unbounded means that the document size grows infinitely. This can happen when we use document embedding.
Here's an example. Let's examine the sample document model of a blog post and it's comments. Currently, all the comments on one blog post or in an array and the blog post document. This looks okay. But what if we get a lot of comments on this post? What if we had thousands of comments on a post? This model allows us to easily retrieve all the blog posts comments in a single read.
But problems will arise as the comments array grows larger. For example if we get thousands of comments, the document will get larger and take up more space in memory. Also, this data model may have an impact on write performance. As comments are added to each document, the entire document is rewritten into MongoDB data storage. Furthermore, it will be difficult to perform pagination of the comments. Comments can't be easily filtered from a single post, so all comments will have to be retrieved and then filtered in the application. Also, there's a maximum document size of 16 megabytes, so we'll eventually have storage problems.
The benefit of this model is that we can retrieve all the documents in a single read, but that's probably not functionality you will need. The model creates problems without providing any real benefit. In this case, embedding comments probably isn't a good idea. Instead, we can break our data up into multiple collections and use references to keep frequently accessed data together. For example here are two collections called blog posts and comments. We can use a blog entry ID field as a reference between the two collections. I hope this lesson helped to explain how our data model has a scale and how it has to match our query pattern.
Ultimately, you don't want more than the document size limit of 16 megabytes, poor query performance, poor write performance, too much memory being used. Effective data modeling will help prevent all those things. Great work.
```

</details>
