# Using Relevance-Based Search and Search Indexes

- **Course:** Introduction To Mongodb
- **Module 9:** MongoDB Atlas Search
- **Lecture #:** 42
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/fdlcr/using-relevance-based-search-and-search-indexes
- **Extracted:** 2026-08-11 09:59:06

---

Hi folks. Let's start learning about Atlas Search, a powerful tool built into MongoDB Atlas that will help you create a search experience for users of your app, without having to create your own search algorithm. In this video, we'll review use cases for Atlas Search. How relevance based search differs from database search.

How a search index differs from a database index, and the components of a search index. Atlas Searches are relevance based search, which is one an applications end-user seeks to surface records based on a search term. It's not a database search for a particular record, for example suppose you go to MongoDB docs and you're searching for specific information on Atlas Search. You can type Atlas Search into the search bar and it will show matches based on what you searched for.

This is relevance-based search. In programming, one of the hardest things to do well is search through many items and return relevant results because it involves complex computation. This is why many engineers turn to additional software outside of their database for search solutions. Managing two systems and the sync between them can slow time to delivery.

Knowing this, MongoDB built to a search solution on top of industry standard open-source search algorithm, Apache Lucene, directly into MongoDB Atlas. Atlas Search starts with search indexes, which are used to specify how the search algorithm should work with this set of data. Search indexes are not the same as database indexes. Database indexes are used by developers and database administrators to make their frequent database queries easier and more efficient.

Search indexes are used to specify how records are referenced for relevance based search. The components of an Atlas Search index include information about the analyzers that are being used. In most cases, lucene.standard, the type of mapping, either dynamic or not, an option to store whole documents in memory for faster post aggregation performance and field mappings. In this video, we've covered the difference between relevance based search, where an application's end-user queries for information and a regular database search done by a developer.

As well as when we might use Atlas Search to create search functionality for an application. We also discussed the difference between a search index, which is used just for searching through database for relevant records, and a database index used for expediting frequent queries. Finally, we looked at the components of an Atlas Search index, where we defined the analyzer, field mappings and configure search settings for memory management. With this knowledge, we can create a search index and explore the different ways we can add relevance-based search to an application.


<details><summary>Timestamped transcript</summary>

```
Hi folks. Let's start learning about Atlas Search, a powerful tool built into MongoDB Atlas that will help you create a search experience for users of your app, without having to create your own search algorithm. In this video, we'll review use cases for Atlas Search. How relevance based search differs from database search. How a search index differs from a database index, and the components of a search index. Atlas Searches are relevance based search, which is one an applications end-user seeks to surface records based on a search term. It's not a database search for a particular record, for example suppose you go to MongoDB docs and you're searching for specific information on Atlas Search.
You can type Atlas Search into the search bar and it will show matches based on what you searched for. This is relevance-based search. In programming, one of the hardest things to do well is search through many items and return relevant results because it involves complex computation. This is why many engineers turn to additional software outside of their database for search solutions. Managing two systems and the sync between them can slow time to delivery. Knowing this, MongoDB built to a search solution on top of industry standard open-source search algorithm, Apache Lucene, directly into MongoDB Atlas. Atlas Search starts with search indexes, which are used to specify how the search algorithm should work with this set of data.
Search indexes are not the same as database indexes. Database indexes are used by developers and database administrators to make their frequent database queries easier and more efficient. Search indexes are used to specify how records are referenced for relevance based search. The components of an Atlas Search index include information about the analyzers that are being used. In most cases, lucene.standard, the type of mapping, either dynamic or not, an option to store whole documents in memory for faster post aggregation performance and field mappings. In this video, we've covered the difference between relevance based search, where an application's end-user queries for information and a regular database search done by a developer. As well as when we might use Atlas Search to create search functionality for an application.
We also discussed the difference between a search index, which is used just for searching through database for relevant records, and a database index used for expediting frequent queries. Finally, we looked at the components of an Atlas Search index, where we defined the analyzer, field mappings and configure search settings for memory management. With this knowledge, we can create a search index and explore the different ways we can add relevance-based search to an application.
```

</details>
