# Querying on Array Elements in MongoDB

- **Course:** Introduction To Mongodb
- **Module 4:** MongoDB CRUD Operations: Insert and Find Documents
- **Lecture #:** 17
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/oxZm2/querying-on-array-elements-in-mongodb
- **Extracted:** 2026-08-11 09:54:29

---

Welcome. In this video, you'll learn how to query your MongoDB database for specific values, also called Elements within an array. First, we'll go over how to query arrays in documents then we'll create a query by using the elemMatch operator to find documents in an array that match specific query criteria. Let's begin with a common use case for querying arrays in MongoDB, searching for every document with a field that contains the value we specify.

For instance, here we have a collection named Accounts. Each document in this collection has a field named Products. Let's examine a query to find all documents that contain the value of InvestmentStock. The syntax may look familiar if you've used Equality Match before.

This is because the query is looking for a Products field that has a value equal to InvestmentStock or a Products field with an array containing an element equal to InvestmentStock. After we run the query, the result provided to us is all documents that have a Products field with either an array or a scalar value containing InvestmentStock. The query doesn't return any documents that don't contain that value. What if you want to query for a value or values, but only return a match when they're an element of an array?

In these situations, we can use the elemMatch operator. To do this, we need to use $elemMatch along with the $eq operator. This ensures that the Products field is an array that contains InvestmentStock. Now, all of the documents returned have a Products field that's an array with an element equal to InvestmentStock.

We can also use $elemMatch to find documents where a single array element matches multiple query criteria. We place each query criteria in $elemMatch separated by a comma. In this example, we'll use a collection called Sales and we'll focus on the ItemsField. This field contains an array of subdocuments with the Items Information.

This query will find all documents with at least one item from the Sales collection. That's a laptop with a price greater than $800 and with a quantity greater than or equal to 1. After we run this query, the documents returned will contain laptops with quantities greater than 1 and prices greater than 800. Let's recap the key points covered in this video.

First, we queried arrays in a document. Then we used $elemMatch to find a subdocument that matches specific criteria in an array.


<details><summary>Timestamped transcript</summary>

```
Welcome. In this video, you'll learn how to query your MongoDB database for specific values, also called Elements within an array. First, we'll go over how to query arrays in documents then we'll create a query by using the elemMatch operator to find documents in an array that match specific query criteria. Let's begin with a common use case for querying arrays in MongoDB, searching for every document with a field that contains the value we specify. For instance, here we have a collection named Accounts. Each document in this collection has a field named Products. Let's examine a query to find all documents that contain the value of InvestmentStock.
The syntax may look familiar if you've used Equality Match before. This is because the query is looking for a Products field that has a value equal to InvestmentStock or a Products field with an array containing an element equal to InvestmentStock. After we run the query, the result provided to us is all documents that have a Products field with either an array or a scalar value containing InvestmentStock. The query doesn't return any documents that don't contain that value. What if you want to query for a value or values, but only return a match when they're an element of an array? In these situations, we can use the elemMatch operator. To do this, we need to use $elemMatch along with the $eq operator.
This ensures that the Products field is an array that contains InvestmentStock. Now, all of the documents returned have a Products field that's an array with an element equal to InvestmentStock. We can also use $elemMatch to find documents where a single array element matches multiple query criteria. We place each query criteria in $elemMatch separated by a comma. In this example, we'll use a collection called Sales and we'll focus on the ItemsField. This field contains an array of subdocuments with the Items Information. This query will find all documents with at least one item from the Sales collection.
That's a laptop with a price greater than $800 and with a quantity greater than or equal to 1. After we run this query, the documents returned will contain laptops with quantities greater than 1 and prices greater than 800. Let's recap the key points covered in this video. First, we queried arrays in a document. Then we used $elemMatch to find a subdocument that matches specific criteria in an array.
```

</details>
