# Updating MongoDB Documents by Using updateOne()

- **Course:** Introduction To Mongodb
- **Module 5:** MongoDB CRUD Operations: Replace and Delete Documents
- **Lecture #:** 21
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/cLaIK/updating-mongodb-documents-by-using-updateone
- **Extracted:** 2026-08-11 09:55:14

---

Welcome, in this video, you'll learn how to use common update operators in the MongoDB shell. First, we'll discuss the updateOne method, which we'll use with two common update operators $set and $push. Then, we'll go over how to use an option called upsert. Let's start with updateOne().

This method updates a single document. It accepts three arguments, a filter document, an update document, and an options object. The first argument, the filter document, contains the selection criteria for the update. The second argument, the update document, contains an update operator expression that will be used in the update.

The third argument is an options object. Note that options is not a required argument. When updating documents, we can use operators like $set or $push with update methods like updateOne. The $set operator does one of two things, it adds new fields and values to a document, or it replaces the value of a field with a specified value.

Likewise, the $push operator does one of two things, it appends a value to an array or if the field is absent, $push adds the array field with the value as its element. You can recognize an operator by the $ sign preceding it. Let's update some documents to observe this method in action. Imagine that you manage a database called audio, that contains a collection called podcasts, you need to update a podcast document with a new subscriber count and host.

You can use the updateOne method and update operators to make these changes. First, we'll run a findOne query so that we can view the podcast document. In the resulting document, the subscribers field is nonexistent and the host array is empty. We need to add a new subscribers field to the document.

What operator can we use with updateOne to do that? Set is a perfect operator for this task because it can be used to add a new field and value to a document. Within the updateOne method of this example, we include the -id field in the filter document. The filter document contains the selection criteria for the update.

Next, we have our update document, it uses the $set operator as the field name to update the number of subscribers to 98562. After running the updateOne method, we receive an output message that shows the matched and modified document counts. This tells us the update was a success. If the update filter doesn't match any documents, then no update occurs.

In this case, we might want to create a document. This is what the $upsert option allows us to do, insert a document with the provided information if matching documents don't exist. The $upsert option is short for update or insert. When the filter that gets passed to the updateOne method yields no matching documents, we can use $upsert to insert a document with the provided information into the collection.

In either case, the update operations provided in the update document will be carried out, either on the match document or on the document that was just inserted. Let's check out an example. We'll use the updateOne method to query a document that doesn't exist in our database, and then we'll examine the output. After running this command without the $upsert option, we get an output message showing that the matched count is 0, the modified count is 0, and the upserted count is 0.

This is expected because the default behavior of db.collection.updateone is to perform the update only if a document matches the filter query. Now let's run the same query, but this time, we'll add upsert: true to our options object. After passing in the filter document and the update document, we'll use the options object. In options, we add upsert: true, this tells MongoDB to create a document if none are found by using the information provided in the query and update documents.

Notice that the output shows an upsertedCount of 1. This means that we have successfully inserted the document, excellent. Let's move on to the $push operator. Now that we've added the subscribers field, let's go over how to add a new host to the MongoDB podcast document.

The document currently contains an empty array for hosts, we'll use the $push operator to add a new host to the array. First, pass in the filter. The filter includes the _id of the document that we want to update. Then, we pass in the update document, which includes the update modifiers that we want to apply.

In this case, we're using the $push to add a host: Nic Raboy. After running the command, you'll be able to determine from the output that the document was modified. Specifically, the matched count and modified count have a value of 1. That means that one document matched our filter and that the same document was updated.

To confirm this, we can use findOne, which shows that our host was successfully added to the document. Awesome work. Let's recap what you learned in this video. You learned how to use operators with the updateOne method to modify your documents.

The $set operator adds a field and value to a document. Set can also be used to replace the value of a field with a specified value if that field already exists. The $upsert option allows you to insert documents with the provided information if matching documents don't exist. Finally, $push is used to add elements to an array.

There are additional update operators that you can explorer in the MongoDB documentation. And now, you're ready to start updating documents in MongoDB.


<details><summary>Timestamped transcript</summary>

```
Welcome, in this video, you'll learn how to use common update operators in the MongoDB shell. First, we'll discuss the updateOne method, which we'll use with two common update operators $set and $push. Then, we'll go over how to use an option called upsert. Let's start with updateOne(). This method updates a single document. It accepts three arguments, a filter document, an update document, and an options object. The first argument, the filter document, contains the selection criteria for the update.
The second argument, the update document, contains an update operator expression that will be used in the update. The third argument is an options object. Note that options is not a required argument. When updating documents, we can use operators like $set or $push with update methods like updateOne. The $set operator does one of two things, it adds new fields and values to a document, or it replaces the value of a field with a specified value. Likewise, the $push operator does one of two things, it appends a value to an array or if the field is absent, $push adds the array field with the value as its element. You can recognize an operator by the $ sign preceding it.
Let's update some documents to observe this method in action. Imagine that you manage a database called audio, that contains a collection called podcasts, you need to update a podcast document with a new subscriber count and host. You can use the updateOne method and update operators to make these changes. First, we'll run a findOne query so that we can view the podcast document. In the resulting document, the subscribers field is nonexistent and the host array is empty. We need to add a new subscribers field to the document. What operator can we use with updateOne to do that?
Set is a perfect operator for this task because it can be used to add a new field and value to a document. Within the updateOne method of this example, we include the -id field in the filter document. The filter document contains the selection criteria for the update. Next, we have our update document, it uses the $set operator as the field name to update the number of subscribers to 98562. After running the updateOne method, we receive an output message that shows the matched and modified document counts. This tells us the update was a success. If the update filter doesn't match any documents, then no update occurs.
In this case, we might want to create a document. This is what the $upsert option allows us to do, insert a document with the provided information if matching documents don't exist. The $upsert option is short for update or insert. When the filter that gets passed to the updateOne method yields no matching documents, we can use $upsert to insert a document with the provided information into the collection. In either case, the update operations provided in the update document will be carried out, either on the match document or on the document that was just inserted. Let's check out an example. We'll use the updateOne method to query a document that doesn't exist in our database, and then we'll examine the output.
After running this command without the $upsert option, we get an output message showing that the matched count is 0, the modified count is 0, and the upserted count is 0. This is expected because the default behavior of db.collection.updateone is to perform the update only if a document matches the filter query. Now let's run the same query, but this time, we'll add upsert: true to our options object. After passing in the filter document and the update document, we'll use the options object. In options, we add upsert: true, this tells MongoDB to create a document if none are found by using the information provided in the query and update documents. Notice that the output shows an upsertedCount of 1. This means that we have successfully inserted the document, excellent.
Let's move on to the $push operator. Now that we've added the subscribers field, let's go over how to add a new host to the MongoDB podcast document. The document currently contains an empty array for hosts, we'll use the $push operator to add a new host to the array. First, pass in the filter. The filter includes the _id of the document that we want to update. Then, we pass in the update document, which includes the update modifiers that we want to apply. In this case, we're using the $push to add a host: Nic Raboy.
After running the command, you'll be able to determine from the output that the document was modified. Specifically, the matched count and modified count have a value of 1. That means that one document matched our filter and that the same document was updated. To confirm this, we can use findOne, which shows that our host was successfully added to the document. Awesome work. Let's recap what you learned in this video. You learned how to use operators with the updateOne method to modify your documents.
The $set operator adds a field and value to a document. Set can also be used to replace the value of a field with a specified value if that field already exists. The $upsert option allows you to insert documents with the provided information if matching documents don't exist. Finally, $push is used to add elements to an array. There are additional update operators that you can explorer in the MongoDB documentation. And now, you're ready to start updating documents in MongoDB.
```

</details>
