from numpy.random import random
import numpy as np


def BSC(input_bits, p):

    output_bits = input_bits.copy()
    error_bits = (random(len(output_bits)) < p)
    suma = np.sum(error_bits)
    output_bits[error_bits] = 1 - output_bits[error_bits]

    return output_bits
