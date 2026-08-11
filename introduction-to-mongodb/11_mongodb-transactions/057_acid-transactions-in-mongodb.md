# ACID Transactions in MongoDB

- **Course:** Introduction To Mongodb
- **Module 11:** MongoDB Transactions
- **Lecture #:** 57
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/M8Q8I/acid-transactions-in-mongodb
- **Extracted:** 2026-08-11 10:01:54

---

In this video, we'll look at how ACID transactions work with the document model in MongoDB. We'll cover the difference between single and multi-document ACID transactions in MongoDB and discuss when you should use a multi-document ACID transaction. Remember, an ACID transaction is a set of database operations that must be atomic. That is, they must either happen altogether successfully or fail together all at the same time.

Due to the nature of the document model, database operations that only affect one document are inherently atomic in MongoDB. In other words, an operation like update one, which is used to update a single document is technically an ACID transaction. This means that if we use update one to update multiple fields in a document, as we see in this example, either the quantity, details and tags fields will all be updated or none of them will be. These changes will all be visible to clients at the same time.

No extra steps are required to make sure that this operation has acid properties. In contrast, operations that affect multiple documents in MongoDB are not inherently atomic and do require some extra steps in order to be an ACID transaction. For example, consider adding an item to a shopping cart and an e-commerce application. We can use the update one method to add an item to a customer shopping cart.

Then we can also use update one on the product inventory collection to make sure that the item is also deducted from the inventory to keep the database consistent. Since these operations affect multiple documents, a shopping cart and a product inventory, these two write operations are not inherently atomic. In order for the database to remain consistent, we need to know that these operations need to be implemented as a multi-document ACID transaction. The decision to use in multi-document ACID transaction requires in-depth knowledge of your application requirements and should not be taken lightly.

The reason for this is that MongoDB essentially locks all the documents involved in a write operation in a multi-document transaction. As such, multi-document transactions incur a much greater performance penalty and can affect the latency of your application. Think about multi-document transactions as a precise tool. They should only be used in the special circumstance when you need to make absolutely certain that multi-document operations are completed with ACID properties.

Here are the key takeaways from this video. When working with MongoDB, all single document operations are inherently atomic. Therefore, no extra steps are needed to provide ACID properties to single document operations. However, if we need multi-document operations to have ACID properties, we then need to make sure that they're wrapped in a multi-document transaction.

Multi-document ACID transactions should be used as a precise tool only when ACID properties are absolutely necessary.


<details><summary>Timestamped transcript</summary>

```
In this video, we'll look at how ACID transactions work with the document model in MongoDB. We'll cover the difference between single and multi-document ACID transactions in MongoDB and discuss when you should use a multi-document ACID transaction. Remember, an ACID transaction is a set of database operations that must be atomic. That is, they must either happen altogether successfully or fail together all at the same time. Due to the nature of the document model, database operations that only affect one document are inherently atomic in MongoDB. In other words, an operation like update one, which is used to update a single document is technically an ACID transaction. This means that if we use update one to update multiple fields in a document, as we see in this example, either the quantity, details and tags fields will all be updated or none of them will be.
These changes will all be visible to clients at the same time. No extra steps are required to make sure that this operation has acid properties. In contrast, operations that affect multiple documents in MongoDB are not inherently atomic and do require some extra steps in order to be an ACID transaction. For example, consider adding an item to a shopping cart and an e-commerce application. We can use the update one method to add an item to a customer shopping cart. Then we can also use update one on the product inventory collection to make sure that the item is also deducted from the inventory to keep the database consistent. Since these operations affect multiple documents, a shopping cart and a product inventory, these two write operations are not inherently atomic.
In order for the database to remain consistent, we need to know that these operations need to be implemented as a multi-document ACID transaction. The decision to use in multi-document ACID transaction requires in-depth knowledge of your application requirements and should not be taken lightly. The reason for this is that MongoDB essentially locks all the documents involved in a write operation in a multi-document transaction. As such, multi-document transactions incur a much greater performance penalty and can affect the latency of your application. Think about multi-document transactions as a precise tool. They should only be used in the special circumstance when you need to make absolutely certain that multi-document operations are completed with ACID properties. Here are the key takeaways from this video.
When working with MongoDB, all single document operations are inherently atomic. Therefore, no extra steps are needed to provide ACID properties to single document operations. However, if we need multi-document operations to have ACID properties, we then need to make sure that they're wrapped in a multi-document transaction. Multi-document ACID transactions should be used as a precise tool only when ACID properties are absolutely necessary.
```

</details>
