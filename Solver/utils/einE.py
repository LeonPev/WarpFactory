
import numpy as np
from Units.Universal_Constants import c, G, pi

def energy_density(E, gu):
    enDen_ = (c**4 / (8 * pi * G)) * E
    enDen = np.zeros_like(enDen_)
    for mu in range(4):
        for nu in range(4):
            for alpha in range(4):
                for beta in range(4):
                    enDen[mu, nu] += enDen_[alpha, beta] * gu[alpha, mu] * gu[beta, nu]
    return enDen