
import numpy as np

def take_finite_difference_1_2(A, k, delta):
    s = A.shape
    B = np.zeros(s)

    if s[k] >= 3:
        if k == 0:
            B[1:-1] = (A[2:] - A[:-2]) / (2 * delta)
            B[0] = B[1]
            B[-1] = B[-2]
        elif k == 1:
            B[:, 1:-1] = (A[:, 2:] - A[:, :-2]) / (2 * delta)
            B[:, 0] = B[:, 1]
            B[:, -1] = B[:, -2]
        elif k == 2:
            B[:, :, 1:-1] = (A[:, :, 2:] - A[:, :, :-2]) / (2 * delta)
            B[:, :, 0] = B[:, :, 1]
            B[:, :, -1] = B[:, :, -2]
        elif k == 3:
            B[:, :, :, 1:-1] = (A[:, :, :, 2:] - A[:, :, :, :-2]) / (2 * delta)
            B[:, :, :, 0] = B[:, :, :, 1]
            B[:, :, :, -1] = B[:, :, :, -2]

    return B