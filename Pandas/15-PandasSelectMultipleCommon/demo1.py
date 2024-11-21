import pandas as pd

# Dataset 
data = {
    "Student" : ["Amit","Dhananjay","Dhananjay","Lakshya","Survi"],
    "Ranks" :[1,2,3,4,5,],
    "Marks" : [95,65,88,79,95]
}

df = pd.DataFrame(data)

x = df[["Ranks",'Marks']]

print("Student Record : \n",df)
print("\nSelecting only two columns : \n",df[["Ranks",'Marks']])
print("-----------------------------------------------")

print(x)