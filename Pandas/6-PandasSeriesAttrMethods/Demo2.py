# Pandas ndim attribute
# Code by Dhananjay

import pandas as pd

# Data 
data = [10,20,30,40,50,60]

# Create Series using Series()
s = pd.Series(data,index=["RowA","RowB","RowC","RowD","RowE","RowF"])

# Display the Series
print("\nSeries : \n",s)

#Display the ndim of series
print ("\nSeries Dimension\n",s.ndim)