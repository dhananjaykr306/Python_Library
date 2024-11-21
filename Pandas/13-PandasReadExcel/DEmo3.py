# Display the last n row of the DataFrame in pandas
# Code by Dhananjay

import pandas as pd

# input the Excel file
# Load the excel file

df = pd.read_excel("odi.xlsx")

# Display the last 5 rows
print("Display last 5 rows : \n",df.tail())
# Display the top 2 rows 
print("Displat the last 2 row : \n",df.tail(2))