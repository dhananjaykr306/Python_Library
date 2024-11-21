# Drop columns using drop()
# code by Dhananjay

import pandas as pd

# Dataset

data = {
    'Id':['S01','S02','S03','S04','S05'],
    'Student':["Dhananjay","Amit","Rakesh","Shaurya","Nayan"],
    "Rank" :[1,2,3,4,5],
    "Marks":[90,70,80,85,98,]
}

df = pd.DataFrame(data)

print("Student Records : \n",df)

# Drop a column
res_df = df.drop("Marks",axis=1)
#res_df = df.drop("Marks",axis='columns')

# Result
print("\n DataFrame after deleting a column : \n",res_df)