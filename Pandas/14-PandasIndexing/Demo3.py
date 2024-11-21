# Indexing in pandas using iloc[:]\# code by Dhananjay

import pandas as pd

# input csv
# Load csv into dataframe

df = pd.read_csv("Students.csv",index_col="Students")
# Display the CSV file records
print("DataFrame : \n",df)

#Retrive row 3 records
res = df.iloc[2]
print("\n",res)