import cmath

import numpy as np


a = [1+1j, 2+2j, 4+3j, 4+4j, 5+5j, 6+6j, 7+7j, 8+8j] 
na = np.array(a).reshape((2,4))

b = [1+1j, 2+2j, 3+3j, 4+4j, 6+5j, 6+6j, 7+7j, 8+8j] 
nb = np.array(b).reshape((4,2))

#Matrix multiplication
print(np.matmul(na,nb))

#vector dot product
print(np.matmul(na.reshape(na.size).conj().T,nb.reshape(nb.size)))
print(np.matmul(nb.reshape(nb.size).conj().T,na.reshape(na.size)))