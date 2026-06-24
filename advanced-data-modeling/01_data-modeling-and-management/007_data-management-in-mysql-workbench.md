# Data management in MySQL Workbench

- **Course:** Advanced Data Modeling
- **Module 1:** Data Modeling and Management
- **Lecture #:** 7
- **URL:** https://www.coursera.org/learn/advanced-data-modeling/lecture/KUcqS/data-management-in-mysql-workbench
- **Extracted:** 2026-06-22 20:10:36

---

As a database engineer, you'll frequently need to create complex and robust database systems. This can be a difficult task, but luckily you can use tools like MySQL Workbench to create database systems quickly and efficiently. In this video, you'll learn how to use MySQL Workbench to create databases and tables and view, insert and select data. Over at M and G, they need to create a database system to manage staff records.

They've decided to create this new database using MySQL Workbench because of its SQL Editor, GUI, and other useful features. Let's help M and G to create their new database using MySQL Workbench. The first task is to create a new database schema. Choose a MySQL server instance and select the schema menu.

To create a new schema, select the create schema option from the menu pane in the schema toolbar. This action opens a new window. Within this new window, enter mg_schema in the Database Name text field, select Apply. This generates a SQL script called CREATE SCHEMA 'mg_schema'.

You are then asked to review the SQL script to be applied to your new database. Click on the Apply button within the review window if you're satisfied with the script. A new window screen appears asking if you'd like to execute the CREATE SCHEMA statement. Select the Finish button to create the mg_schema.

The schema has now been successfully created and is listed in the schema menu. You might need to select the Refresh icon from the menu to view new schemas. To view information on the mg_schema, select it and click the Information icon. This action brings up a new window that contains several options like Tables, Columns, Triggers and more.

You can also double click the schema name to view a sub menu of all created Tables, Views, Procedures and Functions. If you want to delete the schema, right click the name and select the Drop Schema option. The next task is to create a new table inside the mg_schema to hold the staff information. Right click the Tables option in the sub menu, select Create Table from the list of options that appear.

This brings up a new table form. Enter staff in the Table Name text field. Use the default settings for all other fields. Fill the column details in the middle window as required.

Change the name of the first column to StaffID. Define the column as integer and set it as the primary key using the checkboxes. Add the following remaining columns using the same method, FullName, ContactNumber, Role and Email. Set each column's datatype, then declare each column as either null or not null as required.

Finally, click the Apply button to generate the relevant SQL statement. You should now be able to review the SQL statement that creates the staff table. Click the Apply button to generate the relevant SQL statement. Review the SQL statement and click Apply to execute the statement.

Then select Finish to save your changes. You can now view the staff table in the gm_schema database. Select the Information icon to view the table structure. The Information window appears and shows options for Columns, Indexes and other table elements.

Click the Columns tab to show the column structure. Another method is to type DESCRIBE staff in the SQL Editor, then click the Run button to execute the statement. This displays the details of the staff table structure. Your next task is to create a virtual table in the schema called staff view.

First, right click the View sub menu of the mg_schema. Select the Create View option to open the SQL Editor. Type a CREATE VIEW SQL statement to create the virtual table. Create a basic view to show the staff full names and contact numbers.

Click the Apply button to bring up the Review window. You'll see some SQL code with suggestions that you can either accept or amend as required. For now amend the table by creating aliases for the columns so that they're easier to view when querying the table. Finally, click the Apply button, then click Finish to create the table.

You can now view the virtual table in the mg_schema sub menu. Next, mg needs you to populate the staff table with data. To insert data in the staff table, you'd usually use the Insert SQL statement in the SQL Editor. However, with MySQL Workbench, you can populate the table grid directly.

First, right click the staff table, then select rows from the list of options that appear, enter the mg staff records into the table. Click the Apply button to generate an automatic insert into statement. Then click the Apply button again once you've reviewed the statement in the Review window to execute the statement. Finally, select Finish.

The staff records are now stored in the staff table. Your final task is to query data from the M and G database. You can query the database using MySQL Workbench's SQL Editor. Write a select query that extracts all data from the staff_view table.

This query outputs all data that exists within the staff_view table into a table grid. M and G have now created their staff table and populated it with required data. And you should now be familiar with how to use MySQL Workbench to create databases and tables as well as view, insert and select data, great work
