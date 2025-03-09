
import numpy as np

def shapeFunction_Alcubierre(r, R, sigma):
    f = (np.tanh(sigma * (R + r)) + np.tanh(sigma * (R - r))) / (2 * np.tanh(R * sigma))
    return f