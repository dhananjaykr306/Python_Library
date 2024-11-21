# Pandas DataFrame Shape attribute
# code by Dhananjay

import pandas as pd

# Datasets

data = {
    'Student':["Dhananjay","Amit","Survi","Shaurya","Lakshya"],
    "Marks":[70,80,78,68,98],
    "Ranks":[1,2,3,4,5]
}

df = pd.DataFrame(data,index=["RowA","RowB","RowC","RowD","RowE"])

print("\nStudent Records : \n",df)
# return the dimensionality of DataFrame in a tuple form
print("\nShape of DataFrame : ",df.shape)