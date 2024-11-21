# Drop row using drop()
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

#res_df = df.drop(2,axis='index')
res_df = df.drop(2,axis=0)

# Display the result
print("Updated Student Records after removing a row : \n",res_df)