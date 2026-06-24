# SELF-JOIN

- **Course:** Database Structures And Management With
- **Module 1:** Intro to MySQL
- **Lecture #:** 10
- **URL:** https://www.coursera.org/learn/database-structures-and-management-with-mysql/lecture/jD0ca/self-join
- **Extracted:** 2026-06-22 19:38:18

---

The Lucky Shrub database has a table called employees which lists all staff in the business. Some of these staff members are line managers and other employees report to these line managers. Lucky shrub needs to query the data from this table to determine which roles everyone is assigned. They can complete this task using the self join clause, a special joint case.

This clause let's Lucky Shrub create a joint between rows on the same table so that they can extract specific information. But the table must be treated as two tables to perform the required joints. Over the next few minutes, you'll help Lucky Shrub with this query. And by the end of this video you'll be able to apply the self joined concept in MySQL and use an alias to provide same table with two different names.

Let's begin by reviewing the employee table from the Lucky Shrub database. This is the table that stores the required information on employees and their line managers. The table includes five columns, Employee ID, Full name, JobTitle, County and LineManager ID. In this table, the primary key, Employee ID values, are also used in the LineManager ID column, to show who manages each employee in the Lucky Shrub firm.

So, your main task is to list the full name of all line managers and the employees they manage. The full names of both sets of employees exist within the full name column. To complete this task, you can create the employees table as two identical tables, then create an inner join to investigate each employee ID and match it with the line manager ID. Then extract the full name value and print it as either line manager or employee.

And remember, that the line managers are also employees. Before writing the query, remember that the self-joined clause creates two tables from one. In other words, know you're dealing with two tables in your query, not just one. So let's begin with a sequel select statement.

The statement uses e1 with an AS keyword to declare an alias for the first employee table and it also uses e2 with an AAS keyword to declare an alias for the second employee table. Remember that the employee table is the same in both cases. In addition, your statement queries the full name column from the e1 table and it uses the AS keyword to declare a suitable Alias name of line manager from the left table. It then queries the full name column from the e2 table and uses the AS keyword to declare an alias of employee from the right table, in columns from both employee tables.

But only once there's a match between the column values. In this instance, the condition is e1.EmployeeID = e2.lineManagerID;. In other words the condition matches the employee ID with the line manager ID. If it finds a value of true, then the full name was returned from the left table and displayed in the LineManager column.

And the full name is also returned and displayed as an employee from the right table. Press Enter to execute the query, the output results set links the line managers with the employees they manage. A quick summary of the output results set shows that, the employees, Seamus and Greta report to the line manager Simon. Simon reports to himself and all other staff report to Seamus thanks to the self joined clause, lucky show up have now determined which employee is in which role and you should now be able to apply the self joined concept in my sequel and use alias to provide same table with two different names.

Good work.
