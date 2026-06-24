# Emulating the Full Outer JOIN in MySQL

- **Course:** Advanced Mysql
- **Module 3:** MySQL for Data Analytics
- **Lecture #:** 23
- **URL:** https://www.coursera.org/learn/advanced-mysql-topics/lecture/DLVeS/emulating-the-full-outer-join-in-mysql
- **Extracted:** 2026-06-22 20:03:35

---

When analyzing data, there may be times you need to extract all records from two separate tables. You could use a join, but this would just return matching records. Sometimes you'll also need records that don't match, so the solution is to emulate a FULL OUTER JOIN. This method extracts all records, even those that don't match.

In this video, you'll learn how to emulate the FULL OUTER JOIN or FULL JOIN in MySQL to extract data from tables. Lucky Shrub need a list of all their new orders and the clients who placed them. They also need the data of clients who didn't place orders. This data is stored in two tables, clients and orders.

MySQL supports INNER, LEFT, and RIGHT JOINS, but these won't return the required data from both tables. Lucky Shrub need to emulate a FULL JOIN to extract this data. You can help Lucky Shrub to complete this task. But first, let's find out more about what a FULL JOIN is and how it works.

In SQL, a FULL OUTER JOIN returns all records from a left and a right table when it identifies a match between the two. This includes records that match and those that don't. However, MySQL doesn't support the FULL OUTER JOIN, so you need to emulate it using a combination of the LEFT JOIN and the RIGHT JOIN. You also need to use the UNION ALL operator to return duplicate records should they exist.

Alternatively, you could use the UNION operator to retrieve unique records only. Let's take a few moments to explore the syntax for these methods. Here's how to emulate a FULL OUTER JOIN using a UNION ALL operator. First, type SELECT command, followed by the names of the columns that you require.

Then use a FROM clause to target the first table, which is your left table. Next, use a LEFT JOIN clause to join the first table with the second table, the right table. Then use an ON keyword and dot notation to equate the matching columns between the two tables. Now that you've scripted the LEFT JOIN you need to create the RIGHT JOIN.

But you also need to combine these JOINS using a method that returns all duplicate records. It's at this point in your syntax that you can add the UNION ALL operator. Once you've added the operator, create the RIGHT JOIN. As you should already know, the syntax is almost the same as the LEFT JOIN statement.

The key difference is that you must use a RIGHT JOIN clause. When executed, the UNION ALL statement returns all duplicate records should any exist. But what if you only want unique records to retrieve unique records only, you can use the UNION operator. The syntax is largely the same.

You need to script a RIGHT JOIN and a LEFT JOIN statement as before. But this time, place the UNION operator in-between the two statements instead of UNION ALL. Then when executed, the statement only returns unique records. For example, Lucky Shrub can use the UNION operator syntax to return unique records from the clients and orders tables.

Let's see if you can help Lucky Shrub to emulate a FULL OUTER JOIN using the UNION operator. As you learned earlier, Lucky Shrub need records of all new orders from the orders table and the records of the clients who placed these orders from the client stable. They also need the data of clients who didn't place orders. Start with a SELECT statement, then target the following required columns from the client's table using dot notation, client ID, full name, and contact number.

Then target the following columns from the orders table, order ID, cost, and date. Then use the FROM clause to identify clients as the left table. Join it to the orders table with a LEFT JOIN clause. The next step is to use the ON keyword to equate client ID as the matching column between both tables.

Then add the UNION operator so that the syntax retrieves unique records only. Now it's time to script the RIGHT JOIN statement. Again, the syntax is mostly the same as the LEFT JOIN statement. Just use a RIGHT JOIN clause instead of a LEFT JOIN one.

Finally, press Enter to execute the statement. The output shows all client IDs with their related order IDs. It also shows matching order IDs and client IDs, along with IDs that don't have a match. Lucky Shrub now have all the records that they require from their database and you should be familiar with how to emulate a FULL OUTER JOIN in MySQL using the UNION and UNION ALL operators.

Good work.
