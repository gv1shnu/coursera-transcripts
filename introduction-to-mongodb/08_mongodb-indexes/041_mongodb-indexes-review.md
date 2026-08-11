# MongoDB Indexes Review

- **Course:** Introduction To Mongodb
- **Module 8:** MongoDB Indexes
- **Lecture #:** 41
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/lSpYE/mongodb-indexes-review
- **Extracted:** 2026-08-11 09:58:56

---

In this unit, you learned that MongoDB indexes support the efficient execution of queries, you also learned about the trade-offs of using indexes. You gained a deeper understanding of the most common index types and how to create and delete them. To create indexes in a collection, we use the db.coll.createIndex command. We can create single field indexes when the index only includes one field, and compound indexes if the index has more than one field.

When the index includes an array field, it is a multikey index. We also use the getIndexes command and the indexes section in the Atlas UI to review the indexes in a collection. Remember that indexes can include the unique constraint to ensure that the values in the fields defined by the index are unique in the collection. Also remember that the order of the fields and the sort order of the field values matter when defining compound indexes, use the quality, sort and range guideline, and review the sort order of the field values.

Additionally, take into account that indexes can cover queries if all the fields in the query are included in the index keys. Finally, we can use the explain command in the collection or in the queries to determine if the index is being used, and we can delete any unnecessary index by using the dropIndex command. However, be aware that deleting indexes that are in use will impact query performance. Before deleting an index, first hide the index so you can determine the performance impact.

To hide an index, we use the hideIndex command. Now that you've gained a general understanding of how to create and use indexes, you'll be able to improve the performance of your queries in MongoDB. As a next step, review MongoDB's documentation on indexes, congratulations on completing this unit.


<details><summary>Timestamped transcript</summary>

```
In this unit, you learned that MongoDB indexes support the efficient execution of queries, you also learned about the trade-offs of using indexes. You gained a deeper understanding of the most common index types and how to create and delete them. To create indexes in a collection, we use the db.coll.createIndex command. We can create single field indexes when the index only includes one field, and compound indexes if the index has more than one field. When the index includes an array field, it is a multikey index. We also use the getIndexes command and the indexes section in the Atlas UI to review the indexes in a collection. Remember that indexes can include the unique constraint to ensure that the values in the fields defined by the index are unique in the collection.
Also remember that the order of the fields and the sort order of the field values matter when defining compound indexes, use the quality, sort and range guideline, and review the sort order of the field values. Additionally, take into account that indexes can cover queries if all the fields in the query are included in the index keys. Finally, we can use the explain command in the collection or in the queries to determine if the index is being used, and we can delete any unnecessary index by using the dropIndex command. However, be aware that deleting indexes that are in use will impact query performance. Before deleting an index, first hide the index so you can determine the performance impact. To hide an index, we use the hideIndex command. Now that you've gained a general understanding of how to create and use indexes, you'll be able to improve the performance of your queries in MongoDB.
As a next step, review MongoDB's documentation on indexes, congratulations on completing this unit.
```

</details>
