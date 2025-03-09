
import numpy as np
from Metrics import utils

def threePlusOneBuilder(alpha, beta, gamma):
    gamma_up = utils.c3Inv(gamma)
    s = alpha.shape

    beta_up = np.zeros((3,) + s)
    for i in range(3):
        for j in range(3):
            beta_up[i] += gamma_up[i, j] * beta[j]

    metricTensor = np.zeros((4, 4) + s)

    metricTensor[0, 0] = -alpha**2
    for i in range(3):
        metricTensor[0, 0] += beta_up[i] * beta[i]

    for i in range(1, 4):
        metricTensor[0, i] = beta[i - 1]
        metricTensor[i, 0] = metricTensor[0, i]

    for i in range(1, 4):
        for j in range(1, 4):
            metricTensor[i, j] = gamma[i - 1, j - 1]

    return metricTensor