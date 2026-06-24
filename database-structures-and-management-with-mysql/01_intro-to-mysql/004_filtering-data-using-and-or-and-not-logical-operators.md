# Filtering data using AND, OR and NOT logical operators

- **Course:** Database Structures And Management With
- **Module 1:** Intro to MySQL
- **Lecture #:** 4
- **URL:** https://www.coursera.org/learn/database-structures-and-management-with-mysql/lecture/YFVBi/filtering-data-using-and-or-and-not-logical-operators
- **Extracted:** 2026-06-22 19:37:13

---

You might already be familiar with using a where clause and a condition to filter data in a database table. But what if you need to specify multiple conditions in a where clause? You can use logical operators to specify multiple conditions or rules. So when the data is filtered, all specified conditions are applied.

By the end of this video, you'll be able to identify the logical and and/or operators and explain how they're used to combine conditions. And develop a working familiarity with the logical not operator and outline how it is used with data filtering. Before you explore how to filter data using multiple conditions, let's take a moment to recap how the where clause works. It's important that you understand it before working with logical operators.

When filtering data in a database table, you can add a where clause to your sequel select statement to specify a condition or rule for how the data should be filtered. A select statement begins with the select keyword or command. You must then specify the data or columns to be queried. You then add the from keyword followed by the table you need to query.

Finally you must add a where clause and a condition. But as you've just learned it's also possible to specify multiple conditions in the where clause. These conditions are specified using logical operators. Let's begin by exploring the and and or operators.

The and operator is used with the where clause to filter data. It checks of all combined conditions meet the value of true and the or operator checks if any of the combined conditions meet the value of true. Let's take a moment to explore the syntax for each of these logical operators. Write the select statement as usual.

However, in this instance multiple conditions are placed after the where clause and combined using the and operator. The statement checks of all these conditions yield the value of true for a record. If so, then that record is included in the results set. With the or operator a record is included in the result set if any of the conditions separated by or is true.

That is if at least one condition yields a true value for a record in the table, then that record is included in the query results set. Next let's look at the not logical operator. The not operator works slightly differently to other operators. It selects a result to be included in the query results set only if the conditions specified in the where clause are not true.

In other words it reverses or negates the results that are returned once the condition is evaluated. To use the not operator, you just type not after the where clause followed by the required condition. Let's take a few minutes to find out how these operators are used over at Lucky shrub. Lucky shrub are reviewing their accounts and need to generate specific details on their customers and the purchases they've made.

They can complete this task by filtering data with the use of logical operators. In Lucky Shrubs databases a table called customer purchases. This table contains the data Lucky Shrub needs to complete their queries. The data is divided into the following four columns, customer id, customer names, customer locations and purchases.

The value of each customer's individual purchase. Lucky Shrub first need to identify customers from the location Gila county who have made purchases of over $2,000. This requires to search conditions. The first is customers who are from Gila county.

And the second is customers who have made purchases of over $2,000. You can retrieve these details by writing a basic select statement as follows. Begin with select all from the table customer underscore_purchases. Next type the where clause than the first condition as follows.

Purchases column the greater than operator and the figure of 2000. Then type the and operator to include a second condition. This second condition targets location column and uses an equal operator to return all results for Gila county. The and operator here combines the two conditions.

It ensures that both conditions are evaluated when filtering data from the table. So your select statement is instructing sequel to select all records from the customer purchases table that satisfy the following criteria. Purchases greater than $2,000 and made by customers in the location of Gila county. For a record to be included in the results set its purchases column must have a value greater than 2000.

If so then the first condition yields a true value. In addition the location column must have a value of Gila county. If this is the case, then the second condition also yields a value of true. And as you just learned the and operator here insists that the results of both conditions are combined.

This is another instance which yields a value of true. So any records that match are included in the result. Any records in the table that do not yield the value of true for both conditions are omitted from the results. Your query is now ready to run.

So press enter to execute. The results set that this query returns contains two records. There are two customers from Gila county who made purchases over $2,000, Benjamin clause and Julie Marr. Now Lucky Shrub need to identify customers who are from Gila county or Santa Cruz County.

The logical operator or can be used to combine multiple conditions in the where clause. So it's perfectly suited to this task. For this query you first need to generate a list of customers who are from either Gila county or Santa Cruz County. So the first step is to write the following select statement.

Select all from customer purchases and then add the where clause. This where clause is then followed by the first condition location equal to Gila county. Then insert the or operator followed by the second condition, location equal to Santa Cruz County. You now have a where clause that uses the or operator to combine the two conditions.

For a record to be included in the result set its location column must have a value of Gila county. If so, then it meets the first condition and yields a true value. Or the location column must have a value of Santa Cruz county. If this is the case, then the second condition yields a true value.

The or operator ensures that at least one of these conditions will yield a true value. Any matching records will be included in the result. A record in the table that does not yield a true value for either condition is omitted from the result. Press enter to execute the query.

In this case the result returns three records or customers. Next Lucky Shrub need to retrieve the details of customers who do not reside in Gila county or Santa Cruz county. They can perform this task using the not logical operator. It's used in a similar way in the where clause of a select statement.

You can write the statement as before but this time type and not operator after the where clause, then list the conditions, location equal to Gila county or location equal to Santa Cruz county. In this query, the conditions have been enclosed in parenthesis because there are multiple conditions. Parenthesis are not required where you have just one condition. The not operator checks the records for values that do not yield a true value for the given conditions.

In other words, records that do not yield a value of true for either of the listed locations. Press enter to execute the query and generate the output. So all the records that have a location value, which is not Gila county or Santa Cruz county are included in the result, the remaining records are omitted. The output shows four records from the customer purchases table.

If you find all these examples and operators a bit complicated, don't worry. You'll review detailed examples of how to use these operators in later videos in this course. For now, you should just be able to identify each of the operators and explain their syntax.
