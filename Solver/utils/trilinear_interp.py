
import numpy as np

def trilinear_interp(F, x):
    x = np.asarray(x)
    x += 1e-8  # Small offset to avoid division by zero

    xd = (x[0] - np.floor(x[0])) / (np.ceil(x[0]) - np.floor(x[0]))
    yd = (x[1] - np.floor(x[1])) / (np.ceil(x[1]) - np.floor(x[1]))
    zd = (x[2] - np.floor(x[2])) / (np.ceil(x[2]) - np.floor(x[2]))

    c00 = F[int(np.floor(x[0])), int(np.floor(x[1])), int(np.floor(x[2]))] * (1 - xd) + \
         F[int(np.ceil(x[0])), int(np.floor(x[1])), int(np.floor(x[2]))] * xd
    c01 = F[int(np.floor(x[0])), int(np.floor(x[1])), int(np.ceil(x[2]))] * (1 - xd) + \
         F[int(np.ceil(x[0])), int(np.floor(x[1])), int(np.ceil(x[2]))] * xd
    c10 = F[int(np.floor(x[0])), int(np.ceil(x[1])), int(np.floor(x[2]))] * (1 - xd) + \
         F[int(np.ceil(x[0])), int(np.ceil(x[1])), int(np.floor(x[2]))] * xd
    c11 = F[int(np.floor(x[0])), int(np.ceil(x[1])), int(np.ceil(x[2]))] * (1 - xd) + \
         F[int(np.ceil(x[0])), int(np.ceil(x[1])), int(np.ceil(x[2]))] * xd

    c0 = c00 * (1 - yd) + c10 * yd
    c1 = c01 * (1 - yd) + c11 * yd

    c = c0 * (1 - zd) + c1 * zd

    return c