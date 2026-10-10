from sklearn.linear_model import LinearRegression

# Training data
X = [[500], [1000], [1500], [2000], [2500]]
y = [10, 20, 30, 40, 50]

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Make a prediction
prediction = model.predict([[1800]])
prediction = model.predict([[1]])
print("Predicted house price:", prediction[0], "lakhs")