import pandas as pd  
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder # convet text into numerical value
from sklearn.linear_model import LogisticRegression # for categorical binary classification - split data into binary based on category
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# step 1 & 2: Business and Data understanding
data = {
    'age': [25, 30, 22, 40, 35, 23, 31, 28, 45, 37],
    'gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female', 'Male', 'Female'],
    'time_on_site': [5.5, 10.2, 3.1, 8.5, 7.0, 2.0, 6.0, 9.1, 4.3, 11.5],
    'pages_visited': [4, 10, 2, 7, 6, 1, 5, 9, 3, 11],
    'device': ['Mobile', 'Desktop', 'Mobile', 'Desktop', 'Tablet', 'Mobile', 'Tablet', 'Desktop', 'Mobile', 'Desktop'],
    'purchase': ['No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes']
}

df = pd.DataFrame(data)

# Step 3: Data Preparation

# ENcoded categorical features - bcoz machine learning models work with numerical data 
le_gender = LabelEncoder()
df['gender_encoded'] = le_gender.fit_transform(df['gender'])
# fit_transform - goes to the column and assign them values, male = 0, female = 1

le_device = LabelEncoder()
df['device_encoded'] = le_device.fit_transform(df['device'])

#Encode target variable
df['purchase_encoded'] = df['purchase'].map({'No': 0, 'Yes': 1})

# Select features and target
features = ['age', 'time_on_site', 'pages_visited', 'gender_encoded', 'device_encoded'] # using featres we need to guess target
target = 'purchase_encoded' # we need to guess it so we are not taking it in features

x = df[features] # input
y = df[target] # output (prediction)

# split data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3,  train_size=0.7,random_state=42)

# STEP 4 : MODELING 

model = LogisticRegression()
model.fit(x_train, y_train)

# STEP 5 : EVALUATION

y_pred = model.predict(x_test)

print('Accuracy : ', accuracy_score(y_test, y_pred))
print('Confusion matrix:\n', confusion_matrix(y_test, y_pred))
print('Classification Report:\n', classification_report(y_test, y_pred))

# STEP 6: SIMULATED DATA

sample_test_data = pd.DataFrame({
    'age': [29, 24],
    'time_on_site': [7.5, 3.2],
    'pages_visited':[6,2],
    'gender_encoded': [le_gender.transform(['Female'])[0], le_gender.transform(['Male'])[0]],
    'device_encoded': [le_device.transform(['Mobile'])[0], le_device.transform(['Desktop'])[0]],
})

sample_prediction = model.predict(sample_test_data)
print('Sample Preddictions: ', ['Yes' if pred == 1 else 'No' for pred in sample_prediction] )
