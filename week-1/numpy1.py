import numpy as np

N = np.array([10,12,13,14,15])
print(type(N))
print(N.ndim)

N = np.array([1,2,3])
N = np.array(1)
print(N.ndim)

P = np.array([[1,2,3],[4,5,6]])
print(P.ndim)

# initialize numpy arrays
P = np.zeros([1])
print(P)

N = np.zeros([3,4])
print(N)
print(type(N))

# array indexing
S = np.array([[[[1,2,3],[4,5,6]],[[6,7,8],[9,7,8]]]])
print(S[0,0,1])      # [4 5 6]
print(S[0,1,0])      # [6 7 8]

P = np.array([12,23,34,45,56,67,78])
print(P[0])
print(P[5])

Q = np.array([[1,2,3],[6,7,8]])
print(Q[0,0])

# Negative indexing
print(P[-1])

# Array slicing
print(P[2:5])
print(P[:5])
print(P[2:])

# Slicing 2D array
print(Q[0,2:4])
print(Q[:,1:3])

# numpy making 0 matrices
N = np.zeros([1])
P = np.zeros([3,4])
print(P)
print(type(P))

P = np.ones([3,4])
N = np.ones([1])
print(P)
print(type(P))

#looping 1D array 
n = np.array([1,2,3,4,5,6])
for x in n :
    print(x)
    
#looping 2D ARRAY 
p = np.array([[1,2,3],[4,5,6]])
for a in p :
    print(a)

#joining arrays
n1 = np.array([1,2,3,4])
n2 = np.array([4,5,6,7,8])
n3 = np.concatenate((n1,n2))
print(n3)

#split numpy array 
print(np.array_split(n3,4))
sp = np.array_split(n3,5)
print(sp[0])

#searching and sorting of arrays 
p = np.where(n1==4)
print(p)
p = np.sort(n1)
print(p)

n = np.array(['hi','java','pyth','app'])
print(np.sort(n))

#Arithmetic operations on array 
# Sum()
n1 = np.array([1,2,3,4])
n2 = np.array([5,6,7,8])
print(np.sum([n1,n2]))

print(np.sum([n1,n2],axis=1))
print(np.sum([n1,n2],axis=0))

print(np.subtract(n1,n2))
print(np.multiply(n1,n2))
print(np.divide(n1,n2))