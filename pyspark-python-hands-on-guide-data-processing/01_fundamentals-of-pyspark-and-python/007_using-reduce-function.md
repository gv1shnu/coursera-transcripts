# Using Reduce Function

- **Course:** Pyspark Python Hands On Guide Data Processing
- **Module 1:** Fundamentals of PySpark and Python
- **Lecture #:** 7
- **URL:** https://www.coursera.org/learn/pyspark-python-hands-on-guide-data-processing/lecture/aAIVf/using-reduce-function
- **Extracted:** 2026-06-20 10:10:04

---

Okay, so we have given here value one for all the keys inside the particular example. Now in another one, we'll be defining some numerical values inside the array. And then we'll be see how to add all those arrays and print the total edition of it. So now we'll be saying from PySpark import spark context and we'll take here from operator, we are going to import add.

Then we say sc is equal to say spark session dot builder dot app name. Give here say python spark create rdd example dot pass the config as say spark dot some dot config dot option and say some value dot get or create. Now after this, we are creating an array named num, where we are saying sc dot spark context dot parallelize and we are passing here the values that is say 1, 2, 3, 4, 5. Okay, so these are all the numerical values that we have passed and stored inside nums.

Now we have another variable adding, where we are saying nums dot reduce and call the add function. And then after it has done all, we are saying print, say adding all the elements, print here in percentage i, i means for integers, then we are printing here the value of adding. So we'll get adding all elements, the value is 15. So it is 1 plus 2 plus 3 plus 4 and plus 5.

That is the total summation we are getting here. Similarly, now we'll see another example where we'll use the join and we'll join some two different values of arrays together and we'll print the given values in the inside the print statement. So here we are saying from PySpark, we'll be importing spark context. And we'll take sc is equal to say spark session builder dot app name, say Python, spark create already example dot config.

And here we'll pass spark dot some dot config dot option and say some value, then we'll say get or create. And now we'll be creating first x will be equal to sc dot spark context dot parallelize. And we are passing here the value say in again bracket spark one, then we are saying here Hadoop and four, okay, that is the first value or first array that we have created. Similarly, we are creating y and we are saying spark context dot parallelize.

And here we are passing again in bracket, say spark value two and the value as five. Close this closet. Okay, so we created x we created y. Now we are saying joined is equal to x dot join in bracket y.

So we are joining both. Now after this, we are saying final is equal to join dot collect. So we are combining both together storing it in final. And then we are saying here, after it has done, it will combine all and give you one particular array name that is your final.

Now once that is done, then we'll use the print command and we'll say here, double quotes say join rdd. Now I want to print here in percentage s, that is string, the value of final. So we'll get there Hadoop four, five, spark one, two, because whichever will be same, it will by default make it one, okay, and combine the values of others into that. Now we'll see another example wherein we'll see if the values are stored in cached or not.

So for that, we are saying from PySpark, we are importing spark context. And we are saying sc is equal to spark session, builder, app name, Python, spark, create rdd exam dot config. And here we are passing spark dot some dot config dot option, comma, say some value dot get or create. Now after this, again, we are creating say words is equal to sc dot spark, context dot parallelize.

And we are seeing here the first value say scalar, then say Java, Hadoop, then spark, then we have Akka, then we have spark versus Hadoop, then we have PySpark and we have PySpark and spark, close it. Now we are saying words dot cache. So we are storing them in cache first. And then we are saying caching is equal to words dot persist dot is underscore cached is a method which will check if it is cached or not.

And then we are saying print, here we are saying words got cached, print here percentages, which means we're printing true or false, the value of caching. So it says words got cached, yes. So once you create a particular array, automatically it gets cached if you say words dot or that array name dot cache. So in this way, you can see we have created various variations with your RDD using PySpark.

So that's it from this session. Thank you very much.
