# Predict mobile price based camera quality & storage space(in GB)
 
import pandas as pd
from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt


# Step 1: Create Data Set
data = {
    'storage_gb': [64, 128, 128, 256, 256, 512, 512],
    'camera_mp' : [12, 12, 48, 48, 64, 64, 108],
    'price':[300, 350, 400, 450, 500, 600, 700]
}
 
df = pd.DataFrame(data)
 
# Step 2: Features & Target
x = df[['storage_gb', 'camera_mp']]
y = df['price']
 
# Step 3: Train the model
model = LinearRegression()
model.fit(x, y)
 
# Step 4: Predict price for new phones
new_phones = {
    'storage_gb': [128, 256, 512],
    'camera_mp': [24, 64, 108]
}
 
predicted_price = model.predict(pd.DataFrame(new_phones))
 
# Step 5: Print Predicitons
# print('Predicted Phone Prices:')
# for i, price in enumerate(predicted_price):
#     print(f"Phone {i+1}: Storage {new_phones.loc[i, 'storage_gb']} GB, Camera {new_phones.loc[i, 'camera_mp']} MP -> Price: ${int(price)}")

print('Predicted Phone Prices:')
for i, price in enumerate(predicted_price):
    print(f"Phone {i+1}: Storage {new_phones['storage_gb'][i]} GB, Camera {new_phones['camera_mp'][i]} MP -> Price: ${int(price)}")
   
   
# Step 6: Plot relationship
# plt.scatter(df['storage_gb'], df['price'], color='blue', label='Training Data')
# plt.xlabel('Storage (GB)')
# plt.ylabel('Price ')
# plt.title('Phone price vs storage')
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()
 