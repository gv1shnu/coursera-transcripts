# Creating a Search Index with Static Field Mapping

- **Course:** Introduction To Mongodb
- **Module 9:** MongoDB Atlas Search
- **Lecture #:** 44
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/fyrDk/creating-a-search-index-with-static-field-mapping
- **Extracted:** 2026-08-11 09:59:29

---

Hi there. In this video, you will learn how to use static mapping for Atlas Search. The default field mapping of Atlas Search index is dynamic mapping, indexing all of the fields, which makes it simple to get started. However, if we have data with a lot of fields, only some of which an end-user of an application might actually care about.

We can show relevant results by statically mapping certain fields. This type of search index is called static indexing because the fields that are being queried against are always the same. They're static. Static indexing on specific fields makes the search quick and efficient by minimizing the number of fields to be indexed.

Let's jump right into our Atlas Search index. First, we navigate to the Search tab here and create a search index by clicking here. We will use the visual editor for a guided experience and ensure that we are creating a search index for the birds collection in the Bird Guide database. Then we'll click "Next" and refine your index.

Let's imagine we're creating a Bird Guide Book application. In this case, the most important fields that contain information that a user might search by are common name, scientific name, habitat, and diet. Dynamic mapping index is all of the fields present in a collection. In order to save time and processing power, we'll toggle off dynamic mapping and only index the fields that we anticipate will contain the search terms that are end-user my query by clicking Add Field and selecting common name from the drop-down menu.

To set the datatype for the common name field to string, we click on the "Add Data Type" button and make sure that string is selected. Off screen, I'll add field mappings for scientific name, habitat, and diet with the string datatype. Don't forget to click the Save Changes button when you're done. Now that we're done creating the field mappings in the search index, we can click on the Create Search Index button.

That's it. We've created a search index with static field mappings. Sometimes it can take awhile to be generated, but we'll be notified when it's done. Now we can query the search index as if it were a search bar in our bird field guide.

We can query for bluebird here and see the records where bluebird matches common name come up first in our search results. But what if we want to search for something we know is in the data, but in a field we did not index. For example, here I'll search for a wingspan value. As you can see, there are no results because the wingspan was not indexed.

In this lesson, we discussed creating search indexes with static field mappings. Now we can start to really make our search work in a magical way for our user.


<details><summary>Timestamped transcript</summary>

```
Hi there. In this video, you will learn how to use static mapping for Atlas Search. The default field mapping of Atlas Search index is dynamic mapping, indexing all of the fields, which makes it simple to get started. However, if we have data with a lot of fields, only some of which an end-user of an application might actually care about. We can show relevant results by statically mapping certain fields. This type of search index is called static indexing because the fields that are being queried against are always the same. They're static.
Static indexing on specific fields makes the search quick and efficient by minimizing the number of fields to be indexed. Let's jump right into our Atlas Search index. First, we navigate to the Search tab here and create a search index by clicking here. We will use the visual editor for a guided experience and ensure that we are creating a search index for the birds collection in the Bird Guide database. Then we'll click "Next" and refine your index. Let's imagine we're creating a Bird Guide Book application. In this case, the most important fields that contain information that a user might search by are common name, scientific name, habitat, and diet.
Dynamic mapping index is all of the fields present in a collection. In order to save time and processing power, we'll toggle off dynamic mapping and only index the fields that we anticipate will contain the search terms that are end-user my query by clicking Add Field and selecting common name from the drop-down menu. To set the datatype for the common name field to string, we click on the "Add Data Type" button and make sure that string is selected. Off screen, I'll add field mappings for scientific name, habitat, and diet with the string datatype. Don't forget to click the Save Changes button when you're done. Now that we're done creating the field mappings in the search index, we can click on the Create Search Index button. That's it. We've created a search index with static field mappings.
Sometimes it can take awhile to be generated, but we'll be notified when it's done. Now we can query the search index as if it were a search bar in our bird field guide. We can query for bluebird here and see the records where bluebird matches common name come up first in our search results. But what if we want to search for something we know is in the data, but in a field we did not index. For example, here I'll search for a wingspan value. As you can see, there are no results because the wingspan was not indexed. In this lesson, we discussed creating search indexes with static field mappings.
Now we can start to really make our search work in a magical way for our user.
```

</details>
