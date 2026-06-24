# Indexes in MySQL

- **Course:** Advanced Mysql
- **Module 2:** Database Optimization
- **Lecture #:** 14
- **URL:** https://www.coursera.org/learn/advanced-mysql-topics/lecture/WjNH4/indexes-in-mysql
- **Extracted:** 2026-06-22 20:01:56

---

When performing data retrieval, MySQL often scans an entire table even though it only needs to locate specific column values. These queries take a lot of time to execute and place extra load on the database. But my SQL can execute these data retrieval queries faster with the use of indexes that target specific column values. In this video, you'll learn how to use indexes to speed up data retrieval.

Over at Lucky shrub, the sales department needs to retrieve the contact numbers of clients from the database. But there are thousands of clients and phone numbers to sort through. Fortunately, Lucky Shrub can make use of indexes to retrieve this data faster. Before you explore Lucky Shrub's process, let's take a few moments to get a better understanding of indexes.

An index is a data structure that helps to maintain pointers that lead to sorted data. Although you can't see an index within a database, it's still helpful to visualize it as a table that contains two columns, one for pointers and another for sorted data. For example, Lucky Shrub can use an index that lists pointers in one column and the full names of clients as sorted data in a second column. There are two types of indexes used in a My SQL database.

The first is a primary index, also called a clustered index. The second is a secondary or a non-clustered index. A primary index is an index that is stored within the table itself. It's generated automatically once you create a table that contains a primary or unique key, the index enforces the order of rows in the table within the table itself.

A secondary index is created using the My SQL create index statement. The syntax begins with create index, then write the name of the index. A commonly used approach is to write the name of the column you want to create the index on, prefaced by idx for index. Next, use the ON keyword to assign the index to a table.

Finally, add a pair of parenthesis and write a list of columns that the index is to be used against. An index can be created using one or more columns from a table, but you should only create indexes on columns that you'll frequently perform searches against. This is because when you update or insert data into the table, that same data must also be added to or updated within the index, which takes time. Lucky Shrub can use a secondary index to optimize their SQL select query.

They can create an index on the full name column so that client details can be located faster. Now that you're more familiar with the concept of an index, let's see if you can use your new knowledge to help Lucky Shrub. Lucky Shrub need to find the contact number for the client, Jane Delgado. However, there are many client names to search against, and MySQL must scan all rows until it locates the correct name.

Let's quickly review the approach that my SQL usually takes to complete this task. First, type the explain clause to output data that explains how the database executed the query. You can pinpoint potential bottlenecks and sub-optimal queries by reviewing the output. Then type a select statement that selects a contact number from the client's table that matches the value of Jane Delgado.

Press enter to execute the query. The query returns the contact number for Jane Delgado. But as the output results have shown, my SQL had to scan and filter 10 records before it find a matching value. The possible keys column also shows a null value.

This means that there's no key or pointer that can help to make the search easier. The solution is for Lucky Shrub to speed up the search process by creating a secondary index. First type, CREATE INDEX, then add Idx for index to the full name column. Next, target the client's table using the ON keyword, and then place the full name column name in parentheses.

Finally, execute the statement to create the index. To test the efficiency of the index, you can create an execute another explain statement. This time, the output results shows that my SQL only had to locate one row, and it was able to locate possible keys using the index full name index. This means that Lucky Shrub's SQL select query can now search the index and locate the data faster instead of searching through all records in the client's table, and you should now be able to explain what an index is, outline the differences between primary and secondary indexes, and describe the process for creating an index.

Well done.
