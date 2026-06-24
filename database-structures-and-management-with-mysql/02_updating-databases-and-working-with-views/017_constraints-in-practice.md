# Constraints in practice

- **Course:** Database Structures And Management With
- **Module 2:** Updating databases and working with views
- **Lecture #:** 17
- **URL:** https://www.coursera.org/learn/database-structures-and-management-with-mysql/lecture/Z1sxT/constraints-in-practice
- **Extracted:** 2026-06-22 19:39:33

---

Little Lemon restaurant need to build two tables in their database. That let customers create accounts and register bookings. They also need to apply constraints to the columns in these tables to ensure data consistency and integrity. Over the next few minutes, you'll help Little Lemon create these tables and apply the following common constraints.

Not Null, unique, check, and foreign key. By the end of this video, you'll be able to demonstrate how to apply these common constraints in a MySQL database table. The first table that must be created is costumers, which records customer details. The table requires the following constraints.

The Primary Key constraint on the customer ID column, the Not Null constraint on the full name column, and a unique constraint on the PhoneNumber column to ensure that each customer has a unique number. Let's get started. Begin with the create table command and call the table customers. Then add a pair of parenthesis.

Within the parenthesis, define the Customer ID column as Not Null as the Primary Key. This ensures that all IDs are unique in each row of the table and that the column does not accept a null or empty value. Next, add a FullName column with the constraint Not Null. Assign a value of VarChar with a character limit of 100.

Then declare the phone number column as Not Null unique. This ensures that it only accepts a unique number for each customer. Finally, execute the statement. Now let's view the output by writing and executing the following statement.

Show columns from costumers. This shows the customers table. The table contains all relevant constraints. The columns are defined with Not Null.

Two keys have been declared. The Customer ID column is the Primary Key, and the PhoneNumber column only accepts unique values. The next task is to apply referential integrity. This ensures that each customer can make a booking in the restaurant and that each booking must be assigned to a specific customer.

In other words, any Customer ID that exists in the bookings table must also exist in the customers table. Otherwise, it won't be possible to identify who made the bookings. When creating the bookings table, it's important to focus on the referential integrity constraint and the check constraint to limit the number of guests to a maximum of eight. Begin with a create table command, followed by bookings and parenthesis.

In the parenthesis, create the following columns. Booking ID, booking date, table number, number of guests and Customer ID. All columns are defined as Not Null to ensure that each one must accept a value. All columns are also assigned the integer value except Bookings date, which is assigned a date value.

The Booking ID column is defined as the Primary Key. The number of guests column is defined with a check constraint that specifies it's Not Null. Use a smaller than or equal to operator so that it can only accept a maximum of eight guests. Next, define the Customer ID column with the foreign key constraint.

Then use the references constraints, so the foreign key references the Customer ID column in the customers table. Now use on Delete and on Update Cascade options to delete and automatically update the related rows of data in the Bookings table. However, be aware that these actions depend on the Update and Delete operations taking place in the customers table. Click Enter to execute the statement.

To display the table structure type the following syntax, show columns from Bookings. The output set result shows all columns are assigned the required constraints and values. The Customer ID column is MUL. This means that it's not a unique key and multiple rows can have the same key value.

This makes sense because each customer might make multiple Bookings at the same or at different times. This code also joins the two tables and establishes dependencies between them. If you change or delete the Customer ID in the customers table, then you also update or delete the related record in the Bookings table. You should now be able to apply different types of constraints in MySQL databases to maintain data integrity and consistency.

Great work.
