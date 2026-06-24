# MySQL Prepared Statement

- **Course:** Advanced Mysql
- **Module 2:** Database Optimization
- **Lecture #:** 17
- **URL:** https://www.coursera.org/learn/advanced-mysql-topics/lecture/Me8ob/mysql-prepared-statement
- **Extracted:** 2026-06-22 20:02:29

---

Each time you create a statement, it must be compiled and passed by MySQL before it can be executed. This process uses a lot of resources. A more efficient method is to create a prepared statement that can be used repeatedly without requiring a clearance each time. In other words, you can create a prepared statement that MySQL compiles and pauses just once before it is executed.

The statement functions as a template that holds unspecified values as parameters. These can then be added as required. Each time the statement is invoked, MySQL know it is safe to execute. This is much more efficient and optimal way of executing statements without using valuable MySQL resources.

Let us look at an example of how to create and execute a prepared statement from the lucky shrub database. Lucky shrub need to extract data on customer orders from their orders table. Let us help them carry out this task using an optimized prepared statement. The prepared statement must return the following information from the orders table in the database for each specified record, client ID, product ID, quantity, and cost.

The first step is to prepare the statement using the prepare command, then type the statement name. This can be a custom name. In this instance, you can call the statement, GetOrderStatement. Then type the from keyword follow this syntax with a select statement in a single quotation marks.

The select statement extracts the required data from the order stable against a specified value. However, you might have noticed that the value is currently unspecified because it requires an input value. Later, you can enter any value you like to process the statement with any argument. You do not have to wait for MySQL to compile and powers the statement, click Enter to execute the statement.

The database returns the output result, a confirmation message that declares statement prepared. The get order statement is now ready to use. Next, you'd need to declare a variable named order ID and assign it a specific order ID. Let us use an ID of 10.

Now, you can use this variable with the prepared statement. First, type the execute command followed by the statement name. This command is used to execute prepared statements. Next, type the using keyword followed by the variable name.

The using keyword specifies the variable value to be passed to the parameter in the prepared statement. So this prepared statement is basically instructing MySQL to extract the client ID, product ID, quantity, and cost data associated with the order ID 10 in the orders table. Click Enter to execute the query and return the results. Although this prepared statement targeted the order ID 10, you could also target any other order ID from the orders table.

The statement can extract the related data, and it doesn't have to wait until it is compiled by MySQL. You should now be able to create and execute a prepared statement in MySQL. Well done.
