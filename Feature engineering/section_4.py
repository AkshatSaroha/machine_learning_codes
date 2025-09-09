import pandas as pd

# Load dataset
df = pd.read_csv("customer_outliers_handled.csv")

# 1. Create TotalSpend = TotalTransactions * AvgTransactionValue
df['TotalSpend'] = df['TotalTransactions'] * df['AvgTransactionValue']

# 2. Create AgeBand column
def get_age_band(age):
    if age <= 25:
        return '18-25'
    elif age <= 35:
        return '26-35'
    elif age <= 45:
        return '36-45'
    else:
        return '46+'

df['AgeBand'] = df['Age'].apply(get_age_band)

# 3. Convert IsChurned to binary: 1 for Yes, 0 for No
df['IsChurnedBinary'] = df['IsChurned'].map({'Yes': 1, 'No': 0})

# 4. Create HighValueCustomer flag if TotalSpend > 90th percentile
percentile_90 = df['TotalSpend'].quantile(0.90)
df['HighValueCustomer'] = df['TotalSpend'].apply(lambda x: 1 if x > percentile_90 else 0)

# 5. MonthlyTransactionRate = TotalTransactions / (LoginFrequency / 4)
def calculate_monthly_transaction_rate(row):
    if row['LoginFrequency'] == 0:
        return 0  # To Avoid division by zero
    return row['TotalTransactions'] / (row['LoginFrequency'] / 4)

df['MonthlyTransactionRate'] = df.apply(calculate_monthly_transaction_rate, axis=1)

# 6. CustomerScore = (TotalSpend * SatisfactionScore) / CartAbandonRate
def calculate_customer_score(row):
    if row['CartAbandonRate'] == 0:
        return 
    return (row['TotalSpend'] * row['SatisfactionScore']) / row['CartAbandonRate']

# When you use axis=1, the function receives each row of the DataFrame
df['CustomerScore'] = df.apply(calculate_customer_score, axis=1)

print(df)
# BONUS: Save enriched dataset
df.to_csv("customer_features_enriched.csv", index=False)
print("\nEnriched dataset saved as 'customer_features_enriched.csv'")
