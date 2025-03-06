
import numpy as np

def einstein_tensor_2(R_munu, R, gl):
    E = np.zeros_like(R_munu)
    for mu in range(4):
        for nu in range(4):
            E[mu, nu] = R_munu[mu, nu] - 0.5 * gl[mu, nu] * R
    return E