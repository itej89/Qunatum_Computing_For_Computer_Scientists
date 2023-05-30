import cmath

import numpy as np


na = np.array([1, 6+3j, 3+3j, 6-3j, 5, 5+6j, 3-3j, 5-6j, 3])
na = na.reshape((3,3))


na_Tran = np.transpose(na)
na_Conj = np.conjugate(na_Tran)

comparison = na == na_Conj
Is_Hermitian = comparison.all()

print(Is_Hermitian)