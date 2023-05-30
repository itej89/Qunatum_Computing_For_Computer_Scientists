import cmath

class ComplexMath:
    def add(self, a, b):
        return a+b
    def mul(self, a,b):
        return a*b
    def sub(self, a,b):
        return a-b
    def div(self, a,b):
        return a/b

if __name__=="__main__":
    CMath = ComplexMath()
    print(f"Addition : {CMath.add(complex(3,4), complex(4,5))}")
    print(f"Multiplication : {CMath.mul(complex(3,4), complex(4,5))}")
    print(f"Substraction : {CMath.sub(complex(3,4), complex(4,5))}")
    print(f"Division : {CMath.div(complex(3,4), complex(4,5))}")

