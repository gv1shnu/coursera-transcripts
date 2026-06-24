# MySQL JSON

- **Course:** Advanced Mysql
- **Module 2:** Database Optimization
- **Lecture #:** 18
- **URL:** https://www.coursera.org/learn/advanced-mysql-topics/lecture/ymAY1/mysql-json
- **Extracted:** 2026-06-22 20:02:41

---

As a database engineer, you need to work with many different types of data. This can place a lot of pressure on my SQLs resources as it compiles and passes through these different data types. One method of optimizing MySQL use of resources is to store data using the Jason or JavaScript object notation sata type. JSON is an easy method of communicating data between different database systems and it stores data in a simple text format that doesn't require any special pausing.

Here is an example of Jason code from an insert into statement in the lucky shrub database. Lucky shrub use this line of code to store properties and assign them specific values. This line of code is placed within a pair of single quotation marks and curly braces within the insert into statement. Each property and value are typed in double quotation marks and separated by a column.

These are known as key value purse. Each pairing is separated by a comma. Let us explore how lucky shrub makes use of this. MySQL Jason code in their database.

Lucky shrub need to track the actions of clients who use the online stores as they browse lucky shrub products and place orders. Lucky shrub can capture this information and store it in Jason format in MySQL. MySQL can then quickly and efficiently process this data. First create a table called activity that stores client activity.

Then create two columns. The first column is called activity ID and provides a unique identifier for each client activity using an integer data type. The second column is called properties. This is JSON data type column.

It stores the properties of each client activity like a client ID and product ID. It also records if the client has placed an order by placing either a true or false value next to the order property. The next step is to populate the table with data, create three activity IDs and then log client activities using Jason code for three client IDs. Two of these clients have ordered products, one client has not ordered a product.

Now you need to retrieve data from the properties column. Since you are working with Jason data type, you need to retrieve or access this data using a column path operator. Type a select statement that selects the activity ID and properties column. For the properties column use the dollar sign symbol and dot notation to denote each element inside the Jason property.

Place the column path operator between the columns and their elements. Finally execute the statement to return the output results from the activity table. You have now helped lucky shrub to create an optimal method of storing and accessing data from the activity table in their database. You should now be familiar with how to use Jason in MySQL to optimize the database.

Great work
