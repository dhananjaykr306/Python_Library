# pandas name attribute
# code by Dhananjay

import pandas as pd

# Data
data =[10,20,30,40,50]

# Create Series using Series()
s = pd.Series(data,name = "MyNumberSeries")

# Display the Series
print("Series : \n",s)

# Display the name attribute
print("\nSeries Name : ",s.name)