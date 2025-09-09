import seaborn as sns 
import pandas as pd 
import matplotlib.pyplot as plt 

tips = sns.load_dataset("tips")

# 1. Scatter plot: total bill vs tip
# plt.figure(figsize=(6,4))
# sns.scatterplot(data=tips, x='total_bill', y='tip')
# plt.title('Scatter Plot: total bill vs tip')
# plt.xlabel("Total Bill")
# plt.ylabel('Tip')
# plt.tight_layout()
# plt.show()

# 2. Histograph
# plt.figure(figsize=(6,4))
# sns.histplot(data=tips, x='total_bill', bins=10, kde=True, color="blue")
# plt.title('Histograph: total bill')
# plt.xlabel("Total Bill")
# plt.ylabel('Frequency')
# plt.tight_layout()
# plt.show()

# 3. Box plot: Tip amount by per day
# plt.figure(figsize=(6,4))
# sns.boxplot(data=tips, x='day', y='tip', palette="Set1")
# plt.title('Box plot of Tip amount per day')
# plt.xlabel("Day")
# plt.ylabel('Tip')
# plt.tight_layout()
# plt.show()

# 4. count plot : gender distribution
# plt.figure(figsize=(6,4))
# sns.countplot(data=tips, x='sex', palette="pastel")
# plt.title('gender distibution')
# plt.xlabel("Gender")
# plt.ylabel('Count')
# plt.tight_layout()
# plt.show()


# -----------------------------Task-----------------------------------------------------------


# 1. bar plot - avg total bill by day
plt.figure(figsize=(6,4))
sns.barplot(data=tips, x='day', y='total_bill', palette="Set1")
plt.title('Average Total Bill by Day')
plt.xlabel("Day")
plt.ylabel('Total bill')
plt.tight_layout()
plt.show()

# 2. Boxplot
plt.figure(figsize=(6,4))
sns.boxplot(data=tips, x='time', y='tip', palette="Set1")
plt.title('Time (Lunch / Dinner)')
plt.xlabel("Time")
plt.ylabel('Tip')
plt.tight_layout()
plt.show()

# 3. Scatter Plot – Total Bill vs Tip, Colored by Smoking Status
plt.figure(figsize=(6,4))
sns.scatterplot(data=tips, x='total_bill', y='tip')
plt.title('Scatter Plot: total bill vs tip')
plt.xlabel("Total Bill")
plt.ylabel('Tip')
plt.tight_layout()
plt.show()
