import pytest
from experiments.ClassicalDeterministicSystem import ClassicalDeterministicSystem
from complex.ComplexVector import ComplexVector
from complex.ComplexNumber import ComplexNumber

def test_classical_deterministic_system():
    c = ClassicalDeterministicSystem([6, 2, 1, 5, 3, 10], [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 1, 0]])
    assert c.simulate_state(1) == ComplexVector(6, [ComplexNumber(0, 0), ComplexNumber(0, 0), ComplexNumber(12, 0), ComplexNumber(5, 0), ComplexNumber(1, 0), ComplexNumber(9, 0)])