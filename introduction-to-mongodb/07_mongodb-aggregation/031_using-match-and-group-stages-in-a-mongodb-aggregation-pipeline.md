# Using $match and $group Stages in a MongoDB Aggregation Pipeline

- **Course:** Introduction To Mongodb
- **Module 7:** MongoDB Aggregation
- **Lecture #:** 31
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/EVlVl/using-match-and-group-stages-in-a-mongodb-aggregation-pipeline
- **Extracted:** 2026-08-11 09:57:04

---

Hello. In this video, we'll examine two of the most commonly used aggregation pipeline stages, match and group. We'll use match to filter for documents that satisfy a query and use group to group documents by a group key. The match stage filters for documents that meet specified conditions and passes those documents to the next stage of the pipeline.

The match stage takes one argument, which is a query. This query works exactly like a find command, when using a match stage place as early as possible in the pipeline so that it can use indexes because it filters, it reduces the number of documents which lessens the amount of processing required. Let's go through an example of a match stage. We have a collection that contains all the ZIP codes in the United States.

Let's use a match stage to find all of the ZIP codes from California, which is abbreviated as CA. Great. Now what if we wanted to group all of those ZIP codes by city? To do this, we'll add the group aggregation stage.

The group stage groups documents according to a group key. The output of this stage is one document for each unique value of the group key. The group stage requires us to specify an _id, which will be the group key. This is the field that we'll group by.

The group stage may also include one or more fields with an accumulator.An accumulator is an expression that specifies how to aggregate information for each of the groups. For example, we're setting our Group Key to the City field. Then we'll use count as an accumulator to find how many ZIP codes are in each city. Now that we understand match and group, let's put them together and create an aggregation pipeline.

First we call the aggregate method on our ZIPs collection by using dot notation. Then we create a match stage where the criteria state is CA. Then we add a group stage where the group key is the city. This is done by a field reference.

We also add another field called totalZips and use a count accumulator to find out how many zips are in each city. Now let's run the code. Excellent. Our first aggregation pipeline shows us how many ZIP codes are in each city in California.

In this video, you learned how to use the match stage to filter for documents that match the criteria. You also learned how to use the group stage to create a single document for each distinct value that we grouped by. Next, you can learn about more aggregation stages.


<details><summary>Timestamped transcript</summary>

```
Hello. In this video, we'll examine two of the most commonly used aggregation pipeline stages, match and group. We'll use match to filter for documents that satisfy a query and use group to group documents by a group key. The match stage filters for documents that meet specified conditions and passes those documents to the next stage of the pipeline. The match stage takes one argument, which is a query. This query works exactly like a find command, when using a match stage place as early as possible in the pipeline so that it can use indexes because it filters, it reduces the number of documents which lessens the amount of processing required. Let's go through an example of a match stage.
We have a collection that contains all the ZIP codes in the United States. Let's use a match stage to find all of the ZIP codes from California, which is abbreviated as CA. Great. Now what if we wanted to group all of those ZIP codes by city? To do this, we'll add the group aggregation stage. The group stage groups documents according to a group key. The output of this stage is one document for each unique value of the group key.
The group stage requires us to specify an _id, which will be the group key. This is the field that we'll group by. The group stage may also include one or more fields with an accumulator.An accumulator is an expression that specifies how to aggregate information for each of the groups. For example, we're setting our Group Key to the City field. Then we'll use count as an accumulator to find how many ZIP codes are in each city. Now that we understand match and group, let's put them together and create an aggregation pipeline. First we call the aggregate method on our ZIPs collection by using dot notation.
Then we create a match stage where the criteria state is CA. Then we add a group stage where the group key is the city. This is done by a field reference. We also add another field called totalZips and use a count accumulator to find out how many zips are in each city. Now let's run the code. Excellent. Our first aggregation pipeline shows us how many ZIP codes are in each city in California.
In this video, you learned how to use the match stage to filter for documents that match the criteria. You also learned how to use the group stage to create a single document for each distinct value that we grouped by. Next, you can learn about more aggregation stages.
```

</details>
