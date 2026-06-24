# MySQL aliases

- **Course:** Database Structures And Management With
- **Module 1:** Intro to MySQL
- **Lecture #:** 6
- **URL:** https://www.coursera.org/learn/database-structures-and-management-with-mysql/lecture/4mXmD/mysql-aliases
- **Extracted:** 2026-06-22 19:37:35

---

Little Lemon restaurant has run into some problems with their database. Some of the table and column names in the database are too long, which is causing issues with the output of queries. They need to find a way to generate results that are simpler to use, read, and understand. Fortunately, they can solve these issues with MySQL aliases.

Over the next few minutes, you'll discover how Little Lemon can make use of MySQL aliases and by the end of this video, you'll be able to; demonstrate an understanding of the concept of an alias in a database, identify examples of situations in which it is beneficial to use aliases, and demonstrate the use of alias in MySQL queries. But first, you might be wondering what is an alias in the context of SQL? SQL aliases are used to provide database columns and tables with temporary names. These temporary names make it simpler to use, read, and understand the output of the database.

For example, Little Lemon can use aliases to shorten the names of tables and columns in their database. There are three common situations in which it's useful to consider an alias. An alias can be used to rename a table or column whose original name is too long or technical. It can be used with a concatenation function to combine an output into one column instead of two.

You can also use an alias to create distinct table names when dealing with multiple tables. However, it's important to bear in mind that the syntax for creating and using an alias can change depending on which of these issues you're attempting to resolve. Let's take a few minutes to review an example of the syntax for each scenario, beginning with renaming tables. To rename a table, you need to use a select statement which begins with the select keyword.

Then type the original column name followed by the alias. Both must be separated by the AS keyword. The AS keyword creates the alias. You can also include other columns in the table with each separated by a comma.

Then write the FROM keyword followed by the table name. If your table requires multiple aliases, then write out each column name and use the AS keyword for each column you need to create an alias for. For example, in their client orders table, Little Lemon can use an alias to rename lengthy columns, like client order information to just orders. Next, let's review the syntax for a concatenation function that combines an output into one column instead of two.

The select command is used to retrieve data. This is followed by the concat function, which concatenates or combines the information extracted from the column names placed in parentheses. These names must be separated by commas and a pair of double quotation marks. The quotation marks split the output by creating an empty space between the concatenated values.

The AS keyword is then added followed by the name or alias you want to assign to the new concatenated column, and the FROM keyword specifies the table SQL most extract the data from. Little Lemon can use a concatenation function to combine the values contained in the first and last name columns of their client details table. These values are then placed in a new concatenated column called client names. Finally, let's explore the syntax for querying multiple tables.

The first thing to note when querying multiple tables is that you can use a one-character alias to represent each table. For example, if you're querying two different tables, then you can use x for Table 1 and y for Table 2. The syntax then begins with a select command followed by the tables and columns to be queried. You can query columns using dot notation such as x.column1 to query Table 1, Column 1, or y.column2 for Table 2, Column 2.

Next, add the FROM keyword. Then type the original name of each table alongside its alias with both are separated by the AS keyword. Finally, add a where clause and conditions as required. For example, perhaps you're querying prices in an online store database.

I want to return a list of items that are less than $12 for Table 1, and five dollars for Table 2. Those are the three main instances in which MySQL alias can be used along with their related syntax. Now that you're familiar with the concept of MySQL alias, let's see if you can help Little Lemon with their databases. Little Lemon restaurant has a table in their database called Food Orders Delivery Status that keeps track of food orders.

The table has two columns called date food order placed with supplier and date food order received from supplier. However, these column names are too long and complex, so they need to be simplified to make the database more efficient. You can use aliases to simplify the output so that the column names are easier to read and understand when queried. Begin with a select statement and target the order ID column.

Then rename the date food order placed with supplier column as date order placed and rename the date food order received from supplier column as date order received. Notice that there are double quotation marks used for order date received because the alias name contains a space. In other instances, you can declare the alias without the use of quotation marks. Finally, type a FROM keyword followed by the name of the table.

Then click ''Enter'' to execute the query. The output now shows the alias names instead of the original column names, which makes it much easier for Little Lemon to track food orders. However, you can make this table even more efficient. For instance, you could concatenate order ID and order status into one column instead of two.

As you learned earlier, you can use a SQL alias with functions. Write the statement as follows. Begin with a select command and then the concat function. Then place the columns you want to concatenate in a pair of parenthesis.

You should also make sure that you include quotation marks to split the output. Next, use the AS keyword to create the alias. In this instance, you can call the alias column order status, then use the FROM keyword to identify the table. Finally, hit ''Enter'' to execute the query.

The output shows the new order status column with the concatenated info. Finally, let's review how to work with multiple tables in the database. The restaurant has divided their menu into two tables called starters and main courses. Both tables show the names of the meals available to order and the respective costs.

As part of a new promotional campaign, Little Lemon want to promote starters that cost seven dollars or less and main courses that cost $15 or less. So you need to query these tables and identify the meals that match these prices. In this instance, you can use a one-character alias of s to represent starters, and you can use c to represent main courses. Add these aliases into a select statement and use dot notation to request the name and cost of the meals.

Then use the FROM keyword to identify the tables and the AS keyword to create aliases for each one. Courses is c and starters are s. Finally, add a where clause and specify the condition. The condition returns all starters less than seven dollars and all main courses less than $15.

Finally, press ''Enter'' to execute the query. SQL generates an output that shows all related costs in one table. All issues with the Little Lemon's database have now been solved using MySQL aliases. Thanks for your assistance.

Little Lemon's database is now more efficient to use and they've identified some great meals to include in their next promotional campaign. With the skills you've gained from these tasks, you should now be able to; demonstrate an understanding of the concept of an alias in a database, identify examples of situations in which it is beneficial to use aliases, and demonstrate the use of alias in MySQL queries. Great work.
