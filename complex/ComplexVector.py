from .ComplexMatrix import ComplexMatrix
from .ComplexNumber import ComplexNumber

class ComplexVector:
    def __init__(self, n, vector=None):
        if vector:
            self.vector = ComplexMatrix(rows=len(vector), cols=1, matrix=[[element] for element in vector])
        else:
            self.vector = [[ComplexNumber(0, 0)] for _ in range(n)]
        self.length = n
    
    def inner_product(self, other):
        if self.length != other.length:
            raise ValueError("Vectors must have the same length")
        result = ComplexNumber(0, 0)
        for i in range(self.length):
            result += self.vector[i, 0].__mul__(other.vector[i, 0].__conjugate__())
        return result

    def norm(self):
        return self.inner_product(self).get_real() ** 0.5
    
    def distance(self, other):
        return (self - other).norm()