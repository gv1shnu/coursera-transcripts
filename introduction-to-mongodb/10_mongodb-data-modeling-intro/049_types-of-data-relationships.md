# Types of Data Relationships

- **Course:** Introduction To Mongodb
- **Module 10:** MongoDB Data Modeling Intro
- **Lecture #:** 49
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/XuHjx/types-of-data-relationships
- **Extracted:** 2026-08-11 10:00:25

---

Hello. In this video, we'll discuss the different types of relationships your data can have : one-to-one, one-to-many, and many-to-many. We'll also discuss the two main ways to model these relationships; embedding and referencing. In general, you should structure your data to match the ways that your application queries and updates that data.

Remember, in MongoDB, we follow this general principle when modeling data. Data that is accessed together should be stored together. When we don't store data together that is accessed together, the database must search through multiple collections in order to answer your query. This has both a resource costs and a time cost.

With that in mind, It's also important to understand the common types of relationships found in every database. These include one-to-one, one-to-many, and many-to-many. Let's explore each of these relationship types in more detail. One-to-one is a relationship where a data entity in one set is connected to exactly one data entity in another set.

In tabular traditional databases, you might link a table of movies with a table movie directors by using a join. In MongoDB, we can have a one-to-one relationship in a single document. Here we have a document for a single movie Star Wars with a single director, George Lucas. One-to-many is a relationship where a data entity in one set is connected to any number of data entities in another set.

For example, there are many cast members in our movie. This is an example of a one-to-many relationship shown in a single document. This is also an example of a nested array, which is a great way to model one-to-many relationships. The cast is an array datatype.

The benefit of this is that you can use one single query to retrieve all the data that you need for the application. Many-to-many is a relationship where any number of data entities in one set are connected to any number of data entities in another set. The two primary ways to model relationships in MongoDB are called embedding and referencing. Embedding ends when we take related data and insert it into our document.

Referencing is when we refer to documents in another collection in our document. Here are some examples. The first one shows an example of embedding. In this example, the act of documents are embedded within the movie document.

The second one shows an example of referencing. In this example, the film allocations are being referenced by their respective object IDs. Well done. In this video, you learned about data modeling relationships.

Here are the key takeaways. Data that is accessed together should be stored together. Modeling one-to-one, one-to-many, and many-to-many relationships is easy in MongoDB. The two primary ways of modeling data relationships in MongoDB are embedding and referencing.


<details><summary>Timestamped transcript</summary>

```
Hello. In this video, we'll discuss the different types of relationships your data can have : one-to-one, one-to-many, and many-to-many. We'll also discuss the two main ways to model these relationships; embedding and referencing. In general, you should structure your data to match the ways that your application queries and updates that data. Remember, in MongoDB, we follow this general principle when modeling data. Data that is accessed together should be stored together. When we don't store data together that is accessed together, the database must search through multiple collections in order to answer your query.
This has both a resource costs and a time cost. With that in mind, It's also important to understand the common types of relationships found in every database. These include one-to-one, one-to-many, and many-to-many. Let's explore each of these relationship types in more detail. One-to-one is a relationship where a data entity in one set is connected to exactly one data entity in another set. In tabular traditional databases, you might link a table of movies with a table movie directors by using a join. In MongoDB, we can have a one-to-one relationship in a single document.
Here we have a document for a single movie Star Wars with a single director, George Lucas. One-to-many is a relationship where a data entity in one set is connected to any number of data entities in another set. For example, there are many cast members in our movie. This is an example of a one-to-many relationship shown in a single document. This is also an example of a nested array, which is a great way to model one-to-many relationships. The cast is an array datatype. The benefit of this is that you can use one single query to retrieve all the data that you need for the application.
Many-to-many is a relationship where any number of data entities in one set are connected to any number of data entities in another set. The two primary ways to model relationships in MongoDB are called embedding and referencing. Embedding ends when we take related data and insert it into our document. Referencing is when we refer to documents in another collection in our document. Here are some examples. The first one shows an example of embedding. In this example, the act of documents are embedded within the movie document.
The second one shows an example of referencing. In this example, the film allocations are being referenced by their respective object IDs. Well done. In this video, you learned about data modeling relationships. Here are the key takeaways. Data that is accessed together should be stored together. Modeling one-to-one, one-to-many, and many-to-many relationships is easy in MongoDB.
The two primary ways of modeling data relationships in MongoDB are embedding and referencing.
```

</details>
