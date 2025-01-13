from .ComplexNumber import ComplexNumber

class ComplexOperations:
    @staticmethod
    def __add__(c1: ComplexNumber, c2: ComplexNumber):
        return ComplexNumber(c1.real + c2.real, c1.imag + c2.imag)

    @staticmethod
    def __mul__(c1: ComplexNumber, c2: ComplexNumber):
        return ComplexNumber(c1.real * c2.real - c1.imag * c2.imag, c1.real * c2.imag + c1.imag * c2.real)
    
    @staticmethod
    def __sub__(c1: ComplexNumber, c2: ComplexNumber):
        return ComplexNumber(c1.real - c2.real, c1.imag - c2.imag)
    
    @staticmethod
    def __div__(c1: ComplexNumber, c2: ComplexNumber):
        return ComplexNumber((c1.real * c2.real + c1.imag * c2.imag) / (c2.real ** 2 + c2.imag ** 2), (c1.imag * c2.real - c1.real * c2.imag) / (c2.real ** 2 + c2.imag ** 2))
    
    @staticmethod
    def __conjugate__(c: ComplexNumber):
        return ComplexNumber(c.real, -c.imag)
    
    @staticmethod
    def __modulus__(c: ComplexNumber):
        return (c.real ** 2 + c.imag ** 2) ** 0.5
    
    @staticmethod
    def ouput(c1: ComplexNumber, c2: ComplexNumber):
        print(f"Sum: {ComplexOperations.__add__(c1, c2)}")
        print(f"Product: {ComplexOperations.__mul__(c1, c2)}")
        print(f"Difference: {ComplexOperations.__sub__(c1, c2)}")
        print(f"Division: {ComplexOperations.__div__(c1, c2)}")
        print(f"Conjugate (first number): {ComplexOperations.__conjugate__(c1)}")
        print(f"Modulus (first number): {ComplexOperations.__modulus__(c1)}")
