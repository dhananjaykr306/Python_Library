import numpy as np

# Create 1-D Numpy Array and get shape
np1 = np.arange(1,13)
print(np1)
print(np1.shape)

# Create 2-D Array and get Shape,(rows/columns)
np2 = np.arange(1,13).reshape(2,6)
print("2-D array",np2)
print("Shape:",np2.shape)

# Reshape 2-D
np3 = np1.reshape(3,4)
print("2-D array",np3)
print("Shape:",np3.shape)

# Reshape 3-D
np4 = np1.reshape(2,2,3)
print("Array : ",np4)
print("Shape : ",np4.shape)

# Flatten to 1-D
np5 = np4.reshape(-1)
print(np5)
print(np5.shape)

np6 = np4.flatten()
print(np6)
print(np6.shape)