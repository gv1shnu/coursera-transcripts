# Variables and parameters

- **Course:** Advanced Mysql
- **Module 1:** Functions and Triggers
- **Lecture #:** 3
- **URL:** https://www.coursera.org/learn/advanced-mysql-topics/lecture/cmh5Y/variables-and-parameters
- **Extracted:** 2026-06-22 19:59:53

---

you might already be familiar with basic stored procedures and functions from earlier courses. However, mySQL also offers more complex stored procedures and functions which rely on variables and parameters. Over the next few minutes, you learn how to use variables and parameters to build sophisticated functions and procedures. Lucky shrub gardening center have several repetitive but complex queries they need to create for their database.

They can create these queries using variables and parameters. Let's follow their process and find out how it works first. You need to know what the term variable means in the context of MySQL, a variable represents a placeholder that stores a value. This value may change at times depending on the needs of the query.

Basically variables are used to pass values between SQL statements or between a procedure and a SQL statement. There are two different ways in which variables can be used in MySQL. You can create variables inside or outside of a stored procedure and inside or outside of a select statement. So what does a variable look like in MySQL?

A user defined variable is created from alpha numeric characters. You just type the at symbol followed by the name that you want to call your variable, then a sign of value to your variable. Using an equal to operator. Make sure that you end your syntax with a semi colon.

But how do you create a variable inside or outside of a stored procedure To do this. You need to use the set command within your syntax. The set command is used to assign a value to a variable. within a stored procedure.

Let's take a moment to see what the set command looks like in practice when creating a variable inside or outside of a stored procedure. Type the set command followed by the name of the variable, then a sign of value to the variable. For example, Lucky shrub have an orders table in their database that records orders placed with the business. They can create and use a variable called order I.

D. To target the record with the order I. D. Number of three.

They can now use this variable to delete, update or query the record. Or you can create a variable inside a stored procedure. Using the declare command in this instance you type the variable name without an at sign. Then you assign the variable a relevant data type and default value.

Lucky shrub can use this method to create a variable called minimum order cost. The expectation is that this variable stores of value equal to the cost of the minimum order in lucky shrubs database. As you learned earlier, you could also create a variable inside a select statement. However, when assigning a value to a variable in a select statement, you need to use the assignment operator syntax.

This instructs MySQL to assign a value to the variable. A standard equals operator. Just checks that one value equals another. So type a select command and then the name of your variable, then assign a value to your variable.

Using the assignment operator for example, Lucky Shrub can create a max order variable that retrieves the most expensive order from their orders table. They can then access the value by typing select max order. The output shows the most expensive order. It's also possible to create a variable inside of a select statement and assign it a value returned from a function.

You just type the select command followed by the function, then the into keyword and the variable name finally type the from keyword and the name of the table. The value must be extracted from Lucky Shrub can use this method to create a variable called average cost which returns the average cost of items from their orders table. Now that you're familiar with variables, let's move on and explore the topic of parameters. A parameter is used to pass arguments or values to a function or procedure from the outside.

In MySQL, a function only takes input parameters but there are three different types of parameters that can be declared in stored procedures. In out and in out parameters. Let's take a few moments to explore how each of these works. The in parameter is the default parameter.

It's used to pass an argument or value to a stored procedure. To use this parameter type that create procedure command and your procedure name. Type The in keyword in a pair of parentheses. If you don't specify a keyword then MySQL uses in by default.

Then within Your parentheses add another pair of parentheses with your Parameter names. Then add a select statement that outlines the logic of your query. For example, lucky shrub can create a procedure that calculates 20% of each employee's salary for tax purposes. They can then call the procedure against a specific salary value.

This passes the salary to the procedure and returns the amount due in tax. Next let's investigate the out parameter. The out parameter is used to pass a value to a variable outside of the procedure. Here's an example where Lucky Shrub used a procedure called get lowest cost to identify the order with the lowest cost in their orders table.

They use the out keyword to pass the value outside the parameter. So the next step is to call the procedure. The value of the procedure can then be stored in the form of a variable within a pair of parentheses. To display the variable stored value.

Just use a select statement to return the output. Finally, there's the in out parameter. This is a combination of both parameters. It's used to pass an argument to the procedure and then pass the new value back to the outside.

So it's effectively an in and an out parameter. For example, you could create a procedure called square a number that returns the squared value of a specific number using the in keyword and a number variable. The procedure expects an input number through the number parameter. It multiplies this number by itself, then returns the result to the same a number parameter again.

Then you can set a variable called X number with a value of five called the procedure using the X number of variable value. The procedure passes the value through the parameter. It then performs the calculation and returns the result back through the parameter. Use a select statement to output the variable value.

You should now be familiar with how to create more complex stored procedures and functions using variables and parameters. Great work.
