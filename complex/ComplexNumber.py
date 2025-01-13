import math
from .ComplexRepresentation import ComplexRepresentation

class ComplexNumber:
    def __init__(self, component1, component2, representation=ComplexRepresentation.CARTESIAN) -> None:
        self.representation = representation
        if representation == ComplexRepresentation.CARTESIAN:
            self.real = component1
            self.imag = component2
            self.cartesian_to_polar()
        else:
            self.r = component1
            self.theta = component2
            self.polar_to_catesian()

    def get_real(self):
        return self.real
    
    def get_imaginary(self):
        return self.imag
    
    def get_r(self):
        return self.r
    
    def get_theta(self):    
        return self.theta
    
    def get_representation(self):
        return self.representation
    
    def swith_representation(self): 
        if self.representation == ComplexRepresentation.CARTESIAN:
            self.representation = ComplexRepresentation.POLAR
        else:
            self.representation = ComplexRepresentation.CARTESIAN
    
    def cartesian_to_polar(self):
        if self.representation == ComplexRepresentation.CARTESIAN:
            r = (self.real ** 2 + self.imag ** 2) ** 0.5
            theta = math.atan(self.imag / self.real)
            self.r = r
            self.theta = theta
            self.representation = ComplexRepresentation.POLAR

    def polar_to_catesian(self):
        if self.representation == ComplexRepresentation.POLAR:
            x = self.r * math.cos(self.theta)
            y = self.r * math.sin(self.theta)
            self.real = x
            self.imag = y
            self.representation = ComplexRepresentation.CARTESIAN
    
    def __str__(self) -> str:
        if ComplexRepresentation.CARTESIAN:
            return f"{self.real} + {self.imag}i"
        return f"length: {self.r}, angle: {self.theta}"
    
    def __eq__(self, __value: object) -> bool:
        if self.representation == ComplexRepresentation.CARTESIAN:
            return self.real == __value.real and self.imag == __value.imag
        return self.r == __value.r and self.theta == __value.theta