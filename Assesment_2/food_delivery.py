import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load data
df = pd.read_csv('delivery_times.csv')
print(df)

# 2. Boxplot to visualize outliers
plt.figure(figsize=(8,5))
sns.boxplot(data=df, y='Delivery_Time_Minutes', color='purple')
plt.title('Boxplot of delivery Items')
plt.xlabel('Delivery')
plt.ylabel("Delivery Time (minutes)")
plt.grid(True)
plt.show()

# 3. Calculate IQR
Q1 = df['Delivery_Time_Minutes'].quantile(0.25)
Q3 = df['Delivery_Time_Minutes'].quantile(0.75)
IQR = Q3 - Q1

# 4. Upper & lower bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
print(f"\nLower Bound: {lower_bound}, Upper Bound: {upper_bound}")

# 5. Flag outlier
df['Status'] = df['Delivery_Time_Minutes'].apply(
    lambda x: 'Outlier' if x < lower_bound or x > upper_bound else 'Normal'
)

# 6. Print outliers
outlier_iqr = df[(df['Delivery_Time_Minutes'] < lower_bound) | 
                 (df['Delivery_Time_Minutes'] > upper_bound)
                ]
print('\nOutliers using IQR method: \n', outlier_iqr)

# 7. Color the outliers in red in the boxplot
plt.figure(figsize=(8,5))
sns.boxplot(
    data=df,
    y='Delivery_Time_Minutes', 
    color='lightblue', 
    hue='Status', # status column to determine color
    palette={'Outlier': 'red', 'Normal': 'blue'})
plt.title("Boxplot with Outliers Highlighted")
plt.ylabel("Delivery Time (minutes)")
plt.grid(True)
plt.show()

# 8. Hostogram of delivery times
plt.figure(figsize=(8, 5))
sns.histplot(df['Delivery_Time_Minutes'], bins=10, kde=True, color='lightgreen')
plt.title("Histogram of Delivery Times")
plt.xlabel("Delivery Time (minutes)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# 9: Outliers by Customer Area
outlier_counts = outlier_iqr['Customer_Area'].value_counts()
print("\nOutliers by Customer Area:\n", outlier_counts)

df.to_csv("updated_delivery_times.csv", index=False)
print("\nUpdated data uploaded !!!!!")


