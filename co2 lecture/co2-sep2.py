import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = sns.load_dataset("tips")

sns.boxplot(y=data["total_bill"])

plt.show()

#--------------------------------------------------------------------------------------#
import pandas as pd
df = pd.read_csv("temporal.csv")
df
sns.boxplot(df['data science'])
plt.show()

import pandas as pd
df = pd.read_csv("temporal.csv")
df
sns.boxplot(df['deep learning'])
plt.show()

import pandas as pd
df = pd.read_csv("temporal.csv")
df
sns.boxplot(df['machine learning'])
plt.show()
#--------------------------------------------------------------------------------------#
# @title default title text 
df = pd.read_csv("temporal.csv")
df
Q1 = np.percentile(df['data science'], 25, interpolation = 'midpoint')
Q3 = np.percentile(df['data science'], 75, interpolation = 'midpoint')
IQR = Q3 - Q1
print("the out put of IQR")
print(IQR)

""""
the out put of IQR
20.5
"""
#--------------------------------------------------------------------------------------#
# @title default title text 
df = pd.read_csv("temporal.csv")
df
Q1 = np.percentile(df['data science'], 25, interpolation = 'midpoint')
Q3 = np.percentile(df['data science'], 75, interpolation = 'midpoint')
IQR = Q3 - Q1
print("the out put of IQR")
print(IQR)
upper = Q3 + 1.5 * IQR
upper_array = np.array(df['data science'] >= upper)
print("Upper Bound:", upper)
print(upper_array.sum())

#Below lower bound
lower = Q1 - 1.5 * IQR
lower_array = np.array(df['data science'] <= lower)
print("Lower Bound:", lower)
print(lower_array.sum())
#--------------------------------------------------------------------------------------#
# seaborn heatmaps
# generating a 10x10 matrix of random numbers
data = np.random.randint(1,100,(10,10))
sns.heatmap(data)
plt.show()
#--------------------------------------------------------------------------------------#

data = np.random.randint(1,100,(10,10))
sns.heatmap(data,vmin=30,vmax=70)
plt.show()
#--------------------------------------------------------------------------------------#

data = np.random.randint(1,100,(10,10))
sns.heatmap(data,cmap='tab20')
plt.show()
#--------------------------------------------------------------------------------------#

data = np.random.randint(1,100,(10,10))
sns.heatmap(data,cmap='tab20',annot=True)
plt.show()
#--------------------------------------------------------------------------------------#

data = np.random.randint(1,100,(10,10))
sns.heatmap(data,cmap='coolwarm',center=50,annot=True)
plt.show()
#--------------------------------------------------------------------------------------#
data = [12,15,20,20,22,23,25,25,25,30,32,35,40]
plt.hist(data,bins=5,color='skyblue',edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value Range')
plt.ylabel('Frequency')
plt.show()
#--------------------------------------------------------------------------------------#
data = sns.load_dataset("tips")
plt.hist(data['total_bill'],bins=10,color='skyblue',edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value Range')
plt.ylabel('Frequency')
plt.show()
#--------------------------------------------------------------------------------------#
df = sns.load_dataset('iris')
sns.violinplot(x='species',y='petal_length',data=df)
plt.title('Violin Plot')
plt.show()
#--------------------------------------------------------------------------------------#
#Dashboards using python 
