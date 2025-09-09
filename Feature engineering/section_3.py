import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Load the cleaned dataset with outliers handled
df = pd.read_csv("customer_outliers_handled.csv")

# 1. Select numerical columns to normalize
cols_to_scale = ['AnnualIncome', 'AvgTransactionValue', 'LoginFrequency']

# 2. Min-Max Scaling -- all data bw 0 and 1
minmax_df = df.copy()
minmax_scaler = MinMaxScaler()
minmax_df[cols_to_scale] = minmax_scaler.fit_transform(minmax_df[cols_to_scale])

# 3. Z-Score Standardization -- mean=0, std=1 (all data around 0)
standard_df = df.copy()
standard_scaler = StandardScaler()
standard_df[cols_to_scale] = standard_scaler.fit_transform(standard_df[cols_to_scale])

# 4. Histogram Comparison
for col in cols_to_scale:
    plt.figure(figsize=(12, 4))
    
    # Original
    plt.subplot(1, 3, 1)
    sns.histplot(df[col], kde=True)
    plt.title(f"Original: {col}")

    # Min-Max
    plt.subplot(1, 3, 2)
    sns.histplot(minmax_df[col], kde=True, color='green')
    plt.title(f"Min-Max Scaled: {col}")

    # Standardized
    plt.subplot(1, 3, 3)
    sns.histplot(standard_df[col], kde=True, color='orange')
    plt.title(f"Standard Scaled: {col}")
    
    plt.tight_layout()
    plt.show()

# 5. Save Scaled Versions
minmax_df.to_csv("customer_minmax_scaled.csv", index=False)
standard_df.to_csv("customer_standard_scaled.csv", index=False)

print("Files saved:\n- customer_minmax_scaled.csv\n- customer_standard_scaled.csv")
