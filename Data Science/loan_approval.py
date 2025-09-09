import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/loan.csv')

# define feature and target
x = df[['Credit_Score', 'Annual_Income']]
y = df['Loan_Approved']

# split data 
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

# Modeling
model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

# Predict on a new data
new_customer = pd.DataFrame({
    'Credit_Score': [705],
    'Annual_Income': [73000]
})

prediction = model.predict(new_customer)
print("Loan Approved (1 = Yes, 0 = No):", prediction[0])

plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='Credit_Score', y='Annual_Income', hue='Loan_Approved', palette='Set1', s=100)
plt.title('Credit Score vs Annual Income by Loan Approval')
plt.xlabel('Credit Score')
plt.ylabel('Annual Income')
plt.grid(True)
plt.tight_layout()
plt.show()