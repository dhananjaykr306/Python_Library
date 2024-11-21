# Indexing in pandas using loc[:]\# code by Dhananjay

import pandas as pd

# input csv
# Load csv into dataframe

df = pd.read_csv("Students.csv",index_col="Students")
# Display the CSV file records
print("DataFrame : \n",df)

#Retrive a single row
print(df.loc["Dhananjay"])