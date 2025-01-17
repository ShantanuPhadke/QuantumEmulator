from complex.ComplexMatrix import ComplexMatrix
from complex.ComplexNumber import ComplexNumber
from complex.ComplexVector import ComplexVector

class ClassicalDeterministicSystem:
    # transitions = a list of tuples that each signify individual edges between vertices
    # Ex: tuple (i, j) = there is an edge between vertex i and vertex j
    # The constructor will produce the appropriate transition matrix from this.
    def __init__(self, start_state, transitions):
        self.start_state = ComplexVector(len(start_state), [ComplexNumber(element, 0) for element in start_state])
        self.num_states = len(start_state)
        self.transition_matrix = ComplexMatrix(matrix=[
            [
                ComplexNumber(1, 0) if (origin, dest) in transitions else ComplexNumber(0,0) for origin in range(self.num_states)
            ] for dest in range(self.num_states)
        ])

    
    def simulate_state(self, time_clicks):
        state = self.start_state
        for _ in range(time_clicks):
            state = self.transition_matrix * state
        return state
    