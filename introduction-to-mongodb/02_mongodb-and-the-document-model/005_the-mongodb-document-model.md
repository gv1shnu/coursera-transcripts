# The MongoDB Document Model

- **Course:** Introduction To Mongodb
- **Module 2:** MongoDB and the Document Model
- **Lecture #:** 5
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/nknbU/the-mongodb-document-model
- **Extracted:** 2026-08-11 09:52:10

---

Welcome back team. In this video, we'll learn about the MongoDB document model. MongoDB stores data in structures known as documents, that's why it's classified as a document database. Let's take a look at how documents are structured and what data types you can store in them.

We'll also define MongoDB's flexible schema model and discuss how it helps to evolve our applications quickly. First, let's take a closer look at how MongoDB stores our data. The MongoDB database structures data in documents which are similar to JSON objects. Here's an example of a simple document describing a product in an electronic store.

We can see that the document has five fields, including a colors field which holds an array of strings and an available field which holds a Boolean. While documents are displayed in a JSON format, they're stored in the database in a format called BSON. BSON, short for binary JSON, is an extension of JSON providing additional features that MongoDB can leverage. BSON also adds support for additional data types unavailable in standard JSON.

Because MongoDB stores data in BSON, the database can support a huge range of data types, including all the JSON data types such as string, object, array, Boolean, and null, as well as dates, different types of numbers, object IDs, and more. ObjectID is a special data type used in MongoDB to create unique identifiers. In the database, every document requires an ID field that acts as a primary key. If an inserted document doesn't include the ID field, MongoDB will automatically add it and generate an object ID value for it.

By default, MongoDB supports a flexible schema model and polymorphic data. This allows us to store documents with different structures in the same collection together. Documents can contain different fields, and fields may contain different data types from one document to the next. This is unlike relational databases in which it's necessary to declare a table schema before you begin inserting data.

MongoDB's flexible schema enables us to iterate quickly and evolve as our requirements change. Let's take a look at an example of the flexible schema in practice. Say we have an online furniture store which includes a catalog of items. When we start developing our application, we decide to store an ID, a name, and a price for each item.

Later during our development, we discover that we need to add an additional description field. With a relational database, we'd run into a complex chain of dependencies for even a trivial change like this one. Writing schema change scripts, coordinating across engineering teams, and downtime when the script executes. All of this would slow us down.

To make schema changes with MongoDB, we simply update our classes to include new fields and start inserting documents with the new schema. If we want to have more control over the structure and content of our database, we can add optional schema validation rules to set constraints on the structure of documents in the collection. To summarize, in this video, we learn that MongoDB documents are displayed in JSON format but stored in BSON. Compared to JSON, BSON supports additional data types like dates, numbers of various types, and object IDs.

Remember that an object ID is a data type that can be used in MongoDB to create a unique identifier for the required ID field. Finally, we discussed how MongoDB's flexible schema makes it possible to develop quickly, since we can modify our schema at any time. Recall that MongoDB supports polymorphic data. By default, fields and value types can vary across documents within a collection.

Remember that we can constrain the structure of those documents using the optional schema validation if necessary. Now that you're familiar with MongoDB's document model, you're ready to learn data management in Atlas.


<details><summary>Timestamped transcript</summary>

```
Welcome back team. In this video, we'll learn about the MongoDB document model. MongoDB stores data in structures known as documents, that's why it's classified as a document database. Let's take a look at how documents are structured and what data types you can store in them. We'll also define MongoDB's flexible schema model and discuss how it helps to evolve our applications quickly. First, let's take a closer look at how MongoDB stores our data. The MongoDB database structures data in documents which are similar to JSON objects.
Here's an example of a simple document describing a product in an electronic store. We can see that the document has five fields, including a colors field which holds an array of strings and an available field which holds a Boolean. While documents are displayed in a JSON format, they're stored in the database in a format called BSON. BSON, short for binary JSON, is an extension of JSON providing additional features that MongoDB can leverage. BSON also adds support for additional data types unavailable in standard JSON. Because MongoDB stores data in BSON, the database can support a huge range of data types, including all the JSON data types such as string, object, array, Boolean, and null, as well as dates, different types of numbers, object IDs, and more. ObjectID is a special data type used in MongoDB to create unique identifiers.
In the database, every document requires an ID field that acts as a primary key. If an inserted document doesn't include the ID field, MongoDB will automatically add it and generate an object ID value for it. By default, MongoDB supports a flexible schema model and polymorphic data. This allows us to store documents with different structures in the same collection together. Documents can contain different fields, and fields may contain different data types from one document to the next. This is unlike relational databases in which it's necessary to declare a table schema before you begin inserting data. MongoDB's flexible schema enables us to iterate quickly and evolve as our requirements change.
Let's take a look at an example of the flexible schema in practice. Say we have an online furniture store which includes a catalog of items. When we start developing our application, we decide to store an ID, a name, and a price for each item. Later during our development, we discover that we need to add an additional description field. With a relational database, we'd run into a complex chain of dependencies for even a trivial change like this one. Writing schema change scripts, coordinating across engineering teams, and downtime when the script executes. All of this would slow us down.
To make schema changes with MongoDB, we simply update our classes to include new fields and start inserting documents with the new schema. If we want to have more control over the structure and content of our database, we can add optional schema validation rules to set constraints on the structure of documents in the collection. To summarize, in this video, we learn that MongoDB documents are displayed in JSON format but stored in BSON. Compared to JSON, BSON supports additional data types like dates, numbers of various types, and object IDs. Remember that an object ID is a data type that can be used in MongoDB to create a unique identifier for the required ID field. Finally, we discussed how MongoDB's flexible schema makes it possible to develop quickly, since we can modify our schema at any time. Recall that MongoDB supports polymorphic data.
By default, fields and value types can vary across documents within a collection. Remember that we can constrain the structure of those documents using the optional schema validation if necessary. Now that you're familiar with MongoDB's document model, you're ready to learn data management in Atlas.
```

</details>
