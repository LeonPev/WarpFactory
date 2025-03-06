
import numpy as np
from Units.Universal_Constants import c, G, pi

def energy_density_2(E, gu, units):
    G_local = G * units[2]**2 * units[1] / units[0]**3
    c_local = c * units[2] / units[0]
    en_den_ = (c_local**4 / (8 * pi * G_local)) * E
    en_den = np.zeros_like(en_den_)
    for mu in range(4):
        for nu in range(4):
            for alpha in range(4):
                for beta in range(4):
                    en_den[mu, nu] += en_den_[alpha, beta] * gu[alpha, mu] * gu[beta, nu]
    return en_den