import pandas as pd

try:
    df = pd.read_csv('sales_data.csv')
    # print("Data loaded successfully.")
except FileNotFoundError:
    print('File do not exist')

# print('\nInitial 10 records ')
# print(df.head(10))


# print('\n Dataset shape (row, column)', df.shape)
# print('Column names: ', list(df.columns))
# print(df.dtypes)


# print("Number of null records in Data Set")
# print(df.isnull().sum())

# print("Missing values (%): ")
# print((df.isnull().mean() * 100).round(2))

# print("Numerical Summary: ")
# print(df.describe().round(2))

# print("Categorical Summary: ")
# print(df.describe(include='object'))

# print("Number of Unique Cities: ", df['City'].nunique())
# print("Number of Cities: ", df['City'])

# print("Total Quantity sold: ", df["Quantity"].sum())

# print("Top 5 highest price products: ")
# print(df[['Product', 'Price']].sort_values(by='Price', ascending=False).drop_duplicates(subset='Price'))