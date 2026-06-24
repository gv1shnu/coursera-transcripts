# Pyspark Joins Examples

- **Course:** Pyspark Python Hands On Guide Data Processing
- **Module 2:** Advanced Data Handling and Joins in PySpark
- **Lecture #:** 13
- **URL:** https://www.coursera.org/learn/pyspark-python-hands-on-guide-data-processing/lecture/D1kCB/pyspark-joins-examples
- **Extracted:** 2026-06-20 10:11:09

---

So, now let's move on to the actual joins. Now, coming to PySpark inner join, now how will you give inner join in PySpark? So, we give here say inner underscore join is equal to, ta is the table alias now, we say ta dot join in bracket, join the next table that is tb. Here we are giving ta dot name double is equal to tb dot name.

So now in this case, we are seeing what we want to join ta with tb on the common column that is ta dot name is equal to tb dot. So wherever your name parameters would be same, those records would be fetched and displayed if you say inner join dot show. So now in this case, we'll get for pirate and we'll get for ninja, we'll just see the output now. Now, in this case, one pirate will have the ID as one, another will have the ID as two.

Similarly, here one ninja will have ID as three and the next would have ID as three again. So you can see here. Okay, we made a mistake. It is ninka here and it is ninja here.

Therefore, it gave you only one record that is which is common in both the tables. Now, just to show you if you have to translate this to SQL statement, then how we'll have to do is you will have to say it will not run here but just for your information, it is ta dot asterisk comma tb dot asterisk from ta. You give here inner join tb on say ta dot name is equal to tb dot name. That's how you will give if you're using SQL example, okay, but not in PySpark.

So now, similar to this, we can also reference those columns in the latest step now. We'll come to the PySpark left join example. Now how will you give the left join? You can say here left underscore join is equal to ta dot join in bracket.

You give tb then you give ta dot name double is equal to tb dot name comma how that we want as left outer join or left join. Now after we have done this, we can say left join dot show. So we'll get there the record from the left table, all the record and right table only the records that are common there, you will get the values as null for the next table. So see here, wherever they are not common, the value would be null for the second table.

So you can notice that the table A is the left hand side of the query. So you're calling join on the data frame. So it's just like the SQL where the from table is the left hand side in the join. You can also think of it as you're reading from left to right.

So table A is the leftmost table being referenced. So you can use the left or the left outer and the results are exactly the same. It seems like this is a convenience for people coming from different SQL flavor backgrounds. So now notice that how the result now will include null values in this example, because you can use those null values to filter for the for this particular given values.

So now in this case, you can use, for example, say left underscore join dot filter here you can give col in bracket say tb dot name dot is null dot show. So now similarly, we'll see PySpark right join example also. So here we say right underscore join is equal to ta dot join in bracket is ta dot name is equal to tb dot name and how so we are giving here right join and it is right underscore join is equal to ta dot join that is tb then a comma and then we say right join dot show to view it. So again, the code is similar read from left to right.

So table A is the left side table and table B here is the right side table. So if you want to view all the records from table B and return the data from table A when it matches, you choose right or right outer in the last parameter in that case. So we'll see one more that is your full outer join. So for that, we'll have to say full join is equal to ta dot join in bracket tb then ta dot name is equal to tb dot name and how we are giving here in bracket full okay and then we say full outer or a full join dot show.

So we get there all the records from both the tables. So this shows all the records from left table also and all the records from right tables and nulls wherever the two does not match. So now there is one more that is left semi. So now for that you'll have to say say left join in bracket is equal to we say ta dot join here we give tb then we give ta dot name is equal to tb dot name and here we give how is equal to say left semi okay and then we say left join dot show.

So we get only that record which is matching and not from both the tables. So here you will get only the value for name and ID not unlike for left join where you get another value for same values also. So you don't get it from both table you just get it from one table if you use the left semi outer join. So now here if you're just paying attention you will notice that couple of issues at making using PySpark SQL joins a little annoying like for example allies referencing.

If you do not apply an allies to the data frame you will receive an error after you create your join data frame. So with two columns named the same thing referencing one of a duplicate name column returns an error that essentially says it doesn't know which one you have selected. Next example is cross join you can also perform a Cartesian product using the cross join method. Now this is useful if you're looking to repeat every row in a table A for every row in table B.

Next you have that is we have seen this semi that is left semi option. Another you have is joining on multiple columns. Now in the second parameter you can use the ampersand symbol and for the pipe symbol for or between columns. So this is how we have seen what PySpark joins do we have and how can we create multiple examples using those.

So how will you give now cross join you can see the dot cross J capital join in bracket TB. Now this will create a cross join but if you have to create and you have to display then you have to say cross join TB dot show method. So it will create the cross and it will display you the details of the cross join a basically cross join will be total multiplication of all the records of table A with all the records of table B. We also call it as a Cartesian product.

So it will take some time because it will have to multiply all the product details with each other and display you the details in the table format. So whether your records are equal or not equal it doesn't matter when you use cross join you have to display you by default all the documents or all the fields from both the tables using a cross multiplication on it. So you can see this is how you are getting each value of table A will have all the values of table B again second value have all the values of table B third value and fourth value respectively. That's how your cross join would be working right.

So that's it from this session. Thank you very much.
