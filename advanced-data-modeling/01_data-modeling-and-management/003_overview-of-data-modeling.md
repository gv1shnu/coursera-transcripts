# Overview of data modeling

- **Course:** Advanced Data Modeling
- **Module 1:** Data Modeling and Management
- **Lecture #:** 3
- **URL:** https://www.coursera.org/learn/advanced-data-modeling/lecture/0dDnH/overview-of-data-modeling
- **Extracted:** 2026-06-22 20:09:52

---

When developing a database system, you need to make sure that it operates efficiently and that you can extract information from it quickly. The best way to create such a system is to first design a data model. With a data model, you can plan how data is stored and accessed within your database before you create the database system. In this video, you'll explore the concept of data modeling and review different levels of data models.

The jewelry store Mangeta and Gallo or M&G, are in the process of designing and building a database system to store data on customers, products, and orders. But their current design is very inefficient. However, if M&G first focuses on creating a suitable database model, then they can design a more simplified and logical database system. Explore the basics of database modeling, then see if you can assist M&G.

Let's begin with the term data modeling. A data model provides a visual representation of data elements and shows how they relate to one another. In other words, it demonstrates how your database system is structured. This structure helps you to understand how data is stored, accessed, updated, and queried within the database.

It also ensures a consistent structure and high-quality data. Data modeling is used to develop all kinds of databases, particularly entity relational databases. These databases are planned with the use of an entity relationship diagram. There are three different levels of data modeling, conceptual data models, logical data models, and physical data models.

Let's take a few moments to explore these different types. You might already be familiar with conceptual data models from previous courses. A conceptual data model consists of high abstract level of data elements called entities. The relationship between the data elements or entities, links related records of data within your database system.

The purpose of a conceptual model is to present a high level overview of the database system through a visual representation of the entities it contains and their relationship to one another. M&G can make use of a conceptual data model to create their database system. They can present their customers, products, and orders as entities, then document how these entities are related. The conceptual model provides the basis for the logical data model.

Again, you should have a basic familiarity with examples of a logical data model from previous courses. The logical data model builds on the conceptual model by providing a more detailed overview of the entities in their respective relationships. It identifies the attributes of each entity, defines the primary keys, and specifies the foreign keys. M&G can build on their conceptual data model by using it to create a logical data model.

Their logical data model must include all attributes required for each entity. Like a list of the attributes each entity contains. It then needs to define which of these columns serve as the primary key for each table. For example, the client ID column is the primary key for the client's table.

M&G's logical data model also specifies the foreign keys they're using to create relationships between the tables. In the current model, the client table is connected to the orders table through the client ID foreign key. A physical data model is used to create the internal SQL schema of the database, which is implemented in the database management system. The physical data model must outline features like the datatypes, constraints, and attributes.

For example, M&G need to define a specific datatype for each attribute, like varchar for the full name attribute in the client's table, or integer for the contact number attribute. They also need to apply relevant constraints. They can impose a constraint of not NULL for each column in the client's table to make sure that each one contains data. There are also a range of tools available to generate and execute the internal schema of a physical data model.

You'll cover these tools in later lessons. You should now be familiar with the basics of data modeling and the importance of the role that it plays in the development of a database system. You should also be able to differentiate between different levels of data models and explain how each one contributes to the creation of a database system.
