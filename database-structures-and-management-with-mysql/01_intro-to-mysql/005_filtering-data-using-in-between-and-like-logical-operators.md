# Filtering data using IN, BETWEEN and LIKE logical operators

- **Course:** Database Structures And Management With
- **Module 1:** Intro to MySQL
- **Lecture #:** 5
- **URL:** https://www.coursera.org/learn/database-structures-and-management-with-mysql/lecture/yxmf5/filtering-data-using-in-between-and-like-logical-operators
- **Extracted:** 2026-06-22 19:37:24

---

You might already be familiar with filtering data using the AND and OR operators. But what if you need to perform more complex data filtering tasks? Like filtering data based on a pattern. You can use more logical operators, such as IN, BETWEEN, and LIKE.

By the end of this video, you'll be able to identify the IN, BETWEEN, and LIKE logical operators and explain how they're used. And explain how wildcard characters can be used with logical operators to filter data. Let's begin with a review of the IN, BETWEEN, and LIKE operators. The IN operator lets you specify multiple values in the WHERE clause.

The BETWEEN operator selects values within a given range, these values can be numbers, text, or dates. And the LIKE operator is used to filter data based on pattern matching. Let's look at the syntax for the IN operator. The IN operator requires slightly different syntax than a typical SELECT filter statement.

After the WHERE clause, you must type the column name to which the IN operator is applied. You then need to add the IN operator and you must also include the set of values within parenthesis. If the specified columns value of a record matches with any value in the set, then that record will be included in the query results set of the select statement. The IN operator is like a shorthand for multiple OR conditions.

You also can use NOT IN to filter the opposite results of those you receive from the IN operator. Next, let's review the BETWEEN operator. For the BETWEEN operator, you must also specify the column name after the WHERE clause. The BETWEEN operator is then applied along with the two required values.

These two values mark the boundary of a range. In other words, they're the beginning and ending values of the range. The operator then selects values within this given range. The values that can be used with the BETWEEN operator include numbers, text, and dates.

If the specified columns value of a record falls within the value range specified here, that record will be included in the query results set of the select statement. Finally, let's look at the LIKE operator. The LIKE operator is used to filter data based on pattern matching. The operator is placed after the WHERE clause and specified column name.

A pattern to be matched against the column data is then added. This pattern can be written using what I refer to as wildcard characters. The first of these is the percent sign which represents zero, one, or multiple characters. The second is the underscore sign which represents one single character.

For example, a pattern could be written as g_ _% within a pair of single quotes. As you've just discovered, each underscore represents one single character while the percent sign is zero, one, or more characters. So this pattern searches for values that start with the letter g and are at least three characters in length. If the specified columns value of a record matches the given pattern, that record will be included in the query results set of the SELECT statement.

Let's look at a demonstration of these operators in the Lucky Shrub database. Lucky Shrub are performing a review of their accounts. They need to generate specific details on their customers and the purchases they've made. They can complete this task by filtering data with the use of the IN, BETWEEN, and LIKE logical operators.

In Lucky Shrub's database, is a table called customer purchases. This table contains the data Lucky Shrub need to complete their queries. The data is divided into the following four columns. Customer ID, customer names, customer locations, and purchases, the value of each customer's individual purchase.

First, Lucky Shrub need to use the MySQL IN operator in the WHERE clause to identify customers from the location Gila county who've made purchases of over $2000. You might already be familiar with filtering data using the OR operator. The IN operator is like a form of shorthand for multiple OR conditions. You can get the same result as the OR example by using the IN operator.

To extract the required data using the IN operator, write a basic select statement as follows. Begin with SELECT all data from the table customer purchases, next type the WHERE clause then the first condition as follows. Purchases column, the IN operator, and the figure of 2,000. Then within parenthesis specify the set of values separated by a comma.

Gila County and Santa Cruz County. When run, this query returns three records of customers. These are the same results as the OR operator returns. Now let's check out how the MySQL BETWEEN operator functions in the WHERE clause.

In this example, Lucky Shrub need the details of customers whose purchases are in the range of $1,000 and $2,000. Write the SELECT statement as before, then add the WHERE clause. The WHERE clause is followed by the filter column which is purchases. Then add the BETWEEN operator and give the value range.

The range begins with the value 1,000 followed by AND, then ends with the value 2,000. The BETWEEN operator filters out the records that have a purchase value between $1,000 and $2,000 including the beginning and end values. In this case, the BETWEEN operator is a quicker and easier way to filter out the records that have a purchases value greater than or equal to $1,000 and less than or equal to $2,000. Finally, let's see how Lucky Shrub make use of the MySQL LIKE operator.

The LIKE operator is used for pattern matching. When used in a WHERE clause, it searches a column for the given pattern. This means that it filters out data from the table based on the pattern. It's often used in conjunction with wildcards for single or multiple characters.

Let's demonstrate an example using the pattern on the location column. You can filter out the records that have a location value that matches the pattern. Lucky Shrub's pattern must be set to find any values that start with g and are at least three characters in length. First, right the select statement just as you've done before.

Then add the WHERE clause followed by the name of the filter column, location. Finally, add the LIKE operator followed by the pattern, which in this example is g, followed by two underscore characters and a percentage symbol. Press enter to execute the query. The output that's generated contains three values that start with g and are at least three characters in length.

Any values that don't match the pattern have been omitted from the table. Lucky Shrub have completed their data filtering tasks and returned all the required results from their database. You should now be able to combine conditions and filter data using the IN, BETWEEN, and LIKE logical operators. Great work.
