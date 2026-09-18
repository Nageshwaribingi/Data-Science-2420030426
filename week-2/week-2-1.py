#forward fill (use previous values)
#python
import pandas as pd
import numpy as np
df = pd.DataFrame({'Age':[25,30,np.nan,35,40],'Department':['HR','Finance','Finance',np.nan,'IT']})

#display original dataset
print("Original dataset (with missing values):")
print(df)
df_ffill = df.copy()
df_ffill.ffill(inplace=True)
print(df_ffill)