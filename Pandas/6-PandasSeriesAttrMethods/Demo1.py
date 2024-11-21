# pandas dtype attribute
# code by Dhananjay

import pandas as pd

# Data
data =[10,20,30,40,50]

# Create a Series using Series() methods
s = pd.Series(data)

# Display the Series
print("\nSeries :\n",s)

# Display the datatype of Series
print("\nDatatype of the Series : ",s.dtype)