import cmath

import numpy as np


a = np.array([1+1j, 6+2j, 3+3j, 4+4j, 5+5j, 5+6j, 7+7j, 8+8j, 3+9j])
b = np.array([1-1j, 6+2j, 3+3j, 4+4j, 9+5j, 5+6j, 7+7j, 8+8j, 3+9j])

c = a - b

print(np.linalg.norm(c))