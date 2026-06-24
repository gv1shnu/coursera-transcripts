# Dimensional data modeling in practice

- **Course:** Advanced Data Modeling
- **Module 2:** Data Warehousing
- **Lecture #:** 14
- **URL:** https://www.coursera.org/learn/advanced-data-modeling/lecture/4GlFn/dimensional-data-modeling-in-practice
- **Extracted:** 2026-06-22 20:11:53

---

At this stage of the course, you should be familiar with the dimensional data model and many of the key concepts related to it. But how do you build a dimensional data model? The process for building a dimensional data model revolves around four key steps known as Kimball's dimensional data modeling. In this video, you'll explore the approach and review each of these four steps in detail.

Let's begin with a look at Global Super Store and their use of the dimensional data model. Global Super Store wants to perform data analytics to understand their recent sales figures. This requires building a dimensional data model that will help them understand their business and the factors that impact on their sales and profits. Before you explore Global Super Store's process, let's quickly recap the purpose of a dimensional data model and take a high-level look at the four key steps.

A dimensional data model must focus on particular aspects of a business or organization in order to address specific problems. The model is created using a systematic approach that revolves around four key steps. These steps include the business processes, the grain, the dimensions, and the facts. Each of these steps is a choice.

You need to choose a business process that your dimensional model must investigate. You then need to choose the facts and dimensions that can provide the answers you need. Let's work through each of these four steps or choices and understand how they contribute to the process of building a dimensional data model. When building a dimensional data model, the first step is to identify or choose the specific business process to be addressed.

Once you've identified the process, you can then determine the grain of data in the data model. Global Super Store have decided that the business process to be addressed is their sales activity. Once you've decided on the process, you then need to choose the level of detail required. This is referred to as the grain.

What granularity or level of detail is required for the data warehouse to address your process problem? And what's the lowest level of detail required to address the issue? For example, Global Super Store need to analyze their sales data at both a yearly and daily level. They also need to investigate this data at the global and local level.

The next step in the process is to choose the dimensions. In this step, you need to choose the relevant dimensions. In other words, in what context do you need to explore your business activity? As you already know, Global Super Store need to analyze their sales data.

And they need to analyze this data in the context of products, customers, time, and locations. So now that you've identified the business process, the grain, and the dimensions, it's time to establish the facts. This is basically answering the question of, what do you want to measure? You need to select the measures that contain numeric data and populate your fact table with these attributes.

For example, Global Super Store need to explore their facts using the dimensions tables, location, product, and time. They can demonstrate how each of these dimensions impacts the sales. And they can also include relevant attributes that provide useful information about each dimension. Once you've decided what aspect of your business process you need to investigate and chosen the grain, related facts and dimensions, you can then create your schema.

Arrange your dimensions and dimensions tables. Global Super Store can arrange their dimensions and measures in a star schema. Their schema examines the performance of their sales activity in the context of four different dimensions, customers, products, locations, and time. And within each dimension is a set of relevant attributes that target the required data.

Once you've decided what aspect of your business process you need to investigate and chosen the related data and dimensions, you can create your schema. Global Super Store have identified their dimensions and measures step by step based on their business requirements. They can now perform different forms of data analysis to achieve their goals. You should now be familiar with using a systematic approach to build a dimensional data model.

And you should also be able to identify and explain each of the four steps in which you must make your decisions around data. You've made great progress on your advanced data modeling journey.
