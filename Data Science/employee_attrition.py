import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/employee_attrition.csv')

# Feature and target
x = df[['Years_At_Company', "Job_Satisfaction"]]
y = df['Left_Company']

# split data 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# modeling 
model = LogisticRegression()
model.fit(x_train, y_train)

# Evaluate
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

# Predict for a new data
new_employee = pd.DataFrame({
    'Years_At_Company': [2],
    'Job_Satisfaction': [4]
})
prediction = model.predict(new_employee)
print("Prediction for New Employee (1 = Will Leave, 0 = Will Stay):", prediction[0])

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Years_At_Company', y='Job_Satisfaction', hue='Left_Company', palette='Set1', s=100)
plt.title("Employee Attrition Visualization")
plt.xlabel("Years at Company")
plt.ylabel("Job Satisfaction (1-10)")
plt.grid(True)
plt.show()