# Pandas info() method
# code by Dhananjay

import pandas as pd

# Data
data = [10,20,30,40,50]

# Create a Series using the Series() method
s = pd.Series(data, index=["Num1","Num2","Num3","Num4","Num5"],name = "MyNumberSeries")

# Display the Series
print("Series :\n",s)

# Return the info of the series
print("\nSeries Summary: \n",s.info())