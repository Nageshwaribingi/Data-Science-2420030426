# records randomly from the dataset 
import pandas as pd 
data = pd.DataFrame({
    'Student':['A','B','C','D','E','F','G']
})
# randomly select 3 students 
sample = data.sample(n=3,random_state=1)
print("Simple Random Sample:")
print(sample)
print("#--------------------------------------------------------------------------------------#")
# systematic sampling 
import pandas as pd 
data = pd.DataFrame({
    'Student':['A','B','C','D','E','F','G','H','I','J']
})
systematic_sample = data.iloc [::2]
print("Systematic Sample:")
print(systematic_sample)
print("#--------------------------------------------------------------------------------------#")
# systematic sampling 
import pandas as pd 
data = pd.DataFrame({
    'Student':['A','B','C','D','E','F','G','H','I','J']
})
systematic_sample = data.iloc [::3]
print("Systematic Sample:")
print(systematic_sample)
print("#--------------------------------------------------------------------------------------#")
data = pd.DataFrame({
    'Student':['A','B','C','D','E','F','G','H','I'],
    'Department': ['MCA','MCA','BTech','BTech','MBA','MBA','MCA','BTech','MBA']
})
sample = data.groupby('Department').sample(n=3, random_state=2)
print("Stratified Sample:")
print(sample)
print("#------------------------------------------------------------------------------------------------------#")

# cluster sampling 
data = pd.DataFrame({
    'Student':['A','B','C','D','E','F'],
    'Class': ['C1','C1','C2','C2','C3','C3']
})
cluster_sample = data[data['Class']=='C2']
print("Cluster Sample:")
print(cluster_sample)
print("#------------------------------------------------------------------------------------------------------#")

# cluster sampling 
data = pd.DataFrame({
    'Student':['A','B','C','D','E','F'],
    'Class': ['C1','C1','C2','C2','C3','C3']
})
cluster_sample = data[data['Class']=='C1']
print("Cluster Sample:")
print(cluster_sample)
print("#------------------------------------------------------------------------------------------------------#")

#non probability 
import numpy as np 
data = np.arange(1,101)
sample_without_replacement = np.random.choice(data,size=10,replace=False)
sample_with_replacement = np.random.choice(data,size=10,replace=True)
print("Sample without replacement:")
print(sample_without_replacement)
print("Sample with replacement:")   
print(sample_with_replacement)
print("#------------------------------------------------------------------------------------------------------#")
