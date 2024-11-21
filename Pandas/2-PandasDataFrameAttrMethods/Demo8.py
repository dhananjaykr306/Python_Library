# Pandas DataFrame tail() method
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
# Return the last five row of DataFrame
print("\nlast 5 row : \n",df.tail())
print("\nlast 2 row : \n",df.tail(2))