from sklearn.linear_model import LinearRegression
import numpy as np

# Step 1: Training data (sequence of 3 numbers → predict 4th)
# Input: [1, 2, 3] → Output: 4
X_train = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [10, 11, 12],
    [20, 21, 22],
    [100, 101, 102]
])

y_train = np.array([4, 5, 13, 23, 103])  # "Next number" in sequence

# Step 2: Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 3: Predict next number for a new sequence
new_input = np.array([[1, 3, 7]])  # Model should predict 6
prediction = model.predict(new_input)

print(f"Input sequence: {new_input.flatten().tolist()}")
print(f"Predicted next number: {prediction[0]:.2f}")
