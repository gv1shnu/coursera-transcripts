# MySQL ALTER TABLE

- **Course:** Database Structures And Management With
- **Module 2:** Updating databases and working with views
- **Lecture #:** 18
- **URL:** https://www.coursera.org/learn/database-structures-and-management-with-mysql/lecture/NNVFw/mysql-alter-table
- **Extracted:** 2026-06-22 19:39:44

---

Lucky Shrub Gardening Center has bought new heavy machinery, but it can only be operated by qualified employees. The business has a database table called machinery that records the contact info of all qualified employees. However, the table has issues with its constraints and it's also missing some key information. Lucky Shrub can fix these issues by making alterations to the table using the ALTER statement.

Over the next few minutes, you'll learn about the ALTER statement and then use what you've learned to help Lucky Shrub ALTER their database. And by the end of this video, you'll be able to add, delete and modify columns and constraints in an existing table. Let's begin with an overview of the ALTER statement and its syntax. You might often encounter tables in a database that contain missing columns or constraints or their existing columns and constraints may need to be modified.

You can use the ALTER TABLE statement to make these changes. The ALTER TABLE statement is often used alongside different SQL commands. Here's a quick overview of some common commands used with the ALTER TABLE statemen. The MODIFY command is used to target specific columns and instruct SQL to make changes to them.

The ADD command can be used to add a new column to a table and the DROP command can be used to drop or delete a column from the table. So, how are these commands used to make alterations to a table? The ALTER TABLE statement begins with the ALTER and TABLE clauses followed by the name of the table to be altered. Next, insert a MODIFY command followed by the name of the column to be altered and the changes to be made.

For example, you can change the columns data type and add a not null constraint. Then repeat the MODIFY command for all other columns you want to alter. You can also alter a table by adding another column. Just use the ADD column command followed by the name of the new column.

To remove a column from a table, just use the DROP command followed by the name of the column you want to drop or delete. Now, that you're familiar with the ALTER TABLE statement, see if you can help Lucky Shrub make the required changes to their table. The task that Lucky Shrub need to complete are as follows. Set the employee ID column as the primary key, change the column constraints and add a new column to the table.

Let's get started. Lucky Shrubs machinery table includes four columns, employee ID, full name, phone number and county. The table is missing a primary key. Fortunately, the employee ID column is the perfect candidate because all values are unique.

To set this column as the primary key, you can write an ALTER TABLE statement. Add the ALTER Table clauses followed by the table name, then write the MODIFY command and the employee ID column name. Next, set the data type as VARCHAR with a character limit of 10, then set a NOT NULL value to ensure that the column always contains data. Finally, add the primary key value to the column.

The employee ID column is now the table's primary key. It looks like each column in the table is also set to accept NULL values. This means the table can contain empty fields or rows which is poor practice in a database. So to change all columns to NOT NULL, you can write another ALTER TABLE statement.

In fact, you can use the same statement as before and just add a new line for each column. For the full name and county columns, you can write the following syntax. Add a MODIFY command, set the VARCHAR data type to 100 and a value of NOT NULL. For the phone number column, you can write the same syntax but with integer and UNIQUE values.

This means that the column now accepts UNIQUE numeric values only. This avoids any duplicate values. To view the new table structure, write the following statement. Show columns from machinery.

This queries, output shows that the employee ID is now set as the primary key. The phone number is a UNIQUE value and all columns are set as NOT NULL. Now, your final task is to add a new column to the table. Lucky Shrubs Machinery can only be operated by employees aged 18 and over.

So, the company needs to identify each employee's age and determine who is old enough to operate the machinery. There is currently no age column in the table, so you'll need to create it and add a constraint to ensure every new employee added to the table is at least 18 years old. You can write the statement as follows, ALTER TABLE followed by the machinery table name, then the ADD column command. Next, call the new column age and assign it an integer value.

Finally, use the CHECK function to limit the values in this column to at least 18 or more. Then click enter to execute the query. To view the table's new structure, write, show columns from machinery. The output now displays the machinery table with a new age column.

Thanks to your help. All the required changes have now been made to Lucky Shrubs Machinery table. You should now be able to use the ALTER TABLE clause to add, delete and modify columns and constraints in an existing table. Great work.
