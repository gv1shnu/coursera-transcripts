# Deleting MongoDB Indexes

- **Course:** Introduction To Mongodb
- **Module 8:** MongoDB Indexes
- **Lecture #:** 40
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/O7M0n/deleting-mongodb-indexes
- **Extracted:** 2026-08-11 09:58:44

---

Hello. In this video, you'll learn about the impact of deleting an index and how to delete an existing index from a collection. We recommend having indexes in collections because they can speed up queries and improve performance, but indexes also have a write cost. Every time we insert new documents or update them, the index keys need to be updated.

Too many indexes in a collection can affect the system performance formance, so we should delete unused or redundant indexes. Before deleting an index, make sure the index is not being used. Deleting an index that's the only index supporting a query will affect the performance of that query. With no suitable index, queries will have to scan every document in the collection to return results.

This greatly affects performance. We can delete any of the indexes in a collection except for the default index on _ID. Also, recreating an index that was deleted can cost extra time and resources. If we're not sure if the index is needed, hide the index instead of deleting it.

To hide the index, we use the db.collection.hideIndex command. MongoDB does not use hidden indexes in queries, but continues to update their keys. This way, we can assess if removing the index affects the performance and can unhide the index if needed. Unhiding an index is faster than recreating it.

Note that some indexes might seem necessary, but they could be redundant in a collection. As an example, consider compound indexes, which can cover queries that include the index prefix. For instance, these queries, to search for a specific username and the active status can both use a compound index username-1_active_1. So the index username _1 in the collection becomes redundant.

Now let's delete an index. We'll delete 1 index from the customer's collection. First, we use the getIndexes command, which shows us five indexes. Let's delete the compound index on active, birthday and name.

Let's examine the details of this index. Each index has a name and a key. The index name is active _1_birthday_-1, _name_1, and the index key is the list of fields and the store order when creating the index. In a production environment, it's best practice to hide the index before deleting it.

This avoids having to recreate it later if we realize the index was needed for a query. To hide the index, we use the hideIndex method and specify the index by name or key. We can use the dropIndex method on the collection to delete the index and specify the index by name or by key. For this example, we'll use Drop Index in the command line, specifying the index name.

Perfect, the output shows that the index was deleted, the number of indexes was 5, and the delete operation succeeded. We can also delete indexes from the Atlas UI. Let's browse the collections in the cluster and access the customer's collection. From the indexes section, we see that this collection has three indexes.

We can click the Drop Index button for the specific index that we want to delete. If we want to delete multiple indexes, we can use the dropIndexes method. With no parameters, this command deletes all the indexes in the collection except for the _ID index. We can specify one index or an array of indexes to delete from a collection at the same time.

Let's go back to the command line and delete all indexes from the customer's collection. We get an OK response. Now, let's check which indexes are still in the collection by using getIndexes. Great.

Only _ID index remains. Great work. Let's recap what you learned in this video. Deleting indexes may affect the performance of any queries that are using that index.

We use dropIndex to delete one index, and we use dropIndexes to delete more than one index from a collection. We use hideIndex to hide an index before deleting it to confirm that the index is not necessary. We can also delete indexes directly in the Atlas UI with a Drop Index option.


<details><summary>Timestamped transcript</summary>

```
Hello. In this video, you'll learn about the impact of deleting an index and how to delete an existing index from a collection. We recommend having indexes in collections because they can speed up queries and improve performance, but indexes also have a write cost. Every time we insert new documents or update them, the index keys need to be updated. Too many indexes in a collection can affect the system performance formance, so we should delete unused or redundant indexes. Before deleting an index, make sure the index is not being used. Deleting an index that's the only index supporting a query will affect the performance of that query.
With no suitable index, queries will have to scan every document in the collection to return results. This greatly affects performance. We can delete any of the indexes in a collection except for the default index on _ID. Also, recreating an index that was deleted can cost extra time and resources. If we're not sure if the index is needed, hide the index instead of deleting it. To hide the index, we use the db.collection.hideIndex command. MongoDB does not use hidden indexes in queries, but continues to update their keys.
This way, we can assess if removing the index affects the performance and can unhide the index if needed. Unhiding an index is faster than recreating it. Note that some indexes might seem necessary, but they could be redundant in a collection. As an example, consider compound indexes, which can cover queries that include the index prefix. For instance, these queries, to search for a specific username and the active status can both use a compound index username-1_active_1. So the index username _1 in the collection becomes redundant. Now let's delete an index.
We'll delete 1 index from the customer's collection. First, we use the getIndexes command, which shows us five indexes. Let's delete the compound index on active, birthday and name. Let's examine the details of this index. Each index has a name and a key. The index name is active _1_birthday_-1, _name_1, and the index key is the list of fields and the store order when creating the index. In a production environment, it's best practice to hide the index before deleting it.
This avoids having to recreate it later if we realize the index was needed for a query. To hide the index, we use the hideIndex method and specify the index by name or key. We can use the dropIndex method on the collection to delete the index and specify the index by name or by key. For this example, we'll use Drop Index in the command line, specifying the index name. Perfect, the output shows that the index was deleted, the number of indexes was 5, and the delete operation succeeded. We can also delete indexes from the Atlas UI. Let's browse the collections in the cluster and access the customer's collection.
From the indexes section, we see that this collection has three indexes. We can click the Drop Index button for the specific index that we want to delete. If we want to delete multiple indexes, we can use the dropIndexes method. With no parameters, this command deletes all the indexes in the collection except for the _ID index. We can specify one index or an array of indexes to delete from a collection at the same time. Let's go back to the command line and delete all indexes from the customer's collection. We get an OK response.
Now, let's check which indexes are still in the collection by using getIndexes. Great. Only _ID index remains. Great work. Let's recap what you learned in this video. Deleting indexes may affect the performance of any queries that are using that index. We use dropIndex to delete one index, and we use dropIndexes to delete more than one index from a collection.
We use hideIndex to hide an index before deleting it to confirm that the index is not necessary. We can also delete indexes directly in the Atlas UI with a Drop Index option.
```

</details>
