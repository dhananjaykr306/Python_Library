# Display the top n row of the DataFrame in pandas
# Code by Dhananjay

import pandas as pd

# input the Excel file
# Load the excel file

df = pd.read_excel("odi.xlsx")

# Display the top 5 rows
print("Display top 5 rows : \n",df.head())
# Display the top 2 rows 
print("Displat the top2 row : \n",df.head(2))