import matplotlib
matplotlib.__version__

import matplotlib.pyplot as plt 
import pandas as pd
x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.plot(x,y)
plt.show()

#--------------------------------------------------------------------------------------#

plt.title("Line Graph")
plt.plot(x,y)
plt.show()

#--------------------------------------------------------------------------------------#
plt.title("Line Graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot(x,y)
plt.show()

#--------------------------------------------------------------------------------------#

y1 =[]
y2=[]
x = range(-100,100,10)
for i in x :
    y1.append(i**2)
for i in x :
    y2.append(i**2)
plt.plot(x,y1)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title('simple graph')
plt.axhline()
plt.show()

#--------------------------------------------------------------------------------------#

y1 =[]
y2=[]
x = range(-100,100,10)
for i in x :
    y1.append(i**2)
for i in x :
    y2.append(i**2)
plt.plot(x,y1)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title('simple graph')
plt.axvline()
plt.show()

#--------------------------------------------------------------------------------------#

y1 =[]
y2=[]
x = range(-100,100,10)
for i in x :
    y1.append(i**2)
for i in x :
    y2.append(-i**2)
plt.plot(x,y1)
plt.plot(x,y2)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title('simple graph')
plt.axvline()
plt.axhline()
plt.savefig("linegraph.jpg")
plt.show()

#--------------------------------------------------------------------------------------#

y1 =[]
y2=[]
x = range(-100,100,10)
for i in x :
    y1.append(i**2)
for i in x :
    y2.append(-i**2)
plt.plot(x,y1)
plt.plot(x,y2)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title('simple graph')
plt.axvline(color='red')
plt.axhline(color='green')
plt.show()

#--------------------------------------------------------------------------------------#
df = pd.read_csv("temporal.csv")
plt.plot(df['deep learning'],df['machine learning'],color='red')
plt.xlabel('deep learning')
plt.ylabel('machine learning')
plt.title('line plot')
plt.show()
#--------------------------------------------------------------------------------------#

df = pd.read_csv("temporal.csv")
plt.plot(df['data science'],df['deep learning'],color='green')
plt.xlabel('data science')
plt.ylabel('deep learning')
plt.title('line plot')
plt.show()

#--------------------------------------------------------------------------------------#
plt.plot(df['Mes'],df['data science'],label='data science')
plt.plot(df['Mes'],df['machine learning'],label='machine learning')
plt.plot(df['Mes'],df['deep learning'],label='deep learning')
plt.xlabel("Date")
plt.ylabel('Popularity')
plt.title('popularity of AI terms by date')
plt.grid(True)
plt.legend()