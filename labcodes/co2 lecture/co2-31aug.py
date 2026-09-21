# Scatter Plot 
import matplotlib.pyplot as plt
import pandas as pd 
df = pd.read_csv("temporal.csv")
plt.scatter(df['deep learning'],df['machine learning'],color='red',marker="*")
plt.title('Scatter Plot')
plt.xlabel("Deep Learning")
plt.ylabel("Machine Learning")
plt.grid()
plt.show()

#--------------------------------------------------------------------------------------#

import matplotlib.pyplot as plt
import pandas as pd 
df = pd.read_csv("temporal.csv")
plt.scatter(df['deep learning'],df['machine learning'],color='red',marker="^")
plt.title('Scatter Plot')
plt.xlabel("Deep Learning")
plt.ylabel("Machine Learning")
plt.grid()
plt.show()

#--------------------------------------------------------------------------------------#
values =[5,6,3,7,2]
names =["A","B","C","D","E"]
plt.bar(names,values,color='red')
plt.title('Bar Graphs')
plt.xlabel("Names")
plt.ylabel("Values")
plt.show()

#--------------------------------------------------------------------------------------#
values =[5,6,3,7,2]
names =["A","B","C","D","E"]
plt.barh(names,values,color='green')
plt.title('Bar Graphs')
plt.xlabel("Names")
plt.ylabel("Values")
plt.show()
#--------------------------------------------------------------------------------------#
values =[5,6,3,7,2]
names =["A","B","C","D","E"]
c1 = ['red','green']
c2 =['b','g','y']
plt.bar(names,values,width=0.5,color=c1)
plt.show()
plt.bar(names,values,width=0.5,color=c2)
plt.show()
#--------------------------------------------------------------------------------------#
df = pd.read_csv("temporal.csv")
plt.bar(df['deep learning'],df['machine learning'],color='red')
plt.title('Bar Graph')
plt.xlabel("Deep Learning")
plt.ylabel("Machine Learning")
plt.show()
#--------------------------------------------------------------------------------------#
import seaborn as sns 
data = sns.load_dataset("iris")
sns.lineplot(x="sepal_length",y="sepal_width",data=data)
#--------------------------------------------------------------------------------------#
data = sns.load_dataset("tips")
sns.boxplot(data['total_bill'])