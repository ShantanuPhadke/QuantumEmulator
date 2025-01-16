from .ComplexNumber import ComplexNumber

class ComplexMatrix:
    def __init__(self, rows=1, cols=1, matrix=None):
        if matrix:
            self.matrix = matrix
        else:
            self.matrix = [[ComplexNumber(0, 0) for _ in range(cols)] for _ in range(rows)]
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])

    def __getitem__(self, tup):
        row, col = tup
        return self.matrix[row][col]

    def __setitem__(self, tup, value):
        row, col = tup
        self.matrix[row][col] = value

    def __str__(self):
        return '\n'.join([' '.join([str(self.matrix[i][j]) for j in range(self.cols)]) for i in range(self.rows)])
    
    def scalar_multiply(self, scalar: ComplexNumber):
        result = ComplexMatrix(rows=self.rows, cols=self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result[i, j] = self[i, j] * scalar
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError('Matrix dimensions must agree')
        result = ComplexMatrix(rows=self.rows, cols=other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i, j] += self[i, k] * other[k, j]
        return result

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('Matrix dimensions must agree')
        result = ComplexMatrix(rows=self.rows, cols=self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result[i, j] = self[i, j] + other[i, j]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('Matrix dimensions must agree')
        result = ComplexMatrix(rows=self.rows, cols=self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result[i, j] = self[i, j] - other[i, j]
        return result

    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if abs((self[i, j] - other[i, j]).get_real()) > 0.0001 or abs((self[i, j] - other[i, j]).get_imaginary()) > 0.0001 :
                    return False
        return True

    def __ne__(self, other):
        return not self == other

    def __neg__(self):
        result = self.scalar_multiply(ComplexNumber(-1, 0))
        return result
    
    def check_hermitian(self):
        if self.rows != self.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self[i, j] != self[j, i].__conjugate__():
                    return False
        return True
    
    def conjugate_transpose(self):
        result = ComplexMatrix(rows=self.cols, cols=self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result[j, i] = self[i, j].__conjugate__()
        return result
    
    def check_unitary(self):
        if self.rows != self.cols:
            return False
        conjugate_transpose_mult_result1 = self * self.conjugate_transpose()
        conjugate_transpose_mult_result2 = self.conjugate_transpose() * self
        identity_matrix = ComplexMatrix(rows=self.rows, cols=self.cols, matrix=[[ComplexNumber(1, 0) if i == j else ComplexNumber(0, 0) for j in range(self.cols)] for i in range(self.rows)])
        return conjugate_transpose_mult_result1 == identity_matrix and conjugate_transpose_mult_result2 == identity_matrix
    
    def tensor_product(self, other):
        result = ComplexMatrix(rows=self.rows * other.rows, cols=self.cols * other.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                for k in range(other.rows):
                    for l in range(other.cols):
                        result[i * other.rows + k, j * other.cols + l] = self[i, j] * other[k, l]
        return result