# Name your own indexes in pandas series
# code by Dhananjay

import pandas as pd

# Data
data = [10,20,30,40,50]

# Create a Series Using the Series() method
s = pd.Series(data, index = ["RowA","RowB","RowC","RowD","RowE",])

# Display the Series
print("\n Series(With the custom index) \n",s)