# combine two Pandas Series
# code by Dhananjay

import pandas as pd

# Data
data1 = [10,20,30,40,50]
data2 = [25,5,75,95,45]

# Craete a series using the Series() method
series1 = pd.Series(data1)
series2 = pd.Series(data2)

# Display the Series
print("Series1 :\n",series1)
print("Series2 :\n",series2)

def demo(x1,x2):
    if x1>x2:
        return x1
    else:
        return x2

# combine two series into one
# The function return the largest value

res = series1.combine(series2,demo)

# Display the result
print("\nAfter combining\n",res)