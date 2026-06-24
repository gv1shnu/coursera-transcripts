# More Examples Part 2

- **Course:** Pyspark Python Hands On Guide Data Processing
- **Module 2:** Advanced Data Handling and Joins in PySpark
- **Lecture #:** 11
- **URL:** https://www.coursera.org/learn/pyspark-python-hands-on-guide-data-processing/lecture/KpjnI/more-examples-part-2
- **Extracted:** 2026-06-20 10:10:48

---

Now, in this case, either we can collect more data about them or skip the rows in the test file for those categories which are not in the train file. So what if we want to calculate pairwise frequency of categorical columns? You can use a cross tab operation on data frame to calculate the pairwise frequency of columns. Now, let us apply the cross tab operations on age and gender column of the train data frame.

So, what we'll do here is we'll say train dot cross tab. Here we'll give the column as age in single quotes and we'll give the column as gender in single quotes and we'll say here show. So we get the output using age and then we have gender wherein we have female and male. So for every age, we'll see how many female, how many male.

Similarly, we'll move on with the rest values. So now in the above code, the first column of each row will be a distinct value of age and the column names will be the distinct values for gender. The name of the first column will be age gender, pair with no occurrences will have zero count in the contingency table. Now if you want to get the data frame which don't have duplicate rows of the given data frame, then we can use the drop duplicate operation to drop the duplicate rows of a data frame and get the data frame which have or which won't have any duplicate rows.

So to demonstrate, we'll be performing this on two columns that is age and gender of train and we'll get all the unique rows of this column first. So for that, what we'll have to do is first say train.select in bracket, we give the column name age and gender. Then we say drop duplicates.show. So we are displaying the values first.

Now all the values which are being displayed. What if if you want to drop the old rows with the null values? So you have the drop any operation which can be used to drop row from the data frame. It considers three options.

One is how that is any or all. So if any, then drop a row if it contains any nulls. If you say all, then drop a row only if all its values are null. Second option you have is trash.

Now by default it is int, default none if specified. So drop rows that have less than trash non null values. This overrides the how parameter. Then you have the next as subset which is optional list of column names to consider.

Now let us drop null values in train with default parameters and count the rows in output data frame. Now default options are any, none, none or how, trash, subset respectively. So what we are going to do is we are going to say here train dot drop any dot count first. Okay now drop any is also a function.

So we'll use your open close bracket. It will give you a count of it. Now if you want to fill the null values and data frame with some constant number. So you can use the fill any operation here.

The fill any will take two parameters to fill the null values. First is the value. It takes a dictionary to specify which column will replace which value. And second will be a value of type either int, float, string for all the columns.

Then you can have subset specify some selected columns. Now in place of the null values in train data frame, we'll have to pass here some other values. So what we'll do is we'll say train dot fill any in bracket say minus one dot show two. So only showing the top two records here.

So if you want to filter the rows in train which has purchase more than 15,000. So you can apply here the filter operation on purchase column in train data frame to filter out the rows with values more than 15,000. So we need to pass a condition. So let's apply filter on purchase column in train data frame and print the number of rows which has more than purchase.

So for that we'll have to say train dot filter in bracket we'll have to say train dot purchase more than 15,000 dot we want the count of it. So we'll get a total number of count how many columns have purchased more than 15,000. Similarly how to find the mean of each age group in train. So you can use the group by operation which can be used here to find the mean of purchaser for each age group in train.

So let's see how can we get the mean purchase for each column train. So first we'll have to say here train dot say group by here you give the column age dot agg is aggregate here we give bracket then a curly bracket we give here purchase colon mean close the round bracket dot show and then we get the output here for every age what is the average percentage of purchase. So we can also apply some minimum maximum count with the group by when we want to get different summary insights each group. So let us take one example of group by to count number of rows in each age group.

So how will you do that. We can see here train dot group by pass here the column name dot use the count function and say show. So you get here group by age you get the values of the count. So how to create a sample data frame from the base data frame.

Now we can use the sample operation to take sample of data frames. Sample method on data frame will return a data frame containing sample of the base data frame. So the sample method will take some three parameters. First is with replacement which will be true or false to select an observation with or without replacement.

Second is fraction which is equal to x where x is equal to point five shows that we want to have 50 percent data in this sample data. Next is seed for reproduce the result. Now let's create two data frame T1 T2 from train both will have 20 percent sample of train and count the number of rows in each first we'll say T1 is equal to train dot sample in bracket we give false we give 0.2 and we give 42. Next is T2 that is also equal to train dot sample.

Here also we give false we give 0.2 and 43. Now we say T1 dot count comma T2 dot count and we get the output whatever rows are there in T1 and T2. Now how to apply map operations on data frame columns. We can apply a function on each row of the data frame using your map operations.

After applying this we get the result in the form of RDD. So let's apply a map operation on user ID column of train and print the first five elements of mapped RDD. After applying the function so we can take here the lambda functions. So you have to say here train dot select in bracket say column name as user underscore ID dot map in bracket we give lambda X colon here we give X comma one dot take in bracket five.

So we get here the it is train dot select here we have given the column name then we give map in bracket we give lambda X comma one and then we give T. Okay what you will have to do is you will say train dot select user ID dot RDD dot map and then you have to give the lambda equation. So here you get the values that are executed. So now how to sort the data frame based on columns.

We can use the order by operation on data frame to get the sorted output based on some column. So the order by operation takes two arguments first is the list of columns and next is either ascending or descending. Ascending is equal to true or false by getting the values in ascending or descending order. So if you have to sort the train data frame based on purchase so you have to say train dot order by in bracket train dot purchase dot you want in descending order dot you want to show the five records so you get it arranged in descending order.

Then similarly if you want to add a new column in data frame so we can use with column operation to add a new column in base data frame and return a new data frame. So here the with column operation takes two parameters one is the column name which we want to add or replace and the next is the expression on the column. So let's see how with column works. So we are calculating a new column name purchase underscore new in train which is calculated by dividing purchase column by two.

So for that we are saying train dot with column in bracket we give a column name say purchase underscore new then we give here train dot purchase divide by 2.0 dot select the purchase and purchase underscore new and will display the first five records. So we are getting here both the columns where the first purchase column if you divide by two whatever value it is coming in purchase underscore new column. So if you want to drop a column in data frame you can use the drop operation where you can say test dot drop a column dot columns. So that's it from this session.

Thank you very much.
