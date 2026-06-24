# More Examples on Mysql Part 2

- **Course:** Pyspark Python Hands On Guide Data Processing
- **Module 2:** Advanced Data Handling and Joins in PySpark
- **Lecture #:** 15
- **URL:** https://www.coursera.org/learn/pyspark-python-hands-on-guide-data-processing/lecture/fn9IB/more-examples-on-mysql-part-2
- **Extracted:** 2026-06-20 10:11:30

---

Now, we'll come to data exploration. Now, first thing what we'll see is coming to numerical variables wherein we have the describe function. So, in pandas or in spark will give us most of statistical results like your mean, median, max, quartile, standard deviation and all. If you have to just view how it is displaying, you can take here say num underscore calls is equal to, we take here account balance as one value.

Next we take say number of dependents, num underscore calls is equal to account balance and dependents. Then we take here, okay, what we'll do is we'll take here s is equal to say pd.series. We take 1, 2, 3, s is equal to series, 1, 2, 3. Then we'll take s.describe, we get their count, mean, standard, minimum 25%, 50, 75, max.

Similarly, we'll take s is equal to pd.series. This time we'll take say a, a, b, c and we'll say now describe. So, we get their count, unique, top frequency and frequency. Similarly, if you use their time span series, for example, we take s is equal to pd.series in square bracket.

We take np.dateTime 64 and here you take say 2000, 01, 01, first one. Then you again take np.dateTime 64. Say you take here 2011, 01, 01 and one more you take np.dateTime 64, say 2010, 01, 01. Close the round bracket, square and round bracket.

s is equal to, one second, we have not defined here np. We'll have to first input numpy as np and then we have to pass this. Okay, now we say s.describe. Now we get the count, unique, top frequency, first, last and the data type that is the object.

One more we'll define, df is equal to pd.dataFrame. Here we'll define in curly brackets, say categorial, colon, define pd.categorial and again here we give say d, e, f as the values, second we say numeric and here we give 1, 2, 3 as the numerical value and next we say object and here we define a, b, c. Close the curly and the round bracket. Now we say df.describe.

We get there the count, mean, standard, minimum and all the values. Again here if you say df.describe, include all, you get there the standard, also get it for categorial, numeric and object and all the other values also. If you say that include all or you say df.numeric.describe, you get it only for the numeric values. That's how you can specify the object definition.

So that's it from this session. Thank you very much.
