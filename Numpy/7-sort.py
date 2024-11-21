import numpy as np

# np.sort()  Numerical

np1 = np.array([6,7,4,9,0,2,1])
print(np1)

#np1=sorted(np1,reverse=True)
print(np.sort(np1))


# Alphabetical

np2 = np.array(["John","Tina","Aaron","Zed"])
print(np2)
print(np.sort(np2))

# Boolean T/F
np3 = np.array([True,False,True,False,False,True,True])
print(np3)
print(np.sort(np3))

print("Original np1 : ",np1)
print("sorted np1 : ",np.sort(np1))
print("np1 : ",np1)

# 2-D
np4 =np.array([[6,7,1,9],[8,3,5,0]])
print(np.sort(np4))