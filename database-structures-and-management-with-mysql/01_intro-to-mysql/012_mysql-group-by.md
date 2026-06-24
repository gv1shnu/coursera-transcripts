# MySQL GROUP BY

- **Course:** Database Structures And Management With
- **Module 1:** Intro to MySQL
- **Lecture #:** 12
- **URL:** https://www.coursera.org/learn/database-structures-and-management-with-mysql/lecture/4pF2v/mysql-group-by
- **Extracted:** 2026-06-22 19:38:40

---

Lucky Shrub are reviewing recent customer orders in their database. They need to find a way to group records with similar values into one single record so that they can analyze the order data and produce summaries. The MySQL GROUP BY clause and its related aggregate functions are a great way for the company to complete this task. Over the next few minutes, you'll explore these concepts and use them to help Lucky Shrub produce summaries of their orders.

And by the end of this video, you'll be able to group rows into subgroups using the MySQL GROUP BY clause and utilize the MySQL GROUP BY clause with SQL aggregate functions. So before you begin helping Lucky Shrub, let's take a moment to find out what database developers mean by the term GROUP BY. The GROUP BY clause is used in SQL syntax to group rows in a table based on given columns into summary rows, also known as subgroups. To get a better understanding of this clause, let's look at the syntax.

The syntax begins with a SELECT statement, followed by the name of the required column. The FROM clause is then added and targets the name of the table that holds the required column. Finally, there's the GROUP BY clause. After this clause, a list of column names are added.

Each one is separated by a comma. These are the columns according to which the data must be grouped. If there is a WHERE clause in your SELECT statement, then the GROUP BY clause must be placed after this clause. And make sure that the columns listed in the SELECT clause include the columns listed in the GROUP BY clause.

Additionally, the GROUP BY clause is also frequently used with aggregate functions. An aggregate function can be used with the GROUP BY clause to perform one or more calculations and return a single value for each subgroup. You might be familiar with aggregate functions from previous videos, but if not, don't worry. Here's a quick recap of the main aggregate functions used by database developers with the GROUP BY clause.

SUM(), used to add values of given columns together and return a single value. AVG(), used to determine the average of column values. And MAX() which returns the maximum value of one or more given columns. The minimum aggregate function determines the minimum value of one or more given columns.

And finally COUNT() is used to count the number of instances that a given column value occurs. Let's review the syntax of the SELECT statement when using the GROUP BY clause with an aggregate function. First ,input a SELECT statement followed by a list of columns. You can then apply the aggregate function on any of these columns as required.

For example, you can use the MAX aggregate function to calculate the maximum values in column 1. Just make sure to place the column in parenthesis. Next, include the FROM clause and the name of the table that holds the columns. Finally, include the GROUP BY clause followed by the names of the columns by which the data should be grouped.

Make sure that these same columns are also present in the SELECT column list. Lucky Shrub can make use of the GROUP BY syntax and aggregate functions to determine the total number of orders received by each department in the business. So now that you've learned about the GROUP BY clause and aggregate functions, it's time to use your knowledge to help Lucky Shrub. Let's start with a quick review of the order table.

The table contains five columns, Order ID, Department, Order Date, Order Quantity and Order Total. There are multiple records with the same value for the Department column. For example, there were five orders placed with the Lawn Care department. This means that there are a total of five records for the Lawn care department and there are more instances of multiple records with the same value for other departments like decking.

The best approach in this instance is for Lucky Shrub to group all these records so that they have just one row for each group or department. This will make it much easier to analyze the data and produce summaries. You can help them to reduce the departments into five groups or subgroups using the GROUP BY clause. First write a SELECT statement followed by Department, the column name.

Next, insert a FROM clause followed by orders, the table name. Then add the GROUP BY clause and the name of the column. Finally run the statement to generate the output. In the output that's returned, all records in the Department column have been reduced to five groups, one row or one single record for each department in the business.

Now that you have simplified the table, you can use aggregate functions to analyze the data. Lucky Shrubs report must show the number of orders placed with each department. You can use the COUNT function to produce this data. The syntax for this query is almost the same as the previous one you just performed.

The key difference is that you must add the COUNT function followed by the column name in parenthesis after SELECT Department. This specifies which column holds the data and the COUNT function counts the occurrences of each department among the order records. Now just execute the query to generate the output. The output returns the five departments alongside the total number of orders placed with each.

Next, let's find out how much money each department made from these orders. You can use the same syntax from the previous query but this time, use the SUM aggregate function with the orderTotal column. Then execute the query. The output returns the total sum of the selected numeric column.

In other words, it adds the values in the orderTotal column for each instance of each department. Now let's determine the minimum order quantities for each department. Once again, you can use the same syntax but with the MIN function targeting the orderQTY column. Once you run the query, the output returns the smallest value of the column.

Finally, Lucky Shrub also need the average order total for each department. So write the syntax one last time. And in this instance, you can use the average aggregate function to query the orderTotal column. The output that's returned shows the average value of the orderTotal column.

Thanks to your help, Lucky Shrub now have a summary that shows all the relevant data from the Order table grouped together as required. Having proved your skills with Lucky Shrub, you should now be able to group rows into subgroups using the MySQL GROUP BY clause. And you should also know how to use the clause with SQL aggregate functions. Well done.
