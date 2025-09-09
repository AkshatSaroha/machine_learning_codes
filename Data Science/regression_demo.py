import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = {
    'size_sqft': [600, 800, 1000, 1200, 1500, 1800, 2000],
    'price': [15, 20, 25, 30, 35, 40, 50]
}
df = pd.DataFrame(data)



# step 2 : prepare input and output
x = df[['size_sqft']] # input must be 2D
y = df['price']  # output is 1D always

# step 3 : train the model
model = LinearRegression()
model.fit(x,y)

# step 4 : predict price for new house sizes
new_sizes = pd.DataFrame({
    'size_sqft': [1300, 1750, 2100]
})
predicted_prices = model.predict(new_sizes)

# step 5 : print predictions
print('Predicted House Prices:')
for size, price in zip(new_sizes['size_sqft'], predicted_prices):
    print(f'{size} sqft -> ${int(price)}')

# step 6 : plot relationship
plt.scatter(df['size_sqft'], df['price'], color='blue', label='Training data')
plt.xlabel('Size (sqft)')
plt.ylabel('Price ($)')
plt.title('House Price vs Size')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()