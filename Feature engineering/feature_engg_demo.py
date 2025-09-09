import pandas as pd  
from datetime import datetime

data = {
    'CustomerID': [101, 102, 103],
    'PurchaseDate': ['2025-05-01', '2025-05-03', '2025-05-05'],
    'Quantity' : [3, 1, 2],
    'PricePerUnit': [500, 1100, 800],
    'ProductCategory' : ['Electronics','Furniture', 'Outfit']
}

df = pd.DataFrame(data)

# # F 1 - Convert 'PurchaseDate' to datetime format
# df['PurchaseDate'] = pd.to_datetime(df['PurchaseDate'])

# # F 2 - Calculate totalsales = qty * ppu
# df['TotalSales'] = df['PricePerUnit'] * df['Quantity']

# # F 3 - Extract weekday ( 0- monday)
# df['Weekdays'] = df['PurchaseDate'].dt.weekday

# # F 4 - Flag high value purchase
# df['IsHighValue'] = df['TotalSales'] > 1500

# # F 5 - kiski sale kb hui
# df['Category_Weekday'] = df['ProductCategory'] + '_' + df['Weekdays'].astype(str)

# print('\n Feature engineered data: \n', df)


# ---------------------- Task 2 --------------------------

# Feature Engineering Tasks:
# =============================
# Create a column called TotalCost from quantity * price.
# Extract the month name from PurchaseDate.
# Create a binary column IsWeekend (True if weekday >=5).
# Combine CustomerID and ProductCategory into a new identifier.
# If Quantity > 2 and Revenue > 1500, create PremiumBuyer = True.
# Create a feature that classifies TotalRevenue into 'Low', 'Medium', 'High'.
# Add a column DaysSincePurchase from today’s date.
# Apply log transformation on TotalRevenue.
# Create group-wise average revenue using .groupby(ProductCategory).
# Flag customers whose revenue is greater than the 90th percentile.

# F 1 Convert PurchaseDate to datetime
df['PurchaseDate'] = pd.to_datetime(df['PurchaseDate'])

# F 2 - Calculate total cost
df['TotalCost'] = df['Quantity'] * df['PricePerUnit']

# F 3 - extract month name from pdate
df['MonthName'] = df['PurchaseDate'].dt.month_name()

# F 4 - creating isweekend
df['IsWeekend'] = df['PurchaseDate'].dt.weekday >= 5

# F 5 - Combine CustomerID and ProductCategory into a new identifier.
df['CustomerID_ProductCat'] = df['CustomerID'].astype(str) + '_' + df['ProductCategory']

# F 6 - create PremiumBuyer
df['PremiumBuyer'] = (df['Quantity'] > 2) & (df['TotalCost'])

# F 7  Classify Revenue into 'Low', 'Medium', 'High'
def classify_revenue(revenue):
    if revenue < 1000:
        return 'Low'
    elif revenue < 5000:
        return 'Medium'
    else:
        return 'High'

df['RevenueCategory'] = df['TotalCost'].apply(classify_revenue)

# F 8 - Add DaysSincePurchase from today’s date
today = pd.to_datetime(datetime.today().date())
df['DaysSincePurchase'] = (today - df['PurchaseDate']).dt.days

# F 9 - Group-wise average revenue using ProductCategory
df['AvgGroupRevenue'] = df.groupby('ProductCategory')['TotalCost'].transform('mean')

# F 10 - Flag customers whose revenue is greater than the 90th percentile
percentile_90 = df['TotalCost'].quantile(0.90)
df['HighRevenueCustomer'] = df['TotalCost'] > percentile_90

print(df)