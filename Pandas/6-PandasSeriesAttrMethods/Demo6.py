# Pandas index attribute
# Code by Dhananjay

import pandas as pd

# Data
data = [10,20,30,40,50,60]

# Craete the Series using Series()
s = pd.Series(data,index=["RowA","RowB","RowC","RowD","RowE","RowF"],name="MyNumberSeries")

# Display the Series
print("Series : \n",s)

# Display the index attrobute of Series
print("index of the Series : \n",s.index)