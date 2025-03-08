
import numpy as np

def c3_inv(matrix):
    if matrix.shape != (3, 3):
        raise ValueError("Matrix must be 3x3")

    det = np.linalg.det(matrix)
    if det == 0:
        raise ValueError("Matrix is singular")

    r = matrix
    inv_matrix = np.array([
        [(r[1, 1] * r[2, 2] - r[1, 2] * r[2, 1]) / det, (r[0, 2] * r[2, 1] - r[0, 1] * r[2, 2]) / det, (r[0, 1] * r[1, 2] - r[0, 2] * r[1, 1]) / det],
        [(r[1, 2] * r[2, 0] - r[1, 0] * r[2, 2]) / det, (r[0, 0] * r[2, 2] - r[0, 2] * r[2, 0]) / det, (r[0, 2] * r[1, 0] - r[0, 0] * r[1, 2]) / det],
        [(r[1, 0] * r[2, 1] - r[1, 1] * r[2, 0]) / det, (r[0, 1] * r[2, 0] - r[0, 0] * r[2, 1]) / det, (r[0, 0] * r[1, 1] - r[0, 1] * r[1, 0]) / det]
    ])
    return inv_matrix