# More Examples

- **Course:** Pyspark Python Hands On Guide Data Processing
- **Module 1:** Fundamentals of PySpark and Python
- **Lecture #:** 5
- **URL:** https://www.coursera.org/learn/pyspark-python-hands-on-guide-data-processing/lecture/57yO6/more-examples
- **Extracted:** 2026-06-20 10:09:42

---

Now, we will see one example wherein we say, instead of show, we use the collect method. For that, we say again, from pyspark.sql, we are importing spark session and we are saying spark is equal to spark session dot builder in bracket. We give python spark create rdd example, close the double quotes bracket. Then we use the config and we pass here the config name as say spark dot some dot config dot option and we give here say some value.

After this, we have made here one mistake. After spark session, we have to give dot builder and then we have to give dot app name. Then we give here spark create and then we give the config value. Now after this, we give get or create and then we say here, my data is equal to say spark dot spark context.

We use again here parallelize function and this time we pass in square bracket, say one comma two. This has to be again in round. This is the first parameter. Then we have the second parameter.

Then we have the third parameter, then seven, eight and then say nine comma ten. Then we close the brackets and this time we say my data dot collect instead of show. We get the data as it is. It is not displayed in your columnar because we have not given any of the IDs or the column names that we want to display.

Another way in which you can do the operations of your data. Now we'll see extracting a data from a CSV file. For that, we have this dummy one dot CSV file in C drive spark and spark 2.4.2 bin Hadoop 2.7 folder. Now we want whatever data is there in this file should be displayed in our PySpark.

What we'll do is, we'll first say from PySpark dot SQL, we will import spark session. Then we'll say spark is equal to spark session dot builder dot app name and we are giving here say Python spark create RDD example. Then we are saying dot config and we are giving here say spark dot some dot config dot option and then we give here some value. After this, we say get or create.

Now after we do this, we are saying df. Now this time we are going to say spark dot read dot format and here we are giving com dot databricks dot spark dot CSV dot option and then we are giving here, we are having header. So we are giving header is equal to true and we are giving infer schema is equal to true. Now after this, we close the bracket, we say load the file and now here we are going to give the whole path where we have saved it.

So it is C spark in that spark, then we are having spark 2.4.2 bin Hadoop 2.7. In that the file name is dummy one dot CSV and we say here header is equal to true. Now after this, it will extract the data and keep it in df. Then we are saying df dot show.

So we get here all the 20 rows and then we are saying df dot print schema open close bracket. We get what is the column that is of type what and it is in nullable true or false. Similarly, first name is of type string nullable true, then country string nullable true, then sex string nullable true and count is of type integer nullable true. Now suppose we don't want all the 20 rows, we can say df dot show, say five, we're getting only the top five rows, not all the rows.

So we can do that how many rows you want, you don't want to fetch all, you want to fetch the first 10, you can give their show in bracket 10 and then print schema will print the column names and the type of column and whether they are nullable true or nullable false. Now we'll do one more example using for using the count function here we are saying from pi spark, we say input spark context, then we say sc is equal to spark context in bracket we give say local and we give count app. Then we say here sc is equal to we are giving we write down here sc is equal to say spark session dot builder dot app name we give here say python spark create rdd example, close the bracket dot we give config in bracket say spark dot some dot config dot option. Then we give here say some value and then we say get or create after this we are saying we want to create one say words is equal to sc dot parallelize and in this we pass say scala, java, Hadoop, then spark, then we pass here aka, we pass say spark versus Hadoop, then we pass pi spark, then we pass a pi spark and spark, we pass all the string variables inside this function.

Now what mistake have we made it is say word sc that is what we had created earlier right dot we use we have to do here say spark context then dot parallelize. Now after this we'll say counts is equal to say words dot count is a function that we are using to count how many values are there. Now once it has counted we'll use say print will give number of number of elements in rdd and we use here percentage I close the double quotes we give percent in bracket we give counts. Now here we are going to close the double quotes then we give here modular symbol and in bracket we give count.

The way of printing is say print number in the bracket number of elements in rdd and the value you want to print here is percent the value of counts. So here we get the value in the rdd is 8. So that's what we have used here the count function and displayed the values. So that's it from this session.
