# Pandas DataFrame Dtype attribute

# code by Dhananjay

import pandas as pd

# Dataset

data = {
    'Students':["Dhananjay","Survi","Amit","Shaurya","Lakshya"],
    'Marks':[70,80,78,68,98],
    'Rank':[1,2,3,4,5]
}

# create a Dataframe using DataFrame()
df = pd.DataFrame(data,index = ["Student1","Student2","Student3","Student4","Student5"])

print("Student Records\n\n",df)

print("\nDatatype:\n",df.dtypes)
