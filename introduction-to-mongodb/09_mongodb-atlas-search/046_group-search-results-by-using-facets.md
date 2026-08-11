# Group Search Results by Using Facets

- **Course:** Introduction To Mongodb
- **Module 9:** MongoDB Atlas Search
- **Lecture #:** 46
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/tEH9N/group-search-results-by-using-facets
- **Extracted:** 2026-08-11 09:59:52

---

Hi, there. In this video, we'll use facets and the search meta aggregation stage to customize search results by categorizing them. In order to get the most out of this lesson, you should know how to create a search index and how to use the search aggregation stage to create an atlas search query. Facets are buckets that we group our search results into.

For example, when you search for a term in a social media app like Facebook, you may see the results grouped by people, pages, posts, groups, and events. This will help users find what they're looking for faster by suggesting categories where the user can expect to find a specific type of information. To begin creating our facets, we first need to decide which field to use for categorizing the search results. The data types that we might consider for these categories are numbers, dates, or strings.

Let's look at an example where we have a dataset of bird sightings and we would like for our users to search for sightings and see results grouped by the week in which the sightings occurred. We need to create a field mapping in our search index for the field that will be used to create those groupings. To do this, let's first toggle off dynamic mapping to add our field mappings. Scroll down to the field mapping section and then select date from the drop-down menu.

Next week, click "Add Data Type", and select the data type here, in this case, date facet. We can also create field mappings for other fields that the user of this bird tracking application might search by. For example, off-screen, I also added species_common and species_scientific, both with the data type string. With that, our search index is ready to be queried.

Instead of using a regular search stage in the aggregation pipeline, we'll use a $searchMeta stage in order to see the facets and how many results are in each bucket. The buckets that the search will be filtered into are not part of the search results themselves. They're part of the search metadata, information about how the search was carried out. As of now, there are two pieces of metadata for atlas search, the facets and the count, which is the number of results returned in each of the facets.

Let's go to our test aggregation pipeline in MongoDB Atlas and create a $searchMeta stage by selecting $searchMeta in the drop-down. We'll delete the boilerplate text here so we can type out our own example. In our $searchMeta stage, we need to specify the facets by first giving them a name, sightingWeekFacet, and the type, date. We specify the path, date, which is the name of the field with the data that we will use to create the buckets.

Then we create the boundaries, an array of the first days of each week that we wish to have as the buckets and a default bucket for search results that do not fit into any of the facets called other. We then write a query operator for the term Northern Cardinal in the species common field to see search results of Cardinal sightings and what weeks those sightings took place. Let's take a look at our results for this aggregation stage. We see that four buckets of data were created.

And when the results are returned to our applications end-user, they will see the cardinal sightings broken down by the week in which the sighting occurred. We have successfully used facets. In this lesson, we learned how to use facets to make search results easier for your application's users to find records. We updated our search indexes, field mappings, to include facet fields.

Then we used the $searchMeta aggregation stage to specify what buckets we want to use to categorize search results. For next steps, you may want to try implementing facets in your application. To see how to do this, check out the documentation for the driver of your language of choice.


<details><summary>Timestamped transcript</summary>

```
Hi, there. In this video, we'll use facets and the search meta aggregation stage to customize search results by categorizing them. In order to get the most out of this lesson, you should know how to create a search index and how to use the search aggregation stage to create an atlas search query. Facets are buckets that we group our search results into. For example, when you search for a term in a social media app like Facebook, you may see the results grouped by people, pages, posts, groups, and events. This will help users find what they're looking for faster by suggesting categories where the user can expect to find a specific type of information. To begin creating our facets, we first need to decide which field to use for categorizing the search results.
The data types that we might consider for these categories are numbers, dates, or strings. Let's look at an example where we have a dataset of bird sightings and we would like for our users to search for sightings and see results grouped by the week in which the sightings occurred. We need to create a field mapping in our search index for the field that will be used to create those groupings. To do this, let's first toggle off dynamic mapping to add our field mappings. Scroll down to the field mapping section and then select date from the drop-down menu. Next week, click "Add Data Type", and select the data type here, in this case, date facet. We can also create field mappings for other fields that the user of this bird tracking application might search by.
For example, off-screen, I also added species_common and species_scientific, both with the data type string. With that, our search index is ready to be queried. Instead of using a regular search stage in the aggregation pipeline, we'll use a $searchMeta stage in order to see the facets and how many results are in each bucket. The buckets that the search will be filtered into are not part of the search results themselves. They're part of the search metadata, information about how the search was carried out. As of now, there are two pieces of metadata for atlas search, the facets and the count, which is the number of results returned in each of the facets. Let's go to our test aggregation pipeline in MongoDB Atlas and create a $searchMeta stage by selecting $searchMeta in the drop-down.
We'll delete the boilerplate text here so we can type out our own example. In our $searchMeta stage, we need to specify the facets by first giving them a name, sightingWeekFacet, and the type, date. We specify the path, date, which is the name of the field with the data that we will use to create the buckets. Then we create the boundaries, an array of the first days of each week that we wish to have as the buckets and a default bucket for search results that do not fit into any of the facets called other. We then write a query operator for the term Northern Cardinal in the species common field to see search results of Cardinal sightings and what weeks those sightings took place. Let's take a look at our results for this aggregation stage. We see that four buckets of data were created.
And when the results are returned to our applications end-user, they will see the cardinal sightings broken down by the week in which the sighting occurred. We have successfully used facets. In this lesson, we learned how to use facets to make search results easier for your application's users to find records. We updated our search indexes, field mappings, to include facet fields. Then we used the $searchMeta aggregation stage to specify what buckets we want to use to categorize search results. For next steps, you may want to try implementing facets in your application. To see how to do this, check out the documentation for the driver of your language of choice.
```

</details>
