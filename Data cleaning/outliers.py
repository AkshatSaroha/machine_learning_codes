import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

# df = pd.read_csv('employee_skills.csv')
# # print(df)

# # violin plot to show distribution of department wise techskills
# plt.figure(figsize=(10,6))
# sns.violinplot(data=df, x='Department', y='TechSkills')
# plt.title('Department wise techskills distribution')

# plt.tight_layout()
# plt.show()

# filtered_df = df[(df['TechSkills'] >= Q1 - 1.5 * IQR) & (df['TechSkills'] <= Q3 + 1.5 * IQR)]


df = pd.read_csv('Outlier_Handling_Input.csv')
plt.figure(figsize=(10,6))
sns.violinplot(data=df, )
plt.title('')
plt.tight_layout()
plt.show()