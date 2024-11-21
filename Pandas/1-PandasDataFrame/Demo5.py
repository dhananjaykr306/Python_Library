# Iterate a Pandas DataFrame using for loop

# Code by Dhananjay

import pandas as pd

# Dataset
data = {
    'Student':["Amit","Dhananjay","Survi","Shaurya","Lakshya","Manish"],
    'Rank':[1,2,3,4,5,6],
    'Marks':[95,70,80,60,90,80]
}

# DataFrame

df = pd.DataFrame(data,index=["Student1","Student2","Student3","Student4","Student5","Student6",])

print("Student Records\n\n",df)
# Iterating
print("Displaying the columns :")
for cols in df:
    print(cols,sep = " ")