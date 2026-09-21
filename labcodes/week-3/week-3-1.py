import numpy as np 
from scipy.spatial import distance

pointA = np.array([2, 4, 6])
pointB = np.array([5, 1, 9])

#Euclidean distance
euclidean_distance = distance.euclidean(pointA, pointB)
print("Euclidean distance between pointA and pointB:", euclidean_distance)

#similarity (inverse of distance)
similarity = 1 / (1 + euclidean_distance)
print("Similarity between pointA and pointB:", similarity)

manhattan_distance = distance.cityblock(pointA, pointB)
print("Manhattan distance between pointA and pointB:", manhattan_distance)

similarity_manhattan = 1 / (1 + manhattan_distance)
print("Similarity (Manhattan) between pointA and pointB:", similarity_manhattan)

#minkowski distance
minkowski_distance = distance.minkowski(pointA, pointB, p=3)
print("Minkowski distance (p=3) between pointA and pointB:", minkowski_distance)

#similarity
similarity_minkowski = 1 / (1 + minkowski_distance)
print("Similarity (Minkowski) between pointA and pointB:", similarity_minkowski)