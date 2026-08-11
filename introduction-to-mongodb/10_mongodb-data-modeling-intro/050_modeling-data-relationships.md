# Modeling Data Relationships

- **Course:** Introduction To Mongodb
- **Module 10:** MongoDB Data Modeling Intro
- **Lecture #:** 50
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/0EScA/modeling-data-relationships
- **Extracted:** 2026-08-11 10:00:37

---

Hello. In this video, we'll go through a detailed example of how data might be modeled. As a quick recap, there are one-to-one, one-to-many, and many-to-many relationships, and there are two ways to model relationships ; embedding and referencing. With this in mind, let's go through an example of data modeling by using the student record shown here.

When a student's start school, they fill out a form and our web application that creates their profile, which then goes in our database. Looking at this data, we can imagine collecting more pieces of information about the student, such as classes, grades, and so on. Notice that the student has multiple contact phone numbers, a home phone, a cell phone, and emergency contact number. This is messy, so we want to reorganize it.

Right now, each contact phone number is entered as a separate item, which illustrates a one-to-one relationship, but we can also represent the student and his contact phone numbers as a one-to-many relationship by writing the phone numbers and an array like this, but when we model the data this way, we lose some contexts, for example, now we don't know that one of those numbers is an emergency contact number. It would probably be preferable for our model to have more information. In the array, we add the type after the number to specify whether it's the home number, cell phone number, or emergency contact number. If we have a much larger amount of data on the student that we want to store, such as the classes they've taken, we might want to model the data a bit differently.

In this case, we can reference another collection or document. Here we are adding references for the course ID and course name inside the student's document. When we look at this other collection for the courses, we see documents that look like this. Well done.

Here are some key takeaways from this video on data modeling. We can represent relationships in many ways by inserting data into the document, embedding it, or linking it with a reference. The example in this video demonstrates a one-to-many relationship with both embedded and linked examples. Great work everyone.

Now you have an understanding of how flexible MongoDB documents are. You can continue to expand your knowledge by learning more about embedding and referencing in a data model.


<details><summary>Timestamped transcript</summary>

```
Hello. In this video, we'll go through a detailed example of how data might be modeled. As a quick recap, there are one-to-one, one-to-many, and many-to-many relationships, and there are two ways to model relationships ; embedding and referencing. With this in mind, let's go through an example of data modeling by using the student record shown here. When a student's start school, they fill out a form and our web application that creates their profile, which then goes in our database. Looking at this data, we can imagine collecting more pieces of information about the student, such as classes, grades, and so on. Notice that the student has multiple contact phone numbers, a home phone, a cell phone, and emergency contact number.
This is messy, so we want to reorganize it. Right now, each contact phone number is entered as a separate item, which illustrates a one-to-one relationship, but we can also represent the student and his contact phone numbers as a one-to-many relationship by writing the phone numbers and an array like this, but when we model the data this way, we lose some contexts, for example, now we don't know that one of those numbers is an emergency contact number. It would probably be preferable for our model to have more information. In the array, we add the type after the number to specify whether it's the home number, cell phone number, or emergency contact number. If we have a much larger amount of data on the student that we want to store, such as the classes they've taken, we might want to model the data a bit differently. In this case, we can reference another collection or document. Here we are adding references for the course ID and course name inside the student's document.
When we look at this other collection for the courses, we see documents that look like this. Well done. Here are some key takeaways from this video on data modeling. We can represent relationships in many ways by inserting data into the document, embedding it, or linking it with a reference. The example in this video demonstrates a one-to-many relationship with both embedded and linked examples. Great work everyone. Now you have an understanding of how flexible MongoDB documents are.
You can continue to expand your knowledge by learning more about embedding and referencing in a data model.
```

</details>
