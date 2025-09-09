import plotly.express as px 
import pandas as pd 
import seaborn as sns 

tips = sns.load_dataset('tips')
print(tips.head())

# 1. Scatter
fig_scatter = px.scatter(
    tips,
    x='total_bill',
    y='tip',
    color='sex',
    title='Scatter plot: total bill vs tip'
)
fig_scatter.show()

# 2. Bar graph
avg_tips = tips.groupby('day')['tip'].mean().reset_index()
fig_bar = px.bar(
    avg_tips,
    x='day',
    y='tip',
    title='Bar graph: Average tip per day',
    text_auto = True
)
fig_bar.show()

# 3. Pie chart
gender_tip = tips.groupby('sex')['tip'].sum().reset_index()
fig_pie = px.pie(
    gender_tip,
    names='sex',
    values='tip',
    title='Bar graph: Average tip per day',
)
fig_pie.show()

# 4. Line chart
tips['cumulative_tip'] = tips['tip'].cumsum()
tips['index'] = tips.index
fig_line = px.line(
    tips,
    x='index',
    y='cumulative_tip',
    title='Line chart: cumulative tip over the time',
)
fig_line.show()

# 5. Histogram
fig_hist = px.histogram(
    tips,
    x='total_bill',
    nbins=10,
    title='Histogram: dist of total bills',
    color_discrete_sequence=['skyblue']
)
fig_hist.show()


# 6. Box plot
fig_box = px.box(
    tips,
    x='sex',
    y='tip',
    title='Box plot: tip distribution by gender',
    color='sex'
)
fig_box.show()