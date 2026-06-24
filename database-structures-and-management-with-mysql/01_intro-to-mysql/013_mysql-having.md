# MySQL HAVING

- **Course:** Database Structures And Management With
- **Module 1:** Intro to MySQL
- **Lecture #:** 13
- **URL:** https://www.coursera.org/learn/database-structures-and-management-with-mysql/lecture/x4eXU/mysql-having
- **Extracted:** 2026-06-22 19:38:51

---

At this stage of the course, you may be familiar with the Group By clause having helped Lucky Shrub group data from their customer orders in an earlier video. Lucky Shrub now need to filter this grouped data against the list of conditions to determine the best performing departments in the business. They can use the MySQL Having clause to specify filter conditions that will generate this data. Over the next few minutes, you'll explore the Having clause so that you can help Lucky Shrub.

By the end of this video, you'll be able to identify the MySQL Having clause and explain its purpose and demonstrate the use of the Having clause to specify a filter condition for groups of rows. What is the Having clause and what does it add to your grouping data skill set? The Having clause is used in a SQL statement to specify a filter condition for the group data that the Group By clause generates. Let's take a moment to review the syntax for this class, starting with a quick recap of the syntax of a typical SQL statement.

As you learned in previous videos, the Where clause is used in a select statement to specify one or more filter conditions. You must place a Where clause before the use of the Group By clause. The Where clause can't be used to specify a filter condition for the group data that the Group By clause generates. How do you filter this data?

You can add the Having clause to your SQL statement. The Having clause is added after the Group By clause. The Having clause is used to specify the filter condition that needs to be applied to your grouped data. The Having clause evaluates the group filter condition against each group returned by the Group By clause.

If the result is true, the row is included in the results set. However, don't forget that if you omit the Group By clause, then the Having clause behaves just like the Where clause. Let's take a quick look at a basic example of the Having clause. Lucky Shrub can use the Having clause with aggregate functions to determine which of their departments received orders of a certain dollar amount.

Now it's time to use your new Having clause knowledge to assist Lucky Shrub. As you discovered earlier, Lucky Shrub needs to filter their customer order data to check which departments met their monthly sales target of $2,275. Let's see if you can help them out. Let's begin with a review of the order table, which holds the required data.

The table is divided into five columns; OrderID, Department, OrderDate, OrderQuantity, and OrderTotal. The first task is to identify which departments have order totals of a value greater than $2,275. You're only concerned with the department an OrderTotal columns. You can determine the order total of each department by using a select statement with a Group By clause.

First type the Select clause followed by the department column. You then need to include the sum aggregate function, then place the orderTotal column in parenthesis. Next, add the from keyword followed by the table name, which is orders. Finally, include the Group By clause and targeted the department column.

Run the statement to retrieve an output that shows the total sales figures for each of the five departments. Your next step is to filter this data to retrieve the results to have an order total value greater than $2,275. You can use the same statement as before, but this time add the Having clause after the Group By clause. The Having clause is followed by a second instance of the sum aggregate function, which once again targets the OrderTotal column.

Finally, use the greater than operator followed by the figure 2275. This instructs the SQL statement to filter results greater than $2,275. This SQL statement is now ready to execute. However, you could make the syntax more efficient by using an alias.

You should be familiar with the concept of an alias from previous lessons. You can use an alias called total in the Select clause for the aggregate function. This alias can then be referred to in the Having clause. This makes the condition concise and easier to read.

Now you can execute the query. The output that's generated reveals three departments in Lucky Shrub, which met this month's sales targets. Thanks for your assistance. Lucky Shrub has identified their best-performing departments.

You should now be able to identify the MySQL Having clause and explain its purpose. You should also be able to demonstrate the use of the Having clause to specify a filter condition for groups of rows. You're making great progress with grouping data.
