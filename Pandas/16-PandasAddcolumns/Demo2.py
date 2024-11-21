# add a new column to pandas Dataframe using the assign() method
# Code by Dhananjay

import pandas as pd

# Dataset
data = {
    'Id':['S01','S02','S03','S04','S05'],
    'Students':["Dhananjay","Kumar","Shaurya","Rakesh","Nayan"],
    "Rank":[1,2,3,4,5],
    'Marks':[70,80,90,65,80]
}

df = pd.DataFrame(data)
#Display
print("Student Records : \n",df)

# Insert a new column with insert()
df.assign(Roll=[101,102,103,105,104])
# updated DataFrame
print("\nUpdated DataFrame : \n",df)