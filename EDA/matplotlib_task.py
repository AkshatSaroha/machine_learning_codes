import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('matplotlib_sales_data.csv')

df['Date'] = pd.to_datetime(df['Date'])

# Bar
sales_by_region = df.groupby('Region')['TotalSales'].sum()
sales_by_region.plot(kind='bar', title="Total Sales by region", color='blue')
plt.xlabel('Region')
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# Pie
category_sales = df.groupby('Region')['TotalSales'].sum()
category_sales.plot(kind='pie', startangle=90)
plt.title('Sales distribution by Product')
plt.tight_layout()
plt.show()

# Line
sales_by_region = df.groupby('Date')['TotalSales'].sum()
sales_by_region.plot(kind='line', title="Total Sales Over Time", color='blue')
plt.xlabel('Date')
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# Histogram
plt.hist(df['Region'], bins=10, color="lightgreen", edgecolor='blue')
plt.title("Distribution of Units Sold")
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Scatter
plt.scatter(df['Units'], df['TotalSales'], color='red')
plt.title("Units vs Total Sale")
plt.xlabel('Quality')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()