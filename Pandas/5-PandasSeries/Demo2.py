# access the value from pandas series
# code by Dhananjay

import pandas as pd

# Data
data =[10,20,30,40,50,60]

# Create a pandas series using Series() method
s = pd.Series(data)

print("Series : \n",s)

# Access the value
print("\nValue from a Pandas Series : \n",s[2:])