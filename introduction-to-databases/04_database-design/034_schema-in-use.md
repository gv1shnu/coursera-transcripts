# Schema in use

- **Course:** Introduction To Databases
- **Module 4:** Database design
- **Lecture #:** 34
- **URL:** https://www.coursera.org/learn/introduction-to-databases/lecture/Ia7be/schema-in-use
- **Extracted:** 2026-06-22 16:16:34

---

By the end of this video you'll know how to create a simple database schema. Using SQL you'll do this by building the schema for a shopping cart database consisting of three tables. Let's start by creating a new database called shopping cart TB. First I type the create database keyword followed by the name shopping cart TB.

Then I run the statement, the shopping cart DB. Database appears in the left hand Explorer. Now it can create the tables inside this database. First I need to create the customer table which stores the following information on each customer customer ID.

Name, address, email and phone number to create this table. I used to create table keyword and then I type customer followed by parentheses in the parentheses I specify the fields and their data types as follows. The customer ID. Data type is integer while the others are bar char.

I give the name and email fields a character limit of 100. I assign a character limit of 255 for address And I assign the limit of 10 characters for phone. Also note that I've used the primary key keyword on the customer ID. Column.

This designates that field as the primary key of the table. A role you'll learn more about soon. Next is the product table which stores the product ID. Name, price and description.

I can specify this table as follows. The product ID. has the integer data type. The name is of our char with a 100 character limit.

The price has a numeric type with parameters of eight and 2. The description is var char with a 255 character limit. And the product ID. Is set as the primary key within this table.

And finally there's the cart order table which holds the order ID. Customer ID. Product ID. Quantity, order, date and status.

This table is set up as follows the order ID, customer ID. Product ID and quantity are all integer types. Order, date is date and status is var char with a 100 character limit. Order ID.

Is the primary key here. However, this table also introduces something new in the form of two foreign keys. Before moving forward, let's quickly discuss what primary and foreign keys are. You may have noticed that the cart order table contains the customer ID.

And product ID fields. These same fields are also found in the other two tables. This is because these fields in the cart order table are directly linked to the same fields in the corresponding tables. To establish this relationship, each table must contain a primary key.

The referencing table then uses foreign keys that pointed to the external source table or the referenced table. You learn more about primary and foreign keys in greater detail in a later lesson. But for now let's return to the shopping cart database example. All primary keys have been set up.

So the foreign keys for the card order table. Come next I create the first one by using the foreign key key word, along with the customer ID. Column name to link it to the customer ID field. In the customer table, I then used a references keyword followed by the source table name, customer and then customer ID.

And parenthesis creating a foreign key for product ideas similar but with product and product ideas references. So I used the foreign key keyword and name it product ID. I then reference it in the product source table. Product and then product ID.

Then I execute these statements and the tables appear nested beneath shopping ID. In the left hand Explorer. In this video you learned the steps for creating a simple database schema using SQL. The same process applies for both small and large scale databases.
