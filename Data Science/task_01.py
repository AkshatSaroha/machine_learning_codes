import pandas as pd  
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder # convet text into numerical value
from sklearn.linear_model import LogisticRegression # for categorical binary classification - split data into binary based on category
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

import warnings
warnings.filterwarnings('ignore')

# step 1 & 2: Business and Data understanding
data = {
    'study_hours': [1, 2, 3.5, 5, 0.5, 4, 6, 2, 3, 4.5],
    'attendance': ['Low', 'Medium', 'High', 'High', 'Low', 'High', 'High', 'Medium', 'Medium', 'High'],
    'internet_usage': ['High', 'Low', 'Medium', 'Low', 'High', 'Medium', 'Low', 'Medium', 'High', 'Low'],
    'extra_classes' : ['No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes'],
    'pass_exam' : ['No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes']
}

df = pd.DataFrame(data)

# Step 3: Data Preparation

# Encode categorical features
le_attedance = LabelEncoder()
df['attendance_encoded'] = le_attedance.fit_transform(df['attendance'])

le_internet_usage = LabelEncoder()
df['internet_usage_encoded'] = le_internet_usage.fit_transform(df['internet_usage'])

le_extra_classes = LabelEncoder()
df['extra_classes_encoded'] = le_extra_classes.fit_transform(df['extra_classes'])

# encode target variable
df['pass_exam_encoded'] = df['pass_exam'].map({'No': 0, 'Yes': 1})

# select features and target
features = ['study_hours', 'attendance_encoded', 'internet_usage_encoded', 'extra_classes_encoded']
target = 'pass_exam_encoded'

x = df[features]
y = df[target] 

# split data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3,  random_state=42)

# STEP 4 : MODELING
model = LogisticRegression()
model.fit(x_train, y_train)

# STEP 5 : EVALUATION
y_pred = model.predict(x_test)
print('Accuracy : ', accuracy_score(y_test, y_pred))
print('Confusion matrix:\n', confusion_matrix(y_test, y_pred))
print('Classification Report:\n', classification_report(y_test, y_pred))

# sample data
sample_test_data = pd.DataFrame({
    'study_hours': [2.5, 0.5],
    'attendance_encoded': [le_attedance.transform(['Medium'])[0], le_attedance.transform(['Low'])[0]],
    'internet_usage_encoded': [le_internet_usage.transform(['High'])[0], le_internet_usage.transform(['Low'])[0]],
    'extra_classes_encoded': [le_extra_classes.transform(['Yes'])[0], le_extra_classes.transform(['No'])[0]]
})

sample_prediction = model.predict(sample_test_data)
print('Sample Preddictions: ', ['Yes' if pred == 1 else 'No' for pred in sample_prediction] )
