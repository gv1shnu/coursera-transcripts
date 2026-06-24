# Create complex stored procedures

- **Course:** Advanced Mysql
- **Module 1:** Functions and Triggers
- **Lecture #:** 5
- **URL:** https://www.coursera.org/learn/advanced-mysql-topics/lecture/etOGT/create-complex-stored-procedures
- **Extracted:** 2026-06-22 20:00:16

---

You should already be familiar with the process for creating basic stored procedures. In this video, you'll learn how to create more complex stored procedures that require multiple statements. You can learn how these procedures work by helping Lucky Shrub. Lucky Shrub need to determine the current cost of each of their products ahead of their upcoming sale.

They must identify all products that cost less than $50, so they can add an appropriate discount. They need to identify all products that cost more than $50 for further discounts. The required data is stored in the products table in their database. You can help them to complete this task using a complex stored procedure.

First, you need to use a delimiter command, so that MySQL can compile the code in a begin-end block as one compound statement. Type the delimiter command to change the delimiter from the default semicolon to a double forward slash. Click Enter to apply the changes. Next, type the CREATE PROCEDURE command.

Then type the procedure name, GetProductSummary, add a pair of parenthesis and include two OUT parameters along with relevant variables. These parameters output the low price products and high-priced products outside of the procedure. They also store the output values in the variables. Next, you need to create the body of the procedure.

Implement the logic within the begin and end keywords. The logic consists of two select statements followed by a count command that targets the product ID column within the products table. The first statement returns the ID of all products that cost less than $50. The second statement returns all products that cost more than $50.

A double forward slash indicates the end of the query. Click Enter to create the procedure. Finally, change the delimiter to the default semicolon again, so that you can keep using MySQL as usual. Now it's time to execute the procedure.

Type that CALL command followed by the name of the procedure. Then in a pair of parentheses, create the two required variables. You can call the first variable total number of low-price products, and the second variable, total number of high-price products. These variables hold the output results from the OUT parameters.

Click Enter to execute the CALL statement. The procedure retrieves data from the table and passes it to each variable. Now you just need to access the data using a select statement. Type the SELECT command followed by the two variable names.

Make sure the names are separated by a comma. Click Enter to execute the statements. The output results shows the total number of low and high-price products. Lucky Shrub now have all the data they require for their sale thanks to your stored procedure.

Good work.
