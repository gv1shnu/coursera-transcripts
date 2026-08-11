# Connecting to a MongoDB Atlas Cluster with Compass

- **Course:** Introduction To Mongodb
- **Module 3:** Connecting to a MongoDB Database
- **Lecture #:** 10
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/cpLlr/connecting-to-a-mongodb-atlas-cluster-with-compass
- **Extracted:** 2026-08-11 09:53:07

---

Welcome back team. In this video you'll learn how to use your connection string with MongoDB Compass to connect to your cluster. We'll also take a quick tour of compass and show you how to use it to view and interact with your data. MongoDB Compass is a graphical user interface or GUI that allows us to query and analyze our data as well as compose aggregation pipelines.

Once your log back into Atlas, we're going to connect to our cluster using another connection string. Go ahead and click on the Connect button next to Cluster0. This time, on the modal that comes up, we'll go ahead and click on the MongoDB Compass option. This will bring up another modal window which will give us a connection string to use with MongoDB Compass.

Let's go ahead and copy this. I'll then go ahead and switch my screen back over to MongoDB Compass. Back in Compass, we'll go ahead and create a new connection. If your window doesn't open to a new connection by default, you can click New Connection in the upper left hand corner.

On the new connection screen, if your edit connection string is not in the on position, please go ahead and change that to the on position. Now then, in the URI box, we're going to replace what's there with our connection string from Atlas. In this connection string, you'll notice that the password isn't filled in just yet. You'll need to replace this password in order to proceed forward.

Once you've updated your password, you can go ahead and save and connect to this cluster. In the modal box that opens, you'll want to go ahead and name this connection. In my case, I'm going to go ahead and continue to call it Cluster0. You can also choose a color for this connection.

I'm going to of course go with the very smooth shade of green right here. Once you've named your cluster and selected a color, you can go ahead and save and connect to your cluster. Once you've connected to your cluster, you'll be brought to this view encompass. You'll notice the list of databases and their collections on the left hand menu.

Additionally, you'll find tabs for my queries so that you can save your aggregations and queries that you write in the future. Another tab for databases which will give you metadata about the databases available in your cluster. And finally the performance tab which will allow you to monitor performance metrics of your cluster. Although this particular tab is beyond the scope of this lesson, it's there in case you ever need to use it.

From there, let's go ahead and take a look at one of our databases. I'm going to click on sample analytics. You'll see this brings up the list of collections that exist within our database. Additionally, you can click into one of the collections.

This brings up a view that allows you to see the documents that exist within that collection. There's also quite a few additional tabs which we'll go through in just a moment. Very similar to Atlas, you can definitely use the Filter bar in order to filter for specific documents within that collection. On the Aggregations tab, you can compose aggregation statements to run against your collections.

These can even be exported to whatever language you happen to be working with. The Schema tab will help you to analyze the structure of your documents and can even help you to optimize that schema. The Explain Plan tab helps you to understand the performance of the specific queries that you're running against your database. The Indexes tab will allow you to see the indexes that exist on your specific collections.

This tab is also helpful because it can help you to understand the performance of your specific queries. Finally, the Validation tab allows us to create rules to enforce the structure of documents on update and insert statements. If these concepts are new to you, you'll become more familiar with them as you learn more about Atlas and MongoDB. Let's recap what we learned in this video.

We learned that Compass is a graphical user interface that allows us to query data, compose aggregation pipelines, and analyze data. We also learned how to use the connection string with Compass to connect to an Atlas cluster, great work.


<details><summary>Timestamped transcript</summary>

```
Welcome back team. In this video you'll learn how to use your connection string with MongoDB Compass to connect to your cluster. We'll also take a quick tour of compass and show you how to use it to view and interact with your data. MongoDB Compass is a graphical user interface or GUI that allows us to query and analyze our data as well as compose aggregation pipelines. Once your log back into Atlas, we're going to connect to our cluster using another connection string. Go ahead and click on the Connect button next to Cluster0. This time, on the modal that comes up, we'll go ahead and click on the MongoDB Compass option.
This will bring up another modal window which will give us a connection string to use with MongoDB Compass. Let's go ahead and copy this. I'll then go ahead and switch my screen back over to MongoDB Compass. Back in Compass, we'll go ahead and create a new connection. If your window doesn't open to a new connection by default, you can click New Connection in the upper left hand corner. On the new connection screen, if your edit connection string is not in the on position, please go ahead and change that to the on position. Now then, in the URI box, we're going to replace what's there with our connection string from Atlas.
In this connection string, you'll notice that the password isn't filled in just yet. You'll need to replace this password in order to proceed forward. Once you've updated your password, you can go ahead and save and connect to this cluster. In the modal box that opens, you'll want to go ahead and name this connection. In my case, I'm going to go ahead and continue to call it Cluster0. You can also choose a color for this connection. I'm going to of course go with the very smooth shade of green right here.
Once you've named your cluster and selected a color, you can go ahead and save and connect to your cluster. Once you've connected to your cluster, you'll be brought to this view encompass. You'll notice the list of databases and their collections on the left hand menu. Additionally, you'll find tabs for my queries so that you can save your aggregations and queries that you write in the future. Another tab for databases which will give you metadata about the databases available in your cluster. And finally the performance tab which will allow you to monitor performance metrics of your cluster. Although this particular tab is beyond the scope of this lesson, it's there in case you ever need to use it.
From there, let's go ahead and take a look at one of our databases. I'm going to click on sample analytics. You'll see this brings up the list of collections that exist within our database. Additionally, you can click into one of the collections. This brings up a view that allows you to see the documents that exist within that collection. There's also quite a few additional tabs which we'll go through in just a moment. Very similar to Atlas, you can definitely use the Filter bar in order to filter for specific documents within that collection.
On the Aggregations tab, you can compose aggregation statements to run against your collections. These can even be exported to whatever language you happen to be working with. The Schema tab will help you to analyze the structure of your documents and can even help you to optimize that schema. The Explain Plan tab helps you to understand the performance of the specific queries that you're running against your database. The Indexes tab will allow you to see the indexes that exist on your specific collections. This tab is also helpful because it can help you to understand the performance of your specific queries. Finally, the Validation tab allows us to create rules to enforce the structure of documents on update and insert statements.
If these concepts are new to you, you'll become more familiar with them as you learn more about Atlas and MongoDB. Let's recap what we learned in this video. We learned that Compass is a graphical user interface that allows us to query data, compose aggregation pipelines, and analyze data. We also learned how to use the connection string with Compass to connect to an Atlas cluster, great work.
```

</details>
