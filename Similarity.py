# importing the library
from scipy.spatial import distance
import numpy as np

# using in-built method
manhattan_distance = distance.cityblock(point_1, point_2)
print("Manhattan Distance between", point_1, "and", point_2, "is:", manhattan_distance)

def get_manhattan(p1, p2):
    dist  = 0
    
    for i in range(len(point_1)):
        dist += abs(point_1[i] - point_2[i])
    
    print(dist)

# using created method
get_manhattan(point_1, point_2)

# using in-built method
euclidean_distance = distance.euclidean(point_1, point_2)
print("Euclidean Distance between", point_1, "and", point_2, "is:", euclidean_distance)

def get_euclidean(p1, p2):
    dist = 0
    
    for i in range(len(p1)):
        dist += (p1[i] - p2[i]) ** 2
        
    euclidean_dist = np.sqrt(dist)
    print(euclidean_dist)
    
# using created method
get_euclidean(point_1, point_2)

# using in-built method
minkowski_distance = distance.minkowski(point_1, point_2, 3)
print("Minkowski Distance between", point_1, "and", point_2, "is:", minkowski_distance)

def get_minkowski(p1, p2, order=2):
    dist = 0
    
    for i in range(len(p1)):
        dist += np.abs(p1[i] - p2[i]) ** order
        
    minkowski_dist = np.power(dist, (1./order))
    print(minkowski_dist)

# using created method
get_minkowski(point_1, point_2,3)

# the points used for testing

point_1 = np.array((1, 2, 3), dtype='float32')
point_2 = np.array((4, 5, 6), dtype='float32')
