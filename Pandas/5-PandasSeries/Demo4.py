# access a value from a pandas Series with labels
# code by Dhananjay

import pandas as pd

# data
data =[10,20,30,40,50]

# Create a Series using the Series() methods
s = pd.Series(data,index = ["RowA","RowB","RowC","RowD","RowE"])

# Display the Series
print("\n Series (with custom index labels)\n",s)

# Access a value reffering the label
print("Accessing the value of RowD using index : ",s["RowD"])