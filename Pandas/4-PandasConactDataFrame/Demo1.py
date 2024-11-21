# Concatenate two Pandas DataFrame
# Code by Dhananjay

import pandas as pd

# Dataset
data1 = {
    "Id":["S01",'S02','S03','S04','S05'],
    'Student':["Dhananjay","Shaurya","Amit","Survi","Lakshya"],
    "Roll":[101,102,103,104,105]
}

data2 = {
    "Id":["S06","S07","S08"],
    "Student":["Manish","Aman","Dhruv"],
    "Roll":[106,107,108]
}

# DataFrame

dataframe1 = pd.DataFrame(data1,index=["Student1","Student2","Student3","Student4","Student5"])

dataframe2 = pd.DataFrame(data2,index=["Student6","Student7","Student8"])

print("DataFrame1 : \n",dataframe1)
print("\nDataFrame2 : \n",dataframe2)

# concatenate two DataFrame
res_df = pd.concat([dataframe1,dataframe2])
print("concatenated Dataframe : \n",res_df)