import cmath

import numpy as np


m = [[0,0,0,0,0,0],
     [0,0,0,0,0,0],
     [0,1,0,0,0,1],
     [0,0,0,1,0,0],
     [0,0,1,0,0,0],
     [1,0,0,0,1,0]] 
M = np.array(m)

X = np.array([6,2,0,1,0,0])

no_of_times = 102

#vector multiplication
print(np.matmul(np.linalg.matrix_power(M, no_of_times), X))
