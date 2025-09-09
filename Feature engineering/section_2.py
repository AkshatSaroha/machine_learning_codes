import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# Load dataset
df = pd.read_csv('customer_cleaned_imputed.csv')

# Select numerical columns
numerical_cols = ['AnnualIncome', 'AvgTransactionValue', 'LoginFrequency']

# 1. Visualize original distributions
for col in numerical_cols:
    plt.figure()
    sns.boxplot(x=df[col])
    plt.title(f'Original {col} Distribution')
    plt.savefig(f'boxplot_original_{col}.png')
    plt.close()

# 2. Z-score outlier detection
threshold = 3
for col in numerical_cols:
    z_scores = df[numerical_cols].apply(zscore)
    outliers = df[z_scores > threshold]
    print(f'Z-score outliers in {col}:', outliers.shape[0])

# 3. IQR method and bounds
bounds = {}
for col in numerical_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    bounds[col] = (lower, upper)
    print(f'{col} IQR bounds: lower={lower}, upper={upper}')

# 4. Capping and flooring
df_capped = df.copy()
for col in numerical_cols:
    lower, upper = bounds[col]
    df_capped[col] = df_capped[col].apply(
        lambda x: lower if x < lower else upper if x > upper else x
    )

# 5. Visualize distributions after handling
for col in numerical_cols:
    plt.figure()
    sns.boxplot(x=df_capped[col])
    plt.title(f'Handled {col} Distribution')
    plt.savefig(f'boxplot_handled_{col}.png')
    plt.close()

# 6. Save transformed dataset
df_capped.to_csv('customer_outliers_handled.csv', index=False)

