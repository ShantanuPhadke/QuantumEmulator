import pytest
from complex.ComplexNumber import ComplexNumber
from complex.ComplexOperations import ComplexOperations

def test_addition():
    c1 = ComplexNumber(1, 2) # 1 + 2i
    c2 = ComplexNumber(3, 4) # 3 + 4i
    assert ComplexOperations.__add__(c1, c2) == ComplexNumber(4, 6)

def test_multiplication():
    c1 = ComplexNumber(1, 2) # 1 + 2i 
    c2 = ComplexNumber(3, 4) # 3 + 4i
    # c3 = c1 * c2 = (1 + 2i) * (3 + 4i) = 3 + 4i + 6i + 8i^2 = 3 - 8 + 10i = 10i - 5
    assert ComplexOperations.__mul__(c1, c2) == ComplexNumber(-5, 10)

def test_subtraction():
    c1 = ComplexNumber(1, 2) # 1 + 2i
    c2 = ComplexNumber(3, 4) # 3 + 4i
    assert ComplexOperations.__sub__(c1, c2) == ComplexNumber(-2, -2)

def test_division():
    c1 = ComplexNumber(1, 2) # 1 + 2i
    c2 = ComplexNumber(3, 4) # 3 + 4i
    # c3 = c1 / c2 = (1 + 2i) / (3 + 4i) = (1 + 2i)(3 - 4i) / (3 + 4i)(3 - 4i) = (3 - 4 + 6i + 8) / (9 + 16) = 11/25 + 2/25i
    assert ComplexOperations.__div__(c1, c2) == ComplexNumber(11/25, 2/25)

def test_conjugate():
    c = ComplexNumber(1, 2) # 1 + 2i
    assert ComplexOperations.__conjugate__(c) == ComplexNumber(1, -2)

def test_modulus():
    c = ComplexNumber(1, 2) # 1 + 2i
    # |c| = sqrt(1^2 + 2^2) = sqrt(1 + 4) = sqrt(5)
    assert ComplexOperations.__modulus__(c) == (5) ** 0.5