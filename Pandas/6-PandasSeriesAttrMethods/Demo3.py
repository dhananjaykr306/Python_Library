# Pandas size attribute
# Code by Dhananjay

import pandas as pd

# Data
data =[10,20,30,40,50]

# Create a seies using the Series() method
s = pd.Series(data)

# Dispaly the Series
print("Series:\n",s)

# Displat the size of the series
print("\nSeries Size : ",s.size)