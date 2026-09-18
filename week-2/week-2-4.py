#remove duplicates
import pandas as pd
import numpy as np

#sample dataset
df = pd.DataFrame({
    'ID': [1, 2,2, 3, 4, 4],
    'Name': ['Alice', 'Bob', 'Bob', 'Charlie', 'David', 'David'],
    'Age': [25, 30, 30, 35, 40, 40],
})

print("Original dataset (with duplicates):")
print(df)

#remove duplicates
df_exact = df.drop_duplicates()
print("\nDataset after removing duplicates:")
print(df_exact)

#------------------------------------------------------------------------------------------------------------------------------------#

#Subset based removal 
#remove duplicates based on specific key columns (eg. ID and Name)
#remove duplicates based only on ID
print("Original dataset (with duplicates):")
print(df)

df_subset_id = df.drop_duplicates(subset=['ID'])
print("\nDataset after removing duplicates based on ID:")
print(df_subset_id)

#remove duplicates based on Name
df_subset_name = df.drop_duplicates(subset=['Name'])
print("\nDataset after removing duplicates based on Name:")
print(df_subset_name)