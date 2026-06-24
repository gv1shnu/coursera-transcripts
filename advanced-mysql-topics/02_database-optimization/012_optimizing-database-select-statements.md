# Optimizing database SELECT statements

- **Course:** Advanced Mysql
- **Module 2:** Database Optimization
- **Lecture #:** 12
- **URL:** https://www.coursera.org/learn/advanced-mysql-topics/lecture/lH6ZE/optimizing-database-select-statements
- **Extracted:** 2026-06-22 20:01:35

---

When working with a database, it's important that your SQL queries are compiled and executed quickly and efficiently by the database. But this can only happen if your queries are optimized. Over the next few minutes, you'll explore techniques for optimizing select statements. Lucky Shrub have received large numbers of orders from their clients.

This has led to increased volumes of data in their database. They need to query this data using select statements. To improve the performance of their queries, they'll need to make sure that the statements are optimized. Let's find out more about optimization guidelines and explore some techniques that Lucky Shrub can make use of.

As you might already know, select statements belong to a category of SQL statements called data retrieval statements. These types of statements are designed to return data from the database. But if they're not optimized correctly, then they add extra load to the database and slow down its performance. This means that it then takes it longer for the database to execute your SQL select statements or queries and return the data you need.

However, there are a few basic guidelines or best practices that you can follow to optimize your select statements. You might already be familiar with some of these methods. Target only required columns in your select clause. Avoid using functions in predicates and avoid using a leading wildcard in predicates.

Use INNER JOIN where possible and make use of distinct and union clauses only when necessary. Let's take a few moments to explore some examples of these guidelines. When querying a table you might often make use of an asterisk in your select statement to extract all available data. However, instructing MySQL to query all data in a table adds extra load on the database and slows down its performance.

Particularly if you only require data from specific columns. A more optimal approach is to list only the columns in your statement that hold the data you require, instead of using an asterisk. Lucky Shrub can use this method to target the required data in their orders table and return the data faster. Another common mistake that database engineers make, is using MySQL functions and predicates that refer to columns which aren't indexed.

A predicate is an expression that returns a true or false value. An example of this is WHERE clause conditions. You should also avoid using functions in the WHERE clause on a column that's indexed because this prevents the database from using the index. You will explore indexes in more detail later in this lesson.

Using a leading wildcard on predicates can also lead to a slowdown in the database. An example of this is using patterns that begin with a wildcard when combining the LIKE operator in the WHERE clause. MySQL can't make use of an index in a column during a search when it's matched against a pattern with a leading wildcard. Another method for optimizing databases involves using the INNER JOIN instead of the OUTER JOIN where possible.

An OUTER JOIN retrieves all records from both tables, including rows that don't contain matching values. This takes longer for MySQL to process. The INNER JOIN is more efficient because it retrieves only the necessary data or matching records from both tables. This helps to optimize your queries.

Often when creating SQL queries you'll use that distinct clause to eliminate duplicate values or the union clause to combine multiple query results. This can slow down the query because it must perform a sorting operation and eliminate duplicate records. However, if you use UNION ALL instead, then this eliminates the need for a sorting operation and speeds up the execution process. You should now know how to optimize my SQL select queries, and be familiar with basic optimization guidelines.

Well done.
