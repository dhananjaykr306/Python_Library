# Pandas DataFrame index attribute
# code by Dhananjay

import pandas as pd 

# Datasets

data = {
    'Students':["Dhananjay","Survi","Amit","Shaurya","Lakshya"],
    'Marks':[70,80,78,68,98],
    'Rank':[1,2,3,4,5]
}

df = pd.DataFrame(data,index= ["RowA","RowB","RowC","RowD","RowE"])

print("\nStudents Record : \n",df)

# Return the index of df
print("\nDataFrame index",df.index)