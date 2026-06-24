# JOINS

- **Course:** Database Structures And Management With
- **Module 1:** Intro to MySQL
- **Lecture #:** 7
- **URL:** https://www.coursera.org/learn/database-structures-and-management-with-mysql/lecture/4vYAK/joins
- **Extracted:** 2026-06-22 19:37:46

---

Lucky Shrub Gardening Center needs to gather information on their customers and the orders they've placed. But the records are held in three different tables. However, they can extract this information from their database using JOINs clause to join the required elements of these tables together. Over the next few minutes, you'll discover how the JOINs clause works, and by the end of this video, you'll be able to demonstrate an understanding of the JOIN concept in a database and describe the main types of JOINs in MySQL.

Let's take a closer look at the problem that Lucky Shrub has encountered with their database tables. Lucky Shrub needs to determine what products were ordered and which customers placed the orders. However, this information exists in three separate entities or tables: customers, orders, and products. So how can Lucky Shrub extract records from three different tables?

Before you can begin to assist Lucky Shrub, you first need to understand the concept of JOINs. The SQL JOIN clause is used to query data based on a common column between two target tables. For example, the customers and orders tables both contain a customer ID column, and the product ID column is a common column between the orders and products tables. These common columns can be used to join these tables together and extract the required records.

There are four types of JOIN used to combine tables. An INNER JOIN, which extracts or selects records of data that have matching values in both tables, and a LEFT JOIN that extracts or selects records of data from the left table and all matching records from the right table. The RIGHT JOIN which extracts or selects records of data from the right table, a matching record from the left table, and the Self JOIN in which a table is joined with itself to retrieve info that exists in the same table. Let's begin with a review of the INNER JOIN.

An INNER JOIN returns records of data that have matching values or columns in both the left and the right tables. This relationship between the two tables can be conceptualized in the format of a Venn diagram, as can all other joints. In terms of syntax, the left and right tables are identified as Table 1 and Table 2 respectively. Lucky Shrub need to identify the full names of all clients that placed orders with the business.

To complete this query, they need the client's table and the orders table. They can then create an INNER JOIN using the client ID column that exists in both tables. The output result reveals the records of all clients who placed orders. The client ID represents all records with matching IDs to be listed.

The syntax of an INNER JOIN begins with a select statement, which queries the left table and the column with the matching values. The FROM keyword is then added along with the name of the left table. Next is the INNER JOIN clause, followed by the name of the right table. Finally, the ON keyword is used to identify the INNER JOIN that the tables share.

Next, let's move on to review the LEFT JOIN. The LEFT JOIN returns all common records in a similar way to the INNER JOIN. In addition, it returns all available records of the common column from the left table, even if there isn't a match in the right table. Lucky Shrub can use the left join table to extract data from the clients and orders tables using the client ID values.

The JOIN locates four matching records between the two tables and places them in the common area of the Venn diagram. The LEFT JOIN syntax begins with a select statement in which the required columns from Table 1 are identified. The AS keyword is then used to create an alias for each column. The FROM keyword is used to identify the left table, which is the one that must be queried.

Once again, the AS keyword is used to create an alias for this table. The LEFT JOIN clause is then used to join Table 2 and assign an alias. Finally, the ON keyword equates the matching columns between the two tables. Now, let's review an example of the RIGHT JOIN.

The RIGHT JOIN returns all records from the right and left tables, but with the right table as the main target table. For example, Lucky Shrub can use the RIGHT JOIN to extract records of data from the orders and products table based on the product ID values. This lists all products from the products table joined with the matching related orders details in the left table. The RIGHT JOIN syntax is very similar to the LEFT JOIN.

The only difference is that the RIGHT JOIN clause is used to extract records of data. Finally, there's the SELF JOIN. A SELF JOIN is a special case in which a table must be joined with itself. In other words, one table is treated as two in order to extract specific information from either the LEFT, RIGHT or INNER JOIN.

In the case of Lucky Shrub, the business holds records of all staff members in the staff table. The table contains records on sales floor, employees and line managers. Lucky Shrub can treat the table as two tables to determine who is a line manager and who is the sales floor employee. A SELF JOIN syntax is written as a select statement, in which an alias is created for the common column in Table 2.

You've encountered a lot of information in this video, particularly in terms of syntax. Don't worry if it doesn't all make sense at this stage. In the videos that follow, you'll learn how to create each type of JOIN in more detail. But for now, you should be able to demonstrate an understanding of the JOIN concept in a database and describe the main types of JOINs in MySQL.

Well done.
