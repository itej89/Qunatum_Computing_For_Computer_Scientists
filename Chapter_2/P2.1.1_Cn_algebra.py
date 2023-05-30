import cmath

import numpy as np


a = [1+1j, 2+2j, 3+3j] 
na = np.array(a)

b = [1+1j, 2+2j, 3+3j]
nb = np.array(b)

#Addition
print(na+nb)

#Inverse
print(-1*na)

#Scalar multiplication
print(na*3)