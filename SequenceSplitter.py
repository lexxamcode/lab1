import numpy as np
from constants import *

class SequenceSpliiter:
    @staticmethod
    def split_sequence(sequence: np.ndarray):
        return np.hsplit(sequence, M)