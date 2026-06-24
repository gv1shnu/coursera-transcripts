# MySQL Transaction

- **Course:** Advanced Mysql
- **Module 2:** Database Optimization
- **Lecture #:** 15
- **URL:** https://www.coursera.org/learn/advanced-mysql-topics/lecture/oBz8v/mysql-transaction
- **Extracted:** 2026-06-22 20:02:07

---

How often have you encountered an error during a critical activity, forcing you to begin the task from the beginning? This can be particularly stressful when you're working on many related queries at the same time. Thankfully, you can use MySQL transaction to roll your database back to a previous state. In this video, you'll learn how to manage database transactions with MySQL transaction statements.

Lucky Shrub are updating new sales in their orders table and the stock levels in their products table. To carry out this transaction, Lucky Shrub need to create and execute several different queries but they could encounter an error at any point in the process. For example, the Internet connection could fail while inserting data into the table and this could result in invalid data or an incomplete transaction. However, if such an event were to occur, Lucky Shrub can roll back their database and restore it to its original state using transaction commands.

So what are transactions in MySQL? As you just saw with Lucky Shrub, a transaction in MySQL is one or more queries that can be committed permanently to the database. And the database can be rolled back to its original state if any of the queries fail to execute as required. MySQL provides the following set of statements for managing database transactions, START TRANSACTION, BEGIN or BEGIN WORK, COMMIT, and ROLLBACK.

Let's explore each of these statements in more detail. START TRANSACTION is the standard SQL statement for starting a transaction process. This syntax marks the point that you'll return to should you decide to roll back the process. So begin your syntax with START TRANSACTION, then list your SQL statements underneath.

For example, Lucky Shrub can begin their database updates with a START TRANSACTION statement and then follow this with a list of the required SQL queries. However, START TRANSACTION isn't the only way to begin a transaction. With MySQL, you can also use the BEGIN or BEGIN WORK aliases as alternative ways to initiate a transaction. Whichever method you choose, once you've finished typing your SQL statements and you're happy with the result, then it's time to commit the transaction to the database.

You can use that COMMIT statement to commit the transaction changes permanently to the database. Just type the COMMIT statement at the end of your code block. But what if you encounter an error during your transaction like Lucky Shrub and their Internet connectivity issues? Or maybe you typed incorrect code, executed the wrong statement, or entered incorrect data.

You can use the ROLLBACK command to rollback the current transaction and cancel the changes made to the database. Just add the ROLLBACK statement to the end of your SQL statements to return to your START TRANSACTION point. However, it's important to remember that the rollback statement must be enacted before you commit your SQL statements. Once you rollback your code, you then need to type the correct SQL statements.

And once you're happy with these statements, type COMMIT to commit the changes to the database. So let's quickly recap the process. Begin your transaction with START TRANSACTION. Type your required SQL statements and use COMMIT to commit your changes to the database.

And should you encounter any errors or other issues, just use the ROLLBACK statement to return to your START TRANSACTION point. Now that you're familiar with MySQL transactions and the related statements, let's see if you can help Lucky Shrub update the sales and stock levels in their database tables. A client with an ID of Cl1 has just placed an online order for ten bags of artificial grass. This item has a product ID of P1 in the products table.

There are currently 100 bags in stock. This number must be updated to 90 once the client's order is processed. First, type START TRANSACTION to determine the point you can rollback to if an error occurs. Now you need to add the required SQL statements.

The first is an INSERT INTO statement. This statement inserts a new set of values into the required columns in the orders table for the client's order. Then type an UPDATE statement that updates the number of bags of artificial grass in the products table by deducting 10 units from the current stock level. The next step is to use a SELECT statement that creates an inner join between the orders and products table using the ProductID key, which is common to both tables.

Execute this statement to check if the transaction was completed as you expected. Unfortunately, it looks like there was a mistake. These updates have been applied to the client with the ID of C11. It seems you typed the wrong client ID In your code.

No problem, you can restore the data by using the ROLLBACK statement. Now, check the orders and products tables again using SELECT statements. All data has been restored to its original state. So let's type START TRANSACTION once again, followed by the same SQL statements as before, only this time make sure to update the correct client details.

Once you've completed your new set of SQL statements, check that the output is as you expected. Great, this time, all details are correct. You can now type COMMIT to commit your changes to the database. You should now be able to manage transactions in your MySQL databases using transaction statements, great work.
