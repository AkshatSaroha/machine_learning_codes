import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("customer_insights_raw.csv")

print("\nDataset Info")
print(df.info())    

print("\nMissing Value Count")
print(df.isnull().sum())

# Identify columns with missing values and classify them
missing_cols = df.columns[df.isnull().any()]
num_cols = df[missing_cols].select_dtypes(include=['number']).columns.tolist()
cat_cols = df[missing_cols].select_dtypes(include=['object', 'category']).columns.tolist()
print(f"\nNumerical columns with missing: {num_cols}")
print(f"Categorical columns with missing: {cat_cols}")

# Heatmap before imputation
plt.figure(figsize=(10,6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Before Imputation")
plt.show()

# Imputation - replacing missing data points with substituted values
# Numerical: median
df_median = df.copy()
for col in num_cols:
    df_median[col] = df_median[col].fillna(df_median[col].median())

# Numerical: mean
df_mean = df.copy()
for col in num_cols:
    df_mean[col] = df_mean[col].fillna(df_mean[col].mean())

# Categorical: mode
for col in cat_cols:
    mode_val = df[col].mode()[0]
    df_median[col] = df_median[col].fillna(mode_val)
    df_mean[col] = df_mean[col].fillna(mode_val)

# 4. Drop rows with >2 missing values (before imputation)
df_cleaned = df.copy()
rows_to_drop = df_cleaned[df_cleaned.isnull().sum(axis=1) > 2].index
df_cleaned.drop(index=rows_to_drop, inplace=True)

# Impute remaining missing values in cleaned df (median for num, mode for cat)
for col in num_cols:
    df_cleaned[col] = df_cleaned[col].fillna(df_cleaned[col].median())
for col in cat_cols:
    df_cleaned[col] = df_cleaned[col].fillna(df_cleaned[col].mode()[0])

# 5. Save cleaned version
df_cleaned.to_csv("customer_cleaned_imputed.csv", index=False)

# Bonus: Heatmap after imputation
plt.figure(figsize=(10,6))
sns.heatmap(df_cleaned.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values After Imputation")
plt.show()