# Create Categorical Series in Pandas
# Code by Dhananjay

import pandas as pd

# Create a Categorical Series
#s = pd.Series(["p","q","r","s","t"],dtype="category")
s = pd.Series(["p","q","r","s","p"],dtype="category")


# Display the Series
print("Categorical Series : \n",s)

# Append a Category
s =s.cat.add_categories("t")

# Display the updated category
print("\nUpdated Categories\n",s)