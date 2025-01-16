from .ComplexMatrix import ComplexMatrix
from .ComplexNumber import ComplexNumber

class ComplexVector:
    def __init__(self, n, vector=None):
        if vector:
            self.vector = ComplexMatrix(rows=len(vector), cols=1, matrix=[[element] for element in vector])
        else:
            self.vector = ComplexMatrix(rows=n, cols=1, matrix=[[ComplexNumber(0, 0)] for _ in range(n)])
        self.rows = n
        self.cols = 1

    def __getitem__(self, tup):
        return self.vector[tup]

    def __setitem__(self, tup, value):
        self.vector[tup] = value
    
    def inner_product(self, other):
        if self.rows != other.rows:
            raise ValueError("Vectors must have the same length")
        result = ComplexNumber(0, 0)
        for i in range(self.rows):
            result += self.vector[i, 0].__mul__(other.vector[i, 0].__conjugate__())
        return result

    def norm(self):
        return self.inner_product(self).get_real() ** 0.5
    
    def distance(self, other):
        return (self - other).norm()
    
    def tensor_product(self, other):
        tensor_product = self.vector.tensor_product(other.vector)
        return tensor_product
    
    def __eq__(self, __value: object) -> bool:
        return self.vector == __value.vector