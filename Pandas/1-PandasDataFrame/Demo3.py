# Access a group of rows or columns by integer position in a pandas DataFrame

# code by Dhananjay

import pandas as pd

data = {
    'Student':["Amit","Dhananjay","Survi","Shaurya","Lakshya","Manish"],
    'Rank':[3,2,6,5,4,1],
    'Marks':[95,70,80,60,90,80]
}

df = pd.DataFrame(data,index=["RowA","RowB","RowC","RowD","RowE","RowF"])

print("Student Records : \n",df)

# Access using rows or columns by Integer positions
print("\nValues = \n",df.iloc[[1,2]])

print("\nValues = \n",df.iloc[[3,4]])