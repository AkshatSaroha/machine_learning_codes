import pandas as pd  
from scipy.stats import zscore
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from datetime import datetime

df = pd.read_csv('exl_retail_customers_dummy.csv')

# Day 1: Data Loading & Initial Exploration
# print(df.head(10))

# print(df.info())
# print(df.describe())

# # count unique values in Region and Gender column
# print('Unique values in region: ', df['Region'].nunique())
# print('Unique values in Gender: ', df['Gender'].nunique())
# print('Unique values in MembershipLevel: ', df['MembershipLevel'].nunique())

# df['LastPurchaseDate'] = pd.to_datetime(df['LastPurchaseDate'])


# -----------------------------Day 2: Handling Missing Values---------------------------------

# print('Missing values before: \n', df.isnull().sum())
# # drop rows where age is missing
# df = df.dropna(subset=['Age'])

# # Fill missing AnnualIncome by group median based on MembershipLevel
# df['AnnualIncome'] = df.groupby('MembershipLevel')['AnnualIncome'].transform( lambda x: x.fillna(x.median()) )
# # Fill missing Gender with mode of gender
# df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])

# print('Missing values after: \n', df.isnull().sum())


# ----------------------Day 3: Outlier Detection and Treatment------------------------------

# plt.figure(figsize=(10, 4))
# sns.boxplot(x=df["TotalRevenue"])
# plt.title("Before Outlier Treatment")
# plt.show()

# # Detect outliers in TotalRevenue using z-score
# z_score = df[['TotalRevenue']].apply(zscore) # accepts an array not a single value
# threshold = 3
# outliers = (z_score.abs() > threshold)
# print('Outlier detected : \n', df[outliers.all(axis=1)])

# # clean_df = df[(z_score.abs() < threshold).all(axis=1)]
# # print('Data after cleaning using z-score method: \n', clean_df)

# # using IQR method 
# Q1 = df['TotalRevenue'].quantile(0.25)
# Q3 = df['TotalRevenue'].quantile(0.75)

# IQR = Q3 - Q1
# lower_bound = Q1 - 1.5 * IQR
# upper_bound = Q3 + 1.5 * IQR

# outlier_iqr = df[(df['TotalRevenue'] < lower_bound) | 
#                  (df['TotalRevenue'] > upper_bound)
#                 ]
# print('Outliers using IQR method: \n', outlier_iqr)

# #Applying caping and flooring to remove outlier
# print(f'\nFloor value (5th percentile): {lower_bound}')
# print(f'\nCap value (95th percentile): {upper_bound}')


# df['TotalRevenue'] = df['TotalRevenue'].apply(
#     lambda x: lower_bound if x < lower_bound else upper_bound if x > upper_bound else x
# )

# # Boxplots
# plt.figure(figsize=(10, 4))
# sns.boxplot(x=df["TotalRevenue"])
# plt.title("After Outlier Treatment ")
# plt.show()


# ----------------------------------Day 4 -Data Normalization--------------------------

normalize = ['AnnualIncome', 'TotalRevenue']
minmax_scaler = MinMaxScaler()
df_minmax_scaled = pd.DataFrame(minmax_scaler.fit_transform(df[normalize]),
                                columns=[f'{col}_MinMax' for col in normalize])

# Apply standardization using z-score
standard_scaler = StandardScaler()
df_standardized = pd.DataFrame(standard_scaler.fit_transform(df[normalize]),
                                columns=[f'{col}_Zscore' for col in normalize])

df_result = pd.concat([df_minmax_scaled, df_standardized], axis=1)

print('\nNormalized Data (Min-Max & Zscore):\n', df_result.head())


features=['AnnualIncome','TotalRevenue']
minmax_scaler = MinMaxScaler()
df_minmax_scaler = pd.DataFrame(
  minmax_scaler.fit_transform(df[features]),
  columns=[f"{col}_MinMax" for col in features]
)

standard_scaler = StandardScaler()
df_standard = pd.DataFrame(
  standard_scaler.fit_transform(df[features]),
  columns=[f"{col}_zscore" for col in features]
)

df_res = pd.concat([df,df_minmax_scaler,df_standard],axis=1)
print("Normalization data(minmax & zscore)\n",df_res)

# AnnualIncome: Original
plt.subplot(2, 2, 1)
sns.histplot(df_res['AnnualIncome'], kde=True, color='skyblue')
plt.title('Original AnnualIncome')

# AnnualIncome: Min-Max
plt.subplot(2, 2, 2)
sns.histplot(df_res['AnnualIncome_MinMax'], kde=True, color='orange')
plt.title('Min-Max Scaled AnnualIncome')

# TotalRevenue: Original
plt.subplot(2, 2, 3)
sns.histplot(df_res['TotalRevenue'], kde=True, color='green')
plt.title('Original TotalRevenue')

# TotalRevenue: Z-score
plt.subplot(2, 2, 4)
sns.histplot(df_res['TotalRevenue_Zscore'], kde=True, color='red')
plt.title('Z-Score Scaled TotalRevenue')

plt.tight_layout()
plt.show()


# -------------------- Day 5: Feature Engineering --------------------

# RevenuePerPurchase
df["RevenuePerPurchase"] = df["TotalRevenue"] / df["Purchases"]

# CustomerTenureMonths
df["CustomerTenureMonths"] = (datetime.today() - df["LastPurchaseDate"]).dt.days // 30

# Categorize customers based on income brackets
df['IncomeBracket'] = df['AnnualIncome'].apply(
    lambda x : 'Low' if x < 500000 else 'Medium' if x < 1000000 else 'High'
)

# Encode MembershipLevel
df["MembershipLevelEncoded"] = df["MembershipLevel"].map({"Silver": 0, "Gold": 1, "Platinum": 2})


# -----------------------------Day 6: -----------------------------------
#1: Region-wise Revenue: Bar plot
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Region', y='TotalRevenue')
plt.title('Region-wise Total Revenue')
plt.xlabel('Region')
plt.ylabel('Total Revenue')
plt.tight_layout()
plt.show()

#2: Revenue over time: Line chart
df['LastPurchaseDate'] = pd.to_datetime(df['LastPurchaseDate'])
revenue_time = df.groupby('LastPurchaseDate')['TotalRevenue'].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(data=revenue_time, x='LastPurchaseDate', y='TotalRevenue')
plt.title('Total Revenue Over Time')
plt.xlabel('Date')
plt.ylabel('Total Revenue')
plt.tight_layout()
plt.show()

#3: Product-wise share: Pie chart
product_share = df['Product'].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(product_share, labels=product_share.index,  startangle=140)
plt.title('Product-wise Share')
plt.axis('equal')  # Ensures pie chart is circular
plt.tight_layout()
plt.show()

#4: Scatter plot: Purchases vs TotalRevenue
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Purchases', y='TotalRevenue', hue='Region',  palette='Set1')
plt.title('Purchases vs Total Revenue')
plt.xlabel('Purchases')
plt.ylabel('Total Revenue')
plt.tight_layout()
plt.show()