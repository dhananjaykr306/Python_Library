# join DataFrame in Pandas
# Code by Dhananjay

import pandas as pd

# Datasets
data1 = {
    'Id':["S01","S02","S03","S04","S05"],
    "Student":["Amit","Dhananjay","Survi","Shaurya","Lakshya"],
    "Roll":[101,102,103,104,105]
}

data2 = {
    'Rank':[1,2,3,4,5],
    'Marks':[95,70,80,60,90]
}

# DataFrame
dataframe1 = pd.DataFrame(data1)
print("DataFrame1 : \n",dataframe1)

dataframe2 = pd.DataFrame(data2)
print("DataFrame2 : \n",dataframe2)

# join dataframe
res_df = dataframe1.join(dataframe2)
print("Resultanat DataFrame : \n",res_df)