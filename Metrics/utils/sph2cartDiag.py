
import numpy as np

def sph2cartDiag(theta, phi, g11_sph, g22_sph):
    g11_cart = g11_sph
    E = g22_sph

    cosPhi = 0.0 if abs(phi) == np.pi / 2 else np.cos(phi)
    cosTheta = 0.0 if abs(theta) == np.pi / 2 else np.cos(theta)

    g22_cart = (E * cosPhi**2 * np.sin(theta)**2 + (cosPhi**2 * cosTheta**2)) + np.sin(phi)**2
    g33_cart = (E * np.sin(phi)**2 * np.sin(theta)**2 + (cosTheta**2 * np.sin(phi)**2)) + cosPhi**2
    g44_cart = (E * cosTheta**2 + np.sin(theta)**2)

    g23_cart = (E * cosPhi * np.sin(phi) * np.sin(theta)**2 + (cosPhi * cosTheta**2 * np.sin(phi)) - cosPhi * np.sin(phi))
    g24_cart = (E * cosPhi * cosTheta * np.sin(theta) - (cosPhi * cosTheta * np.sin(theta)))
    g34_cart = (E * cosTheta * np.sin(phi) * np.sin(theta) - (cosTheta * np.sin(phi) * np.sin(theta)))

    return g11_cart, g22_cart, g23_cart, g24_cart, g33_cart, g34_cart, g44_cart