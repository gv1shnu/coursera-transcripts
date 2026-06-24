# More Examples Part 1

- **Course:** Pyspark Python Hands On Guide Data Processing
- **Module 2:** Advanced Data Handling and Joins in PySpark
- **Lecture #:** 10
- **URL:** https://www.coursera.org/learn/pyspark-python-hands-on-guide-data-processing/lecture/CVoHw/more-examples-part-1
- **Extracted:** 2026-06-20 10:10:37

---

Now, you can use the count operation to count the number of rows in data frame. Now let's apply the count operation on train and test files to count the number of rows you are having. So, here we are saying train dot count open close bracket comma we are saying test dot count open close bracket. So, we get the output for the first train you are having 550068 records, for the test you are having 233599 total records.

Now how many columns do we have in train and test files along with their names. If you want to get the column names, we can use the columns on data frame. Similar to what we do for getting columns in the pandas data frame. Let us first print the number of columns and the column names in train file and then in the test file.

What we will do is, we will say length train dot columns comma train dot columns. First you will get how many columns you are having, so you are having total 12 columns that is with the help of length train dot columns and if you want to print what column names you are having. So, we are saying train dot columns wherein you are getting the column names displayed say user id, product id, gender, age, occupation, city category, stay in current city, years, marital status, product category 1, 2, 3 and purchase. These are all the columns in your train dot csv.

Similarly, you want to view it for test. What we will do, we will say length in bracket test dot columns comma test dot columns. Now here you will get total you are having 11 columns and whatever are the column names is what it may displayed in your out. We can check that we have total 13 columns in test file and 11 in test file and 12 in your train file.

Purchase column is not present in the test file. Okay, so we can see we have one column in test file which doesn't have the same name. So, this test file has all other columns but there is one column which is not there. Now we will see how to get some summary statistics that is your mean standard deviation, min max count of numerical columns in the data frame.

We have the describe operation which is used to calculate the summary statistics of numerical columns in data frame. If we don't specify the name of columns, it will calculate summary statistics for all the numerical column present in the data frame. What we will first do it, we will say train dot describe open close bracket dot show. Here what we will get is, we will get from the train dot csv file how many columns and their mean standard deviation, max, min max, all the values would be displayed for all the numerical column.

But now, suppose you want to only get it say for specify a name of the category or string or column in the describe option. So instead of all, what do we say is, we say here train dot describe in bracket single quote we give product underscore id dot show. So now we get only for the column name product underscore id. So for that we get the count of it that is how many values we are having, what is the mean standard deviation, what is the minimum value, what is the maximum value available inside your data.

Now we'll see how to select columns from the data. So we don't want to get all the columns, we want only some specific columns from one particular csv file. So to subset the columns, we need to use the select operation on data frame and we need to pass the column name separated by comma inside the select operation. So let us first select the five rows of user id and age from train dot csv.

So here we'll say train dot select in bracket will give user underscore id, that is the first column. Next column we are giving as age dot, we are saying show in bracket five, we get the top five rows for user id and age. Now let us see how to find the number of distinct product in train and test files both. So we just want to see what, how many are unique product.

Distinct operation can be used here to calculate the number of distinct rows. Let us apply this distinct operation to calculate number of distinct product in train and the test file. So what we'll do is we'll say train dot select in bracket will give product underscore id dot, we'll use distinct dot, we want the count of it. This is one operation.

Similarly, from test file, we want to select say product underscore id is the column name. This column we want to view with the distinct dot count. Now we'll get how many are unique product for product id in train and in test. Once it executes, you get the values as 3631 for train and 3491 for test.

After counting the number of distinct values for train and test files, we can see the train file has more categories than the test file. Let us check what are the categories for product which are in test files but not in the train file by applying the subtract operation. We can do the same for all the categorical features also. What we'll do is we'll say first diff underscore cat underscore in train underscore test is equal to we say test dot select in bracket, we give product underscore id then dot we use subtract.

Now after subtract in bracket, we'll give train dot select in bracket product underscore id, close it. Then we say diff underscore cat underscore in train dot distinct then dot count. Okay, for a distinct count of it, it is diff underscore train underscore test dot distinct count. How many are total distinct values?

That is 46. Now above you can see 46 different categories which are in test file but not in train file.
