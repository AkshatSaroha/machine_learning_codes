import pandas as pd  
from scipy.stats import zscore

df = pd.read_csv('Outlier_Handling_Input.csv')
print(df)

# apply zscore - to remove outliers

numerical_cols = ['AnnualIncome', 'SpendingScore']
z_score = df[numerical_cols].apply(zscore)

threshold = 3
outliers = (z_score.abs() > threshold)
print('Outlier detected: \n', df[outliers.any(axis=1)])

clean_df = df[(z_score.abs() < threshold).all(axis=1)]
print('Data after cleaning using z-score method: \n', clean_df)


