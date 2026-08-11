# Using $project, $count, and $set Stages in a MongoDB Aggregation Pipeline

- **Course:** Introduction To Mongodb
- **Module 7:** MongoDB Aggregation
- **Lecture #:** 33
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/EkXVQ/using-project-count-and-set-stages-in-a-mongodb-aggregation-pipeline
- **Extracted:** 2026-08-11 09:57:26

---

Hi, in this video you'll learn about three aggregation stages, project, set, and count. We'll explain when to use these stages and observe each of them in action. We'll start with the project stage. The project stage determines the output document shape.

It allows us to specify the existing or new fields that will be returned by the aggregation. This stage performs a projection similar to the one we apply in find operations. It should usually be the last stage, because it specifies the exact fields in the output. MongoDB already works out which fields are needed and reads only the fields that are required in the pipeline, so there's usually no reason to use project earlier in the pipeline.

Projection can be specified as either inclusion or exclusion. In the project stage, either include the fields you would like to keep by setting the value to 1, or set the value to 0 if you are specifying the fields you want to exclude. If the projected fields are new fields, we can specify the value that we want to assign to them. You can also specify a new value to existing fields in project.

Let's go through an example with the training database and the zips collection. The collection includes the fields state, city, zip, loc, pop, and _id. In the project stage, we can specify the fields to include or exclude in the output. This is just like specifying field projections in the find method.

Let's use aggregate with the project stage to include state and zip in the output. To do this, we'll set the state and zip value to 1. We add a field called population with the value of the pop field. And we explicitly exclude the _id field by setting it to 0, because otherwise it will be included by default.

The documents in the output have only three fields, zip, state, and population. Now let's discuss the set stage. Rather than specifying output like project, the set stage adds or modifies fields in the pipeline. This is useful when we want to change existing fields in the pipeline or add new ones to be used in upcoming pipeline stages without having to specify all the existing fields.

The set stage takes the field names and values that we want to add or change. As an example, let's add a field to show the projected population in the next year based on average population growth in each ZIP code. In the zips collection, we apply a set stage to create a new field called pop_2022. This will be the current population plus the US population growth rate from 2021, 0.31%.

So 1.0031 multiplied by the original population value and rounded to the nearest whole number, because we're referencing people. The new pop_2022 field is now available in the pipeline. Finally, we'll discuss the count stage. This stage counts the number of documents in the pipeline and returns the total count.

The count stage receives a string that represents the new fields that's returned with the total document count. Let's apply the aggregate command in the zips collection with the count stage. We use total_zips as the count field name. Note that the output of this aggregation pipeline is a single document with only one field, which is total_zips.

The value is the total number of documents in the pipeline, 29,367. Excellent, in this video you learned how to use project to specify the output, set to add new fields or change fields, and count to count the total number of documents in the pipeline.


<details><summary>Timestamped transcript</summary>

```
Hi, in this video you'll learn about three aggregation stages, project, set, and count. We'll explain when to use these stages and observe each of them in action. We'll start with the project stage. The project stage determines the output document shape. It allows us to specify the existing or new fields that will be returned by the aggregation. This stage performs a projection similar to the one we apply in find operations. It should usually be the last stage, because it specifies the exact fields in the output.
MongoDB already works out which fields are needed and reads only the fields that are required in the pipeline, so there's usually no reason to use project earlier in the pipeline. Projection can be specified as either inclusion or exclusion. In the project stage, either include the fields you would like to keep by setting the value to 1, or set the value to 0 if you are specifying the fields you want to exclude. If the projected fields are new fields, we can specify the value that we want to assign to them. You can also specify a new value to existing fields in project. Let's go through an example with the training database and the zips collection. The collection includes the fields state, city, zip, loc, pop, and _id.
In the project stage, we can specify the fields to include or exclude in the output. This is just like specifying field projections in the find method. Let's use aggregate with the project stage to include state and zip in the output. To do this, we'll set the state and zip value to 1. We add a field called population with the value of the pop field. And we explicitly exclude the _id field by setting it to 0, because otherwise it will be included by default. The documents in the output have only three fields, zip, state, and population.
Now let's discuss the set stage. Rather than specifying output like project, the set stage adds or modifies fields in the pipeline. This is useful when we want to change existing fields in the pipeline or add new ones to be used in upcoming pipeline stages without having to specify all the existing fields. The set stage takes the field names and values that we want to add or change. As an example, let's add a field to show the projected population in the next year based on average population growth in each ZIP code. In the zips collection, we apply a set stage to create a new field called pop_2022. This will be the current population plus the US population growth rate from 2021, 0.31%.
So 1.0031 multiplied by the original population value and rounded to the nearest whole number, because we're referencing people. The new pop_2022 field is now available in the pipeline. Finally, we'll discuss the count stage. This stage counts the number of documents in the pipeline and returns the total count. The count stage receives a string that represents the new fields that's returned with the total document count. Let's apply the aggregate command in the zips collection with the count stage. We use total_zips as the count field name.
Note that the output of this aggregation pipeline is a single document with only one field, which is total_zips. The value is the total number of documents in the pipeline, 29,367. Excellent, in this video you learned how to use project to specify the output, set to add new fields or change fields, and count to count the total number of documents in the pipeline.
```

</details>
