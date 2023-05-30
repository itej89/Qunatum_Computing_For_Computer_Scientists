
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir+"/manim") 

from manimlib.imports import *

class ComplexTransformation(LinearTransformationScene):
    def construct(self):
        rect = Rectangle(1,2)
        function = lambda point: complex_to_R3(R3_to_complex(point)*(2+3j))

        self.add_transformable_mobject(rect)

        self.apply_nonlinear_transformation(function)

        self.wait()