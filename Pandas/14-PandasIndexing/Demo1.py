# indexing in Pandas using the indexing operator
# code by Dhananjay

import pandas as pd

# load csv
# Load the csv into the DataFrame

df = pd.read_csv("students.csv",index_col= "Students")

# Display the Dataframe
print("DataFrame Records : \n",df)

print("Student marks : \n",df["Marks"])