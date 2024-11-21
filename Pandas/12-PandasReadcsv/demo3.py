# Display the last n row of dataframe in pandas
# code by Dhananjay
import pandas as pd
# Input CSV file
# Loading CSV in DataFrame
df = pd.read_csv("students.csv")

# Display the csv file records
print("Our DataFrame =\n",df)

# Display the top n rows
print("\n last 5 rows\n",df.tail())
print("\nLast 2 row\n",df.tail(2))