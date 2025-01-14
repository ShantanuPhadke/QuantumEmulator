from .ComplexNumber import ComplexNumber
from .ComplexMatrix import ComplexMatrix
from .ComplexRepresentation import ComplexRepresentation

class ComplexOperationsSummary:
    @staticmethod
    def complex_number_ops_summary(c1: ComplexNumber, c2: ComplexNumber):
        print(f"Sum: {c1 + c2}")
        print(f"Product: {c1 * c2}")
        print(f"Difference: {c1 - c2}")
        print(f"Division: {c1 / c2}")
        print(f"Conjugate (first number): {c1.__conjugate__()}")
        print(f"Modulus (first number): {c1.__modulus__()}")

    @staticmethod
    def complex_matrix_ops_summary(V: ComplexMatrix, c: ComplexNumber):       
        print(f"Scalar multiplication: {V.scalar_multiply(c)}")
