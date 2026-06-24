# Introduction to MySQL Workbench

- **Course:** Advanced Data Modeling
- **Module 1:** Data Modeling and Management
- **Lecture #:** 6
- **URL:** https://www.coursera.org/learn/advanced-data-modeling/lecture/EW69z/introduction-to-mysql-workbench
- **Extracted:** 2026-06-22 20:10:25

---

As a database engineer, you need to create, implement, and manage a database system that meets the specific requirements of your business or organization. These can be complicated tasks to carry out, but there are a range of tools and technologies you can use to support your work. One example of the tools that you will make use of is the MySQL Workbench tool. In this video, you'll explore the basics of the MySQL Workbench tool.

You'll also learn how the tool can be used to help model and manage your databases. Over at M&G, the company is developing a new MySQL database management system. The database system must follow some key requirements, particularly in relation to operating systems, data migration, and editing tools. M&G can build a database that meets these requirements using MySQL Workbench.

Take a few minutes to review the basics of MySQL Workbench, then see if you can help them out. Let's start with an overview of MySQL Workbench. MySQL Workbench is a unified visual tool developed by Oracle for database modeling and management. It contains several key features that are useful for creating, editing, and managing databases.

Let's review some of MySQL Workbench's key features. MySQL Workbench is open source and cross-platform. It can be used with multiple operating systems. It simplifies database design and maintenance, and it offers a visual SQL editor and other tools that support developers.

It provides autocomplete and highlighting features for writing SQL statements. It facilitates data migration between different versions of MySQL and between MySQL and other relational database systems. You'll make use of MySQL Workbench in this course to model and manage data in your MySQL database. But first you need to download, install, and set up MySQL Workbench on your operating system.

Download a copy of MySQL Workbench from dev.mysql.com/downloads. Make sure that you download the correct copy for your specific operating system. Once you've downloaded a copy, you then need to double-click the file to install it on your machine. Next, follow the installation wizard with the custom setup.

When you run the wizard makes sure that you install the following software. MySQL Server, MySQL Workbench, and MySQL Shell. If you encounter any difficulties, read the MySQL Workbench installation file for guidance. Next, let's open the MySQL Workbench and find out more about how you can use it to establish connections.

Once you've downloaded a copy of MySQL Workbench, you need to set it up, launch the program and view the MySQL Workbench home screen. The home screen contains a welcome message, links to documentation, blogs and discussion forums, and provides access to various tools and features. You can use the home screen side panel to access MySQL connections models and MySQL Workbench migration wizard. Select the connections option to view a list of connections to local and remote instances of MySQL.

You can use connections to load, configure, group, and view information about each of your MySQL connections. Models displays the most recently used models. Each entry list the date and time the model was last opened. Along with its associated database.

You can also select the plus sign to add a new model. Select the folder button to browse and open saved models, and select the more button to access additional commands. You can also open the migration tab to display an overview of prerequisites for using the wizard. Start a migration process.

Open the ODBC administrator or view documentation. Let's look at the process steps for creating a new user. Creating a new user is the most secure way to connect to your MySQL database because you can manage user roles and privileges. Make sure MySQL Connection is selected.

First, login to the MySQL Server using the root user. Enter the root user password you set when installing MySQL. Save the password for future reference if required. Next, select users and privileges under the management menu to view a list of current database users.

Select add account to add a new user. This opens a new window in which you can enter the new user details. Name the new user, admin 1, enter a password, confirm the password. You can also use this window to control user privileges.

Let's review these privileges. Account limits is used to limit a user's maximum number of queries, updates, and connections. The administrative roles tab lets you assign a role to a new user or assign them associate privileges. In this case, select DBA that grants the right to perform all tasks.

Schema privileges lets you control new user access privileges. Select the apply button to create the new user. The next task is to create a new MySQL connection. From the MySQL Workbench home screen select the plus icon to open the setup new connection form.

Fill in the form to create a new server instance. You can now use the following values. Use test server as the server instance name. In the username text field type admin 1.

You can use the default settings for all other parts of the form. Finally, make sure your host name is 127.0.0.1 and the port number is 3306. Click the test connection button to check that the settings work is required. Enter the password you set for admin 1 user.

If you set it up correctly then MySQL Workbench should confirm that the connection was successful. If not returned to the form and check that you've entered the information correctly. Select okay, to save the connection. Your new MySQL Connection is added to the home screen.

You can now use this connection to begin working with database schemas and SQL queries. You should now be familiar with the basic features of the MySQL Workbench tool and know how to use it to help model and manage your databases. You're well on your way to understanding advanced data modeling.
