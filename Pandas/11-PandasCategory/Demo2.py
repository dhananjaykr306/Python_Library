# Remove Categories in Pandas
# Code by Dhananjay

import pandas as pd

# Create a Categorical Series
s = pd.Series(["p","q","r","s","t"],dtype="category")

# Display the series
print("Series : ",s)

s=s.cat.remove_categories("r")

# Display the updated category
print("Updated Series : \n",s)