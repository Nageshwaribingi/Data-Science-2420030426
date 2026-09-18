import pandas as pd 
#dataframes is a collection of series 
data = {'apples':[3,2,0,1],'oranges':[0,3,7,2]}
df = pd.DataFrame(data)
print(df)

df = pd.DataFrame(data,index=['Ahmed','Ali','Rashed','Hamza'])
print(df.loc['Ali'])

data = {'col_1':[1,2,3,4],'col_2':['A','B','C','D']}
df = pd.DataFrame.from_dict(data)

data = {'row_1':[1,2,3,4],'row_2':['A','B','C','D']}
df = pd.DataFrame.from_dict(data,orient='index')
print(df)

data = {'row_1':[1,2,3,4],'row_2':['A','B','C','D']}
df = pd.DataFrame.from_dict(data,orient='index',columns=['A','B','C','D'])
print(df)

df = pd.read_csv('Iris.csv')
print(df)

#or

df = pd.read_csv('Iris.csv',index_col=0)
print(df)

print(df.head())
print(df.tail(2))
print(df.info())
print(df.shape)