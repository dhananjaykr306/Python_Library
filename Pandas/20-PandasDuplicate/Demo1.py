# Find the duplicate using the duplicated()
# code by Dhananjay
import pandas as pd

# Dataset
data ={
    'Student':["Amit","Dhananjay","Amit","Shaurya","Survi"],
    "Rank":[1,4,1,5,3],
    "Marks":[95,70,95,60,90]
}

df = pd.DataFrame(data)

print("Student Records : \n",df)

# find the dupliactes
res = df.duplicated()
print("Describing Duplicate : \n",res)
duplicates = df[res]
print("\nDuplicate Records: \n", duplicates)