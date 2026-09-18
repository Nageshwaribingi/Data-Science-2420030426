
#coorelation between two variables

from builtins import print

import pandas as pd 
from scipy.stats import spearmanr
#example dataset 
df = pd.DataFrame({
    'X':[10,20,30,40,50],
    'Y':[12,24,33,45,60]
})

#Pearson correlation matrix 
corr_matrix = df.corr(method='pearson')
print("Pearson correlation matrix:\n", corr_matrix)

#--------------------------------------------------------------------------------------#

df = pd.DataFrame({
    'X':[10,20,30,40,50],
    'Y':[10,20,30,40,50]
})

corr_matrix = df.corr(method='pearson')
print("Pearson correlation matrix:\n", corr_matrix)

#--------------------------------------------------------------------------------------#

df = pd.read_csv("iris.csv")
print(df.corr(method='pearson',numeric_only=float))

#--------------------------------------------------------------------------------------#

# df = pd.read_csv("iris.csv")
# print(df.corr(method='pearson')) //error because of non-numeric data , strings 

#--------------------------------------------------------------------------------------#

df = pd.DataFrame({
    'X':[10,20,30,40,50],
    'Y':[12,24,33,45,60]
})

#Spearman correlation co-efficient and p-value
corr_value , p_value = spearmanr(df['X'], df['Y'])
print("Spearman correlation co-efficient:", corr_value)
print(f"p-value: {p_value}")

#--------------------------------------------------------------------------------------#
# for dataset :
# # create a data set with 5 names , 4 different subject marks (DS,ADAS,CD,ASE) and total marks

df = pd.DataFrame({
    'Name':['A','B','C','D','E'],
    'DS':[85,90,78,92,88],
    'ADAS':[88,85,80,90,85],
    'CD':[90,88,85,92,87],
    'ASE':[85,90,88,90,85]
})

#apply both pearson and spearman correlation methods to find correlation between different subjects marks
corr_matrix_pearson = df.corr(method='pearson', numeric_only=True)
print("Pearson correlation matrix:\n", corr_matrix_pearson)

corr_matrix_spearman , p_value_spearman = spearmanr(df[['DS','ADAS','CD','ASE']])
print("Spearman correlation matrix:\n", corr_matrix_spearman)
print(f"Spearman p-value:\n", p_value_spearman)

#--------------------------------------------------------------------------------------#

def hamming_distance(str1, str2):
    #Ensure strings are of equal length 
    if len(str1) != len(str2):
        raise ValueError("Strings must be of the same length")
    
    # Count differing positions
    return sum(el1 != el2 for el1, el2 in zip(str1, str2))

# example usage
str1 = "karolin"
str2 = "kathrin"
distance = hamming_distance(str1, str2)
print(f"Hamming distance between '{str1}' and '{str2}' is: {distance}")

# example usage
str1 = "Hes is Visiting Us"
str2 = "SHe is visiting us"
distance = hamming_distance(str1, str2)
print(f"Hamming distance between '{str1}' and '{str2}' is: {distance}")


#--------------------------------------------------------------------------------------#

def jaccard_index(str1, str2):
    set1 , set2 = set(str1.split()), set(str2.split())
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union) 

# example usage
s1 = "data science is fun  "
s2 ="science makes data useful"

print("Jaccard Index: ",jaccard_index(s1,s2))

#--------------------------------------------------------------------------------------#

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# example sentences 
s1 = "data science is fun"
s2 = "science makes data useful"

# convert text to vector representation
vectorizer = CountVectorizer().fit([s1, s2])
vectors = vectorizer.transform([s1, s2])

# compute cosine similarity
cosine_sim = cosine_similarity(vectors[0], vectors[1])[0][0]
print("Cosine Similarity: ", cosine_sim)

#--------------------------------------------------------------------------------------#
# in between 2 sequencves how much distance exists between them

def lcs_length(X,Y):
    m,n = len(X), len(Y)
    # create a matrix to store lengths of longest common subsequence
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    # build the dp matrix
    for i in range (m):
        for j in range (n):
            if X[i] == Y[j]:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[m][n]

# example usage
seq1 ="ABCDEF"
seq2 ="AEBDF"
length = lcs_length(seq1, seq2)
print(f"Length of Longest Common Subsequence between '{seq1}' and '{seq2}' is: {length}")

