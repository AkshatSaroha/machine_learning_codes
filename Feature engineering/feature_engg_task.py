import pandas as pd
from datetime import datetime
import math

#-----------------------Task 1 -------------------------------
# data = {
#     'CustomerID': ['C001', "C002", 'C003', 'C004', 'C005'],
#     'Age': [22, 45, 33, 27, 51],
#     'AnnualIncome' : [30000, 60000, 48000, 35000, 70000],
# }

# df = pd.DataFrame(data)

# # Age group column
# def age_helper(age):
#     if age < 30:
#         return "Young"
#     elif age <= 50:
#         return "Adult"
#     else:
#         return "Senior"

# df['AgeGroup'] = df['Age'].apply(age_helper)
# print("Modified DataFrame:\n", df)

# avg_income = df.groupby('AgeGroup')['AnnualIncome'].mean().reset_index()
# print("\nAverage Income by Age Group:\n", avg_income)


#---------------------------Task 2------------------------------

# data = {
#     'ProductID': ['P101', 'P102', 'P103', 'P104', 'P105'],
#     'UnitsSold': [50, 30, 100, 15, 75],
#     'UnitPrice': [120, 500, 20, 900, 60]
# }

# df = pd.DataFrame(data)
# print(df)
# df['TotalSales'] = df['UnitsSold'] * df['UnitPrice']

# # Create SalesCategory column
# df['SalesCategory'] = df['TotalSales'].apply(lambda x: 'High' if x > 40000 else 'Low')

# print(df)



#-----------------------------Task 3-----------------------------

# data = {
#     'UserID': ['U001', 'U002', 'U003', 'U004', 'U005'],
#     'LoginTime': ['2023-06-21 08:45:00', '2023-06-21 15:20:00', '2023-06-21 21:10:00', '2023-06-21 06:00:00', '2023-06-21 12:35:00']
# }

# df = pd.DataFrame(data)
# print(df)

# df['LoginTime'] = pd.to_datetime(df['LoginTime'])

# # New column hour
# df['Hour'] = df['LoginTime'].dt.hour

# # Time of dayy
# def calc_time(hour):
#     if 0 <= hour <= 11:
#         return 'Morning'
#     elif 12 <= hour <= 17:
#         return 'Afternoon'
#     else:
#         return 'Evening'
    
# df['TimeOfDay'] = df['Hour'].apply(calc_time)

# print(df)


#---------------------------------Task 4----------------------------

# data = {
#     'PatientID': ['P001', 'P002', 'P003', 'P004', 'P005'],
#     'Weight_KG': [70, 80, 60, 90, 55],
#     'Height_M': [1.75, 1.80, 1.65, 1.70, 1.60]
# }

# df = pd.DataFrame(data)
# print(df)

# # Step 2: Calculate BMI = Weight / Height ** 2
# df['BMI'] = df['Weight_KG'] / (df['Height_M'] ** 2)

# # Step 3: Categorize BMI
# def calculate_bmi(bmi):
#     if bmi < 18.5:
#         return 'Underweight'
#     elif bmi < 25:
#         return 'Normal'
#     elif bmi < 30:
#         return 'Overweight'
#     else:
#         return 'Obese'

# df['BMICategory'] = df['BMI'].apply(catculate_bmi)

# print(df)


#---------------------Task 5------------------------------

# data = {
#     'ReviewID': ['R001', 'R002', 'R003', 'R004', 'R005'],
#     'ReviewText': [
#         "Excellent service and friendly staff",
#         "Poor experience and late delivery",
#         "Quick delivery and good packaging",
#         "Terrible product quality",
#         "Loved the product and price"
#     ]
# }

# df = pd.DataFrame(data)
# print(df)

# # Count number of words 
# df['WordCount'] = df['ReviewText'].apply(lambda x: len(x.split()))

# # Create IsPositive
# positive_words = ['good', 'excellent', 'loved', 'friendly']

# # Check positive words
# df['IsPositive'] = df['ReviewText'].str.lower().apply(
#     lambda text: any(word in text for word in positive_words)
# )
# print(df)


#-------------------------Task 6-----------------------------

# data = {
#     'OrderID': ['O001', 'O002', 'O003', 'O004', 'O005'],
#     'OrderDate': ['2023-06-01', '2023-06-02', '2023-06-03', '2023-06-05', '2023-06-06'],
#     'DeliveryDate': ['2023-06-05', '2023-06-06', '2023-06-04', '2023-06-10', '2023-06-09']
# }

# df = pd.DataFrame(data)
# print(df)

# df['OrderDate'] = pd.to_datetime(df['OrderDate'])
# df['DeliveryDate'] = pd.to_datetime(df['DeliveryDate'])

# # Calculate DeliveryDays
# df['DeliveryDays'] = (df['DeliveryDate'] - df['OrderDate']).dt.days

# # Flag as Delayed 
# df['Delayed'] = df['DeliveryDays'] > 4

# print(df)


#----------------------------Task 7----------------------------

# data = {
#     'ClientID': ['CL001', 'CL002', 'CL003', 'CL004', 'CL005'],
#     'LoanAmount': [100000, 150000, 200000, 120000, 180000],
#     'LoanTerm_Years': [10, 15, 20, 10, 12],
#     'InterestRate': [6, 7, 6.5, 5, 6.8]
# }

# df = pd.DataFrame(data)
# print(df)

# # Calculate TotalInterest
# df['TotalInterest'] = (df['LoanAmount'] * df['InterestRate'] * df['LoanTerm_Years']) / 100

# print(df)


#----------------------------Task 8-------------------------


# data = {
#     'CarID': ['C001', 'C002', 'C003', 'C004', 'C005'],
#     'FuelType': ['Petrol', 'Diesel', 'Electric', 'Petrol', 'Hybrid']
# }

# df = pd.DataFrame(data)
# print(df)
# # One hot encoded
# # Step 2: One-hot encode the FuelType column with prefix 'Is'
# df_encoded = pd.get_dummies(df, columns=['FuelType'], prefix='Is')

# # View the result
# print(df_encoded)


#-----------------------------Task 9----------------------------

# data = {
#     'CustomerID': ['M001', 'M002', 'M003', 'M004', 'M005'],
#     'MonthlySpend': [2000, 500, 1500, 3000, 800]
# }

# df = pd.DataFrame(data)
# print(df)

# # Step 2: Define function to categorize spenders
# def classify_spender(amount):
#     if amount <= 999:
#         return 'Low'
#     elif amount <= 1999:
#         return 'Medium'
#     else:
#         return 'High'

# df['SpenderType'] = df['MonthlySpend'].apply(classify_spender)

# print(df)


#------------------------------Task 10-------------------------

data = {
    'TripID': ['T001', 'T002', 'T003', 'T004', 'T005'],
    'Distance_KM': [400, 300, 500, 350, 450],
    'FuelUsed_L': [40, 30, 50, 38, 42],
    'Duration_Hours': [5, 4, 6, 5, 5.5]
}

df = pd.DataFrame(data)
print(df)

# Calculate FuelEfficiency = Distance_KM / FuelUsed_L
df['FuelEfficiency'] = df['Distance_KM'] / df['FuelUsed_L']

# Calculate AverageSpeed = Distance_KM / Duration_Hours
df['AverageSpeed'] = df['Distance_KM'] / df['Duration_Hours']

print(df)

