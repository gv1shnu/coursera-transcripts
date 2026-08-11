# Finding Documents by Using Comparison Operators

- **Course:** Introduction To Mongodb
- **Module 4:** MongoDB CRUD Operations: Insert and Find Documents
- **Lecture #:** 16
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/XzEDo/finding-documents-by-using-comparison-operators
- **Extracted:** 2026-08-11 09:54:18

---

Hello there. In this video, you'll learn how to use comparison operators in MongoDB, we'll work with the following operators, gt (greater than), lt (less than), lte (less than or equal to), and gte (greater than or equal to). The names of comparison operators follow a pattern so they're easy to remember. Note that each operator starts with a dollar sign to distinguish wish it from a field.

To use a comparison operator, we specify a field followed by the comparison operator and a value. Let's go over each of the comparison operators to get a better idea of how they work. We'll start with the gt, greater than operator. It returns documents where the field contains a value greater than the specified value.

Let's examine the following document which contains an items field that's an array of subdocuments. The items field contains various fields for each item, including the price, which is what we're interested in. We access subdocuments by using dot notation. In this expression, we want to find every document with at least one item price greater than $50.

To access subdocuments, we must first specify the document field name, followed by the name of the subdocument field name in quotes. In this case, it's the items.price field. When we run this command, all the results contain at least one item subdocument with a price greater than $50. We can also easily find items with a price less than $50 by changing a single letter in our expression from gt to lt.

The expression now returns every document that contains an item subdocument with a price less than $50. Next, let's look at lte, the less than or equal to operator. It works like the less than operator, except that it returns all documents less than or equal to a given number. In this expression, we're searching for every document in the sales collection containing a customer whose age is less than or equal to 65.

After we run this command, all the results will contain a customer who is 65 years or younger. While we're at it, let's take a quick look at the greater than or equal to operator. We just need to update the lte operator to gte. The expression now returns every document with a customer whose age is 65 years or older.

Awesome job. You now have a basic understanding of how to implement comparison operators in your queries. Here are the operators we covered gt (greater than), lt (less than), lte (less than or equal to), and gte (greater than or equal to). MongoDB isn't limited to the comparison operators we covered in this video.

We have a wide range of comparison operators to choose from. Check out our documentation to experiment with some of the other operators MongoDB supports.


<details><summary>Timestamped transcript</summary>

```
Hello there. In this video, you'll learn how to use comparison operators in MongoDB, we'll work with the following operators, gt (greater than), lt (less than), lte (less than or equal to), and gte (greater than or equal to). The names of comparison operators follow a pattern so they're easy to remember. Note that each operator starts with a dollar sign to distinguish wish it from a field. To use a comparison operator, we specify a field followed by the comparison operator and a value. Let's go over each of the comparison operators to get a better idea of how they work. We'll start with the gt, greater than operator.
It returns documents where the field contains a value greater than the specified value. Let's examine the following document which contains an items field that's an array of subdocuments. The items field contains various fields for each item, including the price, which is what we're interested in. We access subdocuments by using dot notation. In this expression, we want to find every document with at least one item price greater than $50. To access subdocuments, we must first specify the document field name, followed by the name of the subdocument field name in quotes. In this case, it's the items.price field.
When we run this command, all the results contain at least one item subdocument with a price greater than $50. We can also easily find items with a price less than $50 by changing a single letter in our expression from gt to lt. The expression now returns every document that contains an item subdocument with a price less than $50. Next, let's look at lte, the less than or equal to operator. It works like the less than operator, except that it returns all documents less than or equal to a given number. In this expression, we're searching for every document in the sales collection containing a customer whose age is less than or equal to 65. After we run this command, all the results will contain a customer who is 65 years or younger.
While we're at it, let's take a quick look at the greater than or equal to operator. We just need to update the lte operator to gte. The expression now returns every document with a customer whose age is 65 years or older. Awesome job. You now have a basic understanding of how to implement comparison operators in your queries. Here are the operators we covered gt (greater than), lt (less than), lte (less than or equal to), and gte (greater than or equal to). MongoDB isn't limited to the comparison operators we covered in this video.
We have a wide range of comparison operators to choose from. Check out our documentation to experiment with some of the other operators MongoDB supports.
```

</details>
