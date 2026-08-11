# Using MongoDB Indexes in Collections

- **Course:** Introduction To Mongodb
- **Module 8:** MongoDB Indexes
- **Lecture #:** 36
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/Uc0ar/using-mongodb-indexes-in-collections
- **Extracted:** 2026-08-11 09:58:00

---

Hello. In this video, you'll learn about indexes. We'll discuss what indexes are, how they can improve performance, and the cost of using them. We'll also review the most common index types.

Indexes are special data structures that store a small portion of the collections data in an ordered form that is easy to traverse and search efficiently. Indexes point to the document identity and allow you to look up access and update data faster. Indexes are used in MongoDB to improve query performance. They can speed up queries, reduce disk IO, and reduce the resources required for them.

Indexes also support queries such as equality matches and range based operations and return sorted results. Indexes store data in an ordered form based on the index fields and values so ordered that are provided when the index is created. Without indexes, MongoDB has to read every document in a collection by performing a collection scan to check if it matches the query being run. Also needs to sort the results in memory if the query requires a sorted output.

When using an index, MongoDB only fetches the documents identified by the index based on the query and returns the results faster. If the index includes all the information the query wants to retrieve, MongoDB does not need to read the document. By default, there is only one index created per collection. This default index only includes the underscore ID field.

Every query should use an index. This way, you can create additional indexes in your collections to cover your data queries. Be aware that indexes come with a right performance cost. When we insert new documents in the collection or update the index fields in them, we also need to update the data in the index structure.

Also, right performance can degrade if we have too many indexes in a collection. We need to make sure that all the indexes we have are being used. Otherwise, we should delete the unnecessary or redundant indexes. Now that we've covered the basics of indexing, let's go over the most common index types in MongoDB, single field indexes and compound indexes.

Single field indexes are indexes on one field only. Compound indexes include more than one field in the index. In both these indexes, the starting fields or index prefix can be used to support queries. Both index types can also be multikey indexes if they operate on an array field.

Each array entry has a corresponding index entry. Let's go through an example based on queries run against the customer's collection. Here's an example of a document from this collection. The collection includes information about the customers, such as the username, birthday, if they are active, the accounts they have, and other details about the account.

Let's say that we usually run these customer queries to search for all the customers who are active and have a specific account. In this case, we can define an index with the active and accounts fields to improve the performance of these queries. Because the index has two fields and one of them is an array field, it's a multikey compound index. Both queries can use this index.

Excellent work. Let's go over what you learned in this video. Indexes are ordered data structures that store some fields from a collection to allow faster data retrieval and reduce computation. Indexes support equality matches and range based query operations and return sorted results.

However, they come with a right performance cost. When an index field is updated or inserted, the corresponding index entry must also be updated. The most common index types and MongoDB are the single field indexes and compound indexes. Indexes that operate on an array field are referred to as multikey indexes.


<details><summary>Timestamped transcript</summary>

```
Hello. In this video, you'll learn about indexes. We'll discuss what indexes are, how they can improve performance, and the cost of using them. We'll also review the most common index types. Indexes are special data structures that store a small portion of the collections data in an ordered form that is easy to traverse and search efficiently. Indexes point to the document identity and allow you to look up access and update data faster. Indexes are used in MongoDB to improve query performance.
They can speed up queries, reduce disk IO, and reduce the resources required for them. Indexes also support queries such as equality matches and range based operations and return sorted results. Indexes store data in an ordered form based on the index fields and values so ordered that are provided when the index is created. Without indexes, MongoDB has to read every document in a collection by performing a collection scan to check if it matches the query being run. Also needs to sort the results in memory if the query requires a sorted output. When using an index, MongoDB only fetches the documents identified by the index based on the query and returns the results faster. If the index includes all the information the query wants to retrieve, MongoDB does not need to read the document.
By default, there is only one index created per collection. This default index only includes the underscore ID field. Every query should use an index. This way, you can create additional indexes in your collections to cover your data queries. Be aware that indexes come with a right performance cost. When we insert new documents in the collection or update the index fields in them, we also need to update the data in the index structure. Also, right performance can degrade if we have too many indexes in a collection.
We need to make sure that all the indexes we have are being used. Otherwise, we should delete the unnecessary or redundant indexes. Now that we've covered the basics of indexing, let's go over the most common index types in MongoDB, single field indexes and compound indexes. Single field indexes are indexes on one field only. Compound indexes include more than one field in the index. In both these indexes, the starting fields or index prefix can be used to support queries. Both index types can also be multikey indexes if they operate on an array field.
Each array entry has a corresponding index entry. Let's go through an example based on queries run against the customer's collection. Here's an example of a document from this collection. The collection includes information about the customers, such as the username, birthday, if they are active, the accounts they have, and other details about the account. Let's say that we usually run these customer queries to search for all the customers who are active and have a specific account. In this case, we can define an index with the active and accounts fields to improve the performance of these queries. Because the index has two fields and one of them is an array field, it's a multikey compound index.
Both queries can use this index. Excellent work. Let's go over what you learned in this video. Indexes are ordered data structures that store some fields from a collection to allow faster data retrieval and reduce computation. Indexes support equality matches and range based query operations and return sorted results. However, they come with a right performance cost. When an index field is updated or inserted, the corresponding index entry must also be updated.
The most common index types and MongoDB are the single field indexes and compound indexes. Indexes that operate on an array field are referred to as multikey indexes.
```

</details>
