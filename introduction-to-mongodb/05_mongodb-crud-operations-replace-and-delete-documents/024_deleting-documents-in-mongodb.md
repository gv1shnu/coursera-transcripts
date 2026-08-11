# Deleting Documents in MongoDB

- **Course:** Introduction To Mongodb
- **Module 5:** MongoDB CRUD Operations: Replace and Delete Documents
- **Lecture #:** 24
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/rDRkL/deleting-documents-in-mongodb
- **Extracted:** 2026-08-11 09:55:47

---

Hi folks. In this video, you'll learn how to delete documents in MongoDB by using deleteOne and deleteMany. Let's jump right into it. Imagine that you're working with a database that contains information about various podcasts.

There's a single document for each podcast that gets added to the collection, which is called podcasts. But there's a problem. At some point, a duplicate document for a podcast was inserted accidentally. We need to delete the duplicate.

To achieve this, first we'll use find to determine which document to delete, and then we'll use the deleteOne method. Furthermore, your manager has asked you to remove all podcasts with a category of crime. First, we provide a filter document to the find method that contains the uploaded date of the duplicate document which was provided to us by our manager. The date we were given is April 28th, 2020.

In the shell we'll use the ISODate wrapper to specify the date. Running this command returns the duplicate document. Now we'll use the _id value to write the deleteOne command. The deleteOne method accepts a filter document and options object.

However, we won't be using the options object in this example. In the filter document we'll put the _id value of the duplicate. After running this command, we receive a message that our command was acknowledged and that one document was deleted. Perfect.

Now that you know how to deleteOne document, let's go over the process for deleting more than one. We'll delete all podcasts that have a category of crime. First, we'll run a find for podcasts in the crime category, which returns three results. Now we'll use deleteMany to delete all three podcasts.

We'll pass in a filter document that contains the field category in a value of crime. Like deleteOne, the deleteMany method accepts an options object, but it's not required for this example. When we run this command, we get output showing that three documents were deleted, which is what we want. Now, let's recap what you learned in this video.

To delete one document, use deleteOne by passing in a filter document and an options object if needed. Note that the options object is not required for this query. To delete more than one document, use deleteMany, which also accepts a filter and an options object. Congratulations on working with the deleteOne and deleteMany methods in MongoDB.


<details><summary>Timestamped transcript</summary>

```
Hi folks. In this video, you'll learn how to delete documents in MongoDB by using deleteOne and deleteMany. Let's jump right into it. Imagine that you're working with a database that contains information about various podcasts. There's a single document for each podcast that gets added to the collection, which is called podcasts. But there's a problem. At some point, a duplicate document for a podcast was inserted accidentally.
We need to delete the duplicate. To achieve this, first we'll use find to determine which document to delete, and then we'll use the deleteOne method. Furthermore, your manager has asked you to remove all podcasts with a category of crime. First, we provide a filter document to the find method that contains the uploaded date of the duplicate document which was provided to us by our manager. The date we were given is April 28th, 2020. In the shell we'll use the ISODate wrapper to specify the date. Running this command returns the duplicate document.
Now we'll use the _id value to write the deleteOne command. The deleteOne method accepts a filter document and options object. However, we won't be using the options object in this example. In the filter document we'll put the _id value of the duplicate. After running this command, we receive a message that our command was acknowledged and that one document was deleted. Perfect. Now that you know how to deleteOne document, let's go over the process for deleting more than one.
We'll delete all podcasts that have a category of crime. First, we'll run a find for podcasts in the crime category, which returns three results. Now we'll use deleteMany to delete all three podcasts. We'll pass in a filter document that contains the field category in a value of crime. Like deleteOne, the deleteMany method accepts an options object, but it's not required for this example. When we run this command, we get output showing that three documents were deleted, which is what we want. Now, let's recap what you learned in this video.
To delete one document, use deleteOne by passing in a filter document and an options object if needed. Note that the options object is not required for this query. To delete more than one document, use deleteMany, which also accepts a filter and an options object. Congratulations on working with the deleteOne and deleteMany methods in MongoDB.
```

</details>
