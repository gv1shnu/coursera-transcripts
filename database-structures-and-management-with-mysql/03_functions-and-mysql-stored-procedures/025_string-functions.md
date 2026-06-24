# String functions

- **Course:** Database Structures And Management With
- **Module 3:** Functions and MySQL stored procedures
- **Lecture #:** 25
- **URL:** https://www.coursera.org/learn/database-structures-and-management-with-mysql/lecture/6UlWA/string-functions
- **Extracted:** 2026-06-22 19:41:00

---

Magenta and Gallo, or M&G are performing an inventory review. They require a list of item names and their available quantities. They can extract this data from their database using common MySQL string functions. Over the next few minutes, you'll learn how string functions can be used to perform tasks like this.

By the end of this video, you'll be able to identify common MySQL string functions and explain how these functions are used to process and manipulate data in a MySQL database. Let's take a moment to find out what database engineers mean by the term string functions. String functions are used to manipulate string values. For example, adding strings together or extracting a segment of a string.

Here's a few examples of some commonly used string functions. The concatenation function is used to add several strings together. There's also the substring function, which extracts a segment of a string from a parent string. Uppercase converts a string to uppercase, and lowercase converts a string to lowercase.

Next, let's explore the syntax of these strings to find out how they're used in a MySQL database. A very simple example of a concatenation function begins with a Select command, which cause a concatenation function. You then type a pair of parenthesis in which you include the string values to be concatenated. Ensure both are contained within double-quotes and separated by a comma.

Then include the From keyword and the name of the table that contains the data. You can also use the Where clause to specify a condition. A more complex example of the concatenation function might involve extracting string values from two separate tables. For example, the data that M&G require is on two separate tables, items and MG orders.

M&G can pass their arguments in the Select clause, identify the two tables they required in the From clause, and specify the condition in the Where clause so that SQL filters the required data from the combination of the two tables. This example might seem complicated, but don't worry, you'll explore it in more detail in a few moments when you help M&G query their database. Let's continue to review string function syntax with substrings. The syntax of a substring function is similar, but there are three arguments contained within the parenthesis.

The first of these is the string itself. The next one is the start index, the point in the string at which the substring must begin, and length refers to the length of the string portion that must be extracted. Next, let's review the syntax for the uppercase and lowercase string functions. M&G often convert the values in one column of a table to uppercase, and the values in the second column to lowercase.

Here's how they perform this task. An uppercase string function begins with a select statement and uppercase function. In parenthesis, write the name of the column whose values must be converted to uppercase. Finally, instruct SQL which table to target.

A lowercase string function is very similar. The only difference is that the parenthesis most contain the name of the column whose values are to be converted to lowercase. Next, let's look at how M&G make use of string functions in a MySQL database. As you learned earlier, M&G need a list of item names and their available quantities ordered in the format, item name, order quantity.

The item details are in the items table and the order details are in the MG orders table. The items table records information on items in M&G's inventory within the following columns, Item ID, name, and cost. The MG orders table records data on deliveries within the following columns: Order ID, item ID, quantity, cost, order date, delivery date, and order status. You can extract the required data from these tables using the concatenation string function.

Begin with a Select command, then call the CONCAT function and write a pair of parenthesis. Within the parenthesis pass the arguments, name and quantity. These are the names of the columns for your output. These columns stand for the items table and MG orders table respectively.

Then add a hyphen in-between the arguments to combine them. Use a pair of single quotes for the hyphen and ensure all arguments are separated by commas. Use a From keyword to specify the two tables. Finally, use a Where clause to specify a condition that filters our required data from the combination of the two tables, then execute the query.

MySQL extracts a table that shows the total quantity of each item in the inventory. The next task is to retrieve all string values in the order status column of the MG orders table in both upper and lowercase. You can target the string values from the order status column using the upper and lowercase string functions. In your Select query, call the uppercase function and pass in the column name order status.

Then target the MG orders table with the From keyword. Execute the query to retrieve all values in uppercase. To retrieve all values in lowercase, just type the same query again, but this time call the L case function. Execute the query once more to retrieve all values in lowercase.

As part of their next task, M&G are reviewing an order from a client. They need to extract the first name of this client from the client's table. The client's table records key information on clients and stores it in the following columns, the client ID column in which the required client is assigned an ID of one, the client name, address, and contact number columns. You can retrieve the information M&G need by using the substring function to extract the relevant part of the string from the tables client's name column value.

First, write a select statement and call the substring function followed by a pair of parenthesis. Then pass in the client name column as the first argument to the substring function. Pass in the start index as the second argument, which is the letter K or character one of the string, and passing the length of the string portion you need to extract as the third argument. The client's name is Cation, which has six letters long.

So six is our third argument. Then identify the table to target with the From keyword. Finally, add the Where clause with the client's ID as the condition. Run the query to extract the client's first name.

You've now helped M&G to complete their database tasks using string functions, and you should now be able to identify common MySQL string functions and explain how they're used to process and manipulate data. Great work.
