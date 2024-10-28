import numpy as np
from constants import *

class PdfCalculator:
    @staticmethod
    def Calculate(sequence, mean, std, size, correlation_coef):
        B = np.zeros((size, size))
        i = 0
        while i < size:
            j = 0
            while j < size:
                B[i][j] = std * correlation_coef * np.abs(i - j)
                j += 1
            i += 1
        
        mean_array = np.full(size, mean)
        p = np.dot(np.dot(np.array(sequence - mean_array).T, np.linalg.inv(B)), (sequence - mean_array))
        
        detB = np.linalg.det(B)
        
        result = 1/((2*np.pi*detB)**(size/2)) * np.e**(p/(-2))
        return result