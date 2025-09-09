import pandas as pd  
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df = pd.read_csv('retail_sales.csv')

print('Original Data: \n',df)

features = ['UnitsSold', 'UnitPrice', 'TotalRevenue']

# Applying min max scaler
minmax_scaler = MinMaxScaler()
df_minmax_scaled = pd.DataFrame(minmax_scaler.fit_transform(df[features]),
                                columns=[f'{col}_MinMax' for col in features])

# Applying standardization using zscore
standard_scaler = StandardScaler()
df_standardized = pd.DataFrame(standard_scaler.fit_transform(df[features]),
                                columns=[f'{col}_Zscore' for col in features])

# combine
df_result = pd.concat([df, df_minmax_scaled, df_standardized], axis = 1)

print('\nNormalized Data (Min-Max & Zscore):\n', df_result)