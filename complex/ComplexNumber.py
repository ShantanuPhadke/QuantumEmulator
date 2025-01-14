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
            theta = 0
            if self.real != 0:
                theta = math.atan(self.imag / self.real)
            self.r = r
            self.theta = theta

    def polar_to_catesian(self):
        if self.representation == ComplexRepresentation.POLAR:
            x = self.r * math.cos(self.theta)
            y = self.r * math.sin(self.theta)
            self.real = x
            self.imag = y

    def representations_equal(self, c2):
        return self.get_representation() == c2.get_representation()

    def __add__(self, c2):
        if not self.representations_equal(c2):
            raise ValueError("The representations of the numbers are different. Please call swith_representation to make both numbers in the same form so we can perform the appropriate operation.")
        if self.get_representation() == ComplexRepresentation.CARTESIAN:
            return ComplexNumber(self.real + c2.real, self.imag + c2.imag)
        raise ValueError("The numbers are in the polar form. Addition / Subraction only work in cartesian form. Please swith the respresentations of both.")
    
    def __mul__(self, c2):
        if not self.representations_equal(c2):
            raise ValueError("The representations of the numbers are different. Please call swith_representation to make both numbers in the same form so we can perform the appropriate operation.")
        if self.get_representation() == ComplexRepresentation.CARTESIAN:
            return ComplexNumber(self.real * c2.real - self.imag * c2.imag, self.real * c2.imag + self.imag * c2.real)
        return ComplexNumber(self.r * c2.r, self.theta + c2.theta)
    
    def __sub__(self, c2):        
        return self.__add__(c2 * ComplexNumber(-1, 0))
    
    def __truediv__(self, c2):
        if not self.representations_equal(c2):
            raise ValueError("The representations of the numbers are different. Please call swith_representation to make both numbers in the same form so we can perform the appropriate operation.")
        if self.get_representation() == ComplexRepresentation.CARTESIAN:
            return ComplexNumber((self.real * c2.real + self.imag * c2.imag) / (c2.real ** 2 + c2.imag ** 2), (self.imag * c2.real - self.real * c2.imag) / (c2.real ** 2 + c2.imag ** 2))
        return ComplexNumber(self.r / c2.r, self.theta - c2.theta)
    
    def __conjugate__(self):
        return ComplexNumber(self.real, -1*self.imag)
    
    def __modulus__(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5
    
    def __str__(self) -> str:
        if ComplexRepresentation.CARTESIAN:
            return f"{self.real} + {self.imag}i"
        return f"length: {self.r}, angle: {self.theta}"
    
    def __eq__(self, __value: object) -> bool:
        if self.representation == ComplexRepresentation.CARTESIAN:
            return self.real == __value.real and self.imag == __value.imag
        return self.r == __value.r and self.theta == __value.theta