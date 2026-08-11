# Creating a Search Index with Dynamic Field Mapping

- **Course:** Introduction To Mongodb
- **Module 9:** MongoDB Atlas Search
- **Lecture #:** 43
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/00vDy/creating-a-search-index-with-dynamic-field-mapping
- **Extracted:** 2026-08-11 09:59:17

---

Hello, in this video, we will use MongoDB Atlas to create a search index on a collection. Set the options to use dynamic mapping, and test our search index by making a query. Search indexes are used to define how a relevancebased search should be performed. It is not the same thing as a database index, which is used to make database queries more efficient.

There are just a few steps to set up an Atlas search index and we can do that directly in MongoDB Atlas. A search index with dynamic mapping means that when the search algorithm is run. All fields will be indexed with a few exceptions booleans, objectIds, and timestamps. This is the default and the fastest way to get search running.

In the MongoDB Atlas interface, we can click into the Search tab. Where we will see all of the search indexes that we have in this database. We can create a new search index by clicking on the Create Search Index button. We can click here to use the visual editor to be guided through the creation of a search index.

We will make sure that the correct database and collection are selected. In this example, we'll use the birds collection in the bird_guide database. Let's take a look at the default options for a search index. We see that the index analyzer and search analyzer are lucene .standard.

Lucene is an open source search engine library that is the industry standard for how relevance based search works. Standard refers to how we will tokenize the data into searchable chunks. There are 40 plus index analyzers that can be used for multilanguages or other use cases. For a dynamic search that looks through all of the fields for the user's search term, we will leave dynamic mapping toggled on.

Because we are using dynamic mapping in this example. We will not have to specify any field mappings since we're looking at all of the fields. Then we save our changes and finally push the Create Search Index button. That's it, we've created our first search index.

Sometimes it can take a while to be generated, but we'll be notified when it's done. Now we can run a sample query on our database. Let's click Query. I want to see all of the birds in our collection of bird species that have blue plumage.

So I simply query blue by typing and clicking Search. Here are the results. We see that a score is assigned to each result. This is the relevant score as calculated using Lucene scoring logic.

Based on how prevalent the query term is in any of the fields in the record. This score is used to determine which results will appear at the top of the list. As we get to more advanced Atlas search skills, we can also change how the score is calculated by assigning weights to different fields. In this lesson, we've created our first Atlas search index and ran a query.

We created a search index with dynamic mapping, looked at the components of a search index and ran a search query. Now you can try this out in your own database and run a search on your own data.


<details><summary>Timestamped transcript</summary>

```
Hello, in this video, we will use MongoDB Atlas to create a search index on a collection. Set the options to use dynamic mapping, and test our search index by making a query. Search indexes are used to define how a relevancebased search should be performed. It is not the same thing as a database index, which is used to make database queries more efficient. There are just a few steps to set up an Atlas search index and we can do that directly in MongoDB Atlas. A search index with dynamic mapping means that when the search algorithm is run. All fields will be indexed with a few exceptions booleans, objectIds, and timestamps.
This is the default and the fastest way to get search running. In the MongoDB Atlas interface, we can click into the Search tab. Where we will see all of the search indexes that we have in this database. We can create a new search index by clicking on the Create Search Index button. We can click here to use the visual editor to be guided through the creation of a search index. We will make sure that the correct database and collection are selected. In this example, we'll use the birds collection in the bird_guide database.
Let's take a look at the default options for a search index. We see that the index analyzer and search analyzer are lucene .standard. Lucene is an open source search engine library that is the industry standard for how relevance based search works. Standard refers to how we will tokenize the data into searchable chunks. There are 40 plus index analyzers that can be used for multilanguages or other use cases. For a dynamic search that looks through all of the fields for the user's search term, we will leave dynamic mapping toggled on. Because we are using dynamic mapping in this example.
We will not have to specify any field mappings since we're looking at all of the fields. Then we save our changes and finally push the Create Search Index button. That's it, we've created our first search index. Sometimes it can take a while to be generated, but we'll be notified when it's done. Now we can run a sample query on our database. Let's click Query. I want to see all of the birds in our collection of bird species that have blue plumage.
So I simply query blue by typing and clicking Search. Here are the results. We see that a score is assigned to each result. This is the relevant score as calculated using Lucene scoring logic. Based on how prevalent the query term is in any of the fields in the record. This score is used to determine which results will appear at the top of the list. As we get to more advanced Atlas search skills, we can also change how the score is calculated by assigning weights to different fields.
In this lesson, we've created our first Atlas search index and ran a query. We created a search index with dynamic mapping, looked at the components of a search index and ran a search query. Now you can try this out in your own database and run a search on your own data.
```

</details>
