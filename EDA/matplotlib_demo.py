# import matplotlib.pyplot as plt

# plt.plot([1,2,3,4,5], [10, 50, 30, 60, 80])
# plt.title("Test plot")
# plt.xlabel("X axis")
# plt.ylabel("Y axis")
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt 

# # reading from csv
# df = pd.read_csv('sales_data.csv')

# print('Display initial rows', df.head())

# # conveting to date datatype
# df['Date'] = pd.to_datetime(df['Date'])

# # line chart of dailt total sales
# daily_sales = df.groupby('Date')['Sales'].sum()

# plt.figure(figsize=(10,5))
# plt.plot(daily_sales.index, daily_sales.values, marker='o', color='blue')
# plt.title('Daily sales trend')
# plt.xlabel('Date')
# plt.ylabel('Sales')
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt 

# # reading from csv
# df = pd.read_csv('sales_data.csv')

# df['Date'] = pd.to_datetime(df['Date'])

# sales_by_region = df.groupby('Region')['Sales'].sum()
# sales_by_region.plot(kind='bar', title="Total Sales by region", color='blue')
# plt.xlabel('Rgion')
# plt.ylabel("Total Sales")
# plt.show()


# Line chart
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('sales_data.csv')

df['Date'] = pd.to_datetime(df['Date'])

# sales_by_region = df.groupby('Region')['Sales'].sum()
# sales_by_region.plot(kind='line', title="Total Sales by region", color='blue')
# plt.xlabel('Rgion')
# plt.ylabel("Total Sales")
# plt.show()


# Scattered
# plt.scatter(df['Quantity'], df['Sales'], color='red')
# plt.title("Quality vs sale")
# plt.xlabel('Quality')
# plt.ylabel('Sales')
# plt.tight_layout()
# plt.show()


# 4. Histogram
# plt.hist(df['Sales'], bins=10, color="lightgreen", edgecolor='blue')
# plt.title("Sales distribution")
# plt.xlabel('Sales')
# plt.ylabel('Frequency')
# plt.tight_layout()
# plt.show()

# 5. Pie chart - sales per region
category_sales = df.groupby('Region')['Sales'].sum()
category_sales.plot(kind='pie', startangle=90)
plt.title('Sales per region')
plt.tight_layout()
plt.show()
