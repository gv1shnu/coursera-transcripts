# Subqueries and complex comparison operators

- **Course:** Database Structures And Management With
- **Module 2:** Updating databases and working with views
- **Lecture #:** 21
- **URL:** https://www.coursera.org/learn/database-structures-and-management-with-mysql/lecture/N1inz/subqueries-and-complex-comparison-operators
- **Extracted:** 2026-06-22 19:40:16

---

Little Lemon Restaurant need to perform complex queries in their database and standard subqueries might not be enough for this task. They'll need to use multiple row subqueries with complex comparison operators. Over the next few minutes, you'll explore subqueries and complex comparison operators and learn how to: explain how subqueries interact with complex comparison operators, and demonstrate the use of subqueries in a complex data retrieval scenario. As you might already know, a key advantage of a sub-query is that you can compare it against other values using an operator.

However, there are more complex operators that can be used with multiple row subqueries. ANY operator returns data for any values that meet the specified condition. ALL returns data for all values and the SOME operator returns data for one or more matching values. Let's look at how to write multiple row subqueries using the ALL, ANY and SOME operators.

These comparison operators let you perform a comparison between a single common value on a range of other values. They result in multiple records or target multiple values within a table. Sub-queries can also be used with the EXISTS and NOT EXISTS operators. The EXISTS operator tests for the existence of rows in the results set returned by the sub-query.

It returns true if the sub-query returns one or more records. On the other hand, the NOT EXISTS operator checks for the non-existence or absence of results from the sub-query. NOT EXISTS returns true when the sub-query does not return any row of results. Let's review the syntax for the EXISTS and NOT EXISTS operators.

The syntax is very similar to a standard sub-query. The key difference is that the EXISTS operator is placed after the WHERE clause to determine the existence of the value specified in the sub-query. Or you can use the NOT EXISTS operator to check for the non-existence or absence of results from the sub-query. Let's look at a demonstration of how subqueries are used with these operators.

The Little Lemon Restaurant need to identify all employees earning an annual salary that's less than or equal to the annual salary earned by all employees in the following roles, manager, assistant manager, head chef, and head waiter. The data required to complete this query is in the employees table. The table has four columns as follows, EmployeeID, EmployeeName, Role, and AnnualSalary. You can extract the data required from this table using two queries.

An outer query to identify all employees who are earning an annual salary that's less than or equal to the specified values. A sub-query that extracts the data of annual salaries earned by employees who are in the rows specified earlier. Let's begin with the outer query. It starts with a SELECT command and then asterisk.

Then add a FROM clause that targets the employees table. Next, write a WHERE clause followed by the AnnualSalary column name. Finally, write a less than or equal to operator. Now you must write the sub-query within parentheses.

Write a SELECT command to select the AnnualSalary column then a FROM clause to target the employees table. Next, write a WHERE clause followed by a condition that extracts data from the Role column. Finally, in parentheses write the required roles, manager, assistant manager, head chef, and head waiter. These queries must return a result that lists all employees earning an annual salary that's less than or equal to the annual salary earned by all employees in the role specified.

To ensure that you get the desired result, place the ALL operator after the less than or equal to comparison operator, but before the sub-query. Then execute the query to return the output. The sub-query executes first and identifies the salaries of the manager, assistant manager, head chef, and head waiter roles. These salaries are the values that the outer query uses.

The values are 70,000, 65,000, 50,000, and 40,000. The outer query filters out the employees who earn an annual salary less than or equal to all of these values. The final output shows that the employees with IDs five and six earn an annual salary less than or equal to the other roles. On the other hand, the ANY operator compares the results of the sub-query to determine whether it can exclude records from the outer query that satisfy the conditions for any of the values returned by the sub-query.

Little Lemon's next task is to identify employees earning an annual salary that's greater than or equal to the annual salary earned by any employee in the four roles specified earlier. You can use the same query as before but remember that this time you're checking for values that are greater than or equal to those in the sub-query. Change the comparison operator in the WHERE condition of the outer query to a greater than or equal to operator. Now, just before the sub-query, replace the ALL operator with the ANY operator.

Finally, press "Enter" to execute the query. The output shows that there are four employees who earn a salary greater than or equal to the other roles. For their final query Little Lemon need to determine if their head chef and waiter are are assigned to a booking. They can do this using the EXISTS or NOT EXISTS operators.

The query involves two actions. In the first action, the outer query extracts details of employees and in the second action the sub-query determines if the head chef or head waiter have been assigned to a booking. The required data is held in the bookings table. This table has six columns as follows, BookingID, TableNo, first name of guest, last name of guest, a column for each booking slot or time, and a column that shows the ID of the employee assigned to the booking.

Begin by writing the outer query as follows. SELECT asterisk FROM employees, then add a WHERE clause. The sub-query must determine if there are any employees in the role of head chef or head waiter assigned to a booking. Add the EXISTS operator after the WHERE clause.

Then write the sub-query in parentheses as follows, a SELECT command and then asterisk a FROM clause targeting the bookings table, a WHERE clause, and a condition that must return results for the required employees if they're assigned to a booking. Press "Enter" to execute the query and generate the output. The query returns three records. These are bookings 1, 2, and 6, so the EXISTS operator has checked for the existence of the specified results in the sub-query and that it has found that these results exist.

Therefore, the operator result is true. The result is that the outer query filters out the details of the two employees who are assigned to these three bookings. Let's replace EXISTS with the NOT EXISTS operator to see what results are returned. The output returns the same three records as before.

However, the NOT EXISTS operator checks for the nonexistence of results from the sub-query. Also in this case the WHERE clause filters out employees that do not exist in the results obtained by the sub-query. This returns results of four employees that don't exist in the sub-queries results. In other words, this is the data for employees who don't meet the subqueries criteria and aren't identified in the results.

You should now be able to explain how subqueries interact with comparison operators and demonstrate the use of subqueries in a complex data retrieval scenario. Well done.
