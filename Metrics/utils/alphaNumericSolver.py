
import numpy as np
from scipy.integrate import cumtrapz

def alphaNumericSolver(M, P, R, r):
    G = 6.67430e-11  # Gravitational constant
    c = 299792458  # Speed of light

    c = 299792458  # Speed of light
    dalpha = (G * M / c**2 + 4 * np.pi * G * r**3 * P / c**4) / (r**2 - 2 * G * M * r / c**2)
    dalpha[0] = 0
    alphaTemp = cumtrapz(dalpha, r)
    C = 1/2 * np.log(1 - 2 * G * M[-1] / r[-1] / c**2)
    offset = C - alphaTemp[-1]
    alpha = alphaTemp + offset

    return alpha