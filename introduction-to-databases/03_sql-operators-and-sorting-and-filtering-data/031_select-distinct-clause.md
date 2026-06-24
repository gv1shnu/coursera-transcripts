# SELECT DISTINCT clause

- **Course:** Introduction To Databases
- **Module 3:** SQL Operators and sorting and filtering data
- **Lecture #:** 31
- **URL:** https://www.coursera.org/learn/introduction-to-databases/lecture/nLBBv/select-distinct-clause
- **Extracted:** 2026-06-22 16:16:03

---

Suppose you have a database that contains the records of college students from all over the world. As part of an annual report, a list of all the different countries these students belong to is required. It's very likely many students will come from the same country. So how can you retrieve the results you're looking for without any duplicates.

Look no further than a select distinct clause. In the next few minutes you learn how to describe the select distinct statement and explain what it's used for, demonstrate how to use it in a sequel query and explain how it interacts with the single column, multiple columns and null values. In a few practical examples, let's start by exploring what the select distinct statement is in its most basic form, distinct as its name. States returns only distinct or different values.

In other words, it returns the results without any duplicates. Let's take a closer look at duplicate values. As you can imagine, columns in a table can often contain duplicate values in a college student records. For example, the country column will likely contain duplicate values as there can be many students who are from the same country.

Let's assume you want to find out which countries the students in the college are from. So that you can get an understanding of which nationalities are represented in the college. You can begin by using a sequel select statement. You can write the select keyword then country followed by the from keyword and the student table name.

Running this select query gives you seven records as the result with multiple duplicate records. In this case there are duplicate records for Australia and the USA. So how can you eliminate these duplicates and retrieve a unique set of results? You can use the select distinct statement.

You can write a select statement just like before but this time distinct after the word select, the word distinct will return all unique values in the table with no duplicates. You can then write the from keyword followed by the student table name. Once you run this statement, the country's now only appear once in the resulting records. All the duplicates have been removed.

This is how the selected stink statement can be used to return distinct values from one column. In this case you've returned distinct values from the country column. No, let's take a few moments to explore the select distinct statement in action. The examples that follow focus on the select distinct statement.

With the use of multiple columns or when applied to a column that has a null value. The student table in this example, I want to write a query to determine which countries are represented by students in different faculties. I can use a select distinct statement as before. But this time I allowed the word faculty before country Running this statement produces six records the science faculty of students from three different countries, as does the engineering faculty.

So with this statement which uses multiple columns, I've generated each unique faculty and country combination. Now let's return to the table once more and examine how select this thing deals with null values and columns. In this example, I have a new student named Julia Smith from the USA. She's not yet been assigned a faculty or school address.

As a result, both fields within these columns assigned to Julia Smith contain a value of null. So let's see what happens when I run the same select distinct statement as a previous example. How does it handle the null values? In other words, what results does it return for Julia?

I said let go and received the same result as the last time. But now there's also a record for Julia with a null faculty value and USA as the country. This is because the distinct clause considers null to be a unique value, So it outputs null and USA is a unique faculty in country combination. In this video, you learned how to use the select distinct statement to eliminate duplicate values in a select query result.

You also observed how it behaves in response to values in a single column and multiple columns and two null values in columns. Great work
