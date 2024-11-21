import numpy as np

# Numpy Universal function
np1 = np.array([-3,-2,-1,0,1,2,3,4,5,6,7,8,9])
print(np1)

# print square root of np1 array
np.set_printoptions(precision=3)
print(np.sqrt(np1))

# Absolute value
print(np1)
print(np.absolute(np1))

# Exponents
print(np.exp(np1))

# Min/max
print(np1)
print("min : ",np.min(np1))
print("max : ",np.max(np1))

# sign positive or negative
print(np1)
print(np.sign(np1))

# Trigonometry
print(np1)
print("sin : ",np.sin(np1))
print("cos : ",np.cos(np1))
print("tan : ",np.tan(np1))
print("log : ",np.log(np1))
print(np.log(2.72))