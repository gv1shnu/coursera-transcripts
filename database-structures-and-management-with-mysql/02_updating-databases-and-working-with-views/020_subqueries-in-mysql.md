# Subqueries in MySQL

- **Course:** Database Structures And Management With
- **Module 2:** Updating databases and working with views
- **Lecture #:** 20
- **URL:** https://www.coursera.org/learn/database-structures-and-management-with-mysql/lecture/bsrzc/subqueries-in-mysql
- **Extracted:** 2026-06-22 19:40:06

---

Little Lemon Restaurant need to extract financial info from their database to complete their accounts. They can carry out this task using a subquery. Over the next few minutes, you'll explore the concept of a subquery and learn how to recognize a subquery and understand its syntax, identify scenarios in which a subquery can be used, and explain how subqueries are used to retrieve data. To begin, let's answer the question of, what is a subquery?

As the name states, a subquery is a query within another query. In other words, it's an inner query placed within an outer query. The inner query is viewed as the child query and the outer query as the parent query. But what does a query within a query look like?

Well, the best way to understand the subquery is through its syntax. As you just learned, a subquery is a query within a query, an inner or child query within an outer or parent query. The inner query or subquery executes first and its results are then passed to the outer or parent query. You can also build multiple subqueries in MySQL.

The outer query is presented like any normal query. It contains select, from, and where clauses. Likewise, the subquery is written as a standard query. However, the subquery must always be placed within a pair of parentheses.

When executed, a subquery can return any of the following results: a single value, a single row, a single column, or multiple rows of one or more columns. A key advantage of a subquery is that you can compare it against other values using a comparison operator. You should be familiar with comparison operators from previous lesson items in this specialization. If not, here's a quick recap.

Examples of commonly used standard comparison operators include: equal to, less than, and greater than. There's also less than or equal to, greater than or equal to, and not equal to. Let's look at the syntax for sub-queries and comparison operators. A subquery can be placed before or after a comparison operator in the where clause of your parent query.

Now that you're familiar with the basics of subqueries, here's a demonstration of how they're used. Little Lemon Restaurant are reviewing their accounts and need employee's salary data from their database. This data is held in the employees table. The table contains four columns, employee ID, employee name, role, and annual salary.

Little Lemon must use this table to identify which employees earn a salary higher than that of the Assistant Chef. You can use a subquery to complete this task. This query can be completed in two parts as follows. The outer or main query mostly extract details of all employees whose annual salary is greater than the specified value.

The subquery must identify the annual salary of the Assistant Chef. When executed, the subquery provides a subset of data from the employee's database. This subset of data is then used as an input for the outer query. Begin by writing the outer query as follows.

A select command followed by an asterisk, then the from clause which targets the employees table. The next part of the outer query, most filter out the employees table data based on the annual salary. Add a where clause followed by the annual salary column. Then add the filter condition in the where clause, the annual salary column followed by a greater than operator symbol.

The greater than operator must target a specific value. But how do you determine what this value is? You can use a subquery. Write a subquery within your main query as follows.

Add parenthesis after you're greater than operator. Within the parenthesis, write select annual salary column from employees table. Then write a where clause followed by the role column. Finally, add an equals operator followed by the Assistant Chef value.

Now that you've written both queries, press "Enter" to execute. The subquery executes first and extracts the annual salary of the Assistant Chef. This value is now the input for the outer queries where clause. Next, the outer query is executed.

The outer queries where clause filters out the records of all employees earning an annual salary greater than that of the Assistant Chef. In other words, the outer query filters out the values greater than the value retrieved by the subquery. The subquery result shows that the Assistant Chef earns $45,000 a year and the outer query shows that there are three employees who earn more than the Assistant Chef. These employees or the Manager, Assistant Manager, and Head Chef.

That's an example of how the subquery is used in a database. You should now be able to recognize a subquery, understand its syntax, and identify scenarios in which a subquery can be used. Well done.
