# Programming with RDD

- **Course:** Pyspark Python Hands On Guide Data Processing
- **Module 1:** Fundamentals of PySpark and Python
- **Lecture #:** 4
- **URL:** https://www.coursera.org/learn/pyspark-python-hands-on-guide-data-processing/lecture/kQkCL/programming-with-rdd
- **Extracted:** 2026-06-20 10:09:32

---

Now, in today's session of PySpark, we would be understanding about programming with RDDs. Now, let us first understand what is RDD. So, RDD represents your Resilient Distributed Dataset. An RDD in Spark is simply an immutable distributed collection of object sets.

So, each RDD is split into multiple partitions. Similar pattern with smaller sets, which may be computed on different nodes of the cluster. So, let us understand how do we create RDD. Now, usually there are two popular ways to create the RDDs.

One is loading an external dataset or distributing a set of collection of objects. Now, we'll see one example wherein we'll see some simplest ways to create RDDs by using the Parallelize function, which takes an already existing collection in your program and pass the same to the Spark context. So, we'll see one example of using the Parallelize function. So, now in this session, we would be understanding how to create your PySpark programs using the command prompt.

Okay. So, if you have to run it through the command prompt, what you have to do is, go to your Windows, type cmd, open the command prompt and there you will have to type PySpark and press enter. Once you press enter, it'll load your Spark session and will give you what Spark version you're currently using. So, here we will start from writing from PySpark.sql, we want to import Spark Session.

Now, after this import, we'll create a variable which will be equal to SparkSession.Builder.AppName in bracket. We'll give Python Spark Create RDD example. Then, we'll give the config, that is say spark.sum.config.option and we'll give here say sum-value, close the bracket then we'll give get or create. Okay.

So, if it is not there, it would get it or if it is not there, it will create it. Now, after this statement, we'll create an object df which will be equal to the earlier Spark.SparkContext. We are using here the Parallelize function and in this function, we are going to pass an array. So, we'll open the round bracket, then the square bracket, again the round bracket where we'll pass some values say 1, 2, 3, in bracket say a, b, c, single quotes, close one bracket, then give a comma, again open another bracket, here we are passing say 4, 5, 6, again in single quote, we are passing d, e, f, close it.

Then again, next we are passing say 7, 8, 9, again in single quote say g, h, i, close the single quotes, close the square bracket and the round bracket. Now, we are doing here dot to df and we want to convert this into say column 1, then say in single quotes column 2, then again single quotes column 3 and again single quotes column 4, close the round and the square brackets. So, once we have created this, okay we have not closed the single quote here. Now, after we create, it will create it with the data that we have passed into this and once it has been created, then we will use df dot show method which will print the data that we have already passed using the parallelize function.

So, now it will get the data, it will create this names that we have given here. So, we have column 1, column 2, column 3, column 4. In the first column, we have the value 1, then 2, then 3. The next column has a string that is abc.

Similarly, the second row has 4, 5, 6 and def and the third row has 7, 8, 9 and the text that we have passed here. Now, we'll see another example where we'll use or pass the function in the parallelize function and we'll use some different method to get the data. Now, here we have used df dot show method. So, first of all what we'll do is we'll say from say payspark dot sql, we want to import spark session, then we'll create a variable spark and we'll pass here spark session in then spark session dot we pass here buildup dot app name and we pass a given app name say python spark create rdd example then we say dot config and we pass here a name say spark dot some dot config dot option and say some value then we get or create now after doing this we say employee is equal to the variable spark dot now we are using here create data frame and now in this we are creating say again a round bracket one then the name then we are giving here the salary for example and then we are giving here say department now again we are opening the round bracket giving here second employee name of the employee we are giving say henry so we pass here the name then we pass here the salary and we pass the department again we open this is the third employee name is say sam salary is say 60,000 department again a comma and we pass here the fourth employee with the name as say max say salary as 90,000 department say one and then we close this and now we pass the column names that we want to create so we want first as say id then we want column as name then we want as salary and then we want say department id close the square bracket again the round bracket now after doing this we say employee dot show ok
