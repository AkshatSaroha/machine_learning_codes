import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv('data/vehicle_insurance.csv')

# target and feature
x = df[['Age', 'Accidents_Last_3_Years']]
y = df['Claimed_Insurance']

# splitting
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# modeling
model = LogisticRegression()
model.fit(x_train, y_train)

# evaluate 
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

sample = pd.DataFrame({
    'Age': [42],
    'Accidents_Last_3_Years': [2]
})
prediction = model.predict(sample)
print("Insurance Claim Prediction (1 = Will Claim, 0 = Won't Claim):", prediction[0])

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Age', y='Accidents_Last_3_Years', hue='Claimed_Insurance', palette={0: 'red', 1: 'blue'}, s=100)
plt.title("Vehicle Insurance Claim Visualization")
plt.xlabel("Customer Age")
plt.ylabel("Accidents in Last 3 Years")
plt.grid(True)
plt.show()

# plt.figure(figsize=(6, 4))
# sns.barplot(x='Claimed_Insurance', y='Accidents_Last_3_Years', data=df)
# plt.title("Average Accidents vs Claim Status")
# plt.xlabel("Claimed Insurance (0 = No, 1 = Yes)")
# plt.ylabel("Average Accidents")
# plt.show()


