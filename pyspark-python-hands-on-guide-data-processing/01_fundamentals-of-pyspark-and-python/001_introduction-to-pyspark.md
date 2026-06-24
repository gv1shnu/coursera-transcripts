# Introduction to PySpark

- **Course:** Pyspark Python Hands On Guide Data Processing
- **Module 1:** Fundamentals of PySpark and Python
- **Lecture #:** 1
- **URL:** https://www.coursera.org/learn/pyspark-python-hands-on-guide-data-processing/lecture/MErsH/introduction-to-pyspark
- **Extracted:** 2026-06-20 10:09:01

---

Now, before coming to PySpark, we'll actually see what is or how did the evolution of data occur. Now, it is imperative to understand the reason behind this digital of data that we are witnessing around us today. Now, in the early days, data was generated or accumulated by workers. So only the employees of the company entered the data into the system and the data points were very limited, that is capturing only a few fields.

But then came the internet and the information was made easily accessible to everyone using it. So now the users had the power to enter and generate their own data. Now, this was a massive shift as the number of internet users grew exponentially and the data created by these users grew at an even very higher rate. So for example, you have the login or the sign up forms, which allows the users to fill in their own details, uploading their photos or videos on various social platforms.

Now this resulted in huge data generation and the need for a fast and a scalable framework to process this amount of data. That is where we have the data generation, which has now gone to the next level as machines are generating and accumulating data. So every device around us is capturing data such as cars, buildings, mobiles, watches, flight engines, etc. and they are embedded using multiple monitoring sensors and recording data every second.

Now this data is even higher in magnitude than the user generated data. So now when we have, let's take an example, for example, so earlier when the data was still at enterprise level, a relational database was good enough to handle the needs. But as the size of data increased exponentially over the past couple of decades, a technonic shift happened to handle the big data and it was the birth of Spark. So traditionally we used to take the data and bring it to processor to process it.

But now it's so much data that is overwhelmed the processor. So now we are bringing multiple processors to the particular data. So this is known as parallel processing as data is being processed at a number of places at the same given time. So let us take a simple example to understand what is parallel processing.

Now assume that you are on a particular freeway, there is only one single tollbooth and every vehicle has to get in the single row in order to pass through the tollbooth. Now on an average, it would take one minute for each vehicle to pass. So for example, you have 10 vehicles, it would take around 10 minutes and for 100 it would take about 100 minutes. So this process is known as a single threaded process wherein you have one thread passing through one particular process and taking an equivalent time for all.

But imagine if instead of a single tollbooth, there are 10 different tollbooths on the same freeway and the vehicles can use any one of them to pass through. So now it would take only one minute in total for all the 10 vehicles to pass because there is no dependency for each particular vehicle. So now if we see this is known as the parallel processing. So the parallel or distributed computing works on a similar principle as it paralyzes the task and accumulates the final result at the end.

Now Spark is a framework to handle such massive datasets with parallel processing at high speed and is the robust mechanism. So now let's see how was Spark evolved from 2009. So earlier we had in 2009, it was created by UC Berkeley, then 2010 Spark became an open source which can be downloaded free from internet. In 2013 it was donated to the Apache server and then in 2014 first release of Spark was released that was Spark 1.0.0 after which we had the next version wherein we had the APIs for DataFrame, Machine Language, Pipeline and SparkARQ.

Then in 2016 we had the TensorFrame released for deep learning. In 2018 we had the next release of Spark that was 2.3. In 2019 the latest release of Spark that is 2.4.2 is being released. So we have understood the Spark uses a different data structure that is known as RDD.

Now RDD is known as resilient distributed data or dataset. Now it is resilient in the sense that they have an ability to recreate any point of time during the execution process. So RDD creates a new RDD using the last one and always has the ability to reconstruct in case of any error. So they are also immutable as original RDDs remain unaltered.

Now we'll see the importance or what is actually a Spark architecture that is the Spark core. So when we come to the Spark architecture, the Spark core which is over here is the most fundamental building block of Spark. So it is the backbone of the Spark's supreme functionality features. Spark core enables the in-memory computations that drive the parallel and distributed processing of data.

So all the features of Spark are built on top of Spark core. And it is responsible for managing tasks that is your IO operations, input output operations, your fault tolerance and the memory management etc. Now let us look at the different components that we have in the Spark out of which the first is your Spark SQL. Now this component mainly deals with structured data processing.

The key idea is to fetch more information about the structure of the data to perform additional optimization. Now it can be considered as a distributed SQL query engine. The next we have is the Spark streaming. Now this component deals with processing the real-time streaming data in the scalable and fault tolerance manner.

It uses micro-batching to read and process incoming streams of data. It creates macro-batches of streaming data, executes batch processing and passes it to some file storage or live dashboard. So Spark streaming can ingest the data from multiple sources like flume etc. The next in the source we have is Spark MLlib.

Now this component is used for building your machine learning models on big data in a distributed manner. The traditional techniques of big building ML models using Python's learning library faces a lot of challenges when data size is huge. Whereas MLlib is designed in a way that offers features engineering and machine learning at scale. MLlib has most of the algorithms implemented for classification, regression, clustering, recommendation systems and natural language processing.

The next we have is Spark Graphics or we also call it as Graph Frame. Now this component excels in graph analytics and graph parallel executions. Now graph frames can be used to understand an underlying relationship and visualize the insights from the data. Now coming to your installation of Spark, the first thing you require is you require Anaconda that is the Python, second you require is Java JDK.

If you have not installed then you need to install the JDK of Java. Then you require the Apache Spark and then you will require the WinUtils EXE. So you can download Anaconda installation from the official site of anaconda.com slash distribute and then download. You can download it and you can directly install it on your command prompt.

Now once that is done, you can install your Java version and then download the Spark installation or the Spark download from spark.apache.org slash downloads from where you will choose the exact package of Apache Spark that you require, download it and then you can install it. Now after that, once you have installed, you can go to the command prompt of Spark and from where you can execute all your commands of Spark. So now we would install PySpark and then we'll see the demonstration. That's it from this session.

Thank you very much.
