# What are MySQL triggers?

- **Course:** Advanced Mysql
- **Module 1:** Functions and Triggers
- **Lecture #:** 6
- **URL:** https://www.coursera.org/learn/advanced-mysql-topics/lecture/U8zM2/what-are-mysql-triggers
- **Extracted:** 2026-06-22 20:00:27

---

As a database engineer you'll often need certain actions to occur automatically when specific events take place, like when data is inserted, updated or deleted from a table. But how can you make sure that these actions happen automatically and avoid the need to rewrite code each time they must be invoked, you can do this with the use of MySQL triggers. In this video you'll learn what are MySQL trigger is and how to code and use them. Lucky Shrubs sales team are adding discounts to products however, any discounts over 25% must be reviewed by a manager.

This means that the sales team needs to add a trigger to the database that flags items when they're assigned a discount above the 25% threshold. Let's explore MySQL triggers and find out how Lucky Shrub can use them to complete this task. The first question to answer is what's a MySQL trigger? A MySQL trigger is a set of actions available in the form of a stored program.

These set of actions are invoked automatically when certain events occur. Examples of these events include inserting updating and deleting data from a table in a MySQL database. However, before you can use a trigger, you need to create it and you'll also often need to drop or delete a trigger once it served its purpose. Let's take a moment to explore the syntax for creating and dropping triggers.

A trigger is created using the create trigger statement. To create the trigger type that create trigger statement followed by the name of your trigger because the trigger is often user defined you can create a custom name. However, make sure that each triggers name is unique within the database then define a trigger type. For example, is it an insert, update or delete trigger and should it execute before or after?

Don't worry about this for now you'll explore trigger types in a later video. Next specify which table the trigger must be assigned to and identify how it should be applied to the table. Next you need to define the triggers logic. In other words, specify what it is that the trigger must achieve.

The trigger can insert, update or delete data, it can even combine these actions as required. If it requires multiple statements then these must be enclosed within a begin end block then execute the statement to create the trigger. Again, this part of the syntax isn't a concern at this stage in the lesson you'll review different types of triggers and what they can achieve in a later video. To drop or delete a trigger that you've created you can use the drop trigger command, to use this command just right drop trigger, then add that if exists clause.

This clause makes sure that the drop command only works If MySQL can locate the trigger within the database. If you try to drop a non existent trigger without this clause then MySQL returns an error. Next identify the schema that the trigger belongs to using dot notation to identify both the schema and trigger names. This makes sure that MySQL only deletes the trigger from the specified schema and not the entire database.

Finally type the name of your trigger, then execute the statement to drop the trigger. It's also important to remember that if you drop or delete a table from your database, then MySQL automatically removes all triggers associated with that table. So how can Lucky Shrub sales team make use of these methods As you learned earlier. The team need to add a trigger to their database that flags when employees attempt to add a discount of more than 25% to an item.

An approval request must then be sent to a manager for any flagged items. Lucky Shrub can use create trigger commands to create this trigger. They can name the trigger approval request, they then assign a trigger type of after update so that the trigger executes the logic after an update operation has occurred within the table. Finally, they place the trigger logic within a begin end block.

Finally, let's look at a few more benefits of triggers, triggers are useful for keeping a log of records or changes made within a database. It's basically a way of maintaining audit trails where a record is inserted into the database each time a change is made, triggers are also an alternative to constraints. They can be a useful way to help maintain data integrity by making sure all data is updated as required. They're also useful for performing tasks automatically on specified actions on a database table.

You should now know what a MySQL trigger is and understand the basics of how to create and drop them within a database.
