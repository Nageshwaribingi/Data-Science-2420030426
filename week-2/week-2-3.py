#drop rows with missing values
#python
import pandas as pd
import numpy as np
df = pd.DataFrame({'Age':[25,30,np.nan,35,40],'Department':['HR','Finance','Finance',np.nan,'IT']})

#display original dataset
print("Original dataset (with missing values):")
print(df)

#drop rows with missing values
df_drop_rows = df.dropna()
print("\nDataset after dropping rows with missing values:")
print(df_drop_rows)

#drop columns with missing values
df_drop_cols = df.dropna(axis=1)
print("\nDataset after dropping columns with missing values:")
print(df_drop_cols)

