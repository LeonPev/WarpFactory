
import numpy as np

def ricci_scalar(R_munu, gu):
    R = 0
    for mu in range(4):
        for nu in range(4):
            R += gu[mu, nu] * R_munu[mu, nu]
    return R