import pandas as pd 
df = pd.DataFrame({
    'Study_hours':[2,4,6,8,10],
    'Marks':[20,40,60,80,100]
})

correlation = df['Study_hours'].corr(df['Marks'])
print("Correlation coefficient",correlation)
print("#--------------------------------------------------------------------------------------#")
df = pd.DataFrame({
    'Study_hours':[2,4,6,8,10],
    'Marks':[20,40,60,80,100]
})

covariance= df['Study_hours'].cov(df['Marks'])
print("Covariance",covariance)