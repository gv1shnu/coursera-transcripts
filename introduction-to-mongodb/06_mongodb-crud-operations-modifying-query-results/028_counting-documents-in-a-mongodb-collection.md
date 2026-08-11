# Counting Documents in a MongoDB Collection

- **Course:** Introduction To Mongodb
- **Module 6:** MongoDB CRUD Operations: Modifying Query Results
- **Lecture #:** 28
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/YnHtu/counting-documents-in-a-mongodb-collection
- **Extracted:** 2026-08-11 09:56:31

---

Welcome back, team. In this video, we'll learn how to count the number of documents that match a query. We'll count the documents in MongoDB using the count documents collection method. The syntax for count documents is db.collection.countDocuments.

This method takes two parameters. A query document, which allows us to select the documents that we'd like to count and an options document, which allows us to specify the counting behavior. Since the options document is very rarely used, we won't discuss it here. Let's see what count document does in action.

We'll start with a basic example, counting all the documents in a collection. Later, we'll count documents with a more complex query. In this example, we'll be working with the training database again, but we'll be working with the collections called trips. Let's take a look at one of the documents.

These documents include quite a few fields with information about the beginning and end of trips, the bike ID that was used during that trip, and how long that trip took. Let's run an operation where we simply count the number of total trips in our entire collection. By doing a db.trips.countDocuments, we'll simply count all of the documents that are in the trips collection. As you can see, there's 10,000 documents in the collection right now.

Let's say we want to do something more complex, like only count the trips that are more than 120 minutes. That's something we can do very easily using the count documents method. Let's take a look. In this case, we'll start off with account documents method and our query document again.

We'll start by specifying our trip duration field. To do so, we're going to need to use the greater than operator. We're definitely going to have to insert another document here for our value. Within that document, we'll use the greater than operator with a value of 120.

As we can see, we've created a query now specifically to ask for trip durations that are greater than 120 minutes, we also want to make sure that we're only counting documents for our subscribers. We'll add an additional field to this query document. By running this query, we can see that we have a little over 7,800 documents that fall into this count. Let's recap what we learned in this video.

We saw how to count the number of documents returned from a query using db.collection.countDocuments. Count documents takes two parameters. The first is a query parameter. While we use basic queries in our example, you can include just about any query in your query parameter.

The second parameter specifies options that affect the account behavior. Congratulations, you're ready to count documents to your heart's content.


<details><summary>Timestamped transcript</summary>

```
Welcome back, team. In this video, we'll learn how to count the number of documents that match a query. We'll count the documents in MongoDB using the count documents collection method. The syntax for count documents is db.collection.countDocuments. This method takes two parameters. A query document, which allows us to select the documents that we'd like to count and an options document, which allows us to specify the counting behavior. Since the options document is very rarely used, we won't discuss it here.
Let's see what count document does in action. We'll start with a basic example, counting all the documents in a collection. Later, we'll count documents with a more complex query. In this example, we'll be working with the training database again, but we'll be working with the collections called trips. Let's take a look at one of the documents. These documents include quite a few fields with information about the beginning and end of trips, the bike ID that was used during that trip, and how long that trip took. Let's run an operation where we simply count the number of total trips in our entire collection.
By doing a db.trips.countDocuments, we'll simply count all of the documents that are in the trips collection. As you can see, there's 10,000 documents in the collection right now. Let's say we want to do something more complex, like only count the trips that are more than 120 minutes. That's something we can do very easily using the count documents method. Let's take a look. In this case, we'll start off with account documents method and our query document again. We'll start by specifying our trip duration field.
To do so, we're going to need to use the greater than operator. We're definitely going to have to insert another document here for our value. Within that document, we'll use the greater than operator with a value of 120. As we can see, we've created a query now specifically to ask for trip durations that are greater than 120 minutes, we also want to make sure that we're only counting documents for our subscribers. We'll add an additional field to this query document. By running this query, we can see that we have a little over 7,800 documents that fall into this count. Let's recap what we learned in this video.
We saw how to count the number of documents returned from a query using db.collection.countDocuments. Count documents takes two parameters. The first is a query parameter. While we use basic queries in our example, you can include just about any query in your query parameter. The second parameter specifies options that affect the account behavior. Congratulations, you're ready to count documents to your heart's content.
```

</details>
