# Problem Statement:
# You are working as a data analyst for a retail company. The management wants to understand the sales trends, regional performance, and product-level insights using interactive visualizations. You’ve been provided with a dataset sales_data.csv containing sales transactions.
# Your job is to analyze and visualize this dataset using Plotly Express.
# Task Sections
# 🔷 1. Line Chart: Revenue Over Time
# Goal: Visualize how total revenue changes over time.
# Steps:
# Use px.line() to plot Date vs TotalRevenue.
# Add a title and axis labels.
# Ensure the chart shows trends over days (you may sort the date column first).
# Bonus: Color the line based on region using color='Region'.
# 🔷 2. Bar Chart: Region-wise Revenue Comparison
# Goal: Compare total revenue across different regions.
# Steps:
# Group data by Region and calculate total revenue.
# Use px.bar() to create a vertical bar chart.
# Highlight highest performing region visually (color intensity or annotation).
# Add labels, title, and sort bars if needed.
# 🔷 3. Pie Chart: Product-wise Revenue Share
# Goal: Show each product's contribution to total revenue.
# Steps:
# Group by Product and compute total revenue.
# Use px.pie() to display revenue distribution.
# Add percentages and hover data.
# Customize color palette if desired.
# 🔷 4. Scatter Plot: Units Sold vs Revenue
# Goal: Understand if there's a relationship between units sold and total revenue.
# Steps:
# Use px.scatter() to plot UnitsSold vs TotalRevenue.
# Add product or region as a color dimension.
# Hover should display Product and Region.
# Submission Expectations:
# Create all 4 plots in Plotly Express
# Add appropriate titles, legends, axis labels
# Ensure visual clarity and accuracy
# Interpret: Which region/product had highest revenue?


import pandas as pd
import plotly.express as px

df = pd.read_csv('plotly_sales_data.csv')

df['Date'] = pd.to_datetime(df['Date'])

df.head()

# Line chart - Revenue over time
df_sorted = df.sort_values('Date') # Sort by Date

fig1 = px.line(
    df_sorted,
    x='Date',
    y='Profit',
    color='Region',  
    title='Total Revenue Over Time by Region',
    labels={'Date': 'Date', 'Profit': 'Total Revenue '}
)
fig1.show()

# 2. Bar Chart: Region-wise Revenue Comparison
region_revenue = df.groupby('Region')['Profit'].sum().reset_index()
region_revenue = region_revenue.sort_values(by='Profit', ascending=False)

# Plot
fig = px.bar(
    region_revenue,
    x='Region',
    y='Profit',
    color='Profit',
    color_continuous_scale='Greens',
    title='Total Revenue by Region',
    labels={'Profit': 'Total Revenue '}
)

fig.update_layout(coloraxis_showscale=False)
fig.show()

# 3.  Pie Chart: Product-wise Revenue Share
product_revenue = df.groupby('Product')['Profit'].sum().reset_index()

fig3 = px.pie(
    product_revenue,
    names='Product',
    values='Profit',
    title='Revenue Share by Product',
    hole=0.4,
    color_discrete_sequence=px.colors.sequential.RdBu,
)

fig3.update_traces(textinfo='percent+label', hovertemplate='%{label}: %{value:$,.2f}')
fig3.show()

# 4. Scatter plot
fig4 = px.scatter(
    df,
    x='Sales',
    y='Profit',
    color='Product',
    hover_data=['Product', 'Region'],
    title='Units Sold vs Total Revenue by Product',
    labels={'Sales': 'Units Sold', 'Profit': 'Total Revenue '}
)
fig4.show()
