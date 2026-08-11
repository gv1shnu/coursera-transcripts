# Finding Documents in a MongoDB Collection

- **Course:** Introduction To Mongodb
- **Module 4:** MongoDB CRUD Operations: Insert and Find Documents
- **Lecture #:** 15
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/ZwjCY/finding-documents-in-a-mongodb-collection
- **Extracted:** 2026-08-11 09:54:06

---

Welcome, in this video, you'll learn how to find documents in a collection by using the find method. You'll also learn how to use the in operator when using the find command. Before jumping into our database, let's take a moment to look at the syntax for the find method. To use the find method, append it to the database and collection name in this format, db.collection.find.

For this example, we'll work with a database called training and query is collection called Zips. We can use the find method to view all the documents in the collection. To do this, we run db.zips.find. This returns a cursor with the results, which are addresses in the United States.

The shell will automatically iterate through our cursor once the results are returned. To see more results, we can use the it shell directive, which will iterate through the long list of results. Let's type it and press Enter a couple of times to view more documents that were returned from our query. Now, let's say we want to retrieve a specific document from our collection.

We can do this in two ways, we can use the eq operator, or we can use the implicit syntax of eq to shorten the length of our query with a field and the associated value. To do this, first we specify the field we're interested in. For this example, we want the state field followed by the value of this field. In this case, we want AZ, which is short for Arizona.

After we run the command, the corresponding documents will be returned. Now that we know how to find documents in a collection, let's go a step further by using the in operator. The in operator allows us to select all documents that have a field value equal to any of the values specified in the array. Before we create a query using the in operator, let's first examine how to structure our query.

We specify the field we're interested in, followed by $ in, and then an array of values that we want to match. Let's see the in operator in action to get a better understanding of how this works. In this expression, we want to find every document with a value of the cities of Phoenix or Chicago. After we run this command, the database responds with all the resulting documents of the cities of Phoenix and Chicago.

Here are the key takeaways from this video, we can use the eq operator to find documents with a field and a value. We can use the in operator to select documents that have a field value equal to any of the values specified in the array.


<details><summary>Timestamped transcript</summary>

```
Welcome, in this video, you'll learn how to find documents in a collection by using the find method. You'll also learn how to use the in operator when using the find command. Before jumping into our database, let's take a moment to look at the syntax for the find method. To use the find method, append it to the database and collection name in this format, db.collection.find. For this example, we'll work with a database called training and query is collection called Zips. We can use the find method to view all the documents in the collection. To do this, we run db.zips.find.
This returns a cursor with the results, which are addresses in the United States. The shell will automatically iterate through our cursor once the results are returned. To see more results, we can use the it shell directive, which will iterate through the long list of results. Let's type it and press Enter a couple of times to view more documents that were returned from our query. Now, let's say we want to retrieve a specific document from our collection. We can do this in two ways, we can use the eq operator, or we can use the implicit syntax of eq to shorten the length of our query with a field and the associated value. To do this, first we specify the field we're interested in.
For this example, we want the state field followed by the value of this field. In this case, we want AZ, which is short for Arizona. After we run the command, the corresponding documents will be returned. Now that we know how to find documents in a collection, let's go a step further by using the in operator. The in operator allows us to select all documents that have a field value equal to any of the values specified in the array. Before we create a query using the in operator, let's first examine how to structure our query. We specify the field we're interested in, followed by $ in, and then an array of values that we want to match.
Let's see the in operator in action to get a better understanding of how this works. In this expression, we want to find every document with a value of the cities of Phoenix or Chicago. After we run this command, the database responds with all the resulting documents of the cities of Phoenix and Chicago. Here are the key takeaways from this video, we can use the eq operator to find documents with a field and a value. We can use the in operator to select documents that have a field value equal to any of the values specified in the array.
```

</details>
