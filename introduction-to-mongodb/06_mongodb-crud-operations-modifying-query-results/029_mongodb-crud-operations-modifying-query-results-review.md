# MongoDB CRUD Operations: Modifying Query Results Review

- **Course:** Introduction To Mongodb
- **Module 6:** MongoDB CRUD Operations: Modifying Query Results
- **Lecture #:** 29
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/Sx6sH/mongodb-crud-operations-modifying-query-results-review
- **Extracted:** 2026-08-11 09:56:43

---

In this unit, we learned to modify query results with MongoDB. We first saw how to return query results in a specified order using the cursor.sort method. The sort method takes a short document parameter that defines the sort order of the result set. We also saw how to constrain the number of results using the cursor.limit method.

The limit method takes an argument for the maximum number of documents to return. Remember that limiting results can enhance the performance of your application by avoiding unnecessary data processing. We then practice returning selected fields from a query using protection. We saw how to specify fields to return by adding a projection document as a second parameter in calls to the.find method.

We now know that inclusion and exclusion statements can't be combined in most projections with the exception of the ID field. We can choose to exclude the ID field in any projection, including when we're explicitly including other fields. Finally, we learned to count the number of documents matching a query using the DB.collection.count documents method. The count documents method accepts two parameters, a required query document and an options document.

Now that you've learned how to modify query results in the MongoDB shell, you might want to learn how to carry out some of these operations in your programming language of choice. Feel free to use any one of MongoDB's client drivers. Review MongoDB documentation on crowd operations in that specific language driver or check out one of MongoDB's drivers courses for more information. Congratulations on completing this unit on modifying query results with MongoDB.


<details><summary>Timestamped transcript</summary>

```
In this unit, we learned to modify query results with MongoDB. We first saw how to return query results in a specified order using the cursor.sort method. The sort method takes a short document parameter that defines the sort order of the result set. We also saw how to constrain the number of results using the cursor.limit method. The limit method takes an argument for the maximum number of documents to return. Remember that limiting results can enhance the performance of your application by avoiding unnecessary data processing. We then practice returning selected fields from a query using protection.
We saw how to specify fields to return by adding a projection document as a second parameter in calls to the.find method. We now know that inclusion and exclusion statements can't be combined in most projections with the exception of the ID field. We can choose to exclude the ID field in any projection, including when we're explicitly including other fields. Finally, we learned to count the number of documents matching a query using the DB.collection.count documents method. The count documents method accepts two parameters, a required query document and an options document. Now that you've learned how to modify query results in the MongoDB shell, you might want to learn how to carry out some of these operations in your programming language of choice. Feel free to use any one of MongoDB's client drivers.
Review MongoDB documentation on crowd operations in that specific language driver or check out one of MongoDB's drivers courses for more information. Congratulations on completing this unit on modifying query results with MongoDB.
```

</details>
