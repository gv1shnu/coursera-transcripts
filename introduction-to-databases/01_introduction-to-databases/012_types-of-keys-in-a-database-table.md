# Types of keys in a database table

- **Course:** Introduction To Databases
- **Module 1:** Introduction to Databases
- **Lecture #:** 12
- **URL:** https://www.coursera.org/learn/introduction-to-databases/lecture/buXLd/types-of-keys-in-a-database-table
- **Extracted:** 2026-06-22 16:12:40

---

at this stage of the course, you're probably familiar with the relational database model, but to fully understand how a relational database model works, you first need to understand how tables within a database are related. Essentially, relationships are established between tables with the use of keys. By the end of this video, you'll be able to identify the main keys used in tables in a relational database and explain the relationship between keys in a table. The relational database model is based on two main concepts, entities which are defined as tables and relations that connect to related tables.

To realize how this model works, you need to understand the different key attributes that exist in the relational database to demonstrate. Let's use the example of a sports competition that uses three tables to keep track of the league. The league table, the teams table and the points table. Each table has relevant columns where each column represents an attribute of the table entity.

The league table keeps track of each team's position in the league, their name and the state they represent. The team's table tracks the team name, the team captain and the team coach, and the points table records the team's position in the league, the team's name and how many points the team has this season. Notice that the team's table includes team name, which also belongs to the league table. These attributes could be of a simple attribute type that can hold a single value, for example, in a table of staff members in a college, each staff name attribute as a single value in each row.

Or they could also have a multi value attribute that can have multiple values like a list of subjects taught. However multi value attributes should be avoided in relational database design. You'll learn more about this concept later in the course. Let's use the example of the staff table to explore some examples of attribute keys.

Let's begin with the key attribute. This is a value used to uniquely identify an individual record of data in a table. For example in the staff table the key attribute is staff I. D.

This attribute has unique value in each row of the table so it's the perfect way to uniquely identify each record of data in a relational database there are a range of different types of key attributes. There's also the candidate key attributes. This is any attribute that contains a unique value in each row of the table. In the case of the staff table, both the staff I.

D. And contact numbers are examples of candidate keys. Each has a new unique value in each role. The other columns can contain repeated information so they're designated as non key attributes.

A composite key is a key that is composed of two or more attributes to form a unique value in each new role in the staff table. An example of a composite key is a combination of the staff name and staff title, assuming that there isn't another instance of the same combination elsewhere on the table. A composite key is usually considered when a single attribute key can't be identified, A relational database must also contain a primary key which you should already be familiar with in the staff table. The staff idea is the primary key.

An alternate key also known as the secondary key is a candidate key that was not selected to be the primary key. Just like a primary key. It's a column that contains a unique value in each field. For the staff table, the contact number is a secondary key on each roll and finally there's a foreign key.

The foreign key is an attribute on the table that references a unique key in another table. Typically a foreign key reference is the primary key of another table. For example, the staff I. D.

Might also be a foreign key in one or more tables within the college database. The relationship between primary and foreign keys will be discussed in more detail At a later point in this course, you're now familiar with the different types of keys in a relational database
