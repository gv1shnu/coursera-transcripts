# Data filtering and visualization in Tableau

- **Course:** Advanced Data Modeling
- **Module 3:** Advanced Data Analytics
- **Lecture #:** 21
- **URL:** https://www.coursera.org/learn/advanced-data-modeling/lecture/X7DoV/data-filtering-and-visualization-in-tableau
- **Extracted:** 2026-06-22 20:13:08

---

Once you've imported your data into Tableau, you then need to prepare it for analysis. However, the process is more efficient if you focus only on the data you need to analyze. With Tableau, you can focus on relevant data using the software's filtering and visualization features. In this video, you'll learn how to filter data and create a data analysis chart in Tableau.

Over a global superstore, they're preparing to launch a new marketing campaign in Canada. But first, they need to analyze their sales data to optimize their campaign. They can use data filtering techniques to arrange and exclude data so that their records are focused only on Canada. This provides a more relevant, reliable, and accurate level of information.

You can help global superstore to complete this task by using Tableau. In Tableau, you can filter data in either the data source page or the worksheet. However, filtering data directly in the data source page limits your data analysis and all worksheets to the filtered criteria only. For example, if global superstore filter their categories to include only office furniture, then they can't perform data analytics and other categories in the worksheet.

Let's begin by applying data filtering in the data source page. Click the "Add" option under filters. This opens a dialog box that lists all filtered fields in the data source. Click "Add" again to add a new filter field.

Next, select Region and click "Okay". Click the select from list option in the general tab area. Check Canada, then click "Okay". The data pane now shows filtered records from Canada only.

You can repeat this process to add more data source filters if required. To remove a filter, click, "Edit Filter", select Canada, then Remove and Okay. You can also filter data in the worksheet. Open the sheet tab at the bottom of the page.

In the worksheet, the columns from your data source are displayed as fields on the left side of the data pane. The data pane contains a variety of fields. The fields above the gray line are dimension fields. The fields below the gray line are measure fields.

Dimension fields hold categorical data. In the case of global superstore, this includes product categories, types, and dates. Measure fields hold numeric data like sales, profit, and quantity. Global superstore want to compare sales of all category products sold in Canada.

To help them with this task, drag the category field from the dimension section of the data pane to the rows and the shelf area. Then drag the Sales field from the measures section in the data pane into the columns and the shelf area. The horizontal bar chart that appears shows information about different product categories. You need to filter this data to show only products sold within Canada.

Drag the region dimension from the data pane to the filter card. This opens a pop-up window. In the general tab, select Canada, then click "Apply", and "Okay". Your data is now filtered to show sales and Canada only.

You can also take further steps to make your chart easier to read and understand. Click the swap icon to change the horizontal bar to a vertical chart. Click the descending order icon to filter data from maximum sales to minimum sales. Drag Sales to the color part in the marks section of the screen to change the bar colors based on sales.

Drag profits from the data panes measure section to the label mark. This shows the profit of each category in the chart. You can also provide a title for the sheet. In this instance, you can call the sheet sales in Canada.

A lot of the information in the chart is generic. It might be better to add the sub category to the view to provide more detail around the sales and profits. Drag the subcategory field from the dimension section of the data pane to the columns in the shelf area. Then click on the descending order icon to filter data from the maximum to the minimum values.

You can now view all categories and subcategories. You can even focus on one category like furniture. Drag the category dimension from the left data pane to the filter card. Then use the filter categorical data option to retain the furniture category while unchecking the technology and office supply categories.

Click "Apply" then "Okay". You can also filter categories according to best selling items. Drag the subcategory to the filter card. Then select the top tab, tick by field, and enter a numerical value of two to view the top two categories, then click "Apply".

The wildcard can also be used to filter data based on specific patterns. For example, you can type chair in the text field to include subcategories that contain this text value. In this instance, the data returns the chair subcategory. Another filtering technique is conditioned filtering.

You can use condition filtering to select a field of data and defined specific rules to be applied. For example, you can select the Sales field, then specify a sum value greater than 500,000. Click "Apply" and then "Okay". This returns all values within your data greater than 500,000.

To remove all subcategory filters, just right-click the subcategory and click "Remove". You can also remove the category and keep the region to focus on Canada. You can now view all sales data related to the furniture category and sub categories and Canada. Global Superstore has now filtered the required data for data analysis using Tableau.

You should now also be able to apply different filtering techniques to your data using Tableau. You're making great progress on your data analytics journey.
