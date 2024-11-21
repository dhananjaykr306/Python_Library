import numpy as np

# Search
np1 = np.array([1,2,3,4,5,6,7,8,9,10,3])
print(np1)

# where return tuple of index number
x = np.where(np1==3)
print("index of 3 : ",x)
print(x[0])
print(np1[x[0]])

# return even item
y = np.where(np1 % 2 ==0)
print(np1)
print(y[0])