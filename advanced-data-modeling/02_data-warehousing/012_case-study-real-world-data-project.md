# Case Study: Real world data project

- **Course:** Advanced Data Modeling
- **Module 2:** Data Warehousing
- **Lecture #:** 12
- **URL:** https://www.coursera.org/learn/advanced-data-modeling/lecture/8lQCN/case-study-real-world-data-project
- **Extracted:** 2026-06-22 20:11:30

---

Very large databases are very hard to get data from. ETL pipelines are some of the critical ways in order to ensure that different products get quicker access to the data they need. Hi. My name is Moxxy Herrera.

I use data and pronounce and I'm a software engineer at Meta in the Menlo Park office. ETL stands for extract, transform, and load. This is one of the common ways that data will be transferred to particular areas. You will have some data source and then perhaps a staging area for the data and then a consumer of the data.

Splitting it up into different data consumers allows you to do two things. One, have the raw data stored in a backup in a warehouse, and then it's extracted, then transforms the data that you need so that can be loaded by the consumers that need that data at the time of use. The purpose of an ETL pipeline can vary depending on your uses. Fundamentally, the point is either to bring together a whole bunch of different data sources or have very large data sources abstracted away from the consumers of the data.

The extract is bringing together all those data forces. Transform is doing the data validation, the scrubbing, the cleaning, maybe encryption. Then finally, the loading is where the end consumers are actually taking the data. The exact usage depends on the case.

What this means is that an ETL pipeline is a very common process that's used to solve many different data problems. Part of the point of an ETL pipeline is to take all these different sources that may be built under different systems and bring them into one system that specific consumers can use. This allows for parallelization, and so the decisions are often made around what do the end-consumers need? Where am I getting the data from?

How am I organizing this and what will lead to the most performance approach to this. One of the most common problems when dealing with data pipelines is sometimes handling the volume of data and the very rich source of data. This can make it very difficult to ensure that your pipeline is up-to-date and has the data that is needed at the time of use. Understanding the delay and how these pipelines works are very critical to ensure that you are not expecting data consumers to be able to grab data that is actually available to them.

A change to the database may then trigger a need for a change in the data pipelines that you have built depending on the needs of the consumer, and what the base change is. What this requires is a strong understanding of the need of that pipeline, what its goals are, and a strong sense of ownership by the stakeholders of that pipeline. These updates happen all the time and this could trigger all sorts of different changes in our product team. This requires a lot of ownership and responsibility and understanding of ETL pipelines for when those changes occur and what changes you need to make to accommodate that.

There's a lot of data in the world. In fact, too much data to store in a single database. ETL pipelines are an absolutely fundamental point in this world of big data, cloud computing, and the metaverse.
