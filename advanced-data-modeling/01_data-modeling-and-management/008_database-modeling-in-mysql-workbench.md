# Database modeling in MySQL Workbench

- **Course:** Advanced Data Modeling
- **Module 1:** Data Modeling and Management
- **Lecture #:** 8
- **URL:** https://www.coursera.org/learn/advanced-data-modeling/lecture/bIYwL/database-modeling-in-mysql-workbench
- **Extracted:** 2026-06-22 20:10:47

---

At this stage of the course, you understand the importance of database models, but how do you create these models? You can create database models using professional data modeling tools such as MySQL Workbench. In this video, you'll learn how to use MySQL Workbench and make use of the forward and reverse engineer features. MNG need to develop a basic database to maintain information about their customers and orders.

They can use MySQL Workbench to create a model. Then they can use MySQL Workbench forward engineer feature to transform the data model into a SQL schema and implement it automatically into MySQL. Let's help MNG create their database using MySQL Workbench. In the MySQL Workbench home screen, click the "model's view" from the left sidebar, then click the plus icon next to the models to display a new window.

This action creates a new schema called mydb. Double-click the schema name and change it to mangata_gallo. The next step is to create the data model diagram. This diagram is essential for using the forward engineer feature.

You can create the data model in MySQL Workbench and then transform it into a SQL schema that can be implemented automatically in MySQL. First, double-click "Add Diagram" to create the ER diagram. This action opens the ER diagram designer page. Now, you need to create the tables.

Click the "Add Table" icon and then click a square within the view. This action creates a table entity. Double-click the entity to load the table editor. Change the default table one name to customers.

Now, you need to add columns to the customers' table. Double-click a cell. This creates a default ID customers column. Change its name to customer ID.

Keep the datatype as integer. Check the primary key, not null, and auto-increment boxes. Then add three more columns, full name, contact number, and e-mail. Set the datatypes as required and mark all three columns as not null.

Follow the same steps to create the orders table and set the datatypes as required. You also need to create the orders table foreign key. Define the table's customer ID column as the foreign key using the foreign keys tab at the bottom of the window. Type customer_id_fk in the foreign key text field.

Double-click the corresponding field in the reference table. Then select the customer's table, check the customer ID referenced column, then mark it as on update cascade and on delete cascade. You now have a visual representation of the MNG schema ER diagram with the customers and orders tables. Save your work by clicking "File Save As" and name it mangata_ gallo_model.

Now that you've created the data model, you can synchronize it to the MySQL server using the forward engineer feature. Select the database tab, then the forward engineer option from the menu. This opens the forward engineer to database wizard. Select the connection that you created earlier to connect to the MySQL server.

Leave the default setting as is. Click "Next." The wizard lists some advanced options. You can ignore these for now. Just click "Next." A new window appears called select objects to forward engineer with a series of options.

Check the export MySQL table objects box, then click "Next." The next step displays the SQL script to be executed on the MySQL server to create the internal schema. Review the script to ensure that it creates the schema as required. Click "Next" to forward engineer the SQL script. A message appears stating forward engineer finished successfully.

Click "Close" to close the wizard. The MNG database has now been created in MySQL. You can confirm this by examining the schema list in the navigator section or executing a show databases statement inside the Workbench SQL editor. MNG also need to use MySQL Workbench to reverse engineer a data model.

This means building a data model ER diagram from an existing database. The first step is to go to the database tab, then select the reverse engineer option. Once you're happy with the connection details click "Next." Each connection must be configured appropriately to connect with MySQL server. If you're not happy with the existing connection, you can choose another one and click "Next." A message appears stating execution completed successfully.

Click "Next." A list of available schemas on the server is displayed. Select the database schema you want to reverse engineer then click "Next." A message appears onscreen stating "Retrieval completed successfully." Click "Next." A new screen appears in which you are presented with the option to select all objects. The screen confirms that all objects have been retrieved. Click "Execute." Once the retrieval process has been successfully executed, a message is displayed which states "operation completed successfully." The selected objects have now been reversed engineered successfully.

Click "Next" again. A final screen is displayed, which shows a summary of the import. Click "Finish" to complete the process. MySQL Workbench creates the new ER diagram from the internal MySQL schema.

You can print the data model as a PNG image, share it with others, or apply changes and push it to the database using the forward engineer feature. MNG have now developed a basic schema in their database using MySQL Workbench and you should now know how to make use of the reverse engineer feature in MySQL Workbench to develop a data model diagram. Well done.
