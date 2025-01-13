from .ComplexNumber import ComplexNumber

class ComplexOperations:
    @staticmethod
    def __add__(c1: ComplexNumber, c2: ComplexNumber):
        return ComplexNumber(c1.real + c2.real, c1.imag + c2.imag)

    @staticmethod
    def __mul__(c1: ComplexNumber, c2: ComplexNumber):
        return ComplexNumber(c1.real * c2.real - c1.imag * c2.imag, c1.real * c2.imag + c1.imag * c2.real)
    
    @staticmethod
    def output_sum_and_product(self, c1: ComplexNumber, c2: ComplexNumber):
        print(f"Sum: {ComplexOperations.__add__(c1, c2)}")
        print(f"Product: {ComplexOperations.__mul__(c1, c2)}")