# Create and drop triggers in MySQL

- **Course:** Advanced Mysql
- **Module 1:** Functions and Triggers
- **Lecture #:** 8
- **URL:** https://www.coursera.org/learn/advanced-mysql-topics/lecture/uO75r/create-and-drop-triggers-in-mysql
- **Extracted:** 2026-06-22 20:00:49

---

At this stage of the lesson, you should be familiar with MySQL triggers and the different types of triggers available to database engineers. Now let's take a few moments to find out how you can create and drop these triggers into your databases. To help you understand these concepts, let's look at how they're used in Lucky Shrub. Lucky Shrub database contains an orders table, but several columns that record information on each order placed with the business.

Lucky Shrub want to make sure that no minus values are inserted in the table's quantity column when a new order is recorded, any minus values at the table encounters must be set to a default value of zero. They can complete this task using a before-insert trigger. The trigger is syntax begins with a create trigger command. This is then followed by the name of the trigger, which is order quantity check.

Always make sure that the trigger name is unique within the database. Next, assign the trigger type and specify when it must be invoked. In this instance, it's before insert. In other words, it's invoked before an insert command.

Then type the on keyword followed by the table name. This lets my MySQL know which table to target. You'll also need to type for each row so that MySQL targets each row within the table. Finally, write the trigger's main logic.

This must be a series of one or more SQL statements that execute when the trigger activates. If you have multiple statements, then encodes them within a begin-end block. The trigger's logic checks if a minus value is about to be inserted into the quantity column. This action requires an if statement so that it can access the quantity column.

To create this if statement, you need to use one of two modifiers, new and old. New suits our purposes here is it targets the value of a column after the operation. In other words, the value to be inserted. If you needed to access the column value before the operation, you'd use the old modifier.

Type of statement that says if the new order quantity value is less than zero, then set the new value to zero. Don't worry if you don't quite understand these modifiers, they're covered in more detail later in this lesson. Now, let's find out how to run our trigger. Before running this trigger, make sure you redefine the MySQL delimiter semicolon to a double forward slash, then execute the trigger.

Once executed, change the delimiter back to a semi-colon. Lucky Shrub now have the required trigger in their orders table. Lucky Shrub now need to delete this trigger from the table. You can delete or drop the trigger using the drop trigger statement.

Type dropped trigger, then type the if exists condition to prevent MySQL from returning an error. Next, provide both the schema name and the trigger name using dot notation. The schema name is optional but still recommended. It helps MySQL target the correct trigger and don't forget that if you drop the orders table then all related triggers are also deleted.

You've now helped to Lucky Shrub to create and drop the required trigger from their database and you should now be familiar with how to create and drop triggers from your own databases. Great work.
