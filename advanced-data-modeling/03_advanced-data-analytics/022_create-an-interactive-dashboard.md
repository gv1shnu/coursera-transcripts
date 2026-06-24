# Create an interactive dashboard

- **Course:** Advanced Data Modeling
- **Module 3:** Advanced Data Analytics
- **Lecture #:** 22
- **URL:** https://www.coursera.org/learn/advanced-data-modeling/lecture/ntLKz/create-an-interactive-dashboard
- **Extracted:** 2026-06-22 20:13:19

---

Once you've analyzed your data in Tableau, you then need to determine the most informative way to present it to your audience. With Tableau, you can present data visually in the form of an interactive dashboard. Over the next few minutes you'll learn how to create a basic dashboard with multiple views and interactivity. At Global Superstore, they want to create an interactive dashboard that shows profits and sales by country and indicates how profits are trending over time.

They can then use this dashboard to compare sales and profits in each country. Help Global Superstore to complete this task by creating worksheets in Tableau as follows, one worksheet to show sales and profits in each country, and another worksheet that shows trending profits. You then need to combine these worksheets in one dashboard, where they can interact with one another based on the needs of the user. This tutorial assumes that you're already connected to the data source, and that all necessary data has been cleaned and prepared for analysis.

Let's begin with the map-chart. Click the sheet-tab and change the default title to profit and sales map by country. Double click country in the data pane. The map view is automatically created because the country field is a geographic field.

Drag the profits field from the data pane to the color on the marks card. Change the color so that it's easier to identify this data. Next, drag the sales field from the data pane to the tool tip on the marks card. Select maps, then background maps.

In the background pane, click the normal option. Roll over each country using your mouse to display the name, profits and sales data. Your next task is to create another view that shows the Global Superstore profit trends over time. Create a new worksheet and change the title and sheet name to profits trends.

Drag the order date field from the data pane to the column shelf. Make sure that the order date has been assigned a data type. Drag the profit fields from the data pane to the rows in the shelf section. Tableau automatically generates a trending chart for profit.

You can change the trend lines color set by dragging the profit to the color mark. Select a new color set to differentiate it from other data, then drag the profits field from the data pane to the label mark. This shows the profits made each year. You've created two worksheets that communicate important information.

You now need to combine the two sheets within one dashboard to show how profits are trending within each country. The first step is to set up your dashboard, click the dashboard tab, then the new dashboard option. You can also use the dashboard icon at the bottom of the page. Call your new dashboard profits dashboard.

To the side of the dashboard pane, you can access the sheets you've already created. Drag the map chart to the empty view within the dashboard, and drag the profits chart below the map chart. The dashboard now has two related charts. Global Superstore can use it to compare profit and sales by country.

However, it would also be useful to add some interactivity to this chart. For example, you can add interactivity to view profit trends by clicking on each country. Select the map from the dashboard, then click the use as filter icon. Select a country within the map, like Argentina.

This shows the sales and profits in the map-chart, and it also shows the trend and profits within the selected country. You can repeat these actions for each country. Thanks to your work sheets, Global Superstore can now compare their sales by country, and you should now be able to create a basic interactive dashboard with multiple views and interactivity. You're making great progress.
