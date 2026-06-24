# Comparison functions

- **Course:** Database Structures And Management With
- **Module 3:** Functions and MySQL stored procedures
- **Lecture #:** 27
- **URL:** https://www.coursera.org/learn/database-structures-and-management-with-mysql/lecture/hspZR/comparison-functions
- **Extracted:** 2026-06-22 19:41:21

---

M&G are approaching the end of their business year and need to extract sales revenue data for each item in their inventory. They can extract this data using comparison functions. Over the next few minutes, you'll explore the concept of comparison functions. By the end of this video, you'll be able to identify common MySQL comparison functions and explain how these functions are used to process and manipulate data in a MySQL database.

What do database engineers mean by the term comparison functions? MySQL comparison functions allow you to compare values within a database. For example, the function can be used to determine the highest, lowest, and other values. A benefit of comparison functions is that they can be used with a wide range of values, including numerical, strings, and characters.

Here's a few examples of MySQL comparison functions. The GREATEST function is used to find the highest value, LEAST determines the lowest value, and ISNULL is used as an alternative to the equals operator to test if a value is null. To demonstrate the syntax, let's identify the highest and lowest values from a table that contains numerical values only. The syntax begins with a SELECT command, followed by the name of required column.

Often, this is the column that holds the table's primary key or identifying attribute. Next, type the GREATEST function, followed by parenthesis containing the names of the columns you need to compare. Then use the AS keyword with a column alias of highest to ensure SQL returns the required values in a new table under this column. Next, utilize the LEAST function in the same manner.

Finally, identify the table to be queried. For example, M&G can use the greatest and least syntax to extract sales revenue data. They can target the last four business quarters and deliver the highest and lowest values from each. You'll find out more about how M&G can do this in a few moments.

For now, let's look at the syntax for the final comparison operator, ISNULL. ISNULL is often used with a SELECT command, followed by the name of the required column. Then a FROM keyword is used to identify the required table. An ISNULL function can also be used with a WHERE clause.

The clause calls the ISNULL function and identifies the column it must pass through. Now that you're familiar with the syntax of comparison functions, let's take a few moments to find out how they're used in the M&G database. As you learned earlier, M&G require data on their sales revenue for each item in their inventory for the last four business quarters. The sales revenue data is contained in the sales revenue table.

The table has five columns. One column called ItemID, which identifies each item in the inventory and then individual column for each quarter. M&G first need to identify the highest and lowest revenue each item brought in over the past four quarters. You can have them by using the greatest and least comparison functions, just like the syntax example from earlier.

Start with a SELECT command and list ItemID as the first column, then to identify the items that brought in the highest revenue call the GREATEST function and pass the four business quarter columns as arguments, then create the alias highest. Write a similar line of syntax for the LEAST function and assign it the alias of lowest. Finally, use the FROM keyword to target the sales revenue table. Once executed, the queries output presents the highest and lowest sales revenue values for each item over the last four business quarters.

For example, the item with the ID of one was worth $138,000 to m and g at its peak and 60,000 during its lowest sales period. M&G need to determine which of their most recent orders are yet to be delivered. The delivery data is held in the mg order table. The table contains seven columns.

OrderID, ItemID, Quantity, Cost, OrderDate, DeliveryDate, and OrderStatus. The DeliveryDate column is your primary concern here. All orders yet to be delivered have a NULL value within this column. You can use the ISNULL function on this column with the WHERE clause to filter these orders.

Begin by writing the SELECT statement, as usual, followed by an asterisk, then use a FROM keyword to target the table, finally, write a WHERE clause and call the ISNULL function to pass through the DeliveryDate column. Once executed, the query returns a value of one. This is a true value for all records that have a NULL value for the DeliveryDate column. M&G now have the required sales data, and you should now be able to use comparison functions in a MySQL database.

Great work.
