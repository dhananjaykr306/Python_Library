# Sort the Pandas DataFrame in descending order
# code by Dhananjay

import pandas as pd

# Datasets
data = {
    'Student':["Dhananjay","Shaurya","Amit","Lakshya","Survi"],
    'Marks':[86,85,98,78,56],
    'Rank':[2,3,1,4,5]
}

# Create a DataFrame
df = pd.DataFrame(data,index=["RowA","RowB","RowC","RowD","RowE"])

#Display the DataFrame
print("\nStudent Record :\n",df)

#sort in descending order
print("Sorted DataFrame in descending order based on Rank :\n",df.sort_values(by=['Rank'],ascending=False))

