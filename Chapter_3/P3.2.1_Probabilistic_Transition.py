import cmath

import numpy as np


m = [[0,0,0,0,0,0],
     [0,0,0,0,0,0],
     [0,1/4,0,0,0,1],
     [0,0,0,2/3,0,0],
     [0,0,1/2,0,0,0],
     [1,0,0,0,1/2,0]] 
M = np.array(m)

X = np.array([6,2,0,1,0,0])

no_of_times = 1

#vector multiplication
print(np.matmul(np.linalg.matrix_power(M, no_of_times), X))





#Symbolic
import cmath

import numpy as np

import sympy as sy
from sympy import Matrix


m = [0,0,0,0,0,0,
     0,0,0,0,0,0,
     0,sy.Rational('1/4'),0,0,0,1,
     0,0,0,sy.Rational('2/3'),0,0,
     0,0,sy.Rational('1/2'),0,0,0,
     1,0,0,0,sy.Rational('1/2'),0]

M = Matrix(6,6,m)

X = Matrix(6,1,[6,2,0,1,0,0])

print(M*X)

# no_of_times = 102

# #vector multiplication
# print(np.matmul(np.linalg.matrix_power(M, no_of_times), X))
