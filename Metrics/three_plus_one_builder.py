
import numpy as np
from .three_plus_one_decomposer import c3_inv

def three_plus_one_builder(alpha, beta, gamma):
    gamma_up = c3_inv(gamma)

    s = alpha.shape
    beta_up = np.zeros((3, *s))
    for i in range(3):
        for j in range(3):
            beta_up[i] += gamma_up[i, j] * beta[j]

    metric_tensor = np.zeros((4, 4, *s))

    metric_tensor[0, 0] = -alpha**2 + np.sum(beta_up * beta, axis=0)

    for i in range(1, 4):
        metric_tensor[0, i] = beta[i-1]
        metric_tensor[i, 0] = metric_tensor[0, i]

    for i in range(1, 4):
        for j in range(1, 4):
            metric_tensor[i, j] = gamma[i-1, j-1]

    return metric_tensor