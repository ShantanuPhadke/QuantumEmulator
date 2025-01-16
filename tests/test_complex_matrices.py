import pytest
import math
from complex.ComplexNumber import ComplexNumber
from complex.ComplexMatrix import ComplexMatrix
from complex.ComplexOperations import ComplexOperationsSummary
from complex.ComplexRepresentation import ComplexRepresentation
from complex.ComplexVector import ComplexVector

def test_scalar_multiplication():
    c = ComplexNumber(3, 2) # 3 + 2i
    V = ComplexMatrix(matrix=[[ComplexNumber(6,3)], [ComplexNumber(0,0)], [ComplexNumber(5,1)], [ComplexNumber(4,0)]])
    result = V.scalar_multiply(c)
    assert result ==  ComplexMatrix(
        matrix=[
            [ComplexNumber(12,21)],
            [ComplexNumber(0,0)],
            [ComplexNumber(13,13)],
            [ComplexNumber(12,8)]
        ]
    )

def test_matrix_addition():
    V1 = ComplexMatrix(matrix=[[ComplexNumber(1,2), ComplexNumber(3,4)], [ComplexNumber(5,6), ComplexNumber(7,8)]])
    V2 = ComplexMatrix(matrix=[[ComplexNumber(9,10), ComplexNumber(11,12)], [ComplexNumber(13,14), ComplexNumber(15,16)]])
    result = V1 + V2
    assert result == ComplexMatrix(
        matrix=[
            [ComplexNumber(10,12), ComplexNumber(14,16)],
            [ComplexNumber(18,20), ComplexNumber(22,24)]
        ]
    )

def test_matrix_negative():
    V = ComplexMatrix(matrix=[[ComplexNumber(1,2), ComplexNumber(3,4)], [ComplexNumber(5,6), ComplexNumber(7,8)]])
    result = -V
    assert result == ComplexMatrix(
        matrix=[
            [ComplexNumber(-1,-2), ComplexNumber(-3,-4)],
            [ComplexNumber(-5,-6), ComplexNumber(-7,-8)]
        ]
    )

def test_matrix_multiplication():
    V1 = ComplexMatrix(matrix=[[ComplexNumber(3,2), ComplexNumber(0,0), ComplexNumber(5,-6)], [ComplexNumber(1,0), ComplexNumber(4,2), ComplexNumber(0,1)], [ComplexNumber(4,-1), ComplexNumber(0,0), ComplexNumber(4,0)]])
    V2 = ComplexMatrix(matrix=[[ComplexNumber(5,0), ComplexNumber(2,-1), ComplexNumber(6,-4)], [ComplexNumber(0,0), ComplexNumber(4,5), ComplexNumber(2,0)], [ComplexNumber(7,-4), ComplexNumber(2,7), ComplexNumber(0,0)]])
    result = V1 * V2
    assert result == ComplexMatrix(
        matrix=[
            [ComplexNumber(26, -52), ComplexNumber(60, 24), ComplexNumber(26, 0)],
            [ComplexNumber(9, 7), ComplexNumber(1, 29), ComplexNumber(14, 0)],
            [ComplexNumber(48, -21), ComplexNumber(15, 22), ComplexNumber(20, -22)]
        ]
    )

def test_inner_product():
    V1 = ComplexVector(3, [ComplexNumber(1,2), ComplexNumber(0,0), ComplexNumber(0,1)])
    V2 = ComplexVector(3, [ComplexNumber(0,1), ComplexNumber(1,0), ComplexNumber(3,-1)])
    result = V1.inner_product(V2)
    assert result == ComplexNumber(1, 2)

def test_norm():
    V = ComplexVector(3, [ComplexNumber(0,2), ComplexNumber(3,3), ComplexNumber(0,-1)])
    result = V.norm()
    assert result == math.sqrt(23)

def test_hermitian():
    V = ComplexMatrix(matrix=[[ComplexNumber(1,0), ComplexNumber(2,-1), ComplexNumber(3,2)], [ComplexNumber(2,1), ComplexNumber(0,0), ComplexNumber(1,-1)], [ComplexNumber(3,-2), ComplexNumber(1,1), ComplexNumber(0,0)]])
    assert V.check_hermitian() == True
    V = ComplexMatrix(matrix=[[ComplexNumber(1,0), ComplexNumber(2,-1), ComplexNumber(3,4)], [ComplexNumber(2,1), ComplexNumber(0,0), ComplexNumber(1,-1)], [ComplexNumber(3,-2), ComplexNumber(1,1), ComplexNumber(1,0)]])
    assert V.check_hermitian() == False
    V = ComplexMatrix(matrix=[[ComplexNumber(1,0), ComplexNumber(2,-1)], [ComplexNumber(2,1), ComplexNumber(0,0)]])
    assert V.check_hermitian() == True
    V = ComplexMatrix(matrix=[[ComplexNumber(1,0), ComplexNumber(2,-1)], [ComplexNumber(3,1), ComplexNumber(1,0)]])
    assert V.check_hermitian() == False
    V = ComplexMatrix(matrix=[[ComplexNumber(1,0), ComplexNumber(2,-1)], [ComplexNumber(2,1), ComplexNumber(0,0)]])
    assert V.check_hermitian() == True
    V = ComplexMatrix(matrix=[[ComplexNumber(1,0), ComplexNumber(2,-1)], [ComplexNumber(2,-1), ComplexNumber(1,0)]])
    assert V.check_hermitian() == False

def test_unitary():
    V = ComplexMatrix(matrix=[
        [ComplexNumber(1/2,1/2), ComplexNumber(0,1/math.sqrt(3)), ComplexNumber(3/(2*math.sqrt(15)), 1/(2*math.sqrt(15)))], 
        [ComplexNumber(-1/2,0), ComplexNumber(1/math.sqrt(3),0), ComplexNumber(4/(2*math.sqrt(15)), 3/(2*math.sqrt(15)))],
        [ComplexNumber(1/2, 0), ComplexNumber(0, -1/math.sqrt(3)), ComplexNumber(0, 5/(2*math.sqrt(15)))]
    ])
    assert V.check_unitary() == True

def test_tensor_product_vectors():
    V1 = ComplexVector(2, [ComplexNumber(2,0), ComplexNumber(3,0)])
    V2 = ComplexVector(2, [ComplexNumber(4,0), ComplexNumber(6,0), ComplexNumber(3,0)])
    result = V1.tensor_product(V2)
    assert result == ComplexVector(6, [ComplexNumber(8,0), ComplexNumber(12,0), ComplexNumber(6,0), ComplexNumber(12,0), ComplexNumber(18,0), ComplexNumber(9,0)])

def test_tensor_product_matrices():
    A = ComplexMatrix(matrix=[[ComplexNumber(1,0), ComplexNumber(2,0)], [ComplexNumber(3,0), ComplexNumber(4,0)]])
    B = ComplexMatrix(matrix=[[ComplexNumber(5,0), ComplexNumber(6,0)], [ComplexNumber(7,0), ComplexNumber(8,0)]])
    result = A.tensor_product(B)
    assert result == ComplexMatrix(matrix=[
        [ComplexNumber(5,0), ComplexNumber(6,0), ComplexNumber(10,0), ComplexNumber(12,0)],
        [ComplexNumber(7,0), ComplexNumber(8,0), ComplexNumber(14,0), ComplexNumber(16,0)],
        [ComplexNumber(15,0), ComplexNumber(18,0), ComplexNumber(20,0), ComplexNumber(24,0)],
        [ComplexNumber(21,0), ComplexNumber(24,0), ComplexNumber(28,0), ComplexNumber(32,0)]
    ])

