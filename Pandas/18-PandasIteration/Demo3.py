# Pandas items() to iterate over columns
# Code by Dhananjay

import pandas as pd

# Datasets

data = {
    'Id':["S01","S02","S03","S04","S05"],
    'Student':["Amit","Dhananjay","Shaurya","Lakshya","Survi"],
    "Rank":[1,2,3,4,5]
}

df = pd.DataFrame(data)

# Display the dataframe
print("Student Record : \n",df)

# iterate over columns
for a,b in df.items():
    print(a)
    print(b)