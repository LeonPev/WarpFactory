
import numpy as np

def c4_inv(matrix):
    if matrix.shape != (4, 4):
        raise ValueError("Matrix must be 4x4")

    return np.linalg.inv(matrix)