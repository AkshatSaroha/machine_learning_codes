import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the dataset
df = pd.read_csv('patient_data.csv')

# Step 2: Bar chart - Number of Patients by Region
region_counts = df['Region'].value_counts()

region_counts.plot(kind='bar', color='purple')
plt.title('Number of Patients by Region')
plt.xlabel('Region')
plt.ylabel('Number of Patients')
plt.tight_layout()
plt.show()

# Step 3: Pie chart - Distribution of Diagnosis
diagnosis_counts = df['Diagnosis'].value_counts()

diagnosis_counts.plot(kind='pie', startangle=90)
plt.title('Distribution of Diagnoses')
plt.tight_layout()
plt.show()

# Step 4: Line chart - Total Treatment Cost Over Time
# Aggregate cost per date
cost_over_time = df.groupby('VisitDate')['TreatmentCost'].sum()
cost_over_time.plot(kind='line', marker='o', color='lightgreen')
plt.title('Total Treatment Cost Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cost')
plt.tight_layout()
plt.show()

# Step 5: Histogram - Age Distribution of Patients
plt.hist(df['Age'], bins=10, color='lightblue', edgecolor='black')
plt.title('Age Distribution of Patients')
plt.xlabel('Age')
plt.ylabel('Number of Patients')
plt.tight_layout()
plt.show()

# Step 6: Scatter Plot - Age vs Treatment Cost
plt.scatter(df['Age'], df['TreatmentCost'], color='orange')
plt.title('Age vs Treatment Cost')
plt.xlabel('Age')
plt.ylabel('Treatment Cost')
plt.tight_layout()
plt.show()
