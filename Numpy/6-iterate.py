import numpy as np

# 1-d 
'''
np1 = np.array([1,2,3,4,5,6,7,8,9,10])
for x in np1:
    print(x)
'''

# 2-d Array
'''
np2 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
for x in np2:
    # Print rows
    for y in x:
        # print element in row
        print(y)
'''

# 3-D array
np3 = np.arange(1,13).reshape(2,2,3)
print(np3)
'''
np4 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(np4)

for x in np3:
    for y in x:
        for z in y:
            print(z,sep="\t")
'''

# Use np.nditer()
for x in np.nditer(np3):
    print(x,sep=" ")