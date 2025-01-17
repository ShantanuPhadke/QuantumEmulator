from complex.ComplexMatrix import ComplexMatrix
from complex.ComplexNumber import ComplexNumber
from complex.ComplexVector import ComplexVector
from experiments.ClassicalDeterministicSystem import ClassicalDeterministicSystem

class ClassicalProbabilisticSystem(ClassicalDeterministicSystem):
    # transitions: A dictionary of (to_vertex, from_vertex) tuples to probabilities
    # Just like in the case of the Classical Deterministic System class, the constructor will make the
    # appropriate transition matrix from this data.
    def __init__(self, start_state, transitions):
        # TODO: use the python equivalent of super here
        self.start_state = ComplexVector(len(start_state), [ComplexNumber(element, 0) for element in start_state])
        self.num_states = len(start_state)
        self.transition_matrix = ComplexMatrix(matrix=[
            [
                ComplexNumber(transitions[(origin, dest)], 0) if (origin, dest) in transitions else ComplexNumber(0, 0) for origin in range(self.num_states)
            ] for dest in range(self.num_states)
        ])
    

