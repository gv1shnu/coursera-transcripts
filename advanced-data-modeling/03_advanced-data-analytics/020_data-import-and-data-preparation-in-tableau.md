# Data import and data preparation in Tableau

- **Course:** Advanced Data Modeling
- **Module 3:** Advanced Data Analytics
- **Lecture #:** 20
- **URL:** https://www.coursera.org/learn/advanced-data-modeling/lecture/AAMTM/data-import-and-data-preparation-in-tableau
- **Extracted:** 2026-06-22 20:12:57

---

At this stage of the lesson, your next question might be, how do I use Tableau? In this video, you'll learn how to connect Tableau to your data sources, then clean and prepare your data for analysis. Global Superstore needs to use Tableau to analyze the records of a large Excel file, but they first need to clean and prepare the existing data. Let's help Global Superstore to connect their Excel data source to Tableau, then clean and prepare the data for analysis.

To perform data analysis in Tableau, you first need to establish a live connection to a data source. To establish a live connection, first open Tableau on the connection page. Under the Connect tab on the left-hand side, click "Microsoft Excel". This opens a dialog box that you can use to navigate to the Excel file on your machine.

Select and open the file. The Excel file name appears on the left-hand side of the screen. The data from the Excel file is displayed in the data pane. With a live connection, you can make sure that any updates to the original source are automatically reflected in your database.

However, it's faster to process a data extract, particularly when dealing with large amounts of data. On the left side of the data pane is the metadata grid. This shows relevant information about the different data fields. You can keep or hide the metadata grid by clicking the related button.

Now that you've connected to the data that you need, you can begin to clean it and prepare it for analysis. This process involves fixing errors in the data and shaping it so that it's easier to understand and analyze. You can do this by performing different types of operations like filtering, sorting, and renaming the data. You'll cover these operations in more detail in a later video.

The top of each column specifies the column's datatype along with a suitable symbol. You can change these datatypes as required. Let's take the Order Date column as an example. Select the small arrow next to the symbol above the column.

Click "Describe" on the list of options that appear. This action shows key information about this field of data. Click the "Abc" datatype and select the "Date" datatype. The datatype has now been changed.

You can also hide irrelevant table detail so that you can focus only on the necessary data. You can also change the number of rows displayed within the data pane. Let's hide the Order Date column. Select the small arrow again.

Then select "Hide". The column is now hidden. To show the data again, click the Tableau settings icon, then select the "Show Hidden Fields" option. This action displays faded versions of the fields to indicate what has been hidden.

To restore these fields, click the small arrow and select "Unhide". Your next task is to split the Customer Name column into two separate columns. One for each customer's full name and another for their last name. Click the small arrow and then select the "Split" option.

This automatically creates two new fields. You can rename them as required. Click the corresponding small arrow, select "Rename", and call the columns First name and Last name. Global Superstore also need you to create a new data field for their returns.

The field must include the final date by which each product can be returned under the company's returns policy. This is 15 days from the date of purchase. Select the small arrow in the Orders Date column, and click "Create a Calculated Field". Name this new field Return Date.

In the calculation editor, enter the following basic formula, Order Date plus 15. This formula adds 15 days to each order's order date value. This creates a new returns column populated with the relevant data. When finished, click "Okay".

The new calculated field is added to the data pane. Global Superstore's data has now been cleaned and prepared for analysis. You should now be familiar with how to connect to data sources in Tableau and clean and prepare your own data for data analysis. Great work.
