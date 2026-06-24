# INNER JOIN

- **Course:** Database Structures And Management With
- **Module 1:** Intro to MySQL
- **Lecture #:** 8
- **URL:** https://www.coursera.org/learn/database-structures-and-management-with-mysql/lecture/nwIO5/inner-join
- **Extracted:** 2026-06-22 19:37:57

---

Lucky Shrub Gardening Center require information on orders recently made by their clients. This information is stored in two separate tables. The clients table and the orders table. But there must be a more efficient way to review this information that doesn't involve using two tables at the same time, right?

Thankfully, Lucky Shrub can use the Inner Join clause to return records of data based on a common column with matching values in both tables. In this video, you'll help Lucky Shrub to complete this task. And by the end of this video, you'll be able to apply the Inner Join concept in MySQL, a new sequel aliases to create temporary column names. As you're probably aware by now, databases normally have more than one table.

In fact, database normalization rules dictate that related data should be held in separate tables. So let's begin with a quick review of the two tables. The clients table has four columns, client ID, full name, contact number and address. And the orders table has five columns order ID, client ID, product ID, quantity and cost.

The first task is to identify the full names of all clients who made orders. You can do this using the Inner Join clause in a SQL Select statement. The statement begins with the SELECT command. This is then followed by the column full name attached to the clients table separated by a dot.

This queries data from the full name column of the clients table. Then the FROM keyword is used to target the clients table. Next, the INNER JOIN clause creates a new row of data for each matching record. In other words, where the client ID in the client's table matches the client ID in the orders table and the equal operator ensures the matching condition must be met.

Remember that it's important to specify the table name of each column when you are dealing with multiple tables in the same statement. This is especially important when the column name is used in more than one of the query tables. For example, client ID exists in both the clients and the order tables. Press enter to execute the query.

The output results set lists the full names for all clients that have made orders. This example just extracts a list of names. We can also query other information from both tables. For example, you can display the column names with more user friendly labels if required.

For instance, you can take the client ID, full name and contact number of columns from the clients table and create a JOIN with the product ID, quantity and total cost column from the orders table. You can do this with the following SQL statement. Start with a SELECT command that selects the required columns from the clients table, then use the AS keyword after each column to create an alias. In other words, create a new name for each column, then do the same for the required columns on the orders table.

So in this statement, each column is attached to the related table name and the alias technique is used to create new names for each column. Click enter to execute the query. The result set is a table with all required data related to the four matching clients, ID's. The results set is a table with all required data related to the four matching clients ID's, Cl 1, Cl2, Cl 4, and Cl 6 as shown in the output table.

In this video, you explored how to work with the INNER JOIN clause in MySQL to query data from two tables in the database. Also, you learned how to use an alias to create temporary column names that have more readable labels. Lucky Shrub can now review the data they need using a more efficient table, thanks to the INNER JOIN clause. And you should now be able to apply the inner joint concept in MySQL and use SQL aliases to create temporary column names.

Great work.
