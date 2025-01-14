import pytest
import math
from complex.ComplexNumber import ComplexNumber
from complex.ComplexOperations import ComplexOperationsSummary
from complex.ComplexRepresentation import ComplexRepresentation

def test_addition():
    c1 = ComplexNumber(1, 2) # 1 + 2i
    c2 = ComplexNumber(3, 4) # 3 + 4i
    assert c1 + c2 == ComplexNumber(4, 6)

def test_multiplication():
    c1 = ComplexNumber(1, 2) # 1 + 2i 
    c2 = ComplexNumber(3, 4) # 3 + 4i
    # c3 = c1 * c2 = (1 + 2i) * (3 + 4i) = 3 + 4i + 6i + 8i^2 = 3 - 8 + 10i = 10i - 5
    assert c1 * c2 == ComplexNumber(-5, 10)

def test_subtraction():
    c1 = ComplexNumber(1, 2) # 1 + 2i
    c2 = ComplexNumber(3, 4) # 3 + 4i
    assert c1 - c2 == ComplexNumber(-2, -2)

def test_division():
    c1 = ComplexNumber(1, 2) # 1 + 2i
    c2 = ComplexNumber(3, 4) # 3 + 4i
    # c3 = c1 / c2 = (1 + 2i) / (3 + 4i) = (1 + 2i)(3 - 4i) / (3 + 4i)(3 - 4i) = (3 - 4 + 6i + 8) / (9 + 16) = 11/25 + 2/25i
    assert c1 / c2 == ComplexNumber(11/25, 2/25)

def test_conjugate():
    c = ComplexNumber(1, 2) # 1 + 2i
    assert c.__conjugate__() == ComplexNumber(1, -2)

def test_modulus():
    c = ComplexNumber(1, 2) # 1 + 2i
    # |c| = sqrt(1^2 + 2^2) = sqrt(1 + 4) = sqrt(5)
    assert c.__modulus__() == (5) ** 0.5

def test_cartesian_to_polar():
    c = ComplexNumber(1, 2) # 1 + 2i
    # r = sqrt(1^2 + 2^2) = sqrt(1 + 4) = sqrt(5)
    # theta = atan(2/1) = atan(2)
    c.cartesian_to_polar()
    assert c.get_r() == (5) ** 0.5
    assert c.get_theta() == math.atan(2)

def test_polar_to_cartesian():
    c = ComplexNumber((5) ** 0.5, math.atan(2), ComplexRepresentation.POLAR) # 1 + 2i
    # r = sqrt(1^2 + 2^2) = sqrt(1 + 4) = sqrt(5)
    # theta = atan(2/1) = atan(2)
    c.polar_to_catesian()
    assert abs(c.get_real() - 1) <= 0.0002
    assert abs(c.get_imaginary() - 2) <= 0.0002