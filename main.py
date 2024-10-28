from SequenceGenerator import SequenceGenerator
from SequenceSplitter import SequenceSpliiter
from PdfCalculator import PdfCalculator
from constants import *
import matplotlib.pyplot as plt

if __name__ == "__main__":
    first_sequence, second_sequence = SequenceGenerator.make_two_normal_sequences()
    splitted_first = SequenceSpliiter.split_sequence(first_sequence)
    splitted_second = SequenceSpliiter.split_sequence(second_sequence)
    # plt.plot(splitted_first[0])
    # plt.plot(splitted_second[0])
    # plt.show()
    
    pdf = PdfCalculator.Calculate(splitted_first[0], M1, D0, len(splitted_first[0]), r)
    print(pdf)