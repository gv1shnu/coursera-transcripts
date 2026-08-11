# Updating MongoDB Documents by Using findAndModify()

- **Course:** Introduction To Mongodb
- **Module 5:** MongoDB CRUD Operations: Replace and Delete Documents
- **Lecture #:** 22
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/Fgzeu/updating-mongodb-documents-by-using-findandmodify
- **Extracted:** 2026-08-11 09:55:26

---

Welcome. In this video, you'll learn how to update and return the same document in MongoDB. We'll cover how and when to use the findAndModify method. We'll also explain how findAndModify is different from the updateOne method.

findAndModify is used to return the document that has just been updated. For example, imagine we're creating an app that tracks the number of users who download a podcast. One way to update and return the number of downloads is to use the updateOne and findOne methods. First, we would use updateOne to increment the downloads field, then we would use findOne to return the document by using the underscore ID.

The problem with this approach is that it makes two round trips to the server where findAndModify is only one. Additionally, if we make our update via updateOne, another user could modify the document before our findOne, and we will get a different version of the document. To prevent this, we can use findAndModify. This is a powerful method that guarantees the correct version of the document will be returned without another thread modifying the document before we're able to view it.

Let's take a look at an example of the document we want to modify. Notice the downloads field is currently set to 6012. Here we use findAndModify to increment the downloads field by one. This method accepts a document as an argument with several embedded document fields.

The fields we'll focus on are the query field which accepts a query document, the update fields, which accepts an update document, and the new fields which accepts a Boolean value. By default, the return document does not include the modifications made as part of the update. Set the new option to true so that the modified document is returned. In this example, the query field is set to the underscore ID for the podcast document.

The update field is set to a document that includes the modification we want to make to the downloads field, and the new option is set to true, which will return the updated document shown here. Now, let's recap what you've learned in this video. We use the findAndModify method to update and return the document that matches our query. We set the new option to true to make sure the new version of the updated document is returned.

The best approach to updating documents depends on the situation, but using findAndModify guarantees that the exact document you've just updated will be returned.


<details><summary>Timestamped transcript</summary>

```
Welcome. In this video, you'll learn how to update and return the same document in MongoDB. We'll cover how and when to use the findAndModify method. We'll also explain how findAndModify is different from the updateOne method. findAndModify is used to return the document that has just been updated. For example, imagine we're creating an app that tracks the number of users who download a podcast. One way to update and return the number of downloads is to use the updateOne and findOne methods. First, we would use updateOne to increment the downloads field, then we would use findOne to return the document by using the underscore ID.
The problem with this approach is that it makes two round trips to the server where findAndModify is only one. Additionally, if we make our update via updateOne, another user could modify the document before our findOne, and we will get a different version of the document. To prevent this, we can use findAndModify. This is a powerful method that guarantees the correct version of the document will be returned without another thread modifying the document before we're able to view it. Let's take a look at an example of the document we want to modify. Notice the downloads field is currently set to 6012. Here we use findAndModify to increment the downloads field by one.
This method accepts a document as an argument with several embedded document fields. The fields we'll focus on are the query field which accepts a query document, the update fields, which accepts an update document, and the new fields which accepts a Boolean value. By default, the return document does not include the modifications made as part of the update. Set the new option to true so that the modified document is returned. In this example, the query field is set to the underscore ID for the podcast document. The update field is set to a document that includes the modification we want to make to the downloads field, and the new option is set to true, which will return the updated document shown here. Now, let's recap what you've learned in this video.
We use the findAndModify method to update and return the document that matches our query. We set the new option to true to make sure the new version of the updated document is returned. The best approach to updating documents depends on the situation, but using findAndModify guarantees that the exact document you've just updated will be returned.
```

</details>
