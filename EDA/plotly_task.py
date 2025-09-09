import plotly.express as px 
import pandas as pd 

df = pd.read_csv('ecommerce_sales.csv')

# df['Date'] = pd.to_datetime(df['Date'])

# 1. Bar Chart: Total Sales by Region
# bar_data = df.groupby('Region')['Sales'].sum().reset_index()
# bar_fig = px.bar(
#     bar_data, 
#     x='Region', 
#     y='Sales', 
#     title='Total Sales by Region')
# bar_fig.show()

# 2. Pie Chart: Sales Share by Category
# pie_data = df.groupby('Category')['Sales'].sum().reset_index()
# pie_fig = px.pie(
#     pie_data, 
#     names='Category', 
#     values='Sales', 
#     title='Sales Share by Category'
# )
# pie_fig.show()

# 3. Line Chart: Sales Trend Over Time
df['Sales'] = df['Sales'].cumsum()
df['Date'] = pd.to_datetime(df['Date'])
line_fig = px.line(
    df, 
    x='Date', 
    y='Sales', 
    title='Sales Trend Over Time'
)
line_fig.show()

# 4. Scatter Plot: Quantity vs Sales
# scatter_fig = px.scatter(
#     df,
#     x='Quantity',
#     y='Sales', 
#     color='Category', 
#     title='Quantity vs Sales'
# )
# scatter_fig.show()