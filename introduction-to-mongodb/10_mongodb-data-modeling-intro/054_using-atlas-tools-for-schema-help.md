# Using Atlas Tools for Schema Help

- **Course:** Introduction To Mongodb
- **Module 10:** MongoDB Data Modeling Intro
- **Lecture #:** 54
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/rjGVg/using-atlas-tools-for-schema-help
- **Extracted:** 2026-08-11 10:01:21

---

Hello, in this video, you will learn about schema anti-patterns and the tools that MongoDB provides to identify them. We'll use the data explorer and the performance advisor in Atlas to find schema suggestions. Schema design patterns are guidelines that help developers plan, organize, and model data. When applications are developed without following schema best practices, it can result in sub-optimal performance or non-scalable solutions.

The most common schema anti-patterns include massive arrays, massive number of collections, bloated documents, unnecessary indexes, queries without indexes. And data that's accessed together but stored in different collections. It's not always easy to recognize these anti-patterns, but some of the tools available in MongoDB Atlas can help us identify and resolve them. Let's see two of these tools in action, data explorer and performance advisor.

The first tool, data explorer, is available with the free tier of Atlas. In Atlas, click Browse collections to access the data explorer. Here we can select a collection and view the storage size, number of documents, and total index size. The Indexes tab shows the collection indexes and their stats.

This helps us identify unnecessary indexes that can be dropped. The schema anti-pattern tab highlights any issues in the collection and provides details to resolve them. We'll select Learn how to fix this issue, to read more about this first antipattern and then follow the guidelines to remove it. In this case, we need to view the indexes and their usage.

We'll order by the usage column and identify the ones that have not been used based on the recent queries. Then we will determine if they can be deleted. If we know some of these indexes are not being used, we'll click Drop Index. This brings us to the second tool, the Atlas performance advisor.

The performance advisor can tell us which indexes are redundant. When working in an M10 tier or higher. The performance advisor section provides recommendations to improve the performance of the most active collections and collections with slow running queries. The performance advisor section shows index recommendations, identifies unnecessary indexes, and highlights issues with the schema.

Now, let's recap what you learned in this video. Atlas allows us to identify and address schema design anti-patterns. The data explorer is available with the free tier of Atlas. It shows schema anti-patterns as well as collection and index stats for each collection.

The performance advisor is available in an M10 tier and higher. This tool analyzes the most active collections and provides recommendations to improve the schemas.


<details><summary>Timestamped transcript</summary>

```
Hello, in this video, you will learn about schema anti-patterns and the tools that MongoDB provides to identify them. We'll use the data explorer and the performance advisor in Atlas to find schema suggestions. Schema design patterns are guidelines that help developers plan, organize, and model data. When applications are developed without following schema best practices, it can result in sub-optimal performance or non-scalable solutions. The most common schema anti-patterns include massive arrays, massive number of collections, bloated documents, unnecessary indexes, queries without indexes. And data that's accessed together but stored in different collections. It's not always easy to recognize these anti-patterns, but some of the tools available in MongoDB Atlas can help us identify and resolve them.
Let's see two of these tools in action, data explorer and performance advisor. The first tool, data explorer, is available with the free tier of Atlas. In Atlas, click Browse collections to access the data explorer. Here we can select a collection and view the storage size, number of documents, and total index size. The Indexes tab shows the collection indexes and their stats. This helps us identify unnecessary indexes that can be dropped. The schema anti-pattern tab highlights any issues in the collection and provides details to resolve them.
We'll select Learn how to fix this issue, to read more about this first antipattern and then follow the guidelines to remove it. In this case, we need to view the indexes and their usage. We'll order by the usage column and identify the ones that have not been used based on the recent queries. Then we will determine if they can be deleted. If we know some of these indexes are not being used, we'll click Drop Index. This brings us to the second tool, the Atlas performance advisor. The performance advisor can tell us which indexes are redundant.
When working in an M10 tier or higher. The performance advisor section provides recommendations to improve the performance of the most active collections and collections with slow running queries. The performance advisor section shows index recommendations, identifies unnecessary indexes, and highlights issues with the schema. Now, let's recap what you learned in this video. Atlas allows us to identify and address schema design anti-patterns. The data explorer is available with the free tier of Atlas. It shows schema anti-patterns as well as collection and index stats for each collection.
The performance advisor is available in an M10 tier and higher. This tool analyzes the most active collections and provides recommendations to improve the schemas.
```

</details>
