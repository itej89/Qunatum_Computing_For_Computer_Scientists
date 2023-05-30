
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir+"/manim") 

from manimlib.imports import *

class ComplexTransformation(LinearTransformationScene):
    def construct(self):
        line = Line((0,-2,-4), (0, 4,6))
        line.set_stroke(RED, 2)
        # function = lambda point: complex_to_R3(((R3_to_complex(point)*(2+3j)) + (1+1j))/((R3_to_complex(point)*(4+3j)) + (3+2j)))
        function = lambda point: complex_to_R3(1/R3_to_complex(point+1))
        
        self.add_transformable_mobject(line)

        self.apply_nonlinear_transformation(function)

        self.wait()