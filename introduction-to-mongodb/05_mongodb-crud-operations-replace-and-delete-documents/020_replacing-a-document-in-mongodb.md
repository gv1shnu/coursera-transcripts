# Replacing a Document in MongoDB

- **Course:** Introduction To Mongodb
- **Module 5:** MongoDB CRUD Operations: Replace and Delete Documents
- **Lecture #:** 20
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/dThC3/replacing-a-document-in-mongodb
- **Extracted:** 2026-08-11 09:55:03

---

Hello. In this video, you'll learn how to replace a document in MongoDB. Sometimes documents are incorrectly inserted into a collection. Luckily, it's a simple process to replace those inserted documents within your collection.

Let's get started. To replace a single document, we'll use the replace one method. This method accepts three arguments a filter, a replacement document, and an options object. The options object is not required and won't be taught in this video.

To understand how the replace one method works, let's use an example. Imagine you work for a publisher that has a database for released and unreleased computer science books. Unreleased books still get an entry in the database, but because they're incomplete, Some of them have temporary titles or missing data. We can replace any entry or document that has missing or incorrect data with an updated document that contains the accurate information.

But we can keep the same underscore ID, which is pretty convenient. Let's look at an example document. Here we see the ISBN, publication date, and thumbnail URL all have placeholder information. This is because the document was created before the book was ready to publish.

To replace this placeholder document with an updated one, we'll start by using the replace one method on the books collection. Notice that we're using the document structure here, which is indicated by curly brackets. We'll want to identify which document we want to replace. To do this, we'll specify the underscore ID in our filter.

You'll recall from previous lessons that underscore IDs are a good filter criteria because they are guaranteed to be unique. Now imagine that the publisher has up-to-date information about the placeholder document that they want to add to the database. In a scenario like this, it makes sense to replace the entire document because the updated information applies to most fields in the document. We'll replace the document with a different one, bypassing the replacement document as the second parameter to the replace one method.

The replacement document contains all the data excluding the underscore ID field that will take the place of the current document. When we run the command, the output shows us a matched count and modified count, both of which are one. The matched count is the number of documents that matched our filter. The modified count refers to how many of those documents were modified.

Given this output, we can feel confident that our replacement was a success. But if we want to be sure, we can run find one on the document. This command locates a single document based on the certain criteria. Again, the criteria is the underscore ID.

Running this command allows us to confirm that the document has been updated and that it has the same document underscore ID as before. Excellent work. Now let's recap what you learned in this video. You replaced a document in MongoDB by using replace one.

This method accepts a filter and a replacement document. In return, you'll get output that contains the number of matched and modified documents.


<details><summary>Timestamped transcript</summary>

```
Hello. In this video, you'll learn how to replace a document in MongoDB. Sometimes documents are incorrectly inserted into a collection. Luckily, it's a simple process to replace those inserted documents within your collection. Let's get started. To replace a single document, we'll use the replace one method. This method accepts three arguments a filter, a replacement document, and an options object.
The options object is not required and won't be taught in this video. To understand how the replace one method works, let's use an example. Imagine you work for a publisher that has a database for released and unreleased computer science books. Unreleased books still get an entry in the database, but because they're incomplete, Some of them have temporary titles or missing data. We can replace any entry or document that has missing or incorrect data with an updated document that contains the accurate information. But we can keep the same underscore ID, which is pretty convenient. Let's look at an example document.
Here we see the ISBN, publication date, and thumbnail URL all have placeholder information. This is because the document was created before the book was ready to publish. To replace this placeholder document with an updated one, we'll start by using the replace one method on the books collection. Notice that we're using the document structure here, which is indicated by curly brackets. We'll want to identify which document we want to replace. To do this, we'll specify the underscore ID in our filter. You'll recall from previous lessons that underscore IDs are a good filter criteria because they are guaranteed to be unique.
Now imagine that the publisher has up-to-date information about the placeholder document that they want to add to the database. In a scenario like this, it makes sense to replace the entire document because the updated information applies to most fields in the document. We'll replace the document with a different one, bypassing the replacement document as the second parameter to the replace one method. The replacement document contains all the data excluding the underscore ID field that will take the place of the current document. When we run the command, the output shows us a matched count and modified count, both of which are one. The matched count is the number of documents that matched our filter. The modified count refers to how many of those documents were modified.
Given this output, we can feel confident that our replacement was a success. But if we want to be sure, we can run find one on the document. This command locates a single document based on the certain criteria. Again, the criteria is the underscore ID. Running this command allows us to confirm that the document has been updated and that it has the same document underscore ID as before. Excellent work. Now let's recap what you learned in this video.
You replaced a document in MongoDB by using replace one. This method accepts a filter and a replacement document. In return, you'll get output that contains the number of matched and modified documents.
```

</details>
