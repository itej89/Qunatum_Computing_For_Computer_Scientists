import cmath

import numpy as np


a = [1+1j, 2+2j, 3+3j, 4+4j, 5+5j, 6+6j, 7+7j, 8+8j] 
na = np.array(a).reshape((2,4))

b = [1+1j, 2+2j, 3+3j, 4+4j, 5+5j, 6+6j, 7+7j, 8+8j] 
nb = np.array(b).reshape((2,4))

#Addition
print(na+nb)

#Inverse
print(-1*na)

#Scalar multiplication
print(na*3)