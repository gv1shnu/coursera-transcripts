# MySQL COPY TABLE

- **Course:** Database Structures And Management With
- **Module 2:** Updating databases and working with views
- **Lecture #:** 19
- **URL:** https://www.coursera.org/learn/database-structures-and-management-with-mysql/lecture/Hu6jB/mysql-copy-table
- **Extracted:** 2026-06-22 19:39:55

---

Lucky Shrub are planning an overhaul of their database. In preparation, they want to create copies of their data to keep it safe during the rebuild. They can complete this task using the copy table process. Over the next few minutes, you'll learn about the process for copying a table and then help Lucky Shrub up to copy tables in their database.

By the time you complete this video, you will have learned how to: copy data from an existing table to a new table within the same database, copy a table to a new location while ensuring it retains its constraints, and copy data from an existing table to a new table from a different database. These tasks are carried out using the CREATE TABLE syntax. However, before you explore this syntax, let's take a moment to review the process for copying tables. It's important that you're familiar with the process before you begin copying tables.

You first need to identify the database and the table you want to copy the data from. Next, determine the columns you want to copy. Either all columns or just some of them. Then use the CREATE TABLE statement to build a new table with a relevant table name.

Finally, use the SELECT command to structure the new table by specifying the columns you want to copy data from. Now that you're familiar with the process steps, let's review the CREATE TABLE syntax. The copy table SQL statement begins with the CREATE TABLE command, followed by the name of your new table. Next, write the SELECT command, then identify the columns to be copied.

You can copy one, several, or all columns. Finally, use the FROM command followed by the name of the existing table you want to copy. But what about copying a table between two different databases? Once again, begin with a CREATE TABLE command.

However, in this instance, you must use dot notation to identify the names of the new database and table. Then use the SELECT command to select the existing table's columns. Finally, use the FROM clause. Then follow this with another instance of dot notation that identifies the names of the existing table and database to be copied.

Lucky Shrub are now ready to begin copying tables in their database. They want to carry out the process as follows. First, they need to copy the clients table to a new table called ClientsTest in the same database. They then need to copy a few select columns to the table.

Next, they need to make sure that all constraints from the original table were copied over to the new one. Finally, they want a copy a table from one database to another. Use your new knowledge of the copying tables process to help them out. First, let's review the clients table in the Lucky Shrub database by typing select asterisk, from clients, then click "Enter" to execute the query.

This generates the client table onscreen. The table contains four columns: ClientsID, FullName, ContactNumber, and Location. For the first part of the test, Lucky Shrub need to copy the clients table to a new table called ClientsTest in the same database. You can perform this task using the create table SQL query to create two statements.

In the first statement, use a basic create table clause to create the new ClientsTest table. In the second statement, type the select command with the asterisk as shorthand for all columns. Then type the existing table name, which is clients. Finally, click "Enter" to execute the query.

This query copies all columns and their data from the clients table to the new ClientsTest table. To check that the query was successful, you can type the following statement. Select asterisk from ClientsTest. Then click "Enter" to execute.

This query generates the ClientsTest table, and the table contains a copy of all the data as required. Next, Lucky Shrub need you to copy partial data only. They need to copy the FullName and ContactNumber columns from the clients table to another table. Begin with a create table statement, followed by the name of the new table, which is ClientsTest2.

Then use a select command. But in this instance, specify just the FullName and ContactNumber columns. Type the from keyword followed by the name of the existing table, which is clients. Finally, use the WHERE clause in the select statement to specify a condition.

In this case, copy the data only for those employees who live in Pinal County. Click "Enter" to execute the query. The queries output shows the ClientsTest2 table and the table contains a copy of all the data from ClientsTest for all employees from Pinal County. The test worked.

Next, you need to make sure that all constraints from the original table were copied over to the new one. It's important to remember that copying data using the methods you've encountered so far doesn't copy the key constraints. You can check the constraints on the original table by typing and executing the statement. Show columns from clients.

The query generates the clients table. The table structure shows all columns with the key constraints set for the ClientID and ContactNumber columns. Now let's check for these constraints on the ClientsTest table by typing and executing the following statement. Show columns from ClientsTest.

This statement shows the ClientsTest table. The table is missing the primary and unique keys defined in the original table. How can you copy these keys? You can use the following statement.

Create table ClientsTest3 like Clients. The like keyword creates an exact copy of the existing table structure. Press "Enter" to execute the statement, then type and execute the following SQL statement to display the new table structure. Show columns from ClientsTest3.

The output shows an exact copy of the initial clients table and all the key constraints have been copied as expected. Your final task is to copy the Clients table from the Lucky Shrub database to the new test database. Begin with a create table statement. Then specify the new database and table names as testDB.ClientsTest.

Type select, asterisk, to instruct SQL to copy all data. Finally, add the from keyword followed by the existing database and table names which are Lucky Shrub.Clients. Click "Enter" to execute the query. Now you just need to check that the query was successful by moving into the test database.

Type testDB, then show tables to reveal all tables in the test database. This statement reveals all the tables created in the test database, including the ClientsTest table you just copied over from the Lucky Shrub database. The table contains all the data from the original one. Lucky Shrub now have all the required copies of their tables in their database.

You should now be able to: copy data from an existing table to a new table within the same database, copy a table to a new location while ensuring it retains its constraints, and copy data from an existing table to a new table from a different database. Great work.
