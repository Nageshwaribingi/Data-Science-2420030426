import pandas as pd 
from sklearn.preprocessing import MinMaxScaler
#Example dataset 
data = pd.DataFrame({
    'A': [10,20,30,40,50],
    'B': [5,15,25,35,45],
})
print(data)
#Apply Min-Max Normalization
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(data)

# Convert back to DataFrame
normalized_df = pd.DataFrame(normalized_data, columns=data.columns)

print("Normalized Data (Min-Max Scaling):")
print(normalized_df)

print("#--------------------------------------------------------------------------------------#")

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
standardized_data = scaler.fit_transform(data)
standardized_df = pd.DataFrame(standardized_data, columns = data.columns)
print("\nStandardized Data (Z-score):")
print(standardized_df)

print("#--------------------------------------------------------------------------------------#")

df = pd.DataFrame({'color':['Red','Blue','Green','Red','Blue']})
one_hot = pd.get_dummies(df,columns=['color'])
print(one_hot)
print("#--------------------------------------------------------------------------------------#")
import pandas as pd 
from sklearn.preprocessing import MinMaxScaler, StandardScaler,LabelEncoder
import seaborn as sns 
#load dataset 
tips = sns.load_dataset("tips")
print("Original DAta(first 5 rows):")
print(tips.head())
#1. Normalization (Min-Max scaling)
numeric_cols = tips.select_dtypes(include=['float64','int64']).columns
scaler_minmax = MinMaxScaler()
tips_normalized = tips.copy()
tips_normalized[numeric_cols] = scaler_minmax.fit_transform(tips[numeric_cols])
print("\nNormalized Data (first 5 rows):")
print(tips_normalized.head())
#2.Standardization (Z-score)
scaler_standard = StandardScaler()
tips_standardized = tips.copy()
tips_standardized[numeric_cols] = scaler_standard.fit_transform(tips[numeric_cols])

print("\nStandardized Data (first 5 rows): ")
print(tips_standardized.head())
#3.Encoding categorical Variables 
#(a) one-hot encoding 
tips_onehot = pd.get_dummies(tips, columns=['sex','smoker','day','time'])
print("\n one-hot encoded data (first 5 rows):")
print(tips_onehot.head())
print("#--------------------------------------------------------------------------------------#")
import pandas as pd 
import seaborn as sns 
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

#load dataset 
tips = sns.load_dataset("tips")

#select numeric columns 
numeric_cols = tips.select_dtypes(include=['float64','int64'])

#step 1 : Standardize the data (important for PCA)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numeric_cols)

#step 2 : Apply PCA
pca = PCA(n_components=2)
pca_result=pca.fit_transform(scaled_data)

#step 3 :create a dataframe with pca results 
pca_df = pd.DataFrame(data=pca_result,columns=['PC1','PC2'])

print("Explained variance ratio:",pca.explained_variance_ratio_)
print("\nPCA Result (first 5 row):")
print(pca_df.head())

print("#--------------------------------------------------------------------------------------#")

import matplotlib.pyplot as plt 

plt.scatter(pca_df['PC1'],pca_df['PC2'],alpha=0.7)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal COmponent 2')
plt.title('PCA Projection of Tips Dataset')
plt.show()
print("#--------------------------------------------------------------------------------------#")
