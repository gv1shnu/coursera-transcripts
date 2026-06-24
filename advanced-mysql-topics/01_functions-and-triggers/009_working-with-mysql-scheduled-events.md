# Working with MySQL Scheduled Events

- **Course:** Advanced Mysql
- **Module 1:** Functions and Triggers
- **Lecture #:** 9
- **URL:** https://www.coursera.org/learn/advanced-mysql-topics/lecture/rzJiv/working-with-mysql-scheduled-events
- **Extracted:** 2026-06-22 20:01:01

---

When working with MySQL databases will often be tasks or events that must be completed at specific times like inserting data or generating reports. With MySQL scheduled events you can make sure that these events occur at the scheduled time even if you're not present. In this video, you'll learn what of MySQL event is. Review the syntax used to create events and explore some examples.

Lucky shrub often make use of MySQL scheduled events. For example, the Finance Department has just requested a report on all orders received this month. However, this report must be generated at 11:59 P.M. On the last day of the month.

Lucky Shrub can use a one time event to create this report. They can schedule their MySQL database to generate the report at the specified time and date. Before you find out how Lucky Shrub can create this event. Let's first find out more about what a MySQL scheduled event is.

A scheduled event in MySQL is a task executed according to a given schedule. In other words, it's an event that takes place at a specified time. Each event has a unique name and contains one or more SQL statements. They're stored in the database and can be executed just once or they can be a recurring event.

The main types of scheduled events that you'll work with in MySQL include one time events and recurring events. One time events are scheduled events that occur just once, for example, inserting data into a table one hour from now. And a recurring event is a scheduled event that occurs on a regular basis, like generating a weekly report from a database. So how do you create a MySQL scheduled event, events are created in MySQL using the create event keywords.

Let's find out more about how this syntax works. First create the event using the create event keywords. You can follow these keywords with if not exists, this tells MySQL to create the event only if it doesn't already exist. Then follow these keywords with a unique event name, next, type on schedule keywords and specify a scheduled time at which the event must occur then type the do keyword.

This keyword is followed by the event body in which you specify the logic of the event using SQL statements. So how can you use this syntax to differentiate between one time and recurring events. If you're scheduled event is a one time event, then specify the schedule using the at clause. This is followed by a time stamp, an interval keyword and a specific time at which the event must be executed.

For example, Lucky Shrub can use this syntax to generate a one off revenue report 12 hours from now. And they can create their event logic within a begin end clause, creating a recurring event is more complicated. The syntax is largely the same. The key difference is that you must use the every clause instead of at followed by an interval.

You can also use the starts and ends keywords with the time stamps and intervals to designate specific start and end points for the event. Lucky Shrub can use the recurring events in tax to create a daily stock check event. If the event identifies that some stock levels are too low. It sends out an order to restock those items.

You'll find out more about how Lucky Shrub can create this and the previous event in just a moment. Before then let's look at how to delete or remove an existing, MySQL event that's no longer needed using a drop event statement. First type the drop event keywords. It's also good practice to include if exists.

This tells MySQL to check if the event still exists and hasn't already been dropped from the database. Finally type the events name and then execute the statement. Now that you're familiar with scheduled events and their syntax. Let's see if you can help Lucky Shrub generate that report.

As you saw earlier Lucky Shrubs Finance Department has just requested a report on all orders received this month. They need the report generated at 11:59 P.M on the last day of the month. However, it's now the last day of the month and it's also approaching 12 noon. So they need the report 12 hours from now.

This is a one off event. So begin with the create event keywords, then assign the event a unique name. Let's use GenerateRevenueReport. Now you need to specify the schedule since this is a one time event use the at clause, then schedule the event to occur 12 hours from now.

So include the current time stamp and add a 12 hour interval. The next step is to add the schedules logic. Type the do keyword and begin and end block within this block instruct MySQL to select all data inserted into the orders table this month and to place that data within a report data table. Great, 12 hours from now, the Finance Department will have their report.

Lucky shrub need your help with another task. They're reviewing their stock and need to make sure that they have at least 50 units available for each item on sale. You can help them by using a recurring event. First create the event and call it daily restock.

Then specify the schedule as this is a recurring event use the every clause and schedule it to occur once a day. Next add the do keyword followed by a begin and end block, within this block to find the events logic. MySQL must check if the number of items for any record in the products table is below 50. If MySQL locates a record below 50, then the number of items must be updated.

If at any stage you need to remove this event, just type the drop event keywords then if exists followed by the event name. Great work, you've helped Lucky Shrug to create these events in their database. You should now be familiar with the basics of MySQL scheduled events include different types of events and their syntax well done.
