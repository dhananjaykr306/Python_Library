# Pandas head() method
# code by Dhananjay

import pandas as pd

# Data
data = [10,20,30,40,50,60,70,80,90,100]

# Create Seris using Series()
s = pd.Series(data,name="MyNumberSeries")

# Display the Series
print("Series : \n",s)

print("\nThe first 5 rows of the Series : \n",s.head())

print("\nThe first 7 rows of the Series : \n",s.head(7))