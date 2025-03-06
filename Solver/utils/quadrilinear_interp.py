
from .trilinear_interp import trilinear_interp
import numpy as np

def quadrilinear_interp(F, x):
    t1 = int(np.floor(x[0]))
    t2 = int(np.ceil(x[0]))
    t = x[0]

    if t1 == t2:
        c = trilinear_interp(np.squeeze(F[t1]), x[1:])
    else:
        c1 = trilinear_interp(np.squeeze(F[t1]), x[1:])
        c2 = trilinear_interp(np.squeeze(F[t2]), x[1:])

        c = (c1 * (t2 - t) + c2 * (t - t1)) / (t2 - t1)

    return c