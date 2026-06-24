# Developing user-defined functions

- **Course:** Advanced Mysql
- **Module 1:** Functions and Triggers
- **Lecture #:** 4
- **URL:** https://www.coursera.org/learn/advanced-mysql-topics/lecture/AI2qz/developing-user-defined-functions
- **Extracted:** 2026-06-22 20:00:04

---

You might already be familiar with MySQL built-in functions. But what if none of these built-in functions meet your project's needs? No problem, you can develop your own user-defined functions. In this video, you'll find out what user-defined functions are and learn how to create your own.

Lucky Shrub are having a sale in which they're offering a 10% discount on selected products. But rewriting the same statement for every product during every transaction would be very time consuming. Instead, Lucky Shrub need you to create a user-defined function that they can invoke when needed to calculate these discounts. Before you begin helping Lucky Shrub, let's make sure you understand what database engineers mean by the term user-defined functions.

You might already be familiar with built-in MySQL functions like string or numeric functions. User-defined functions are created to perform operations that can't be completed with built-in functions. Users develop code that implements equations or formulas to complete a task and return a result. Let's break this process down.

A database engineer creates their own code. The code carries out a specific function and the function then returns the required result. To build a function in MySQL, you can use that create function command alongside the returns clause and the return command. These commands and clauses specify the data type and values to be returned by the function.

Let's find out how this syntax works. Begin your statement with that create function command, then assign a name to your function. Follow the function name with parentheses and parameters. The parentheses are mandatory but you don't always need to include parameters.

Next, specify the return data type followed by the keyword, deterministic. Deterministic means that the function always returns the same result for the same input parameters. For example, if a sum function is defined as deterministic, then it always returns the same result for the numbers it adds together. Finally, you can implement the logic with the return keyword.

Let's look at how Lucky Shrub can make use of a user-defined function. Lucky Shrub can use this syntax to create a function called find total cost. A cost parameter with a decimal data type passes a user input value of cost, and the returns clause defines the functions return type as a decimal number with five digits. Finally, the return command calculates and returns the final cost after deducting 10%.

So each time Lucky Shrub needs to determine the sale price of their items, they just invoke the function in a select statement followed by the current price in parentheses. But what if you want to develop a more sophisticated function? For example, Lucky Shrub want to offer a 10% discount to customers who make purchases of $100 or more and a discount of 20% on purchases of $500 or more. The first step is to use the delimiter command to compile the whole function as a single compound statement using begin end keywords.

Then, click Enter to change the delimiter from the default semicolon to a double forward slash. Next, use that create function command and name your function GetTotalCost, include a cost parameter with a decimal data type that passes a user input value of cost. The returns clause defines the functions return type as a decimal number with five digits, and the return command calculates the final cost after the discount has been deducted. The function is also defined as deterministic so that it always returns the same result for the same input parameters.

The next step is to use the begin and end keywords to determine the body of the function. Use an If Else statement to check the input cost and deduct the appropriate amount. Then, add the return command to calculate the final cost once the discount has been deducted. Finally, click Enter to create the new function.

Then, change the delimiter to the default semicolon so you can use MySQL as usual. Now, it's time to test the function using a select statement. A customer has just made a purchase that cost $500, so Lucky Shrub need to determine the discount to be applied. Type a select command followed by the name of the function alongside the purchase value in parentheses, then click Enter to execute the function.

The output result is 400, so this customer's purchase now costs $400 following a 20% discount. If you want to drop the function, just use the drop function statement followed by the functions name, click Enter to drop the function. Lucky Shrub can now apply discounts to their customers purchases as required, and you now know how to create your own user-defined functions in MySQL for your own specific projects. Great work.
