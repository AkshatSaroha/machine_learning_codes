import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

data = pd.read_csv('data_cleaning_customer_data.csv')

# print('Original Data: ')
# print(data.head())

# # check missing values
# print('Missing values: ')
# print(data.isnull().sum())

# # impute missing values in age
# data['Age'] = data['Age'].fillna(data['Age'].median())

# # impute missing values in annualIncome
# data['AnnualIncome'] = data['AnnualIncome'].fillna(data['AnnualIncome'].median())

# # Drop rows where membership is missing
# data.dropna(subset=['MembershipLevel', 'PurchaseFrequency'], inplace=True)

# # Remove outliers in AnnualIncome
# data = data[data['AnnualIncome'] > 25000]

# print('\n Cleaned data summary: ')
# print(data.describe())


df = pd.read_csv('data_cleaning_customer_data.csv')

# plt.figure(figsize=(10,5))
# sns.heatmap(df.isnull(), cbar=False, yticklabels=False)
# plt.title('Heatmap of Missing Values')
# plt.tight_layout()
# plt.show()

# df_dropped = df.dropna()
# plt.figure(figsize=(10,5))

# mode
# Impute age with mean
# df['Age'] = df['Age'].fillna(df['Age'].mean())

# # Impute annual income with median
# df['AnnualIncome'] = df['AnnualIncome'].fillna(df['AnnualIncome'].median())

# # Impute customerSatisfaction with mode
# df['CustomerSatisfaction'] = df['CustomerSatisfaction'].fillna(df['CustomerSatisfaction'].mode()[0])
# # print(df.describe())
# print(df)

print(df.head(5))
# // Forward Fill
df['AnnualIncome'] = df['AnnualIncome'].ffill()

# // Backword Fill
df['MembershipLevel'] = df['MembershipLevel'].bfill()

print(df.head(5))
 