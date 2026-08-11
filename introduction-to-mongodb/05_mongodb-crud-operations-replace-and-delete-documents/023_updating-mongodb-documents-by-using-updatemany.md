# Updating MongoDB Documents by Using updateMany()

- **Course:** Introduction To Mongodb
- **Module 5:** MongoDB CRUD Operations: Replace and Delete Documents
- **Lecture #:** 23
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/lrt1G/updating-mongodb-documents-by-using-updatemany
- **Extracted:** 2026-08-11 09:55:36

---

Hello. In this video, you'll learn how to update multiple documents in a single MongoDB collection by using the updateMany method. The updateMany method accepts a filter document, an update document, and an options object. The options object is not required, and we won't use it in this video.

The filter document contains the selection criteria for the update. In this example, year 2022 is the filter document within the updateMany method. The update document contains the modifications to apply to all documents that match the filter. Imagine that we want to update all the books in a collection that meet certain criteria, we can use the updateMany method to do this.

Here's one document from the books collection. It includes information about a single book, including fields like underscore, id, title, publish date, status, and authors. We'll use updateMany to update all documents that were published before 2019 to have a status of legacy. First, let's examine the filter document.

Here, we'll use the lt operator less than followed by the date January 1, 2019, because we want books that were published before 2019. Any documents that match this filter will get updated. Then we need to tell MongoDB how to update the documents that match the filter. In the update document, we use the set operator to update the value of the status field to legacy.

Now we can run the updateMany method on the books collection. The output shows that our update was successful because the matched count and modified count are both the same. Pretty useful, right? Now that you know how to use updateMany, let's go over when to use it.

It's important to note that updateMany is not an all-or-nothing operation. By this, we mean that in the rare instance where the operation fails, updateMany will not roll back the updates, so only some documents may be updated. If this happens, you need to run updateMany again to update the remaining documents. UpdateMany also lacks isolation, which means that updates will be visible as soon as they're performed.

Because of this, updateMany is not appropriate for some use cases that may be essential for business requirements, such as financial transactions. Let's recap what you learned in this video. In MongoDB you can update multiple documents with updateMany. This method accepts a filter document, an update document, and an options object.

It returns an output message that shows the number of matched and modified documents. When the operation fails, updateMany does not roll back the updates if all documents aren't updated. Running updateMany again will complete the multi-document update. Overall, updateMany is a convenient and efficient way to update multiple documents in a collection.


<details><summary>Timestamped transcript</summary>

```
Hello. In this video, you'll learn how to update multiple documents in a single MongoDB collection by using the updateMany method. The updateMany method accepts a filter document, an update document, and an options object. The options object is not required, and we won't use it in this video. The filter document contains the selection criteria for the update. In this example, year 2022 is the filter document within the updateMany method. The update document contains the modifications to apply to all documents that match the filter.
Imagine that we want to update all the books in a collection that meet certain criteria, we can use the updateMany method to do this. Here's one document from the books collection. It includes information about a single book, including fields like underscore, id, title, publish date, status, and authors. We'll use updateMany to update all documents that were published before 2019 to have a status of legacy. First, let's examine the filter document. Here, we'll use the lt operator less than followed by the date January 1, 2019, because we want books that were published before 2019. Any documents that match this filter will get updated.
Then we need to tell MongoDB how to update the documents that match the filter. In the update document, we use the set operator to update the value of the status field to legacy. Now we can run the updateMany method on the books collection. The output shows that our update was successful because the matched count and modified count are both the same. Pretty useful, right? Now that you know how to use updateMany, let's go over when to use it. It's important to note that updateMany is not an all-or-nothing operation.
By this, we mean that in the rare instance where the operation fails, updateMany will not roll back the updates, so only some documents may be updated. If this happens, you need to run updateMany again to update the remaining documents. UpdateMany also lacks isolation, which means that updates will be visible as soon as they're performed. Because of this, updateMany is not appropriate for some use cases that may be essential for business requirements, such as financial transactions. Let's recap what you learned in this video. In MongoDB you can update multiple documents with updateMany. This method accepts a filter document, an update document, and an options object.
It returns an output message that shows the number of matched and modified documents. When the operation fails, updateMany does not roll back the updates if all documents aren't updated. Running updateMany again will complete the multi-document update. Overall, updateMany is a convenient and efficient way to update multiple documents in a collection.
```

</details>
