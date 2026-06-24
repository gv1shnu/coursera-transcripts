# MySQL Common table expression (CTE)

- **Course:** Advanced Mysql
- **Module 2:** Database Optimization
- **Lecture #:** 16
- **URL:** https://www.coursera.org/learn/advanced-mysql-topics/lecture/0OgqA/mysql-common-table-expression-cte
- **Extracted:** 2026-06-22 20:02:18

---

When working with databases, you'll often need to write complex SQL queries. These can be difficult to manage, however, you can optimize these queries by compiling them into simple blocks using a common table expression or CTE. In this video, you'll learn how to make use of CTEs to optimize your database queries. Over Lucky Shrub, the finance department must calculate the average sale for each customer over the last three financial years.

To carry out this task, Lucky Shrub need to create one SELECT statement that contains several complicated SQL queries that include functions, strings, operators, and clauses. Fortunately, you can help Lucky Shrub to minimize the complexity of these queries using a CTE. Before you help them out, let's explore the basics of a CTE. A CTE is a method of optimizing complex database queries by compiling them into simple blocks of code.

These blocks can then be used to rewrite the query by calling the CTE when required. This simplifies the query and makes it much easier to read and maintain. A common table expression can be created for one or multiple queries. It all depends on the requirements of your database.

Let's begin with an exploration of the syntax for a single CTE. The syntax for a single CTE query uses the WITH clause to start the common table expression. This is then followed by the name of the CTE, this can be a custom name. The AS keyword is then used to associate the query within parentheses with the CTE name.

Finally, create a SELECT statement to query the name of the common table expression. The syntax for creating multiple queries is a bit more complex. Start your code block using the WITH clause, then list the queries underneath the WITH clause. Make sure that each query has a unique name and is separated by a comma.

Finally, type your SELECT statement to execute a CTE, type its name after the SELECT statement, or you can execute multiple CTE at once. To execute more than one CTE add a SELECT statement for each CTE, place a UNION operator in between your statements to return data for all statements in the output result, for example, Lucky Shrub can use multiple queries to calculate their average sale. Let's explore Lucky Shrub's use of CTEs in more detail. See if you can help them out using your new skills.

As you discovered earlier, Lucky Shrub need to calculate the average sale over the last three financial years. Their current approach is to create three separate SELECT statements, one for each year. The statements are combined using a UNION operator. Each statement calculates the average cost by using aggregate and string concatenation functions.

The data is extracted from the orders table and the conditions are specified using a WHERE clause. You can click Enter to execute these statements and return the average sale for each year. Although they work as intended, these queries are quite complex and difficult to manage, but you can use a common table expression or CTE to improve their readability. Start by using the WITH clause, then rewrite the first expression as average sales 2020 followed by the required logic.

You can use an AS keyword to return it as average sale for improved readability. Then create the second and third expressions, use the AS keyword to associate the expression with the query, and make sure that each expression is separated by a comma. Now you just need to type three SELECT statements. Each statement uses an asterisk symbol to extract all data from each of the three expressions.

Place UNION operators between the queries to combine the results. Finally, press Enter to execute the code. The output is the same as the last query you executed. However, this time you've created a query that is more optimal.

All expressions are now contained within a simple block of code that is easy to read and maintain. You should now be familiar with how to use a CTE to optimize your database. Nice work.
