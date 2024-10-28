import numpy as np
from constants import *

class SequenceGenerator:
    @staticmethod
    def make_two_normal_sequences():
        first_sequence = SequenceGenerator.make_normal_and_corellated_sequence(M0, D1, M*K, r)
        second_sequence = SequenceGenerator.make_normal_and_corellated_sequence(M1, D1, M*K, r)
        
        return (first_sequence, second_sequence)
    
    @staticmethod
    def make_normal_and_corellated_sequence(mean, std, size, correlation_coef):
        sequence = np.random.normal(mean, std, size)
        
        correlated_sequence = np.zeros(size)
        correlated_sequence[0] = sequence[0]
        
        for i in range(1, size):
            correlated_sequence[i] = correlation_coef*correlated_sequence[i - 1] + np.sqrt(1-correlation_coef**2)*sequence[i]
        
        return correlated_sequence
