# Pandas DataFrame head() method
# code by Dhananjay

import pandas as pd

# Datasets

data = {
    'Student':['Dhananjay','Amit','Survi','Shaurya','Lakshya',"Manish"],
    'Marks':[70,80,68,78,98,98],
    'Ranks':[1,2,3,4,5,6]
}

# creating the DataFrame using the DataFrame() method

df = pd.DataFrame(data,index=["Row1","Row2","Row3","Row4","Row5","Row6"])
print("\n\nStudent Records:\n",df)
# Return the first five row of DataFrame
print("\nfirst 5 row : \n",df.head())
print("\nfirst 2 row : \n",df.head(2))