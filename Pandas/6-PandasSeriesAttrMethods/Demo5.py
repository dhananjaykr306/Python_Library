# pandas hasnan attributes
# code by Dhananjay

import pandas as pd
import numpy as np

# Data
data = [10,20,30,40,50,np.nan]

# Create a Series using the Series() method
s = pd.Series(data,name="MyNumberSeries")

# Display the Series
print("Series : \n",s)

# Return the nan attribute
print("\nDoes the Series has Nan?",s.hasnans)