import pandas as pd

df = pd.read_csv('customer_data.csv')

# Convert signup_date 
df['signup_date'] = pd.to_datetime(df['signup_date'])
df['signup_month'] = df['signup_date'].dt.month
df['signup_weekday'] = df['signup_date'].dt.weekday

# Encode gender column
gender_col = {'Male': 0, 'Female': 1, 'Other': 2}
df['gender_encoded'] = df['gender'].map(gender_col)

# binary feature is_returning_customer
df['is_returning_customer'] = df['num_previous_orders'].apply(lambda x: 1 if x > 0 else 0)

# Bin the total_spent
def bin_spent_func(total_spent):
    if total_spent < 100:
        return 'Low'
    elif total_spent <= 300:
        return 'Medium'
    else:
        return 'High'
df['total_spent_bin'] = df['total_spent'].apply(bin_spent_func) 

# one hot encode
df = pd.get_dummies(columns=['country'], prefix='country', data=df)

# make changes to the csv file
# df.to_csv('customer_data_processed.csv', index=False)

print(df)