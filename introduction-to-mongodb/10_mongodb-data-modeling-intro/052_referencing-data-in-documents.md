# Referencing Data in Documents

- **Course:** Introduction To Mongodb
- **Module 10:** MongoDB Data Modeling Intro
- **Lecture #:** 52
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/krPhS/referencing-data-in-documents
- **Extracted:** 2026-08-11 10:00:58

---

Welcome, in this video, you'll learn how to model your data by using references. Before we begin, let's recap our key principle of data modeling with MongoDB. Data that is accessed together should be stored together. This means that you are storing your related data in a single document.

But there are times when you might want to store related information in separate documents, or maybe even in separate collections. When we want to store data in two different collections but also ensure it's clear that those collections are related, we can use references. References save the _id field of one document in another document as a link between the two. References are simple and sufficient for most use cases.

Using references is sometimes called linking or data normalization. Let's go through an example. This is a fairly simple document containing information about a student who is taking multiple courses. The course_id is our reference.

Referencing avoids duplication of data and in most cases, results in smaller documents. However, with reference data, you'll need to query data from multiple documents. This can cost extra resources and impact read performance. Use this guide which can be found in the lecture notes to help you decide whether to use embedding or referencing.

Great work. Now you understand how to use references in your MongoDB documents.


<details><summary>Timestamped transcript</summary>

```
Welcome, in this video, you'll learn how to model your data by using references. Before we begin, let's recap our key principle of data modeling with MongoDB. Data that is accessed together should be stored together. This means that you are storing your related data in a single document. But there are times when you might want to store related information in separate documents, or maybe even in separate collections. When we want to store data in two different collections but also ensure it's clear that those collections are related, we can use references. References save the _id field of one document in another document as a link between the two.
References are simple and sufficient for most use cases. Using references is sometimes called linking or data normalization. Let's go through an example. This is a fairly simple document containing information about a student who is taking multiple courses. The course_id is our reference. Referencing avoids duplication of data and in most cases, results in smaller documents. However, with reference data, you'll need to query data from multiple documents.
This can cost extra resources and impact read performance. Use this guide which can be found in the lecture notes to help you decide whether to use embedding or referencing. Great work. Now you understand how to use references in your MongoDB documents.
```

</details>
