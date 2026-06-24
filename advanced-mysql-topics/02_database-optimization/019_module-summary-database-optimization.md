# Module summary: Database optimization

- **Course:** Advanced Mysql
- **Module 2:** Database Optimization
- **Lecture #:** 19
- **URL:** https://www.coursera.org/learn/advanced-mysql-topics/lecture/fM8Mv/module-summary-database-optimization
- **Extracted:** 2026-06-22 20:02:51

---

Congratulations, you've reached the end of the second module in this course. Let's take a moment to recap some of the key skills you've gained in this module's lessons. In the first lesson, you learned how to optimize database queries. And you now understand that database optimization is the process of maximizing the speed and efficiency of the databases performance when executing queries.

You know that optimization focuses on two different kinds of statements, data retrieval or select statements, which return data from the database and data change statements used to alter data within the database. You learn that by optimizing a database you can process data much more quickly and efficiently. During this lesson, you also learned how to implement different optimization techniques on select queries, including targeting only required columns in your select clause. Avoiding the use of functions in predicates and avoiding the use of a leading wildcard in predicates.

You also learn to use INNER JOIN where possible and make use of distinct and union clauses only when necessary. And you also explored the use of indexes to help maintain pointers that lead to sorted data. During your study of indexes, you learned that there are two types of indexes. The first is a primary index, also called a clustered index.

The second is a secondary or a non-clustered. And you then reviewed the syntax for creating a secondary index. This involves using a create index statement, a custom index name, and the on keyword to target the required table and columns. In lesson two, you explored further optimization techniques.

Now that you've completed this lesson, you're able to make use of mySQL transaction statements to manage queries and roll the database back to its original state if any of the queries fail to execute as required. You can manage database transactions using statements like start transaction, begin or begin work, commit and rollback. You can start your transaction using start transaction. And you know that if you encounter an error with your queries, you can add the rollback statement to the end of your SQL statements to return to your start transaction point.

As you worked through this lesson, you also learned how to optimize select queries using MySQL common table expressions. You can now use a CTE to compile complex queries into simple blocks of code. These blocks can then be used to rewrite the query by calling the CTE when required. This simplifies the query and makes it much easier to read and maintain.

Start your code block using the width clause, then list the queries underneath. Finally, type your select statement followed by the query name. You could also execute multiple CTE at once using the union operator between statements. You then explored MyQ prepared statements.

You could now make use of prepared statements to limit the number of times MySQL must compile and parse code. And you discovered how to interact with a MySQL database using the JSON data type. As you worked through these lessons, you also enhanced your understanding of the topics through reading items. Tested your knowledge of optimization techniques in quiz environments, and demonstrated your ability to make use of MySQL optimization techniques in a lab environment.

Having completed this module, you should now be able to make use of a wide range of database optimization techniques. You can deploy these techniques to make sure that your statements are compiled, parsed, and executed quickly and efficiently in MySQL. Great work.
