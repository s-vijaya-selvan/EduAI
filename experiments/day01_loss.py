import numpy as np

actual = np.array([
    0.90,
    0.40,
    0.80,
    0.30
])

predicted = np.array([
    0.85,
    0.55,
    0.70,
    0.25
])

errors = actual - predicted
squared_errors = errors ** 2
mse = np.mean(squared_errors)

print("Actual:")
print(actual)
print("\nPredicted:")
print(predicted)
print("\nErrors:")
print(errors)
print("\Squared errors:")
print(squared_errors)
print("\nMSE:")
print(mse)