# Optimizing database SELECT statements in practice

- **Course:** Advanced Mysql
- **Module 2:** Database Optimization
- **Lecture #:** 13
- **URL:** https://www.coursera.org/learn/advanced-mysql-topics/lecture/JAFuG/optimizing-database-select-statements-in-practice
- **Extracted:** 2026-06-22 20:01:45

---

Lucky Shrub have received large numbers of orders from their clients and need to query this data quickly and efficiently using SELECT statements. They must make sure their queries are optimized so that MySQL can compile and execute them efficiently. First, the sales department needs to find out which orders are arriving on September 12th. They can write a SELECT query that uses the where clause and date underscore add function, but sorting through the data to calculate delivery dates using that date underscore add function in the where clause places a lot of extra load on the database.

A more efficient method is to generate a custom column in the orders table called expected delivery date. This column shows the expected date of each delivery. Now Lucky Shrub just need to scan this column for all values that match September 12th and they no longer need to use a function. The sales department's next task is to process an order for a customer with the surname of Ito.

First, they need to find the customer's details in the client's table in the database. One method is to use a SELECT statement that combines a leading wildcard with the like operator, but MySQL can't make use of an index when there's a leading wildcard. The solution is to add a new column to the client's table using an alter table statement and call it reverse full name. The reverse full name column contains the client names, but reversed.

In other words, the client's last name or surname is listed first, then their first name. You can run an update statement on the client's table to carry out this task. Next, use the create index syntax to create an index on the new column. Don't worry about the syntax for now.

You'll explore it in more detail in a later video. You can now make use of a trailing wildcard with the like operator on the reverse full name column to achieve the same result, and you can still use the index. Finally, the finance department need to report on all orders placed with the store. They can extract this information by targeting the product and orders tables in the database.

Usually, this task can be completed by using an outer join query. However, this type of query also returns records that don't match from both tables even though they're not required. A more efficient method of querying these tables is for Lucky Shrub to use an inner join that targets the shared product ID columns from both tables. This returns only the matching records.

It's a much more efficient way to execute the query. You should now know how to optimize MySQL SELECT queries and be familiar with basic optimization guidelines. Well done.
