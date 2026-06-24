# Basics of Python

- **Course:** Pyspark Python Hands On Guide Data Processing
- **Module 1:** Fundamentals of PySpark and Python
- **Lecture #:** 2
- **URL:** https://www.coursera.org/learn/pyspark-python-hands-on-guide-data-processing/lecture/h5DRV/basics-of-python
- **Extracted:** 2026-06-20 10:09:11

---

Now, once you start the command prompt of PySpark, you will get this Jupyter environment wherein you can create or type your PySpark code and you can execute them. Now we will see currently the basics of Python, that is the data science, the basics of Python in the sense how to create variables and calculations with that. Then we'll see how to create some string variables, some string operations on the variables. We'll go ahead with creating some arrays in the format of list.

Then we'll see how to manipulate those, how to use some methods available for arrays. Similarly for strings. And then we'll gradually move with the PySpark demonstration. So first of all, if we have to create variables and we have to assign values in those variables and to see what values we have already assigned.

So for example, we are taking here A is equal to 5. Now if you have to execute this, you can click on the run button given. A variable named A is created with a value of 5. If you want to check what value is assigned in that, just type A here and click on run.

So the output what you get is 5. Now for example, you want to say A plus 2 and you want to execute this, you get the value as 7. Similarly, say A minus 2 for the minus operation or say multiplication, or you want to check it for say float 2. You get the value.

Now we have converted this because the value would be coming in float format. Similarly, if you say A modulus 2, you get the remainder there. These are the basic arithmetic operations. That is your sum, subtraction, multiplication, exponential.

Exponential would be say A. So that is A raised to 2. So that is 5 raised to 2. Now next we have, there are some types and the conversions for that.

For example, if we say A dot str, or rather we say str in bracket A. So we are converting the value of A variable, which is actually 5. We want it in the format of string, so we are getting there single quote. Similarly, if you say int in bracket A, then you get the value as printed as the integer format.

Or you say float A. You get the value in the float format. Similarly, you say Boolean A. Boolean means if the value is stored, you will get true.

If it is not, you will get false. So here we are getting, for one single variable, we can use multiple functions for converting and storing them. Similarly, suppose you are saying help and A, and you run this, you get some help which you can use on the given variables. These all are the functions which you can use to get the help for a particular given variable.

Now, this variable what we had created was of type numeric. Now we are creating say my str. Here we are saving the value, say this string is awesome. For example, we take I capital is awesome.

And we execute this. So we have created a string. Now if we have to print this, we use again same my underscore str. Now if you want to do across some multiple operations or arithmetic operations on your string variables, in that case, you can say my str, suppose, multiplied by two.

That means we want the same string twice multiplied by two. Or you are saying my str plus say init, then you will get that particular string and one more word added at the end of it, or you want to add something in first. So you already want to check suppose m in my str, you get m is there in my str, you will get the value either true or false. Similarly, suppose we are saying a plus my str.

So you get a added prior to the particular given string. Now similar to this, as we have seen a normal integer variable, we have seen normal string variables will move on with the list variables also. Now how will we create a list say we are giving first creating a variable saying here is then we are creating b is equal to nice. Now we execute both the codes together, then we are saying my underscore list is equal to in square brackets, we are giving say my list, then the value of a and b, because we want the list in my list to be first will be my then list and then is and then nice.

That is what we want into our list created, we create this. Now we want another list created, say my list two. And here we want giving an array, we are giving say 4567 first, then we are giving say, 3456 in the second one. So first string is a string value, second string is of your integer values.

Now let's see how to manipulate or select certain list element using certain various combinations. So if we are saying here, my list at the index one, so in that case, at the index one, you're having list because this will be your index number zero, this is index number one, this is index number two and index number three, we want to get whatever is value is there on index number one of my list. Similarly, you say here, my underscore say list in bracket minus three. Now, what does minus three will give you the third last item, this is the last item, this is the second last item, this is the third last item.

Suppose we give here instead of this, we say my underscore list minus two. So you get the second last item, that is is the value of A. Similarly, suppose you say my underscore list, you give here one colon three, we want to select the item at the index one and index two. That is what we are selecting.

So what is there at index number one is list and index number two will be a value that is list and is being fetched. Similarly, you say my underscore list one colon and then close it, we want to fetch items after the index number zero, that is from index number one. So one, two, and three, all the values would be fetched and displayed, or you're saying my underscore list, you're giving here colon three. In this case, we are saying I want to fetch items before index number three.

Or suppose you want to copy my underscore list. So what you will do just say my underscore list in bracket, just colon, that will copy your list and print it as it is. Then we have the next is subset list of list. That is, if we want to fetch some multiple values or giving a particular exact combination of the values.

For example, the second list that we had created at was my list two. In this we are saying fetch one and zero. Now when we are saying this, it is going to fetch three. Now why this?

Because this is your first row, zero, one, two, three. This is your second row, index zero, one, two, three. Now we are saying we want to fetch one comma zero. So this is zero.

So one is this and one comma zero would be three. That is what it is fetching. Then we are saying suppose my underscore list two, here we are fetching from one and we are going colon two. Now in this case, we are fetching from the first item, three and four, that is the first and the second, till the second operation or till the second value we want to fetch all.

So this is zero. This is one. It will not fetch the second value. Till second, whatever values are there, it would be fetched and displayed.

Now coming to certain list operations that we have. For example, here we are saying my underscore list plus my underscore list. Now we are doing an addition of both the list. In my underscore list, we had my list is nice.

That is what value we had. Now here we are getting similar value, but twice because we have added same list again and displayed. Or if we are saying my underscore list multiplied by two, again, in this case, the output would be same. But we are just saying we want to multiply the values of same by twice, or we are saying now my underscore list two, if it is more than four.

Now this is not supported over here, you will not get any output. Now if we want to see some list methods that we have, or we want to get some index of in particular item, so we are saying same my underscore list dot index in bracket, we pass the value A. So we are getting for A. A is the value we have created here, which is having the value is in it.

So we are fetching the index of it. So how many values are there, there are two values into it. And this A in my list, my underscore list, where is the position of this A, we have given there, this is 0, 1, 2, 3. So it is at the second position.

Similarly, if we are saying my underscore list dot count the value of A. The value of A you're counting that is coming to one that will just get the count of in particular item.
