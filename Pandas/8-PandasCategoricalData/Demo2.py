# create Categorical DataFrame in Pandas
# Code by Dhananjay

import pandas as pd

# Create a categorical DataFrame
df = pd.DataFrame({"cat1":list("pqrs"),"cat2":list("abcd"),"cat1":list("xyzw")})

# Display the DataFrame
print("Categorical DataFrame : \n",df)

# Display the datatype 
print("\nDatatype of each column\n",df.dtypes)