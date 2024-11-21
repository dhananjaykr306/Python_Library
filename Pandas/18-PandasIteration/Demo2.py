# Pandas iterrows() to iterate over rows
# code by Dhananjay

import pandas as pd

# Datasets
data ={
    'Id':["S01","S02","S03","S04","S05"],
    'Student':["Dhananjay","Shaurya","Amit","Lakshya","Survi"],
    'rank':[1,2,3,4,5],
}

df = pd.DataFrame(data)
print("Student Records : \n",df)

# Iterate over rows using itertuple()
print("\n Display the rows : \n")
for row in df.itertuples():
    print("\n",row)