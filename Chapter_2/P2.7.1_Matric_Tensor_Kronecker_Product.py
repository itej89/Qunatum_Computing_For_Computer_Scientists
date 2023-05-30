import cmath

import numpy as np



na = np.array([1+1j, 6+2j, 3+3j, 4+4j, 5+5j, 5+6j, 7+7j, 8+8j, 3+9j])
nb = np.array([1-1j, 6+2j, 3+3j, 4+4j, 9+5j, 5+6j, 7+7j, 8+8j, 3+9j])

na = na.reshape((3,3))
nb = nb.reshape((3,3))



print(np.kron(na, nb))