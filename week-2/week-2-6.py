#case normalizaztion (lowecase/uppercase)
#python
#Sample dataset with inconsistent case

df = pd.DataFrame({
    'Name':['Alice','bob','CHARLIE','david','Eve']
                   })
#convert all to lowercase
df['Name_lower'] = df['Name'].str.lower()

#convert all to uppercase
df['Name_upper'] = df['Name'].str.upper()

print(df)