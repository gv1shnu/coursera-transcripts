# Date functions

- **Course:** Database Structures And Management With
- **Module 3:** Functions and MySQL stored procedures
- **Lecture #:** 26
- **URL:** https://www.coursera.org/learn/database-structures-and-management-with-mysql/lecture/XSvaB/date-functions
- **Extracted:** 2026-06-22 19:41:10

---

M&G are reviewing some recent orders delivered to the store. They must determine how many days have passed between the days these items were delivered and the day they were ordered. They can complete this task using date functions. In this video, you'll explore date functions and learn how to identify common MySQL date functions and explain how these functions are used to process and manipulate data in the MySQL database.

First, let's find out what date functions are. Date functions are used in a MySQL database to extract time and date values in a range of different formats. M&G often use date functions to identify key time and date details for customer orders. Commonly used date functions that M&G take advantage of include current date, which returns the date in year, month date format and current time, which returns the time in hours, minutes, seconds format.

There's also date format which is used to format a date according to a given format. Once that format is valid in MySQL and date difference identifies the number of days between two date values. Perhaps M&G can use the date difference function to find out how many days have passed between orders, but before you find out how let's take a few moments to explore the syntax for these functions. In most instances, date functions are written as select statements, to extract today's date in year month date format.

Just type, select the current date function and open parenthesis, for the current time in hours, minutes, seconds format type, select the current time function and open parenthesis. However, the syntax becomes a bit more complicated with date format and date difference. To change the date format type, the date format function and open parenthesis within the parenthesis type today's date in standard SQL, year, month date format enclosed in double quotation marks. Then input a valid MySQL format in a pair of single quotes.

You can refer to the further reading section at the end of this lesson for a list of valid formats. To determine the number of days between two date values type, the select command and date difference function followed by parenthesis. Within the parenthesis type, the first and second date values in year, month, date format and ensure both are enclosed in double quotation marks. Then run the query to create the output.

Now that you've reviewed the syntax for date functions let's see if you can use this knowledge to help M&G. M&G need to complete a series of time and date tasks using date functions. The first of these tasks is extract the current date and time to retrieve this data just write select command followed by the current date function and a second select command followed by the current time function. Execute these queries to return the current date and time.

Now M&G needs you to format a date by displaying the month name of a given date. You can do this by using select and calling the date format function, then pass in the order date as the first argument. Type the required format to get the full month name. Finally identify the required table.

Execute the query to create the output. For the final task M&G must determine the number of days between the delivery date and order date for their most recent orders. As you discovered earlier the date difference function can be used to complete this task. The delivery data is contained in the M&G orders table.

The table records delivery data within the following columns, order ID, item ID, quantity, cost, order date, delivery date and order status. To complete this task, you need to focus on the values from the delivery date and order date columns. First write a select query and call the date difference function. Pass the values from the delivery date column as the first argument.

Then pass the values from the order date column as the second argument. Use the from clause to target the M&G orders table and finally use the where clause to filter out the records that do not have a null delivery date. Once executed, the query reveals the number of days between the delivery and order dates for the most recent orders. M&G now know how many days passed between the delivery date and order date for their most recent orders.

And you should now be capable of using common MySQL date functions to process and manipulate data, well done
