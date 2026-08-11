# Creating a Multikey Index in MongoDB

- **Course:** Introduction To Mongodb
- **Module 8:** MongoDB Indexes
- **Lecture #:** 38
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/BANYP/creating-a-multikey-index-in-mongodb
- **Extracted:** 2026-08-11 09:58:22

---

Hi. In this video, we'll define multikey indexes and discuss how MongoDB works with array fields that are used in indexes. We'll also work with a multi-key single field index. Let's work through an example by using the customers collection.

This collection contains details about each customer. It includes the email as a unique string to identify each customer, the customer's birthday, and the accounts related to the customer in array field. In a collection, there are different field types, including arrays and sub-documents. For example, the documents in the customer's collection includes the accounts build, which is an array.

When we define an index on an array field, that index is called a multikey index. Multikey indexes can index primitives, sub-documents, or sub-arrays. We can have an array field in a single field index or in the compound index. For instance, these two commands will create multi-key indexes because they include the field accounts, which is an array.

There is a limitation of only one array field per index. If an index has multiple fields, only one of them can be an array. Internally, MongoDB decomposes the array and stores each unique valley found within it as an individual index entry. If we have an application that runs queries on the customer's collection and we wanted to find customers with a specific account number, we should also have an index on the account's field.

When we use the get indexes method to find the indexes in the collection, the output indicates that there are three indexes. The default index on underscore ID, and two more single field indexes on the birthday and email fields. This shows no index on the accounts field. Let's confirm that another way.

We can run the explain command to see the query execution plan. Explainable show us that our query currently searches for documents with the account 627788 and that our query forces the database to perform a collection scan because there's no index on the accounts array. Let's fix that. We can create a single field index on the accounts field for the customer's collection.

Excellent. The account underscore one index is now created as a single field multikey index. Now we'll repeat the previous Explain command to see the execution plan for the query that searches for customers with the 627788 account. Great.

The output shows that MongoDB uses the new index in the IX scan stage. The index is on the account field that is a multikey index. Note that multikey indexes need to fetch the documents after the IX scan stage because the index entries have each of the array value stored separately. Congratulations.

Now you know how to index arrays by using multikey indexes in MongoDB. Let's recap what you've learned in this video. A multikey index is any index where one of the index fields contains an array. The array can hold nested objects or other field types.

In a compound index, only one of the fields can be an array.


<details><summary>Timestamped transcript</summary>

```
Hi. In this video, we'll define multikey indexes and discuss how MongoDB works with array fields that are used in indexes. We'll also work with a multi-key single field index. Let's work through an example by using the customers collection. This collection contains details about each customer. It includes the email as a unique string to identify each customer, the customer's birthday, and the accounts related to the customer in array field. In a collection, there are different field types, including arrays and sub-documents.
For example, the documents in the customer's collection includes the accounts build, which is an array. When we define an index on an array field, that index is called a multikey index. Multikey indexes can index primitives, sub-documents, or sub-arrays. We can have an array field in a single field index or in the compound index. For instance, these two commands will create multi-key indexes because they include the field accounts, which is an array. There is a limitation of only one array field per index. If an index has multiple fields, only one of them can be an array.
Internally, MongoDB decomposes the array and stores each unique valley found within it as an individual index entry. If we have an application that runs queries on the customer's collection and we wanted to find customers with a specific account number, we should also have an index on the account's field. When we use the get indexes method to find the indexes in the collection, the output indicates that there are three indexes. The default index on underscore ID, and two more single field indexes on the birthday and email fields. This shows no index on the accounts field. Let's confirm that another way. We can run the explain command to see the query execution plan.
Explainable show us that our query currently searches for documents with the account 627788 and that our query forces the database to perform a collection scan because there's no index on the accounts array. Let's fix that. We can create a single field index on the accounts field for the customer's collection. Excellent. The account underscore one index is now created as a single field multikey index. Now we'll repeat the previous Explain command to see the execution plan for the query that searches for customers with the 627788 account. Great. The output shows that MongoDB uses the new index in the IX scan stage.
The index is on the account field that is a multikey index. Note that multikey indexes need to fetch the documents after the IX scan stage because the index entries have each of the array value stored separately. Congratulations. Now you know how to index arrays by using multikey indexes in MongoDB. Let's recap what you've learned in this video. A multikey index is any index where one of the index fields contains an array. The array can hold nested objects or other field types.
In a compound index, only one of the fields can be an array.
```

</details>
