# Finding Documents by Using Logical Operators

- **Course:** Introduction To Mongodb
- **Module 4:** MongoDB CRUD Operations: Insert and Find Documents
- **Lecture #:** 18
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/Ow8xo/finding-documents-by-using-logical-operators
- **Extracted:** 2026-08-11 09:54:41

---

Hello. In this video, you'll learn how to use logical operators in MongoDB. The logical operators we'll work with are $and and $or. Let's start with $and.

The and operator performs a logical and operation on an array of one or more expressions. It will return all documents that meet all the criteria specified in the array. The and operator also has an implicit syntax that we often use to simplify a query expression. All we need to do is add a comma between each query expression.

This comma acts just like the and operator. When using the and operator, remember that if any one of the criteria isn't met in a given document, the document will not be included in the results. Before we dive into an example, let's examine a sample document from a collection called Routes. Every document in this collection holds information about a particular flight route, like the number of stops, type of airplane, airline source airport, and destination airport.

Now, let's examine the following query. Inside the and operator array, we're searching for all documents that have an airline named Southwest Airlines and have a number of stops greater than or equal to one. We can simplify the syntax by using implicit and the query will return the same documents. After running this command, MongoDB returns all documents that contain one or more stops, and the airline is Southwest Airlines.

That was easy. Let's move on to the next logical operator $or. The or operator performs a logical or operation on an array of two or more expressions and selects the documents that match at least one of the expressions given. In this example, we've created a new query using the or operator that searches for every flight coming out of or going into the Seattle Tacoma International Airport, which is abbreviated as SEA.

After running the query, MongoDB returns all documents that contain either a destination or a source airport of SEA. Logical operators are useful when used by themselves, but we can also use them together. That means we can have an and operator expression made up of multiple or operator expressions. Let's take a look at this in practice.

First, we'll use the and operator with multiple or expressions. In this example, we'll search for every flight that has SEA as either a destination or source airport. We'll also search for every flight operated by American Airlines or that are flown on an Airbus 320 airplane. Running the query returns all documents that contain flights that have flown in or out of SEA, and flights operated by American Airlines or that are flown on an Airbus 320.

You may be wondering why we didn't use the implicit and syntax in this situation. Let's see what happens when we run the same query without the and operator. The returned results don't look quite right. There are a lot of airplane values that are Airbus 320sand some airline values that are American Airlines, but we don't see incoming and outgoing flights for SEA.

Why didn't this work? Our first or expression, the incoming and outgoing flights was overwritten by the subsequent or expression American Airlines or Airbus 320. This happened because we can't store two fields with the same name in the same JSON object. As a general rule, when including the same operator more than once in your query, you should use the explicit and operator.

Excellent job, you now know how to implement the $and and $or logical operators in your queries. You also learned how to use the explicit $and when using other expressions with the same operator.


<details><summary>Timestamped transcript</summary>

```
Hello. In this video, you'll learn how to use logical operators in MongoDB. The logical operators we'll work with are $and and $or. Let's start with $and. The and operator performs a logical and operation on an array of one or more expressions. It will return all documents that meet all the criteria specified in the array. The and operator also has an implicit syntax that we often use to simplify a query expression.
All we need to do is add a comma between each query expression. This comma acts just like the and operator. When using the and operator, remember that if any one of the criteria isn't met in a given document, the document will not be included in the results. Before we dive into an example, let's examine a sample document from a collection called Routes. Every document in this collection holds information about a particular flight route, like the number of stops, type of airplane, airline source airport, and destination airport. Now, let's examine the following query. Inside the and operator array, we're searching for all documents that have an airline named Southwest Airlines and have a number of stops greater than or equal to one.
We can simplify the syntax by using implicit and the query will return the same documents. After running this command, MongoDB returns all documents that contain one or more stops, and the airline is Southwest Airlines. That was easy. Let's move on to the next logical operator $or. The or operator performs a logical or operation on an array of two or more expressions and selects the documents that match at least one of the expressions given. In this example, we've created a new query using the or operator that searches for every flight coming out of or going into the Seattle Tacoma International Airport, which is abbreviated as SEA. After running the query, MongoDB returns all documents that contain either a destination or a source airport of SEA.
Logical operators are useful when used by themselves, but we can also use them together. That means we can have an and operator expression made up of multiple or operator expressions. Let's take a look at this in practice. First, we'll use the and operator with multiple or expressions. In this example, we'll search for every flight that has SEA as either a destination or source airport. We'll also search for every flight operated by American Airlines or that are flown on an Airbus 320 airplane. Running the query returns all documents that contain flights that have flown in or out of SEA, and flights operated by American Airlines or that are flown on an Airbus 320.
You may be wondering why we didn't use the implicit and syntax in this situation. Let's see what happens when we run the same query without the and operator. The returned results don't look quite right. There are a lot of airplane values that are Airbus 320sand some airline values that are American Airlines, but we don't see incoming and outgoing flights for SEA. Why didn't this work? Our first or expression, the incoming and outgoing flights was overwritten by the subsequent or expression American Airlines or Airbus 320. This happened because we can't store two fields with the same name in the same JSON object.
As a general rule, when including the same operator more than once in your query, you should use the explicit and operator. Excellent job, you now know how to implement the $and and $or logical operators in your queries. You also learned how to use the explicit $and when using other expressions with the same operator.
```

</details>
