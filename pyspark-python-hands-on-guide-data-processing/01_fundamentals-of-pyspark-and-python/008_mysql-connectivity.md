# Mysql Connectivity

- **Course:** Pyspark Python Hands On Guide Data Processing
- **Module 1:** Fundamentals of PySpark and Python
- **Lecture #:** 8
- **URL:** https://www.coursera.org/learn/pyspark-python-hands-on-guide-data-processing/lecture/3QCwl/mysql-connectivity
- **Extracted:** 2026-06-20 10:10:15

---

In this session of PySpark, we'll be learning some more advanced features which using RTD, that is connecting your MySQL database table and viewing that details of the table using your PySpark. So for that, first of all, what we'll have to do is, we have to install MySQL. Once you install MySQL, you will get this MySQL prompt where you have to connect using your password for root. And once you connect, here first we'll create a database, we'll create a table, we'll add some dummy records in the table and we'll try to fetch the records that we have added in MySQL.

After this, we'll see in PySpark how to connect this MySQL database table and how to fetch these records in PySpark. So for that, here we are first saying, say create database, say demo1. Now it will create a database and give you query. Now we'll do first use demo1.

So we have changed the database to demo1 now. Now in this database, we are creating a table, say demo table. Now in this demo table, we'll have first column as id, which is of type integer. Next column is of name, which is of type varchar and the length in that will be 20.

Then we have a column age, which is also of type integer. So this will create a blank table named demo table, which will have three columns id, name and age. Now we'll fire an insert statement saying insert into say demo table values in bracket. First is of type integer.

Next we are giving in double quotes say abhai. Next we are giving age as 25. This is one record that we want to insert. Another record that we want to insert is to name bunty age 25.

You want to insert one more record again, give a comma and give your say abc and say 30. Once you have completed, give a semicolon at the end. So once you have executed, you will get three records inserted. If you want to view, you will have to write down select statement, select star from the table name.

So you will get here all the table structure with the table data that we have added. So now in our MySQL, we are having a database named demo one. In that database, we are having a table named demo table, which is having three values inserted into it. Now I want to fetch this values in my PySpark using certain commands of PySpark.

So now let us see how do we go about it. So when you come to PySpark, the first thing is you will have to import certain jar files. So what we'll have to do is we'll have to say import MySQL. Now this MySQL is a jar file that we have downloaded and we have pasted in the folder where you have the jar files.

Just to show you where you have to save it. So that folder is it's in C drive spark, the spark Hadoop folder in that you have jar folder. So here you can see we have put this MySQL jar file in the same folder because whenever we run PySpark, this is what path we have given from this we run PySpark. So whatever files you have to give link which are not there available over here, you can download those jar files and you can put them over here.

So once you put them here, you say import MySQL that file, all the classes would be automatically imported. Now what we have to do is we have to say data frame underscore say MySQL, which is equal to we are giving here SQL context dot read dot format. Here we give JDBC dot options and we give here in this first is the URL. Now URL will be equal to JDBC colon MySQL colon slash slash 3306 is the port of MySQL demo one is our database name.

So we have given link till the database. Now we say driver is equal to we given double quotes com dot MySQL dot JDBC dot driver close this. Then we are giving DB table is equal to the table that we have created that is demo table. Then we give user to how you will be connecting is using root user and you will be providing their password for it.

That is in this case, it is root 123. Then you close this. Then you say load and open close bracket. We had made a mistake here here after MySQL colon.

So we have to give here also a colon and then the port number. Now once we have done this, the next step is we have given here all the connections, the table name and everything. So what we are seeing here is we say data frame underscore MySQL dot show. Now when we do this, it by default fetches all the data from the table that we have created and it gives us the table displayed or the values displayed in PySpark.
