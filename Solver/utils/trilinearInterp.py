
import numpy as np

def trilinear_interp(F, x):
    x = x + 1e-8
    xd = (x[0] - np.floor(x[0])) / (np.ceil(x[0]) - np.floor(x[0]))
    yd = (x[1] - np.floor(x[1])) / (np.ceil(x[1]) - np.floor(x[1]))
    zd = (x[2] - np.floor(x[2])) / (np.ceil(x[2]) - np.floor(x[2]))

    c00 = F(np.floor(x[0]), np.floor(x[1]), np.floor(x[2])) * (1 - xd) + F(np.ceil(x[0]), np.floor(x[1]), np.floor(x[2])) * xd
    c01 = F(np.floor(x[0]), np.floor(x[1]), np.ceil(x[2])) * (1 - xd) + F(np.ceil(x[0]), np.floor(x[1]), np.ceil(x[2])) * xd
    c10 = F(np.floor(x[0]), np.ceil(x[1]), np.floor(x[2])) * (1 - xd) + F(np.ceil(x[0]), np.ceil(x[1]), np.floor(x[2])) * xd
    c11 = F(np.floor(x[0]), np.ceil(x[1]), np.ceil(x[2])) * (1 - xd) + F(np.ceil(x[0]), np.ceil(x[1]), np.ceil(x[2])) * xd

    c0 = c00 * (1 - yd) + c10 * yd
    c1 = c01 * (1 - yd) + c11 * yd

    c = c0 * (1 - zd) + c1 * zd

    return c