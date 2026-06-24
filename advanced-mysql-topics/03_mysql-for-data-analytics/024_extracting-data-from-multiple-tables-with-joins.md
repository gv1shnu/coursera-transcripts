# Extracting data from multiple tables with JOINS

- **Course:** Advanced Mysql
- **Module 3:** MySQL for Data Analytics
- **Lecture #:** 24
- **URL:** https://www.coursera.org/learn/advanced-mysql-topics/lecture/f6sfh/extracting-data-from-multiple-tables-with-joins
- **Extracted:** 2026-06-22 20:03:45

---

At this stage of the module, you should now be familiar with the data analysis process and how the results can inform data analytics. Now let's look at an example of how to perform data analysis in MySQL by querying multiple tables using JOINS. Lucky Shrub need to identify all clients who bought 10 items or more from a specific product line so that they can send them a special offer to make more purchases. The clients must have made their purchases after September 5th, 2020 and there must be 50 units or more of the product currently available in stock so that all special offers can be redeemed.

There are three tables in the database that contain the required data. The orders table with information on each order, the clients table which contains key information about each client and the products table which holds the data on all products in the store. You can help Lucky Shrub to query these tables by using an inner joint to target the following data. The client ID and contact number columns from the clients table, the order ID quantity and date columns from the orders table and the number of items column from the products table.

Let's get started. Begin with a SELECT statement then use dot notation to identify the required columns from each table. Next use an as keyword to create an alias for the product tables, number of items column. Rename it as items in stock then target the clients table with a from keyword and use the inner join clause to join it to the orders and products tables within a pair of parentheses.

The first join is created between the clients and orders table using the client ID column which exists in both tables. The second joint is created between the orders and products tables using their respective product ID columns. Next add a where clause and parentheses. Within the parentheses, state the following, customers must have purchased 10 or more units of the item.

All purchases must have been made after the September 5th, 2020 and there must be at least 50 units of the item currently in stock. Finally click Enter to execute the query. MySQL extracts the required data from the tables and displays it on screen. You have now performed data analysis on three tables within the Lucky Shrub database.

And through data analytics, you can use this data to identify clients that you can send special offers to. Great work.
