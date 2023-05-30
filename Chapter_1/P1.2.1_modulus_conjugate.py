import cmath

class ComplexMath:
    def modulus(self, a):
        return  cmath.sqrt(a*a.conjugate())
    def conjugate(self, a):
        return a.conjugate()

if __name__=="__main__":
    CMath = ComplexMath()
    print(f"Modulus : {CMath.modulus(complex(3,4))}")
    print(f"Conjugate : {CMath.conjugate(complex(3,4))}")

