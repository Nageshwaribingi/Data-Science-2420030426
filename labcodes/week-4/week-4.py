#--------------------------------------------------------------------------------------#
# AUGUST 26 2026 

import seaborn as sns 
tips = sns.load_dataset("tips")
print(tips.head())

#--------------------------------------------------------------------------------------#
#define the problem 
# predict whether a passanger survived the titanic disaster based on features 
objective = "Classificatiion: Survived (Yes/No)"
success_criteria = "Accuracy > 80%"
constraints = "Limited featues, missing values, imbalanced classes"
print("Objective:",objective)
print("Success Criteria:",success_criteria)
print("Constraints:",constraints)
#--------------------------------------------------------------------------------------#
#Data cleaning and preprocessing 
#handle missing values 
df = sns.load_dataset("titanic")
import pandas as pd 
#FIll missing values 
df['age'].fillna(df['age'].median(),inplace=True)
df['embarked'].fillna(df['embarked'].mode()[0],inplace=True)
#drop duplicates
df.drop_duplicates(inplace=True)
#Encode catergorical variables
df = pd.get_dummies(df,columns=['sex','class','embarked'],drop_first=True)
#Feature engineering : family size 
df['family_size']=df['sibsp'] + df['parch']
print(df.head())

#--------------------------------------------------------------------------------------#
#Exploratory Data Analysis (EDA)
import matplotlib.pyplot as plt 
df = sns.load_dataset("titanic")
#Histogram of age 
sns.histplot(df['age'],bins=20,kde=True)
plt.title("Age Distraction")
plt.show()
#--------------------------------------------------------------------------------------#
import seaborn as sns 
import matplotlib.pyplot as plt 
df=sns.load_dataset("tips")
# Histogram of age
sns.histplot(df['size'],bins=10,kde=True)
plt.title("Age Distribution")
plt.show()
#--------------------------------------------------------------------------------------#
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
corr = df.corr(numeric_only=True)
print(corr)
sns.heatmap(corr,annot=True,cmap="coolwarm")
plt.title("Correlation Matix")
plt.show()