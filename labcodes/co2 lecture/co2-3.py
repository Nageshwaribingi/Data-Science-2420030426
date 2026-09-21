import matplotlib.pyplot as plt 
import pandas as pd
df = pd.read_csv("Temporal.csv")
x_values = [0,1,2,3,4,5]
y_values=[0,1,4,9,16,25]
plt.scatter(x_values,y_values,color='blue')
plt.title('scatter plot')
plt.show()