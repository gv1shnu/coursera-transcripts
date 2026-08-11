# Embedding Data in Documents

- **Course:** Introduction To Mongodb
- **Module 10:** MongoDB Data Modeling Intro
- **Lecture #:** 51
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/WC6lI/embedding-data-in-documents
- **Extracted:** 2026-08-11 10:00:47

---

Welcome. In this video, you'll learn about how to model your data by using embedding. Embedding is often used when you have one-to-many or many-to-many relationships in the data that's being stored. MongoDB recommends embedding documents in order to simplify queries and improve overall query performance.

Let's begin with an overview of embedded documents, also known as nested documents. These are documents that contain a document inside of another document. Embedded documents can range from fairly straightforward, such as first name, last name embedded in a name field to complex with many embedded fields. Embedded documents can be used for any type of a relationship model.

To illustrate this, consider this document with embedded sub-documents for name and address. In the name field, the customer has only one name, Sarah Davis. This is embedded as first name, last name. In the address field, the customer has three addresses, so it's a one-to-many relationship.

Nessa documents like this one shown here, make it easy to retrieve complete address information for our customer. Embedding data like this is useful because it meets the principle of data that is accessed together should be stored together. Embedded documents enable us to store all kinds of related information in a single document. This can both simplify and reduce the number of queries required by your application.

Embedding avoids application joins, which minimizes queries and provides better performance for read operations. Furthermore, embedded data models allow developers to update related data in a single right operation. However, you should be aware of some issues that can arise when using embedded data models. First, embedding data into a single document can, over time make your document larger and larger as you add data.

Storing large documents in your database can lead to excessive memory and add latency for reads. This is because large documents must be read into memory in full. The result of this is an often slow application performance for your end-user. Second, when embedding, you might accidentally structure your document in a way that data is added continuously without limit.

This creates what we refer to as an unbounded document. Unbounded documents run the risk of exceeding the maximum based on document size of 16 megabytes. Both large documents and unbounded documents are schema anti-patterns, which you should avoid. You can read more about schema anti-patterns in the official MongoDB documentation which you can find on our website.

Well done. Here are some key takeaways from this video. Embedded documents capture relationships between data by storing related data in a single document. MongoDB recommends embedding documents in order to simplify queries and improve overall query performance.

Embedding documents is ideal for one-to-many and many-to-many relationships among data. Embedding also has a well-known pitfalls, such as large an unbounded documents, depending on query frequency.


<details><summary>Timestamped transcript</summary>

```
Welcome. In this video, you'll learn about how to model your data by using embedding. Embedding is often used when you have one-to-many or many-to-many relationships in the data that's being stored. MongoDB recommends embedding documents in order to simplify queries and improve overall query performance. Let's begin with an overview of embedded documents, also known as nested documents. These are documents that contain a document inside of another document. Embedded documents can range from fairly straightforward, such as first name, last name embedded in a name field to complex with many embedded fields.
Embedded documents can be used for any type of a relationship model. To illustrate this, consider this document with embedded sub-documents for name and address. In the name field, the customer has only one name, Sarah Davis. This is embedded as first name, last name. In the address field, the customer has three addresses, so it's a one-to-many relationship. Nessa documents like this one shown here, make it easy to retrieve complete address information for our customer. Embedding data like this is useful because it meets the principle of data that is accessed together should be stored together.
Embedded documents enable us to store all kinds of related information in a single document. This can both simplify and reduce the number of queries required by your application. Embedding avoids application joins, which minimizes queries and provides better performance for read operations. Furthermore, embedded data models allow developers to update related data in a single right operation. However, you should be aware of some issues that can arise when using embedded data models. First, embedding data into a single document can, over time make your document larger and larger as you add data. Storing large documents in your database can lead to excessive memory and add latency for reads.
This is because large documents must be read into memory in full. The result of this is an often slow application performance for your end-user. Second, when embedding, you might accidentally structure your document in a way that data is added continuously without limit. This creates what we refer to as an unbounded document. Unbounded documents run the risk of exceeding the maximum based on document size of 16 megabytes. Both large documents and unbounded documents are schema anti-patterns, which you should avoid. You can read more about schema anti-patterns in the official MongoDB documentation which you can find on our website.
Well done. Here are some key takeaways from this video. Embedded documents capture relationships between data by storing related data in a single document. MongoDB recommends embedding documents in order to simplify queries and improve overall query performance. Embedding documents is ideal for one-to-many and many-to-many relationships among data. Embedding also has a well-known pitfalls, such as large an unbounded documents, depending on query frequency.
```

</details>
