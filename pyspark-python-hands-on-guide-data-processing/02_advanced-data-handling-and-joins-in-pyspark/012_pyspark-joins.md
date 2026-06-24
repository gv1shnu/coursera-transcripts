# Pyspark Joins

- **Course:** Pyspark Python Hands On Guide Data Processing
- **Module 2:** Advanced Data Handling and Joins in PySpark
- **Lecture #:** 12
- **URL:** https://www.coursera.org/learn/pyspark-python-hands-on-guide-data-processing/lecture/15VS4/pyspark-joins
- **Extracted:** 2026-06-20 10:10:59

---

Now, in this session, we would look about what is PySpark Joins. Now PySpark DataFrames have a join method which takes basically three parameters. One is DataFrame on the right side of the join, which fields are being joined on and what type of join that is inner, outer, left outer, right outer or left semi. Now you can call the join method from the left side of DataFrame object.

For example, you have an object name say df1, you can say df1.join in bracket df2, df1.column1 is equal to df2.column1 and you can specify there in single quote inner. Now one of the challenges for working with PySpark is that it's Python and Pandas but with some subtile differences. Now for example, you can't just say DataFrame.column.lower to create a lower case version of the string column. Instead, you will have to use lower in bracket DataFrame.column, so you'll have to use there a lower function instead.

So in this session of PySpark, we would attempt by cementing how join works in PySpark once and for all. I will be using certain examples from the, for the given code wherein we will create certain arrays first, we'll set up some values and do it and then we'll see how it has been used for joins. So first of all, we'll create here say valuesA which is equal to, we are creating here an array. Now here we are giving say pirate then 1, which is the one column or the one row that we have created.

Then we create say monkey and 2, another row we created. Then we create say ninja3 and the last one we create say spaghetti and say food. Now after which we close our square bracket. Then we create table A which is equal to, here we say spark.createDataFrame and in bracket we create or we pass their values A and we give there the column names that we want, that is name and ID both in square.

Now once it is created, now basically we are transferring the data of value A into table A and creating a table with column name and ID. Okay, so now it has created a table A for us. Now similarly we'll be creating say valuesB is equal to, in round bracket we'll give say rutabaga and 1, next value we give say pirate2, next value we give say ninja3 and the last value we give say darthvader4. Now after this again we create here say table B which is equal to, again we say spark.createDataFrame and here again we pass say valuesB and we give here the column name as name and ID.

We just missed it, it is table B is equal to spark.createDataFrame in bracket, valuesB and then in square bracket name ID, okay. So now if we have to view what values are there in table A, we can say tableA.show, we'll get whatever values we have stored in table A, that is the value will be pirate, monkey, ninja, spaghetti with IDs 1, 2, 3 and 4 respectively. So it will fetch and it will give me the values in the data here. Similarly if we say tableB.show, so we'll get whatever table data values you have stored in table B, that is the array values B that you have created, okay.

Now after this we have created or in order to create a data frame in PySpark, you can use the list of structure tuples. Now in this case we have created table A with name and ID. So the spark.createDataFrame takes two parameters, list of tuple and the list of column names that we have given. So the data frame object.show command displays the content of the data frame that you have created.

So the last piece we need to perform is to create an alias for this table, that is giving a short name instead of table A and table B. So the alias like in the SQL allows you to distinguish where each column is coming from. The column are named which are the same if you know if like name is referring table A or table B. So you can say there the alias name dot the column name in that case.

So the alias provides a short name for referencing fields and for referencing the fields after creation of the join table. So now here we say ta is equal to tableA.alias ta. Similarly we say tb is equal to tableB.alias tb. So we have created here the table aliases that is ta and tb.
