# LEFT and RIGHT JOIN

- **Course:** Database Structures And Management With
- **Module 1:** Intro to MySQL
- **Lecture #:** 9
- **URL:** https://www.coursera.org/learn/database-structures-and-management-with-mysql/lecture/MVWmQ/left-and-right-join
- **Extracted:** 2026-06-22 19:38:07

---

Looking shrub need to review date on orders made by their clients. This data exists in two separate tables, clients and orders. Lucky stroke can query data from both tables using the left and right join clauses in MySQL. These clauses will work because both tables share several closely connected columns.

In this video, you'll help lucky SRO abuse the left and the right join clauses. By the end of this video, you'll be able to demonstrate how to apply a left join and right join in MySQL and utilize aliases to create temporary columns and table names. Let's quickly review the two tables before creating the query. The client's table contains four columns, customer ID, full name, contact number, and address.

The orders table contains five columns. Order ID, client ID, product ID, quantity, and cost. The first step is to create a query for the client ID and client-named columns within the client's table, which is the left table. Then you must create a join with the following columns from the order table, the right table, Order ID, quantity, and cost.

You can use the left join clause in the SQL statement to complete this task. To start, use the select command to retrieve data followed by the column client ID and full name attached to the client's table separated by a dot. This syntax retrieves data from the two columns from the client's table. This data then joins the order ID, quantity, and cost columns from the orders table.

As you're probably already aware, it's important to specify the table name of each column when dealing with multiple tables in the same statement. This is especially important when the column name is used in more than one of the query tables. For example, the client ID column exists in both the clients and orders tables. You can also use this SQL as keyword to create suitable aliases for the column names when displayed in the output results set.

You can use the as keyword to create aliases for the two tables as follows. C for clients and O for orders. This now means that instead of repeatedly typing clients to specify the column source table, you can just use C and instead of using the word orders you can write O. In this statement, the left join clause creates a new row of data for each matching records from the left table, the client's table.

It does this even if there are no matching records in the orders table, which is the right table. For example, the clients with IDs Cl3 and Cl5 IL-5 yet to place any orders. This means that no values will be inserted for related columns from the right table. Finally, press Enter to execute the query.

The output result table contains several known values for the clients with IDs of Cl3 and Cl5. This is because they have not yet made any orders. Next, let's create a similar query using the right join concept. You can use similar syntax to the previous query.

Just replace the left keyword with the right keyword. In this statement, clients represents the left table and the orders represents the right table. The right join clause extracts data from both tables based on the client ID values. Just like the previous example.

Executing this query should return all requested information from the orders table, right table joined by the requested information from the client's table, left table based on the common column client ID. Press "Enter" to run the query and create the output. The output shows that the right join has returned all records from the right or orders table where a client has made an order. That extracted the matching records from the left or clients table based on the client ID values.

No, no-values were printed in the output result table. This is because all clients who made orders already exist in the client's table. Looking shrub now have the order and client information they need. And you should now be able to demonstrate how to apply a left join and right join in MySQL and utilize aliases to create temporary columns and table names.

Good work.
