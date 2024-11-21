# pandas tail() method
# code by Dhananjay

import pandas as pd

# Data
data =[10,20,30,40,50,60,70,80,90,100]

# Create pandas series using series()
s = pd.Series(data,name="MySeriesNumber")

# Display the Series
print("Series : \n",s)

print("\nThe last 5 row of the Series \n",s.tail())
print("\nThe last 7 row of the Series \n",s.tail(7))