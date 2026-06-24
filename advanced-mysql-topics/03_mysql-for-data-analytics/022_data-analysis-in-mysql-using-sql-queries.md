# Data analysis in MySQL using SQL queries

- **Course:** Advanced Mysql
- **Module 3:** MySQL for Data Analytics
- **Lecture #:** 22
- **URL:** https://www.coursera.org/learn/advanced-mysql-topics/lecture/d4mpU/data-analysis-in-mysql-using-sql-queries
- **Extracted:** 2026-06-22 20:03:24

---

Analyzing data in a MySQL database requires a good understanding of how to access data and extract relevant information using SQL queries. You should already be familiar with many of these like subqueries, joins, and views. Over the next few minutes, you'll learn about the role that these SQL queries play in the data analysis process. Over at Lucky Shrub, they need to perform data analysis on the client orders within their database.

However, the types of data analysis they need to perform are very different. They include simple data extraction tasks using basic SQL queries on tasks that involve advanced subqueries, joining tables and creating virtual ones. Once these tasks are completed and the required data is extracted, they can analyze it and prepare it for data analytics. Let's explore the relationship between SQL queries and the data analysis process to find out more about how they support Lucky Shrub's business.

As you should already know, data analysis involves collecting and presenting the data in your database. The data can then be used to gather further insights to support the data analytics process in MySQL. Data can be collected from a database using a wide range of SQL queries. At this stage of the course, you should be familiar with many of these SQL queries.

For example, you can extract or collect data using joins to join two tables together, subqueries to create a query within a query, and views to create virtual tables. You can also use functions to perform sophisticated operations and return different results and filter required data using operators. The basic process for performing data analysis in MySQL using SQL queries works as follows. You can extract the required data from your database using a wide range of one or more SQL queries.

You can then use further SQL queries to present a description of the results of your data analysis. You can then gain further insight from these initial results using data analytics. Let's explore an example of this process. Lucky Shrub need a list of all products that sell in quantities of 100 items or more.

They can extract this data using a subquery that targets the tables that hold the data and filters the required results. Once they execute the subquery, MySQL returns the records that they need, a list of the top selling products. Once Lucky Shrub identify their top-selling products, they can then use different types of SQL queries and data analytics tools to generate further insights and plan for the business's future. All these insights and potential strategies are made possible by the data collected through SQL queries.

For example, now that they know what their best-selling products are, they can continue to buy more of them and they can buy less of the products that don't sell as well. They could even offer discounts on certain items to try and increase sales. To recap this process, Lucky Shrub create a SQL sub query to target the data they require. They then extract this data from the database through data analysis.

This data can then be explored further using more sophisticated queries to generate business insights. Now that you're familiar with this process, it's time to put it into action. As you discovered a few moments ago, Lucky Shrub need to perform data analysis on their client orders. Let's see if you can help them out.

The data that Lucky Shrub require is in the orders table in their database. They've extracted the data from the table, but they now need to target specific data that provides insight into the performance of the business. For example, Lucky Shrub need a list of all products that sell 10 items or more. You can extract this data with a select statement that targets the order tables product ID column.

Then add a where clause that targets any product ID that has sales data. Next, add a subquery that selects product IDs from the orders table that's sold in a quantity equal to or greater than 10. Execute the statement to extract the data. MySQL outputs a table that displays the required records.

Joins are also a useful method of performing data analysis in MySQL, you can use different joins to explore the relationships that exist between data. Lucky Shrub need to analyze and extract data on their clients and the orders they placed over the last 10 days. However, the data exists in two separate tables. You can help them analyze the data in these tables using joins.

Write a select statement to join the required columns from the orders and products tables using an inner join. Then use the between keyword to filter the client IDs and related orders from the required dates. Execute the statement to show the required data. Views are also helpful for analyzing data.

They can be used to create virtual tables that focus on specific types of data. Lucky Shrub need to analyze their sales data and extract the top five best-selling products. You can use a select statement and a virtual table or view to help Lucky Shrub analyze their data for this information. Write a Create View statement called a new virtual table top products.

Then write a select statement that uses an inner join to combine the required columns from the products and orders tables. These tables hold all the sales data you need to help Lucky Shrub carry out their analysis. Finally, use an Order By clause to order the extracted records in descending order, then execute the statement. The statement creates a new virtual table called top products that shows the name, quantity, and cost of the top five best-selling products.

You can use a select statement to extract all data in this virtual table to perform further data analysis. All these insights and potential strategies are made possible by the data collected through SQL queries. On what SQL queries you use all depends on what data you need to extract and analyze and what you want to achieve from this analysis. You should now be familiar with performing data analysis in MySQL using SQL queries.

Great work.
