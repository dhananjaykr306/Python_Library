# Select multiple columns in a range with pandas
# Code by Dhananjay

import pandas as pd

# Datasets
data ={
    'Id' :["S01",'S02','S03','S04','S05'],
    "Students":["Dhananjay","Amit","Nayan","Shaurya","Survi"],
    "Rank":[1,2,3,4,5],
    "Marks":[95,70,80,60,90],
    "Address":["East","West","South","North","Central"]
}

df = pd.DataFrame(data)

print("DataFram :\n",df)

print("\n Selecting columns in range : [3-5]\n",df[df.columns[2:5]])