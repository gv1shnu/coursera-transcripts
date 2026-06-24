# Foreach Loop

- **Course:** Pyspark Python Hands On Guide Data Processing
- **Module 1:** Fundamentals of PySpark and Python
- **Lecture #:** 6
- **URL:** https://www.coursera.org/learn/pyspark-python-hands-on-guide-data-processing/lecture/2yfXA/foreach-loop
- **Extracted:** 2026-06-20 10:09:53

---

Now, let us see some more examples on RTD. Here we'll say from pyspark.sql import spark context from pyspark. Then we say sc is equal to spark session.builder.appname. Here we'll give say python spark create RTD.example.config in bracket spark.sum.config.option.

And say some value. Then we'll say here get or create. And then we create here words is equal to sc.spark context.paralyze function. And here we pass some values, say scala, then java, then hadoop, then spark.

Then we pass akka, then say spark versus hadoop, then pyspark and spark. Close the square and the round bracket. Then we define here a function f wherein we pass one parameter. And here we say print in bracket the value of x.

Then we say for e is for for each loop. And here we say words dot for each value of f. We get all the values displayed. Now, after this, we'll see another example wherein we'll use filter.

So we'll use some lambda equations, we'll fetch some values out of the values wherever the string spark is there, and then we'll print the particular values. For that, we'll have to say from pyspark, we'll import spark context. And we'll take sc is equal to spark session dot builder dot app name in bracket, say python spark create rdd example dot pass the config as say spark dot some dot config dot option. And we pass here say some value, then we say get or create.

After this, again, we create words. And we pass here sc dot spark context dot parallelize. And we pass here the values, say scala again, java hadoop, then we say spark, we say akka, then we pass spark versus hadoop. Then we have the next as pyspark and we have say pyspark and spark.

Now in this range of values, we are creating say words underscore filter and we are saying in this we want the filter given what is the filter we are using here lambda x colon we want wherever spark is there in x that filter we are giving for words underscore filter. Then we are saying another variable filtered is equal to say words underscore filter dot we are saying collect collect all those values store them in the variable filter. Now after it has fetched the values we are using here print command and we are saying print say filtered rdd and here we pass the value in string we want to print what value so here we are giving in bracket again the variable name we get the values printed wherever the text spark is appearing all those values would be fetched and displayed. Now let's see another example where we will be printing the key and the value pair or we'll be using the mapping and printing the key and the value pair again we would be using your lambda equation we will be starting from pyspark import spark context we'll say sc is equal to spark session dot builder dot app name give here say python spark create rdd example dot pass here config as say spark dot some dot config dot option and say some value.

Now after this we are saying get or create we'll be seeing here say words is equal to spark context dot parallelize and in square brackets we'll pass scala then java hadoop then say spark then we pass ca then we park versus hadoop then we have pyspark and we have pyspark and spark. Now after this again close the values and now we are seeing here words underscore map is equal to words dot map again pass here lambda equation colon x comma one for individual values starting from the first one we are assigning there the key as one so it will start from one until go until whatever number of values are having inside your collection then we are saying here mapping is equal to words underscore map dot collect the value store them in mapping and after that we'll be using here print saying key value pair print here in percentage s close the double quotes percentage and say mapping so you will get their key and the value pair for first one you are getting the key as one starting from one you're getting all the values printed.
