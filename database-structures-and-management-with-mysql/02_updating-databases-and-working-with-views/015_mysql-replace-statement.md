# MySQL REPLACE statement

- **Course:** Database Structures And Management With
- **Module 2:** Updating databases and working with views
- **Lecture #:** 15
- **URL:** https://www.coursera.org/learn/database-structures-and-management-with-mysql/lecture/dLFxx/mysql-replace-statement
- **Extracted:** 2026-06-22 19:39:11

---

Lucky Shrub Gardening Center are hiring some new employees. Once these new employees have been hired, the company then needs to add their contact details to the database. Some of these contact details must also replace those of employees who've recently left. The Replace command is the best method for Lucky Shrub to make these changes.

In this video, you'll learn how the Replace command can be used to help Lucky Shrub make these changes. Once you've helped Lucky Shrub, you'll then know how to explain how the Replace command works in a MySQL database and demonstrate an understanding of the Replace command by inserting or updating data. Let's begin with an overview of the Replace command. The Replace command is used to insert or update data in a table.

However, unlike the standard Insert and Update commands, Replace first checks for a duplicate key. If found, it deletes the existing record and replaces it with the new one. Now that you know what the Replace command is used for, it's time to look at the syntax. But first, let's quickly recap the syntax for the Insert command.

Its similarity to the Replace command should help you to understand the Replace command better. You should be familiar with the Insert Into command from the previous course. With this command, you instruct SQL to insert new values into designated columns within your chosen table. The Replace command works in much the same way.

You type out your table name, column names, and values just like before. The only difference is that you must begin the statement with a Replace command. You can also use Replace command with the set keyword. The set clause assigns a value for the selected column, but without using the where clause to specify the condition.

In other words, it locates the required record of data, then replaces the values with a new set. If you don't specify a column value in the set clause, then the Replace command uses a default value or sets the value to null. The Replace command is a complicated concept, and its similarity to other commands can be confusing. To help you further, let's take a moment to visualize how the Replace command works.

As you just learned, the Replace command first checks if the new record of data already exists in the table by checking the primary or unique key of existing records. If there's no matching key, then Replace works like a normal insert statement and adds the new data. If a matching key is found, then the command deletes the existing record and replaces it with a new one. Now that you're familiar with how the Replace command works, take a few moments to see if you can help Lucky Shrub insert and replace new and existing employee records in their database.

Lucky Shrub's employee contact records are stored in the employee's contact info table. The table consists of three columns: the employee ID, which is the primary key, the contact number, and email address columns. You need to insert a new record of data for the new employee, Seamus Hogan, with the following details. An ID equal to 1, a contact number, and then email address.

You can add this data to the table using the standard Insert command. Just type Insert Into, followed by the table and column names. Then, add the values to be inserted into each column, ID, contact number, and email address. Click "Enter" to execute the query.

The new employee record is added to the table. You can do the same with the Replace command for the employee Thomas Eriksson. Begin with the Replace Into command, followed by the table and column names to be updated. Then, use the values keyword and list the values to be added to the table for Thomas.

These values are as ID, contact number, and email address. Click "Enter" to execute the query. You can then use a Select statement to check the table's records. The output shows that Thomas's contact details are now in the table as are those of Seamus.

However, Seamus has decided to leave Lucky Shrub to work for a rival gardening center. So you now need to replace his details with those of a new employee, Maria Carter. You can try updating the table using the Insert command. Type an Insert Into statement just like before and assign Maria an ID of 1 in your statements values, alongside her contact number and email address so that her records replace those of Seamus in the table.

Then, execute the query. But it looks like SQL can't execute this query. Instead of adding Maria's details to the table, it's returned an error message warning of a duplicate entry. This is because you're trying to assign Maria an ID of 1.

But this ID is already assigned to Seamus as a primary key value. The primary key must always have a unique value in each row of the table. Otherwise, MySQL returns an error message. So how can you replace Seamus's records with Maria's?

Type the statement again, but this time use the Replace command instead of Insert. Then click "Enter" to execute the query. MySQL has accepted the statement with no errors. Let's query the table to make sure it contains Maria's records.

Type a Select statement and from keyword followed by the table name. Then click "Enter" to execute the query. The output returns the contact details for Maria and Thomas. MySQL has replaced Seamus's records just like you instructed.

There's one more task to complete. Maria has recently changed her contact number, so the number also needs to be updated in the table. You can use the Replace commands to update the record of data. Type, the Replace command and the table name.

Then, use the set clause with Maria's employee ID of 1, followed by the new value, which is her contact number. But make sure that you set values for all columns. Otherwise, they'll be set to null or default values. Press "Enter" to execute the query.

You can use a Select statement to check the table and confirm that Maria's details were updated. Thanks to your efforts, Lucky Shrub's employee contact info is now up to date. You should now be able to explain how the Replace command works and demonstrate the Replace command by inserting or updating data. Great work.
