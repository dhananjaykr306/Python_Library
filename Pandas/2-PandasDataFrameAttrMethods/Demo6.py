# pandas DataFrame T attribute
# code by Dhananjay

import pandas as pd

# Dataset
data = {
    'Student':['Dhananjay','Amit','Survi','Shaurya','Lakshya'],
    'Marks':[70,80,78,68,98],
    'Ranks':[1,2,3,4,5]
}

# Creating DataFrame from DataFrame() method
df = pd.DataFrame(data,index=["RowA","RowB","RowC","RowD","RowE"])
print("\nStudent Records :\n",df)
# Return the transpose of DataFrame
print("\nTranspose of DataFrame\n",df.T)