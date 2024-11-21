# Display the top n rows
# code by Dhananjay

import pandas as pd

# input the csv file
# Loading the DataFrame
df = pd.read_csv("students.csv")

# return top n rows
print(df.head(5))