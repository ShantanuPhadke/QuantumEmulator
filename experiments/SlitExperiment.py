from complex.ComplexMatrix import ComplexMatrix
from complex.ComplexNumber import ComplexNumber
from complex.ComplexVector import ComplexVector
from experiments.ClassicalProbabilisticSystem import ClassicalProbabilisticSystem

class SlitExperiment():
    # slit_to_target_probabilities: dictionary of tuples to probabilities
    # Assume both slit and target indices are 0-indexed
    def __init__(self, start_state, num_slits, num_targets, slit_to_target_probabilities):
        self.num_slits = num_slits
        self.num_targets = num_targets
        self.size = 1 + self.num_slits + self.num_targets
        self.transitions = {}
        # First define the probabilities for going from the start point to each of the slits (equally likely)
        for slit in range(self.num_slits):
            self.transitions[(0, 1+slit)] = 1/self.num_slits
        # Next define the probabilities for going from each slit to each target
        for (slit, target) in slit_to_target_probabilities:
            self.transitions[(1+slit, 1+self.num_slits+target)] = slit_to_target_probabilities[(slit, target)]
        # Finally, set the probability of staying at each of the targets to 1
        for target in range(self.num_targets):
            self.transitions[(1+self.num_slits+target, 1+self.num_slits+target)] = 1
        self.system = ClassicalProbabilisticSystem(start_state, self.transitions)

    def simulate(self):
        return {
            'transition_matrix': self.system.transition_matrix, 'end_state': self.system.simulate_state(2)
        }