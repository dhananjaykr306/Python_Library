# Remove Duplicate using drop_duplicate()
# Code by Dhananjay

import pandas as pd

#Dataset
data = {
    "Student":["Amit","Dhananjay","Amit","Survi","Shaurya"],
    "Rank":[1,4,1,5,4],
    "Marks":[90,70,90,60,90]
}

# Create the DataFrame
df = pd.DataFrame(data)
print("\nStudent Records : \n",df)
# remove the duplicate
res = df.drop_duplicates()
print("\nnew DataFrame after deleting duplicate : \n",res)
