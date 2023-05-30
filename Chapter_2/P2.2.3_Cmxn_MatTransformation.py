import cmath

import numpy as np


a = [1+1j, 6+2j, 3+3j, 4+4j, 5+5j, 5+6j, 7+7j, 8+8j, 3+9j] 
na = np.array(a).reshape((3,3))

b = [1+1j, 2+2j, 3+3j] 
nb = np.array(b)

print(nb.shape)

#vector multiplication
print(np.matmul(na,nb))
