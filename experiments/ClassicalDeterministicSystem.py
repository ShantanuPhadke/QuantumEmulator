from complex.ComplexMatrix import ComplexMatrix
from complex.ComplexNumber import ComplexNumber
from complex.ComplexVector import ComplexVector

class ClassicalDeterministicSystem:
    def __init__(self, start_state, transition_matrix):
        self.start_state = ComplexVector(len(start_state), [ComplexNumber(element, 0) for element in start_state])
        self.transition_matrix = ComplexMatrix(matrix=[[ComplexNumber(element, 0) for element in row] for row in transition_matrix])
    
    def simulate_state(self, time_clicks):
        state = self.start_state
        for _ in range(time_clicks):
            state = self.transition_matrix * state
        return state
    