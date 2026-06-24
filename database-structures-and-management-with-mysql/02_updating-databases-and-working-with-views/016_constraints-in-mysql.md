# Constraints in MySQL

- **Course:** Database Structures And Management With
- **Module 2:** Updating databases and working with views
- **Lecture #:** 16
- **URL:** https://www.coursera.org/learn/database-structures-and-management-with-mysql/lecture/05ziv/constraints-in-mysql
- **Extracted:** 2026-06-22 19:39:23

---

Little Lemon Restaurant have built two new tables in their database that allow customers to create accounts and register bookings. To make sure that these tables work is required, the restaurant has set up constraints which ensure that the tables only accept valid data. Over the next few minutes, you'll learn about the concept of constraints in MySQL by exploring how Little Lemon have made use of them in their database. And by the end of this lesson, you'll be able to identify the main types of constraints and explain how they function and explain the MySQL on the lead cascade and on update cascade options.

Let's begin with an overview of what database engineers mean by the term constraints. When creating a table, you might decide that each column must hold a unique value in each row of the table like a phone number. You can enforce this rule using the unique constraint which prevents any violation of the rule whenever data is inserted or updated in your database. There are three main types of constraints in MySQL database, which can be used to enforce these rules.

Key constraints which apply rules to key types. Domain constraints, used to govern the values that can be stored for a specific column and referential integrity constraints, which established rules for referential keys. Let's take a few moments to explore each of these three MySQL constraint types and discover how they're used by Little Lemon in their database. As you learned in the previous course, all tables include different types of keys, like primary keys and foreign keys.

You can use constraints to establish rules for these keys. For example, the primary key constraint can be used to specify that one or more column values must always be unique and they cannot accept a null value. Little Lemons database contains a table called customers. This table records key data on customer bookings using the primary key constraint.

The table has three columns called, customer ID, full name and phone number. Customer ID is defined as the primary key which returns data on the tables unique records. Thanks to the primary key constraint, these columns values must always be unique and it can never accept no value. In other words, every row in the column must hold the customer ID and all customer ideas must be unique.

Next let's look at domain constraints, as you learned earlier, these are special rules defined for values that can be stored for a certain column. Little Lemons database contains a bookings table that records data on customer bookings. However, the restaurant can only facilitate a maximum of eight guests per booking. So they enact the SQL check constraint on the number of guests column.

This limits the value range that can be placed in the column, which means the table rejects any numeric values greater than eight. Finally, let's explore referential integrity constraints. You learned earlier that this type of constraint establishes rules for referential keys, but how exactly does this work? Basically, in a referential integrity constraint there are two types of tables, a referencing table that holds a primary key and a reference table that contains a foreign key.

The value of the foreign key column that exists in the referencing table must always exist in the referenced table. Otherwise, a connection can't be established between the two tables. To understand this better, let's explore the example of the related tables in Little Lemons database in the form of an entity relationship diagram. Little Lemons database includes two related tables.

The customers table that holds data on customers and the bookings table that records information on customers bookings with the restaurant. Each booking in the booking table must relate to a specific customer in the customers table. Otherwise, the restaurant can't identify who made the bookings. And this also means that each customer must already be registered in the customers table before they can make a booking in the bookings table.

The customer ID column in the bookings table is defined as the foreign key. This is the attribute that joins the two tables together and establishes dependency between them. This means that if a row of data is altered or deleted in the customers table, then this action destroys the related role of data in the bookings table. In other words, deleting a row of data from the customers table violates the referential integrity rule and this results in an error message from MySQL, warning that the action directly impacts on the bookings table.

So, how can you make the required changes to the bookings table without violating the referential integrity constraint? In this instance you can use the on the lead cascade option. This option automatically deletes the related rows of data from the bookings table. And if you want to update a primary key value in the customers table, you can use the on update cascade option to automatically update the related rose in the bookings table.

You'll discover more about these options in a later video. You should now be able to identify the main types of constraints and explain how they function. And you should also be able to explain the MySQL on delete cascade and on update cascade options. Well done.
