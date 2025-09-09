import pandas as pd  

df = pd.read_csv('cap_floor.csv')

print('Original data: \n', df)

# Calculating 4th and 5th percentile
lower_cap = df['PurchaseAmount'].quantile(0.05)
upper_cap = df['PurchaseAmount'].quantile(0.95)

print(f'\nFloor value (5th percentile): {lower_cap}')
print(f'\nCap value (95th percentile): {upper_cap}')

#Applying caping and flooring
df['PurchaseAmount'] = df['PurchaseAmount'].apply(
    lambda x: lower_cap if x < lower_cap else upper_cap if x > upper_cap else x
)
print('\n Data after capping and flooring: \n', df)

