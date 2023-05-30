import cmath

class ComplexMath:
    def toPolar(self, a):
        return cmath.polar(a)
    def toCartisian(self, r, phi):
        return cmath.rect(r, phi)

if __name__=="__main__":
    CMath = ComplexMath()
    print(f"Polar : {CMath.toPolar(complex(3,4))}")
    print(f"Conjugate : {CMath.toCartisian(cmath.polar(complex(3,4))[0], cmath.polar(complex(3,4))[1])}")

