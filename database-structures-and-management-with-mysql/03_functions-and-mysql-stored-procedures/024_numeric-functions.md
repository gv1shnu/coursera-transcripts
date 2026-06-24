# Numeric functions

- **Course:** Database Structures And Management With
- **Module 3:** Functions and MySQL stored procedures
- **Lecture #:** 24
- **URL:** https://www.coursera.org/learn/database-structures-and-management-with-mysql/lecture/mPfow/numeric-functions
- **Extracted:** 2026-06-22 19:40:49

---

The jewelry store, Magenta and Gallo, also known as M&G, are reviewing client orders in their database. They must determine the average amount of money that each client has spent with the business. M&G can use numeric functions to extract this information. In this video, you will explore numeric functions and learn how to identify common MySQL numeric functions and explain how these functions are used to process and manipulate data in a MySQL database.

At this stage of the course, you've encountered some basic functions. Here's a quick reminder of what database engineers mean by the term functions in the context of my MySQL. As you've learned in earlier lessons a function is a piece of code that performs an operation and returns a result. Some functions accept parameters or arguments, while other functions do not.

Functions are very useful for manipulating data in a database table. Broadly speaking, MySQL functions can be grouped into five different categories as follows. Numeric functions, string functions, date functions, comparison, and control flow functions. You'll review each of these functions in more detail over the course of this lesson.

The focus of this video is MySQL numeric functions which can be divided into two categories. Aggregate functions, which can be used on a set of values and math functions which perform basic mathematical tasks on data. You should already be familiar with aggregate functions, having used these previously in the course with select statements to calculate aggregated values. Let's just recap them briefly.

Commonly used aggregate functions include Sum, Average, and Max. There's also the minimum aggregate function and count. Now that you've recapped aggregate functions, let's look at some common math functions. A number can be rounded to a specific decimal place using the round function and the MOD function can be used to return the remainder of one number divided by another.

These functions are a great way for M&G to perform additional tasks while also determining the average dollar amount that each client has spent with the business. But how can you and M&G make use of these functions in a MySQL database. You can build them into your SQL SELECT statements. Let's review the syntax.

The round syntax begins with a SELECT command, followed by the name of the column to be queried. You then call the round function followed by a pair of parenthesis. Within these parenthesis write the required arguments. The first argument can be a column name or any numeric value.

The second argument must be the number of decimal places. Finally, write the FROM keyword followed by the required table name. The MOD syntax is very similar, just called the MOD function instead of round. Within parenthesis, identify the column or value and instruct MySQL, what number to divide the value by.

Finally, identify the table that holds the data. When working with the MOD function, bear in mind that the first argument can be a table column or any numeric value. While the second argument must be the value by which the first will be divided. For example, M&G can use the round syntax and average numeric function to determine the average dollar amount each client spent, rounded down to two decimal places.

Let's take a few moments to explore M&G's database and find out more about how they make use of numeric functions. As you learned earlier, M&G are reviewing client orders and must determine the average dollar amount that each client has spent with the business. The company has a table called client orders that shows the average amount each client has spent. The table has two columns, Client ID, which shows the ID of each client and average cost, which displays the average amount each client has spent.

However, even though this table shows the average amount, M&G need to round down these values to two decimal places. You can help them using the round function, write SELECT followed by the column names, then call the round function on the average cost column. In parenthesis, put the average cost column as the first argument then pass the number 2 as the second argument to round the value to two decimal places. Next, use the from keyword to target the client orders table.

Finally, group by Client ID. Execute the query to create the output and display all decimal places reduced to two. In the next task, M&G are restocking their inventory and need to identify which items they've placed and even number of orders for. The data they need is in the table M&G orders.

The table contains several columns but the ones you need to complete this task are Order ID, Item ID, and Quantity. To determine if a given quantity is odd or even, you can divide the quantity by 2. The remainder is your answer. This can be done using the MOD function.

First, write SELECT, followed by the column names, then call the MOD function. Pass the quantity column as the first argument and the number 2 as the second argument, execute the query. The query returns the following values, a value of zero if there is no remainder when all data is divided by two or it returns just the remainder value. The output shows that an even number of orders have been placed for items 1,3,5, and 6.

M&G have now completed their database tasks using common MySQL functions and you should now be able to identify frequently used MySQL numeric functions and explain how these functions contribute to data processing a manipulation in a MySQL database. Well done.
