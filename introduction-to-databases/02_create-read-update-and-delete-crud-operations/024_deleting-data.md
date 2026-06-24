# Deleting data

- **Course:** Introduction To Databases
- **Module 2:** Create, Read, Update and Delete (CRUD) Operations
- **Lecture #:** 24
- **URL:** https://www.coursera.org/learn/introduction-to-databases/lecture/7BLRk/deleting-data
- **Extracted:** 2026-06-22 16:14:49

---

In this example, I'll demonstrate how to delete a single record from a table in a database. I'm using the student table from a college database and deleting the record of a student with the last name of Miller. I go to the SQL tab in phpMyAdmin. I write a delete statement beginning with the keyword delete from.

Then I specify the table name as student table. I add a where clause and the condition to delete the data I want. I need a database to scan the list of students and identify the last name or value of Miller, and then delete that record from the table. I type where followed by last name equal to Miller.

I then run this statement by pressing the go button. I get a confirmation that the record Miller has been deleted from the database. I can then access the student table on the left panel to ensure that the record or instance of Miller has been removed. Let's explore another example this time by deleting multiple records from the student table.

Now I want to delete the records for the two students within the engineering department. The beginning of the statement is the same as the previous example. I begin with the delete and form keywords followed by the name of the table I'm working with, which is student table. The where clause is the key difference in this example.

I type where followed by department equal. To engineering. This instructs SQL to identify all records that have a value of engineering within the department column and remove those rows from the table. But I need to be careful.

If I don't correctly specify the where clause, then all the records in the table will be deleted. Now that I've completed my statement, I select Go to run it. I then check the table by clicking it on the left panel and confirm that the records for the two engineering students have been deleted from the table. Finally, let's quickly explore how to delete all records from a table.

In this task, the syntax remains largely the same as in the previous examples. The key difference is that I removed the where clause so that now by syntax, just state, delete from student table. I remove the where clause. That now my syntax just states delete from student table.

In other words, I'm instructing the database to remove all records from the student table. Then I click Go and confirm the deletion. Once the deletion has been confirmed, I check the student table, which is now empty. I now know that all records have been deleted.
