import numpy as np
"""list1 = [1,2,3,4,5]
print(list1)
print(list1[0])

list2 = ["John Elder",41,[1,2,3,4,5],True]
print(list2)
"""
# Numpy - Numeric Python

# ndarray = n- dimension array

np1 = np.array([0,1,2,3,4,5,6,7,8,9])
print(np1)

print(np1.shape)

# Range
np2 = np.arange(10)
print(np2)

#Step

np3 = np.arange(0,10,2)
print(np3)

# zeros
np4 = np.zeros(10)
print(np4.shape)
print(np4)
# 2 Dimensional
np5 = np.zeros((2,10))
print(np5)
print(np5.shape)
# 3 Dimensional
np6 = np.zeros((2,2,10))
print(np6)
print(np6.shape)

# Full
np7 = np.full((10),7)
print(np7)
print(np7.shape)

# multidimensional full
np8= np.full((2,10),8)
print(np8)
print(np8.shape)

# Convert Python list to np
my_list = [1,2,3,4,5,6,7,8,9]
a = np.array(my_list)
print(a)

print(np8[0][1])