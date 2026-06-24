# Types of MySQL triggers

- **Course:** Advanced Mysql
- **Module 1:** Functions and Triggers
- **Lecture #:** 7
- **URL:** https://www.coursera.org/learn/advanced-mysql-topics/lecture/vPLWO/types-of-mysql-triggers
- **Extracted:** 2026-06-22 20:00:37

---

as you might know by now. A MySQL trigger is a set of actions that can be invoked automatically when certain events occur. But how do you determine when and how these triggers are executed? Well, you can control the behavior of your triggers by using different types over the next few minutes.

You'll explore the different types of triggers available and learn when to use them. Lucky Shrub are rebuilding their orders table which records orders within their database. They need to assign a new set of constraints or rules on this table. Maybe they can create these rules using triggers.

Let's find out which types of triggers Lucky Shrub can make use of and in what order these triggers should occur. Let's explore the two main types of triggers to find in SQL row level triggers and statement level triggers. A row level. SQL trigger is invoked for every row inserted, updated or deleted in a table.

So if 100 rows are added to a table, then the role level trigger is invoked 100 times a statement level trigger on the other hand is invoked once for each action and it occurs just once, no matter how many rows are inserted, updated or deleted. So a single insert statement could add 100 rows to a table but it only activates once for all 100 rows. It's important to be aware of both types of triggers. However, MySQL only supports row level triggers so they'll be the focus of this lesson.

As you learned earlier triggers are typically used to perform three types of actions, insert data into a table, update data in a table and delete data from a table. But how can you determine when an insert update or delete trigger occurs? Well depending on when a trigger is action, it can be classified as either before or after trigger. Let's find out what this means.

The before key word or modifier indicates that the trigger must be invoked before any action is performed on a table robe while after, indicates that the trigger is invoked after the action is performed on each row. By combining these modifiers with the insert update and delete key words. You can create different types of triggers. For example, the before insert trigger is automatically invoked before an insert event occurs on a table while after insert is invoked after an insert event.

Similarly, a before update trigger is invoked before an update event occurs and an after update trigger is invoked after the event. Finally, before delete triggers are invoked before data is deleted in a table and after delete triggers are invoked after data is deleted. In each instance, the syntax is largely the same for each type of trigger. Begin with a create trigger command followed by the name of your trigger.

Next add the modifier and keyword to determine when your trigger must occur and on what action it must take place. For example, before insert instructs MySQL to invoke the trigger before an insert event occurs on the table, then type the on keyword and the name of the table. This is followed by the for each row keyword. This instructs MySQL to carry out the action for each row in the table finally type the logic of the trigger as you might recall.

This is usually typed within a begin end block, particularly if you need to specify multiple statements. Let's look to Lucky Shrub for an example, they want to impose a new constraint on their orders table. This new rule must state that no minus values can be inserted in the table's, order quantity field. So Lucky shrub can begin with the create trigger command.

They can then name the trigger order, quantity check next they add the modifier and keyword before insert. Then they assigned the trigger to the orders tab and make sure it applies to each row. Finally they create the trigger logic. Within begin and end statements.

The logic states that if the table encounters an order with a value of less than zero, then it must set the value to zero by default. Now each time a new row is inserted into the table. The before insert trigger carries out the required action before it inserts a new value. Let's take a moment to explore some more types of triggers that Lucky shrub can use Lucky shrub want to maintain an audit trail of all updates made to their orders.

Table with an after insert trigger they can send a log message from the orders table to the audits table each time a new order is inserted. The company also needs to create a log that captures the date and time and order record is deleted from the orders table. They can use an after delete trigger for this task. After record is deleted.

The trigger inserts a record in the log with the date and time. These are just a few examples of how the different types of triggers work in mySQL. You'll explore them all in more detail later in this course. But for now you should be familiar with the different types of triggers available and know how to create them.

Good work.
