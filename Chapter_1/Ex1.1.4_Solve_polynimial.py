import cmath

import numpy as np

class PolynomialSolver:
    def roots(self, coeff):
        poly = np.poly1d(coeff)
        return poly.r

if __name__=="__main__":
    PolySolve = PolynomialSolver()
    print(PolySolve.roots([1,2,2]))

