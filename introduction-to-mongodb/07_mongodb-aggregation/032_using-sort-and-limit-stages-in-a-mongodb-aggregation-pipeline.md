# Using $sort and $limit Stages in a MongoDB Aggregation Pipeline

- **Course:** Introduction To Mongodb
- **Module 7:** MongoDB Aggregation
- **Lecture #:** 32
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/AO7HN/using-sort-and-limit-stages-in-a-mongodb-aggregation-pipeline
- **Extracted:** 2026-08-11 09:57:15

---

Hi there, in this video you'll learn about the sort and the limit aggregation stages. These two stages can be combined to quickly find the documents with the top or bottom values in a data set. A sort stage sorts all input documents and passes them through the pipeline in sorted order. This can be a numeric value, strings that can be arranged in alphabetical order, dates or timestamps.

When entering the field to sort by, we use one to indicate a sort in ascending order where the lesser values come first. And we use -1 to indicate a sort in descending order, where the greater values come first. Now let's work through an example. We have a collection with all of the zip codes in the United States, along with other information including the population for each zip code.

Let's sort the documents by the population using the pop field. We want to find which zip codes contain the greatest population. So we'll create a sort stage and focus on the pop field. We want to find the greatest values first, so we'll put it in descending order by using -1.

When we view the results, we find that the 11226 zip code in Brooklyn has the greatest population of any zip code with a population of 111,396. The documents are ordered, so it's easier to identify the greatest value, but the results still show all of the documents at this point in the aggregation pipeline. Let's limit the results to the top five documents with the greatest population. To do this, we'll use the limit stage, which limits the number of documents that are passed on to the next aggregation stage.

It only takes a positive integer that represents how many documents to retain. Let's add a limit stage to our aggregation pipeline and limit the number of documents to three. This will show us only the three zip codes with the greatest populations. When we run the pipeline the results now show only three documents.

It's important to note that when we're creating aggregation pipelines, we are explicitly specifying the order of stages. This means that we need to be mindful that our stages are in the intended order. For example, if we first limited and then sorted here, we would get a sorted list of the first five records in the collection, which is not what we want. In this video, you learned how to use sort to order documents based on the values in a field.

You also learned how to use limit to restrict the number of documents in the aggregation pipeline. These stages can be used to help organize the data in a collection and help answer questions in data analysis. Great work.


<details><summary>Timestamped transcript</summary>

```
Hi there, in this video you'll learn about the sort and the limit aggregation stages. These two stages can be combined to quickly find the documents with the top or bottom values in a data set. A sort stage sorts all input documents and passes them through the pipeline in sorted order. This can be a numeric value, strings that can be arranged in alphabetical order, dates or timestamps. When entering the field to sort by, we use one to indicate a sort in ascending order where the lesser values come first. And we use -1 to indicate a sort in descending order, where the greater values come first. Now let's work through an example.
We have a collection with all of the zip codes in the United States, along with other information including the population for each zip code. Let's sort the documents by the population using the pop field. We want to find which zip codes contain the greatest population. So we'll create a sort stage and focus on the pop field. We want to find the greatest values first, so we'll put it in descending order by using -1. When we view the results, we find that the 11226 zip code in Brooklyn has the greatest population of any zip code with a population of 111,396. The documents are ordered, so it's easier to identify the greatest value, but the results still show all of the documents at this point in the aggregation pipeline.
Let's limit the results to the top five documents with the greatest population. To do this, we'll use the limit stage, which limits the number of documents that are passed on to the next aggregation stage. It only takes a positive integer that represents how many documents to retain. Let's add a limit stage to our aggregation pipeline and limit the number of documents to three. This will show us only the three zip codes with the greatest populations. When we run the pipeline the results now show only three documents. It's important to note that when we're creating aggregation pipelines, we are explicitly specifying the order of stages.
This means that we need to be mindful that our stages are in the intended order. For example, if we first limited and then sorted here, we would get a sorted list of the first five records in the collection, which is not what we want. In this video, you learned how to use sort to order documents based on the values in a field. You also learned how to use limit to restrict the number of documents in the aggregation pipeline. These stages can be used to help organize the data in a collection and help answer questions in data analysis. Great work.
```

</details>
