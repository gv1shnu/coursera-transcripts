# Viewing Records from Mysql

- **Course:** Pyspark Python Hands On Guide Data Processing
- **Module 1:** Fundamentals of PySpark and Python
- **Lecture #:** 9
- **URL:** https://www.coursera.org/learn/pyspark-python-hands-on-guide-data-processing/lecture/L1aYL/viewing-records-from-mysql
- **Extracted:** 2026-06-20 10:10:26

---

Now, suppose you want to know what are the columns and those are of type of what type you want to view them. So what you can do is you can say data frame underscore MySQL dot print schema open close bracket. You will get there from this table. First column is ID which is of type integer name of type string and age of type integer.

So you can get the table print schema will give you the table structure with the types and whether it is nullable true or false. Now this was a simple example wherein we had connected MySQL and we had viewed the data of your MySQL into PySpark. Let us see one example of RDD dot data frame versus PD dot data frame. Now first of all what we'll do is we'll create some list.

So here we are saying my underscore list. So here we are saying is equal to in this square bracket we give a single quote a one comma two second we give b say two comma three then we give again one more c three comma four. Close this. Another we create that is call underscore name that is equal to in single quotes we give a then we give b then we give c.

Now after this we say PD dot say data frame in bracket we give my underscore list comma columns is equal to call underscore name. Okay now before that what we'll do is we'll say from PySpark we are importing say spark context then we say sc is equal to spark context. Okay now we may have to give some more coding in this that is first of all what we'll do is we'll create one data frame from RDD. So we'll create a list of tuple each tuple will contain name of the person with age then we'll create RDD from the list of about we'll create each tuple or to a row and then we'll create a data frame by applying the create data frame on RDD with the help of SQL context.

So again one more thing what we'll do is we'll say from PySpark dot SQL we want to import row. Now after this we are saying L is equal to in square bracket then round bracket we give first say Ankit then 25 one data close second we are giving say Jalfaizi and 22 then we are giving Saurabh and 20 and then we are giving say Bala and 26 close this then we are creating RDD object that is equal to sc dot parallelize L after this we say people is equal to RDD dot map in bracket we are giving the lambda equation so here we are giving lambda X colon use the object row give here name is equal to X in bracket zero comma age is equal to int in bracket X at the index one then close the brackets. Now after this we are saying schema people is equal to SQL context dot now we are seeing here create data frame in bracket people. Now once it has been created we'll check the type of schema people.

So for that we'll say type in bracket schema people and we'll get the output as it is of type PySpark SQL data frame dot data frame. Now we'll create a data frame from the CSV file. Now this is what we have created by giving the values inside the list. Okay.

So now what we'll do is for reading a CSV in the Apache Spark we need to specify a new library in our Python shell. Now that is we'll have to first download the Spark CSV package and extract this package into the home directory of Spark. Then we need to open the Spark shell and include the package. Now that package is your Spark CSV underscore 2.10 colon 1.3 point zero.

That is what we'll have to download and we'll have to put into the Spark home package. Okay. Now how will you include that. You will have to say when you are running the PySpark you have to say PySpark dash dash packages and you have to specify com dot data breaks colon Spark CSV the version 2.11 colon 1.5 point zero.

Now once you do that it will automatically download and include that into your PySpark session. Okay. So now we can use that package directly. So now what we are doing we are saying train object is equal to say SQL context dot load.

Now we are giving here source as com dot data breaks dot Spark dot CSV and we are giving the path that is equal to in single code say train dot CSV. Then we give the header is equal to true and we give inf infer schema as capital of schema as is equal to true. Now what we'll do is we'll give here the whole path instead. So we'll give here say C colon slash Spark slash then let's open C colon Spark home and this is where we have the file.

So we'll just copy this part here instead of just giving the file name and what we'll do is give here dashes. So this is what we want to include. Okay. Now here SQL context is correct.

Now we are giving here the what we'll have to do is we'll have to say Spark is equal to Spark session dot builder dot app name give here say Python Spark create RDD example dot config is equal to Spark dot some dot config dot option and then comma some value dot get or create. After this we say train is equal to say Spark dot read dot format in bracket say com dot Databricks dot Spark dot CSV dot option and here we give header is equal to true that will be in single quotes and infer schema is equal to true again in single quotes. After this we say use the load method and here we give the path that is let us paste the path that we have given. See here we'll give the path.

Okay so that is what we have given in C drive Spark Spark folder train dot CSV again we give header is equal to true. Now once we have said this we'll do another one that is test is equal to again we'll say Spark dot read dot format say com dot Databricks dot Spark dot CSV dot options here we give again header is equal to true then infer schema is equal to true dot use the load method again here we are giving C colon folder Spark then Spark dash 2.4.2 bin Hadoop 2.7 in that we have a file test dot CSV and we give here header is equal to true. So we have set it for train we have set it for test also. Now once we have done this we'll give data frame manipulations now that comes when you have loaded the data set.

Now let's start playing with it. How can you do that. First thing that you can do is you can say train dot print schema that we have already used wherein you will get the column names and the type of the column where it is it's also nullable true or false. Similarly what you can do is you can see the first or you can use the show first or some observations so we can use here the head operations to see the first observation say first five operations we want to see.

So here you can give train dot head in bracket five so only the first five records would be viewable in that case. Now after this what you can do the next thing is the above result will be also like comprised of true. But when you use this say you say train dot show instead of this you say to and you say here truncate is equal to true. So then you get it in proper table arrangement output will be differ.

If you use normally train dot head or train dot show then in the bracket you give the values. Now we'll continue this in the next video.
