# Word Count

- **Course:** Pyspark Python Hands On Guide Data Processing
- **Module 2:** Advanced Data Handling and Joins in PySpark
- **Lecture #:** 16
- **URL:** https://www.coursera.org/learn/pyspark-python-hands-on-guide-data-processing/lecture/R5LpG/word-count
- **Extracted:** 2026-06-20 10:11:40

---

So, now let's see some more extra examples on this. So, first we'll import PySpark. From PySpark, we'll import the spark-context and spark-conf. After this, we say conf is equal to spark-conf.

We set the app name saying reduce and we set the master as local square bracket asterisk. After this, we give here input integers is equal to say 1, 2, 3, 4, 5. What do we want is, we want multiplication product of all. That is 1 into 2 into 3 into 4 into 5.

So here we take next as integer rdd is equal to sc.paralyzeInputIntegers. After this, we create a variable product that is equal to integer. We have made here a spelling mistake, rdd.reduce. Use the lambda equation, say x, y colon x multiplied by y.

After it does all the product, the last step is you have to simply print it. So here you will give print in double code product is colon print here dot format is for printing product. So we get product is 120. So similar to this, we'll create another value.

We are having one file that is primenums.txt. Now that is available in, if you go to desktop, in this you have in folder primenums file. Now here all are the prime numbers given. What do we basically want is, we want the addition of all these numbers together printed on the command prompt.

So for that, what we'll have to do is, we'll say from pyspark, we will import spark context and sparkconf. After which we give conf is equal to sparkconf.setAppName and we give here in double code say primenumbers. Then we set the master as local asterisk, close the double quotes. Then we are saying lines is equal to a c.txt file.

Now here you will give the path that is c, users, the username, then desktop. On that you have the folder python spark tutorial master. In that again you have python spark tutorial master in which you have in folder and in this in you have prime underscore nums dot text file. We have given the reference of that file.

Now after this we say numbers is equal to lines dot flat MAPMAPMAP, give the lambda equation say line colon, we give line dot split, we give here tab because we are splitting the numbers using tab. So whenever a tab is there, which means that one number has ended. Then we give here valid numbers is equal to numbers dot. Now we will give here a filter lambda number colon num.

Then we give here int numbers is equal to valid numbers dot map lambda number colon convert to int the value of number and then you say print sum is colon print here in the given format that is int numbers dot reduce lambda x comma y colon x plus y. So you get here the sum of all the numbers printed as 24, 1, 33. So that's how we have seen some more exam. Now let's do one more example of count, but this time will not give any file will directly give the values here.

So we see here PySpark will import ParContext and SparkConf, then we'll say Conf is equal to SparkConf dot set app name, say count dot set master as local asterisk. Then we'll give here the input words is equal to double quotes, say Spark Hadoop, again Spark Ive, CPig, Cassandra, and again Hadoop. We are giving multiple values just to see whether the input will be proper. So after this, we say word rdd is equal to sc dot parallelize input words.

It is word rdd sc dot e. Then we say here a print command and we give count colon print here dot format word rdd dot count. So we print here that and next we continue with the total count is 7. Okay.

Now we give here say world count by value. Here we give is equal to word rdd dot count by value is another function which we can use and now we are saying once it is done, we'll print the count by value using a for loop. We'll give your first print say count by value colon and then we'll use your for word count in world count by value dot items colon and in this we are giving print, print here, give a colon again here dot format, you're printing the word comma the count of it. So you get Spark is there two times, Hadoop comes two times, Hive comes one, Pig comes one time and Cassandra comes one time.

Similar way, what we'll do is import this same. Now here, what we'll do is we'll take one more, but we'll take H as capital and second when we take here Spark as capital, the next thing is parallelize method to be called. Now, after this, we call the print method count, we print total count. What will be, it will be plus two.

So it will be nine this time. Then we say world count by value printed and again we give that the print command for count by value and then we give the for loop for word comma count in the world count by value dot items. Here, we want to print the values of the word and the count using the format word count. So now if you see, as we have given this different, so Spark with all small would be considered another thing and Spark with S capital would be a separate thing for PySpark.

It is a very case sensitive language. So if you give here, it's in capital, it will be different. If you give it in small, it is different for PySpark. So now, then we'll see the use of take method.

So here again, we'll include from PySpark, import Spark context and SparkConf. That is one word. Then we'll say conf is equal to SparkConf dot set the app name, say take dot set the master local asterisk. Then we give your input words is equal to say Spark, Hadoop, Spark, Pig, Hive, Cassandra and Hadoop again.

After this, we take word rdd equal sc dot parallelize input words. Then we take here words is equal to word rdd dot take in bracket three. Now how will you print that? For that, we'll have to give a for loop saying for word in words.

Then here we give print word. So Spark, Hadoop, Spark, that is what it is picking up the first three values, not the other values. Okay. If you use there the take method, so that's how you can use it.

Okay. So we have gone through many of the basic examples for your PySpark. Now the next session will be starting with the intermediate level course. That is with the introductory level course of PySpark.

Thank you very much.
