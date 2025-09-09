import pandas as pd  
from scipy.stats import zscore

df = pd.read_csv('Outlier_Handling_Input.csv')
print(df)

Q1 = df['PurchaseCount'].quantile(0.25)
Q3 = df['PurchaseCount'].quantile(0.75)

IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outlier_iqr = df[(df['PurchaseCount'] < lower_bound) | 
                 (df['PurchaseCount'] > upper_bound)
                 ]
print('Outliers using IQR method: \n', outlier_iqr)



clean_df_iqr = df[(df['PurchaseCount'] >= lower_bound) & 
                  (df['PurchaseCount'] <= upper_bound)]
print('Data after cleaning using IQR method: \n', clean_df_iqr)