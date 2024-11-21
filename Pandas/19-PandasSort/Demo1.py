# sort the pandas DataFrame(default ascending order)
# code by Dhananjay

import pandas as pd

# Dataset
data ={
    "Student":["Dhananjay","Amit","Survi","Shaurya","Lakshya"],
    "Marks":[95,90,25,82,95],
    "Rank":[1,3,5,4,1]
}

# Create a DataFrame
df = pd.DataFrame(data,index=["RowA","RowB","RowC","RowD","RowE"])

# Display the Record
print("Student Records : \n",df)

# Sort in ascending order
print(df.sort_values(by=['Rank','Student']))
