import pandas as pd  
from scipy.stats import zscore
import matplotlib.pyplot as plt

df = pd.read_csv('z_score_outlier_task.csv')

print('Before removing outliers: \n', df)

# Calculating Z-scores for the Price column
numerical_cols = ['Price']
z_score = df[numerical_cols].apply(zscore)

# Detecting outliers 
threshold = 3
outliers = (z_score.abs() > threshold)
print('\n Outlier detected: \n', df[outliers.any(axis=1)])

clean_df = df[(z_score.abs() < threshold).all(axis=1)]
print("\n After removing outliers: \n", clean_df)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.boxplot(df['Price'])
plt.title("Before Removing Outliers")

plt.subplot(1, 2, 2)
plt.boxplot(clean_df['Price'])
plt.title("After Removing Outliers")

plt.tight_layout()
plt.show()