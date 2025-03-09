
import numpy as np

def compactSigmoid(r, R1, R2, sigma, Rbuff):
    f = np.abs(1. / (np.exp(((R2 - R1 - 2 * Rbuff) * (sigma + 2)) / 2 * (1. / (r - R2 + Rbuff) + 1. / (r - R1 - Rbuff))) + 1) * (r > R1 + Rbuff) * (r < R2 - Rbuff) + (r >= R2 - Rbuff) - 1)
    if np.any(np.isinf(f)) or np.any(~np.isreal(f)):
        raise ValueError('compact sigmoid returns non-numeric values!')
    return f