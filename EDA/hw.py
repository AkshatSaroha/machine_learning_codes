import plotly.express as px
import pandas as pd

df = px.data.tips()

print(df.head())

# Histogram
fig = px.histogram(df, x='total_bill', nbins=30, title='Distribution of Total Bill')
fig.show()

# Box plot - by sex
fig = px.box(df, x='sex', y='tip', color='sex', title='Tip Amount by Gender')
fig.show()

# Box plot - by day
fig = px.box(df, x='day', y='tip', color='day', title='Tip Amount by Day')
fig.show()

# Bar Plot – Total tip amounts by day of the week
tip_by_day = df.groupby('day')['tip'].sum().reset_index()
fig = px.bar(tip_by_day, x='day', y='tip', title='Total Tip Amount by Day', color='day')
fig.show()

# Scatter Plot – total_bill vs. tip
fig = px.scatter(df, x='total_bill', y='tip', color='sex', title='Total Bill vs Tip by Gender',
                size='size', hover_data=['day', 'time']
                )
fig.show()

# Pie Chart – Smokers vs Non-Smokers
smoker_counts = df['smoker'].value_counts().reset_index()
smoker_counts.columns = ['smoker_status', 'count']

fig = px.pie(smoker_counts, names='smoker_status', values='count',
             title='Smokers vs Non-Smokers')
fig.show()
