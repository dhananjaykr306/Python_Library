# Pandas DataFrame size attribute
# code by Dhananjay

import pandas as pd

# Dataset

data = {
    'Students':["Dhananjay","Survi","Amit","Shaurya","Lakshya"],
    'Marks':[70,80,78,68,98],
    'Rank':[1,2,3,4,5]
}

df = pd.DataFrame(data,index=["RowA","RowB","RowC","RowD","RowE"])

print("\nStudent Records : \n",df)
# size of DataFrame
print("\nNumber of elements : ",df.size)