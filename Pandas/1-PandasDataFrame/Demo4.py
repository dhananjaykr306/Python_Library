# Name your index in a Pandas DataFrame

# code by Dhananjay

import pandas as pd

# Dataset
data = {
    'Student':["Amit","Dhananjay","Survi","Shaurya","Lakshya","Manish"],
    'Rank':[1,2,3,4,5,6],
    'Marks':[95,70,80,60,90,80]
}

# Use the index argument to set your indexes
df = pd.DataFrame(data,index=["Student1","Student2","Student3","Student4","Student5","Student6"])

print("DataFrame = \n",df)