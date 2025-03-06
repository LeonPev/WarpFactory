
import numpy as np
from Analyzer.changeTensorIndex import change_tensor_index

def c3_inv(matrix):
    return np.linalg.inv(matrix)

def three_plus_one_decomposer(metric):
    # Check that the metric is covariant and change index if not
    metric = change_tensor_index(metric, "covariant")

    # Covariant shift vector
    beta_down = np.array([metric["tensor"][0][1], metric["tensor"][0][2], metric["tensor"][0][3]])

    # Covariant gamma
    gamma_down = np.array([
        [metric["tensor"][1][1], metric["tensor"][1][2], metric["tensor"][1][3]],
        [metric["tensor"][2][1], metric["tensor"][2][2], metric["tensor"][2][3]],
        [metric["tensor"][3][1], metric["tensor"][3][2], metric["tensor"][3][3]]
    ])

    # Contravariant gamma
    gamma_up = c3_inv(gamma_down)

    # Contravariant shift vector
    s = metric["tensor"][0][0].shape
    beta_up = np.zeros((3, *s))
    for i in range(3):
        for j in range(3):
            beta_up[i] += gamma_up[i][j] * beta_down[j]

    # Lapse rate
    alpha = np.sqrt(np.sum(beta_up * beta_down, axis=0) - metric["tensor"][0][0])

    return alpha, beta_down, gamma_down, beta_up, gamma_up