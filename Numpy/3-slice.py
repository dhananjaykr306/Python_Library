import numpy as np

# Slicing Numpy Arrays

np1 = np.array([1,2,3,4,5,6,7,8,9])
print(np1)

# Return 2,3,4,5

print(np1[1:5])

# Return from something till the end of the array?
print(np1[3:])

# Return Negative Slices
# 7,8
print(np1[-3:-1])

# Steps
print(np1[1:5]) # 2,3,4,5
print(np1[1:5:2])# 2,4

# Steps of 2 on the entire array
print(np1[::2]) # 1,3,5,7,9

# Steps of 3 on the entire array
print(np1[::3])

# slice a 2-D array
np2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# pull out single item
# 8
print(np2[1,2])

# Slice a 2-D array 2,3
print(np2[0:1,1:3])

# slice a 2-D array [[2,3],[7,8]]
print(np2[:,1:3])