# Access group of row or columns in a Pandas DataFrame

# code by Dhananjay

import pandas as pd

data = {
    'Student':["Amit","Dhananjay","Survi","Shaurya","Lakshya","Manish"],
    'Rank':[1,2,3,4,5,6],
    'Marks':[95,70,80,60,90,80]
}

df = pd.DataFrame(data, index = ["RowA","RowB","RowC","RowD","RowE","RowF"])

print("Student Record : \n",df)

# accessing the values in the student column corresponding to the RowA label
print("\nvalues = ",df.loc['RowA','Student'])
print("\nValues =",df.loc['RowA','Marks'])