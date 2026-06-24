# MySQL UNION operator

- **Course:** Database Structures And Management With
- **Module 1:** Intro to MySQL
- **Lecture #:** 11
- **URL:** https://www.coursera.org/learn/database-structures-and-management-with-mysql/lecture/5WtXa/mysql-union-operator
- **Extracted:** 2026-06-22 19:38:29

---

Lucky Shrub are filing their end of year tax returns and must provide information on all employees that they have hired over the last 12 months. There are several full-time employees in the business, and there are several part-time employees who were recently hired to help with the holiday season. But the records for the full-time and part-time employees are stored in separate tables. How can Lucky Shrub combine these records into one table?

They can use the MySQL UNION operator. Over the next few minutes, you'll discover how the UNION operator works and by the end of this video, you'll be able to demonstrate an understanding of the UNION operator and explain how the UNION operator is used in MySQL. Let's begin with a definition of the UNION operator. The UNION operator is used to combine result sets with multiple statements in the same query.

For example, you can use the UNION operator to join two SELECT statements in order to combine their results sets and present as one table. How does the UNION operator work? Let's look at the syntax and find out. You begin with a SELECT statement, followed by the names of the columns that must be queried.

The FROM keyword is then used to target the table in which the records are located. Next, you add a UNION operator, followed by a SELECT statement that queries the required records from the second table. The UNION operator essentially creates a union between the two SELECT statements. There are a few best practices that must be observed when creating SQL SELECT statements with a UNION operator.

Every SELECT statement must have the same number of columns. All related columns have similar data types, and all related columns must have the same order in every SELECT statement. But what about cases where the same value exists in both tables but appears only once in the combined set of results like a name or location? This happens because the UNION operator only returns distinct values from the targeted tables.

To list all values including duplicated data, you can use the ALL keyword. The use of the ALL keyword after the UNION operator ensures that all values remain, even duplicated ones. Let's explore our working example of the union operator. As you saw earlier, Lucky Shrub need to gather information on all employees that they have hired over the last 12 months.

But the data for their full-time and part-time employees is stored in separate tables. Let's help them out. Lucky Shrub need to combine the records from two tables into one using the MySQL UNION operator. Both the full-time employees and part-time employees' tables include the same four columns; EmployeeID, FullName, ContactNumber, and Location.

Lucky Shrub need to query the full names and addresses or locations of all employees. To combine the results from both tables, you can write two SELECT statements that target the full name and location columns. One statement targets the full-time employees' table, the other targets the part-time employees' table, and a UNION operator is placed in between both statements to combine the results. Before executing these statements, you must check that each of these SELECT statements includes the same number of columns.

In addition, all columns must contain the same data types and must be placed in the same order in both statements. Finally, click "Enter" to execute the query. The output places the results of both SELECT queries into the one table that contains two columns; FullName and Location. These columns hold all required records for all Lucky Shrub's part-time and full-time employees.

However, Lucky Shrub has two employees named Julia Marr, one who works part-time and another who works full-time. But only one Julia Marr appears in the combined set of results. This is because the UNION operator only returns distinct values. Yet it's interpreted both instances of Julia Marr as a duplicated value.

Fortunately, you can use the UNION operator to generate an output that contains both employees. Just write the same SELECT statement once again with a UNION operator in-between, but this time place the ALL keyword after the UNION operator. As you learned earlier, the ALL keyword ensures that the output retains all results from both tables even if there are duplicate values. Finally, click "Enter" to execute the query.

The output is then generated onscreen and it contains both instances of Julia Marr. Thanks to the UNION operator, Lucky Shrub now have all the information they need. Having helped them out, you should now be able to demonstrate an understanding of the UNION operator and explain how the UNION operator is used in MySQL. Well done.
