# Introduction to MongoDB Aggregation

- **Course:** Introduction To Mongodb
- **Module 7:** MongoDB Aggregation
- **Lecture #:** 30
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/MeD1o/introduction-to-mongodb-aggregation
- **Extracted:** 2026-08-11 09:56:54

---

Hi folks, in this video we'll introduce and explore the MongoDB aggregation framework that's used to build multistage queries. By the end of the lesson, you'll be able to identify the components of an aggregation pipeline. In the context of databases, aggregation is the analysis and summary of data. An aggregation stage is an aggregation operation that is performed on the data and does not permanently alter the source data.

MongoDB took this concept a step further by creating an aggregation pipeline in which the developer specifies the aggregation operations one at a time in order. We can run a single aggregation stage to get the information that we need. But what makes aggregation in MongoDB unique is that we can string together aggregation stages to create a pipeline. A pipeline consists of multiple stages where data can be filtered, sorted, grouped, and transformed.

Documents that are output from one stage become input into the next stage. In MongoDB Atlas, we can use a visual editor to create and test aggregation pipelines by adding stages one by one. We can see the results from each stage. This is a great way to get started with aggregation, and you may want to use this tool to explore the different stages.

However, for the purposes of this course, we'll be showing aggregation done using the MongoDB CLI so that you can more easily see the whole pipeline in this video. There's also support for aggregation in MongoDB language drivers so take a look at the documentation for the language of your choice. Let's break down the pieces of an aggregation pipeline using.notation on the collection db.collection name and the aggregate function, which takes an array of aggregation stages to form the pipeline. First, let's learn about the stages of aggregation.

Each stage is a single operation on the data. Some of the commonly used stages are match, which filters for data that matches certain criteria, group, which groups documents based on criteria, and sort, which puts the documents in a specified order. These operations are useful both individually and together in a pipeline for analyzing the data. Each stage includes syntax to carry out the operation.

The syntax for each stage is dependent on the stage. If you're unsure about the syntax, refer to the documentation for that particular stage. The syntax for some stages may include expressions. For example, the match stage expects the same syntax as the MongoDB find method and most other aggregation stages like this example with project, you can expect to use expression operators.

When looking at aggregation syntax, you may notice that sometimes field names are prefixed with a dollar sign. This is a field path. It allows us to refer to the value in that field. In this example, we're setting a new field called default username to a concatenated string composed of the values from the first name field and the last name field.

In this video, we discussed what aggregation is and how to set up an aggregation pipeline. We also explained different aggregation stages, operators and expressions and field references. These basics of aggregation will take you far. The next step is to explore each aggregation stage and learn more about what they can do.


<details><summary>Timestamped transcript</summary>

```
Hi folks, in this video we'll introduce and explore the MongoDB aggregation framework that's used to build multistage queries. By the end of the lesson, you'll be able to identify the components of an aggregation pipeline. In the context of databases, aggregation is the analysis and summary of data. An aggregation stage is an aggregation operation that is performed on the data and does not permanently alter the source data. MongoDB took this concept a step further by creating an aggregation pipeline in which the developer specifies the aggregation operations one at a time in order. We can run a single aggregation stage to get the information that we need. But what makes aggregation in MongoDB unique is that we can string together aggregation stages to create a pipeline.
A pipeline consists of multiple stages where data can be filtered, sorted, grouped, and transformed. Documents that are output from one stage become input into the next stage. In MongoDB Atlas, we can use a visual editor to create and test aggregation pipelines by adding stages one by one. We can see the results from each stage. This is a great way to get started with aggregation, and you may want to use this tool to explore the different stages. However, for the purposes of this course, we'll be showing aggregation done using the MongoDB CLI so that you can more easily see the whole pipeline in this video. There's also support for aggregation in MongoDB language drivers so take a look at the documentation for the language of your choice.
Let's break down the pieces of an aggregation pipeline using.notation on the collection db.collection name and the aggregate function, which takes an array of aggregation stages to form the pipeline. First, let's learn about the stages of aggregation. Each stage is a single operation on the data. Some of the commonly used stages are match, which filters for data that matches certain criteria, group, which groups documents based on criteria, and sort, which puts the documents in a specified order. These operations are useful both individually and together in a pipeline for analyzing the data. Each stage includes syntax to carry out the operation. The syntax for each stage is dependent on the stage.
If you're unsure about the syntax, refer to the documentation for that particular stage. The syntax for some stages may include expressions. For example, the match stage expects the same syntax as the MongoDB find method and most other aggregation stages like this example with project, you can expect to use expression operators. When looking at aggregation syntax, you may notice that sometimes field names are prefixed with a dollar sign. This is a field path. It allows us to refer to the value in that field. In this example, we're setting a new field called default username to a concatenated string composed of the values from the first name field and the last name field.
In this video, we discussed what aggregation is and how to set up an aggregation pipeline. We also explained different aggregation stages, operators and expressions and field references. These basics of aggregation will take you far. The next step is to explore each aggregation stage and learn more about what they can do.
```

</details>
