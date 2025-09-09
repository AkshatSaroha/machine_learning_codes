# Task 1
import pandas as pd

data = {
    'CustomerID': ['C001', 'C002', 'C003', 'C004', 'C005', 'C006', 'C007', 'C008'],
    'Name': ['Amit', 'Anita', 'Ravi', 'Sunita', 'Manoj', 'Priya', 'Karan', 'Neha'],
    'Age': [29, None, 35, None, 42, None, 31, 30],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female']
}

df = pd.DataFrame(data)
print(df)
# Count missing values
missing_count = df['Age'].isnull().sum()
print('\nMissing count : ', missing_count)

# Impute missing values with the mean
mean_age = df['Age'].mean()
df['Age'].fillna(mean_age, inplace=True)

print("\nDataFrame after imputation:")
print(df)


# TASK 2

# import pandas as pd

# data = {
#     'CustomerID': ['C101', 'C102', 'C103', 'C104', 'C105', 'C106', 'C107'],
#     'Name': ['Rahul', 'Pooja', 'Aakash', 'Neeta', 'Sanjay', 'Rekha', 'Vikas'],
#     'MembershipLevel': ['Gold', 'Silver', None, 'Gold', 'Platinum', None, 'Silver']
# }

# df = pd.DataFrame(data)

# missing_rows = df[df['MembershipLevel'].isnull()]
# print("Rows with missing MembershipLevel:")
# print(missing_rows)

# df_cleaned = df.dropna(subset=['MembershipLevel'])

# print("\nDataFrame after dropping missing MembershipLevel:")
# print(df_cleaned)


# TASK 3
# import pandas as pd

# data = {
#     'ProductID': ['P001', 'P002', 'P003', 'P004', 'P005', 'P006', 'P007', 'P008'],
#     'ProductName': ['Shampoo', 'Biscuits', 'Soap', 'Toothpaste', 'Cookies', 'Facewash', 'Juice', 'Cream'],
#     'Category': ['Personal Care', 'Food', None, 'Personal Care', 'Food', 'Personal Care', 'Food', None]
# }

# df = pd.DataFrame(data)

# missing_rows = df[df['Category'].isnull()]
# print("Rows with missing Category:")
# print(missing_rows)

# category_mode = df['Category'].mode()[0]
# print(f"\nMost frequent Category (mode): {category_mode}")

# df['Category'] = df['Category'].fillna(category_mode)

# print("\nDataFrame after mode imputation:")
# print(df)


# TASK 4
# import pandas as pd

# data = {
#     'Date': ['2023-07-01', '2023-07-02', '2023-07-03', '2023-07-04', '2023-07-05', '2023-07-06'],
#     'CustomerID': ['C001', 'C001', 'C001', 'C001', 'C001', 'C001'],
#     'Location': ['Mumbai', None, None, 'Delhi', None, None]
# }

# df = pd.DataFrame(data)

# df['Location'] = df['Location'].fillna(method='ffill')

# print("DataFrame after forward fill:")
# print(df)
