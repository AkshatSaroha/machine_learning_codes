# Weather Prediction Module
import pandas as pd
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

# Step 1: Create Data Set
data = {    
    'temperature': [30, 25, 28, 22, 35, 27, 29, 31, 24, 26],
    'humidity': [70, 65, 75, 80, 60, 55, 50, 85, 90, 95],
    'wind_speed': [10, 12, 8, 15, 5, 7, 9, 11, 6, 14],
    'will_rain': ['No', 'Yes', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'No']
}

df = pd.DataFrame(data)

df['will_rain_encoded'] = df['will_rain'].map({'No': 0, 'Yes': 1})  # Convert variable to number

# Step 2: Data Preparation
x = df[['temperature', 'humidity', 'wind_speed']]
y = df['will_rain_encoded']

# step 3: Model Training
model = LogisticRegression()
model.fit(x, y)

# step 4: Predict weather for new data
new_weather_data = pd.DataFrame({
    'temperature': [32, 26, 30],
    'humidity': [68, 72, 65],
    'wind_speed': [9, 10, 8]
})  

predicted_rain = model.predict(new_weather_data)
print('Predicted Weather Conditions:')

for temp, hum, wind, will_rain in zip(new_weather_data['temperature'], new_weather_data['humidity'], new_weather_data['wind_speed'], predicted_rain):
    print(f"Temperature: {temp} C, Humidity: {hum}%, Wind Speed: {wind} km/h-> Will Rain: {will_rain} {' - Yes' if will_rain else ' - No'}")

# Step 5: Plot relationship
plt.scatter(df['temperature'], df['will_rain_encoded'], color='blue', label='Training Data')
plt.xlabel('Temperature (C)')
plt.ylabel('Will Rain (Encoded)')
plt.title('Weather Prediction: Temperature vs Will Rain')
plt.legend()
plt.grid(True) 
plt.tight_layout()
plt.show()
