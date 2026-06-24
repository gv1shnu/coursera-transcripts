# MySQL CREATE VIEW

- **Course:** Database Structures And Management With
- **Module 2:** Updating databases and working with views
- **Lecture #:** 22
- **URL:** https://www.coursera.org/learn/database-structures-and-management-with-mysql/lecture/t41NM/mysql-create-view
- **Extracted:** 2026-06-22 19:40:27

---

Lucky Shrub have had particularly good sales so far this year, they now need to identify the top three best-selling products to make sure they have enough quantity in stock for the next few months. There's a lot of data to parse through in their database so they've decided the easiest way to identify the best-selling products is with the use of a virtual table or view. In this video, you'll explore views and then use what you've learned to help Lucky Shrub. By the end of this video, you'll be able to explain the concept of views in database and demonstrate how to create, rename, and drop views in MySQL database.

Let's begin by developing an understanding of what database engineers mean by the term views. Views are virtual tables created from one or multiple tables depending on the requirements. The view presents a table interface that lets the database users access and manipulate the data within the table using MySQL. Why do database engineers use views?

Let's look at some common use cases. Views can be used to create a subset of a table's data. For example, a table might have seven columns but you only need data from three, so you could create a subset from these three columns. Views can also be used to combine data from multiple tables.

You might need to query two columns from one table and four from another. You can use views to combine both sets of columns into one virtual table. Now that you understand what views are, let's review the syntax. The syntax begins with the CREATE command followed by the VIEW keyword and the name of the view or virtual table.

The AS keyword is then used to define the view table functionality. Next, use the SELECT command to specify the columns the table must be built from. You can specify these columns using dot notation, making sure to include both the table and column name. For example, table1, column1 to select the first column in the first table.

Then use the FROM keyword to specify the tables that the data must be extracted from. Finally, you can use the WHERE clause and a condition to set data order and filtering rules. That's how you can create a view by extracting data from one table. However, creating a virtual view based on multiple tables requires a bit more effort.

Let's find out more. When creating a view from multiple tables, much of the syntax remains the same. The key difference is after the SELECT command. You must list the columns that you require from both tables using dot notation.

You then need to create an inner join after the FROM keyword in which you join the two tables together. Then use the ON keyword to determine the matching columns used to create the JOIN. Let's take a closer look at the use of dot notation. Dot notation is used to link columns with tables.

This is particularly important if you're dealing with multiple tables. Multiple tables might give rise to a potential conflict in names. For example, two tables could use the same name for a specific column. To avoid this, you can establish a link between each column and its respective table by placing a dot in between them.

However, dot notation is optional if your query is only dealing with one table. The view syntax presents a clear five-step process for creating a virtual table or view. Create the virtual table using the create view syntax. List the columns to be moved from the original table to the virtual one.

Specify the original table from which data must be extracted to create the view. Set the conditions and finally, set the data order and filtering rule. Now that you've been introduced to what a view is and been shown how to create one, it's time to see if you can assist Lucky Shrub. As you discovered earlier, Lucky Shrub need to identify their top three best-selling products with the use of a virtual table or view to make sure they have enough quantity in stock for the next few months.

Let's use your new knowledge of views to help them out. You can create a virtual table or view for Lucky Shrub using the data in the orders and products tables in their database. Let's take a moment to familiarize ourselves with these tables before using them to create the view. The orders table has six columns that include information about the OrderID, ClientID, ProductID, Quantity, and Cost.

While the products table has three columns that include information about the ProductID, Item name, and Price. Lucky Shrub want to identify their top three best-selling products, so to create the view you only need data from the item name column from the products table, the order quantity, and total cost columns from the orders table. As you learned earlier, the key steps for creating the view lie in the syntax, so write create command and the view keyword. Then write the name of the view which you can call Top3Products, include the AS keyword to define the view table's functionality.

Then use the Select command and dot notation to target the required columns for your view. Next, use the from keyword to identify the tables. However, the view is created from two separate tables, so you'll need to join these tables together using inner join based on their matching ProductID value. Finally, use order by to list the products based on the highest cost, with only the Top3Products appearing onscreen in descending order.

Execute the query to generate a new virtual table called Top3Products with the three required columns, item, quantity, and cost. You can now query this virtual table just like any other normal table using the following basic SQL statement, select asterisk, from Top3Products. The table prints the top three best-selling products along with their name, quantity, and cost. Why don't you try rename the table to something shorter, like TopProducts?

You can rename a virtual table using the MySQL rename command. To rename the table write rename table, Top3Products to TopProducts. This syntax is used to rename all types of tables in MySQL. In this statement, you just specify the view's current name after the rename table clause.

Then you specify the view's new name after the TO keyword. Finally, click "Enter" to execute the query. The table has now been renamed TopProducts. What if you no longer require a virtual table?

You can just drop it using the SQL drop command, drop view, TopProducts, click "Enter" to execute the query. The view has now been removed and there's no impact on the original table it was created from. Thanks to the view, Lucky Shrub now know what their top three best-selling products are, and they can make sure that they have enough quantity in stock for the next sales period. You should now be able to explain the concept of views and database and demonstrate how to create, rename, and drop views in MySQL database.

Well done.
