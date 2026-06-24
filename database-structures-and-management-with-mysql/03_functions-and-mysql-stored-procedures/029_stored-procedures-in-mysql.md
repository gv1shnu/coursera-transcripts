# Stored procedures in MySQL

- **Course:** Database Structures And Management With
- **Module 3:** Functions and MySQL stored procedures
- **Lecture #:** 29
- **URL:** https://www.coursera.org/learn/database-structures-and-management-with-mysql/lecture/KB5Tc/stored-procedures-in-mysql
- **Extracted:** 2026-06-22 19:41:43

---

Lucky Shrub often perform the same queries on their database every day. Each time they perform these queries, they have to rewrite the same SQL code again. There must be an easier way, right? Well, with MySQL, Lucky Shrub can use the stored procedure's method to save a specific query as a block of code that they can then recall whenever required.

Over the next few minutes, you'll discover how this works by exploring the concept of stored procedures. By the end of this video, you'll be able to demonstrate an understanding of stored procedures in a MySQL database, and create and drop simple stored procedures in MySQL. Let's begin with an overview of what database engineers mean by the term stored procedures. A stored procedure is a block of code or pre-prepared query that can be stored in your database.

You can then invoke or call the stored procedure using the call command. There are a lot of benefits to be gained from using stored procedures. With stored procedures, your code is more consistent. Your code is also reusable.

You no longer need to write the same SQL statements repeatedly. Your code is also easier to use and maintain. Next, let's explore the syntax to get a better understanding of how the stored procedure works. First, to create a basic stored procedure, write the create procedure command.

This must be followed by the name of the procedure and a pair of parenthesis which hold the list of parameters. This parenthesis is required even if your stored procedure contains no parameters. Then write the rest of your procedure logic as required. For example, if your procedure must select all data from a table, then write a select command with an asterisk and the from keyword followed by the table name.

When writing a stored procedure with one or more parameters, the syntax is much the same. The key difference is that you must include all required parameters within the parenthesis, then write the rest of your procedure logic. Once you've created the stored procedure, the next step is to invoke it. To invoke a procedure, you can use the call command followed by the procedure name.

Make sure to include the parenthesis. But what if you no longer required a stored procedure? How do you remove it from your database? To delete a stored procedure, you can use the drop procedure command followed by the procedure name.

In this instance, you don't need to include any parenthesis. As you learned earlier, Lucky Shrub make heavy use of the same queries in their database. For example, they often need to query the list of products in their database products table to find items for customers or check what's in stock in their store. However, they need to rewrite the same query each time they interact with the products table.

It's a time-consuming process. Why don't you use your new knowledge of stored procedures to help them create a reusable query? Lucky Shrub need to create a stored procedure that can extract all data from their products table. The table holds data on all products in the store and is divided into three columns.

The productID column, the item column used to list all products by name, and price column, which lists all prices rounded to two decimal places. To create a stored procedure that returns all data from the table, you can write the following syntax. Begin with the create procedure command, followed by the procedure name. Since the goal of this procedure is to return details of all products, you can call it GetProductsDetails, then add parenthesis.

This stored procedure doesn't require any parameters, so you can leave the parentheses empty. Next, write a select command and an asterisk symbol to instruct MySQL to extract all data. Finally, write the from keyword and target the products table. Click "Enter" to run the query.

The new procedure, GetProductsDetails, has been created. Lucky Shrub can now call this query to extract data from the table instead of rewriting a new select statement each time. To demonstrate the stored procedure, just write the following call command: call GetProductsDetails and parenthesis. Click "Enter" to run the procedure, and extract a set of results that includes all product data.

Lucky Shrub also frequently write queries to identify the lowest priced products in their database so that they can add these items to sales or promotions. You can create a stored procedure with one or more parameters for this query. Begin with the create procedure command, then write the procedure name. You can call it GetLowestPricedProducts.

In parenthesis, you need to declare the parameters, lowest price and the integer value. These parameters return the lowest integer values in the form of a table column called lowest price. Next, write a select command and an asterisk symbol. Then write the from clause and target the products table.

After the from clause, include a less than or equal to operator, followed by the lowest price parameter. Click "Enter" to execute the query. In this statement, you've declared a parameter with an integer datatype that must pass an integer value into the stored procedure. However, don't forget that this query also includes parameters.

Each time the query is called, you need to specify the value of the stored procedure most process. As an example, let's return the data of products with a price of less than or equal to $50 by typing, the call command, the GetLowestPriceProduct stored procedure name, and placing the value of 50 in parenthesis. Click "Enter" to execute the query. The query passes the value of 50 to the stored procedure through the parameter.

The output appears on screen with a list of all products price less than or equal to $50. Finally, Lucky Shrub have decided to remove the GetProductsDetails stored procedure from their database. To drop the stored procedure from the database, type drop procedure command, and the name of the procedure, GetProductsDetails. Click "Enter" to execute the query.

The store procedure has now been dropped from the database. Lucky Shrub can now perform queries in their database much more efficiently, thanks to the use of stored procedures. You should now be able to demonstrate an understanding of stored procedures in a MySQL database and create and drop simple stored procedures in MySQL. Well done.
