# Create a Pandas DataFrame
# Code by Dhananjay
import pandas as pd

# Datasets

data = {
    'Student':["Amit","Dhananjay","Survi","Shaurya","Lakshya","Manish"],
    'rank': [1,2,3,4,5,6],
    'marks' :[95,70,80,60,90,80]
}


df = pd.DataFrame(data)
print("Student Record \n : ",df)