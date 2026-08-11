# Introduction to Data Modeling

- **Course:** Introduction To Mongodb
- **Module 10:** MongoDB Data Modeling Intro
- **Lecture #:** 48
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/h5CNS/introduction-to-data-modeling
- **Extracted:** 2026-08-11 10:00:15

---

Welcome to this video on data modeling in this video, you'll learn the purpose of proper data modeling, the differences between the traditional relational data model and the document model, and the advantages of the document model. First, data modeling is the process of defining how data is stored and the relationships that exist among different entities in your data. We refer to the organization of data inside a database as a schema. To develop your schema, instead of thinking about your database, we recommend thinking about your application instead.

Consider questions such as what does my application do? What data will I store, how will users access this data? What data will be most valuable to me? Asking these questions will help you describe your tasks as well as those of your users or customers.

It will also help you describe what your data looks like and the relationships among the data, the tooling you plan to have, and the kind of access patterns that might emerge. This is how we build a proper data model let's also talk about why. What's the purpose of having a good data model? Having a good data model has many benefits.

It can make it easier to manage your data, make queries more efficient, use less memory and CPU, and even reduce cost. As a general principle in MongoDB, data that is accessed together should be stored together. MongoDB implements a flexible document data model. This means that collections do not enforce any document structure by default.

That means that documents, even those in the same collection, can have different structures. Each document in MongoDB can be different, which is known as polymorphism. This doesn't mean that the MongoDB document model is schema less we consider MongoDB to be schema flexible. That is, you're encouraged to define a schema you can use schema validation, and you can store any kind of data in MongoDB.

You can even store documents that have other documents that are nested or embedded. This embedded document model enables us to build complex relationships among our data. If it makes sense for your application, you can normalize your data by using references. The key principle here is how your application will reference or use the data, rather than how it's stored in the database.

This is the opposite of how data is modeled in a relational database. In a relational database, we get the data requirements, model the data, and then pass the data along to the developer to wrangle. In MongoDB, we start with the application requirements and ask how the user will interact with our application then we model our data accordingly. In MongoDB, you're not constrained to one way of storing data.

You can choose to normalize some data, embed other data that will be accessed together, or use any combination of storage methods that makes sense for your application. The purpose of the data modeling exercise is to understand your data so that it can be stored, queried, and used resources optimally. This will help ensure that your queries and your application are more performant. Once you've considered your users and how your application data will be used, it's time to begin modeling relationships.


<details><summary>Timestamped transcript</summary>

```
Welcome to this video on data modeling in this video, you'll learn the purpose of proper data modeling, the differences between the traditional relational data model and the document model, and the advantages of the document model. First, data modeling is the process of defining how data is stored and the relationships that exist among different entities in your data. We refer to the organization of data inside a database as a schema. To develop your schema, instead of thinking about your database, we recommend thinking about your application instead. Consider questions such as what does my application do? What data will I store, how will users access this data? What data will be most valuable to me?
Asking these questions will help you describe your tasks as well as those of your users or customers. It will also help you describe what your data looks like and the relationships among the data, the tooling you plan to have, and the kind of access patterns that might emerge. This is how we build a proper data model let's also talk about why. What's the purpose of having a good data model? Having a good data model has many benefits. It can make it easier to manage your data, make queries more efficient, use less memory and CPU, and even reduce cost. As a general principle in MongoDB, data that is accessed together should be stored together.
MongoDB implements a flexible document data model. This means that collections do not enforce any document structure by default. That means that documents, even those in the same collection, can have different structures. Each document in MongoDB can be different, which is known as polymorphism. This doesn't mean that the MongoDB document model is schema less we consider MongoDB to be schema flexible. That is, you're encouraged to define a schema you can use schema validation, and you can store any kind of data in MongoDB. You can even store documents that have other documents that are nested or embedded.
This embedded document model enables us to build complex relationships among our data. If it makes sense for your application, you can normalize your data by using references. The key principle here is how your application will reference or use the data, rather than how it's stored in the database. This is the opposite of how data is modeled in a relational database. In a relational database, we get the data requirements, model the data, and then pass the data along to the developer to wrangle. In MongoDB, we start with the application requirements and ask how the user will interact with our application then we model our data accordingly. In MongoDB, you're not constrained to one way of storing data.
You can choose to normalize some data, embed other data that will be accessed together, or use any combination of storage methods that makes sense for your application. The purpose of the data modeling exercise is to understand your data so that it can be stored, queried, and used resources optimally. This will help ensure that your queries and your application are more performant. Once you've considered your users and how your application data will be used, it's time to begin modeling relationships.
```

</details>
