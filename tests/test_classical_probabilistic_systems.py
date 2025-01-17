import pytest
from experiments.ClassicalProbabilisticSystem import ClassicalProbabilisticSystem
from experiments.SlitExperiment import SlitExperiment
from complex.ComplexVector import ComplexVector
from complex.ComplexNumber import ComplexNumber

def test_classical_deterministic_system():
    c = ClassicalProbabilisticSystem([1/6, 1/6, 2/3], {(0,1): 1/3, (0,2): 2/3, (1,0): 1/6, (1,1): 1/2, (1,2): 1/3, (2,0): 5/6, (2,1): 1/6})
    assert c.simulate_state(1) == ComplexVector(3, [ComplexNumber(21/36, 0), ComplexNumber(9/36, 0), ComplexNumber(6/36, 0)])

def test_slit_experiment():
    s = SlitExperiment(
        [1,0,0,0,0,0,0,0], 2, 5, {(0,0): 1/3, (0,1): 1/3, (0,2): 1/3, (1,2): 1/3, (1,3): 1/3, (1,4): 1/3}
    )
    assert s.simulate()['end_state'] == ComplexVector(8, [
        ComplexNumber(0,0), ComplexNumber(0,0), ComplexNumber(0,0), ComplexNumber(1/6,0), ComplexNumber(1/6,0), ComplexNumber(1/3,0), ComplexNumber(1/6,0), ComplexNumber(1/6,0)
    ])