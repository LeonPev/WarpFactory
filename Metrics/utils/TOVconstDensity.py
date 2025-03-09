
import numpy as np

def TOVconstDensity(R, M, rho, r):
    c = 299792458  # Speed of light
    G = 6.67430e-11  # Gravitational constant
    P = c**2 * rho * ((R * np.sqrt(R - 2 * G * M[-1] / c**2) - np.sqrt(R**3 - 2 * G * M[-1] * r**2 / c**2)) / (np.sqrt(R**3 - 2 * G * M[-1] * r**2 / c**2) - 3 * R * np.sqrt(R - 2 * G * M[-1] / c**2))) * (r < R)
    return P