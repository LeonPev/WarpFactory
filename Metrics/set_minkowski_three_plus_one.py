
import numpy as np

def set_minkowski_three_plus_one(grid_size):
    alpha = np.ones(grid_size)
    beta = np.zeros((3, *grid_size))
    gamma = np.zeros((3, 3, *grid_size))
    for i in range(3):
        gamma[i, i] = 1
    return alpha, beta, gamma