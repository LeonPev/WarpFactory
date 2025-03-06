
from .c4Inv import c4_inv
from .ricciT import ricci_tensor
from .ricciS import ricci_scalar
from .einT import einstein_tensor
from .einE import energy_density
import numpy as np

def met2den(gl, delta=np.array([1, 1, 1, 1])):
    # Calculate metric tensor inverse
    gu = c4_inv(gl)

    # Calculate the Ricci tensor
    r_munu = ricci_tensor(gu, gl, delta)

    # Calculate the Ricci scalar
    r = ricci_scalar(r_munu, gu)

    # Calculate Einstein tensor
    e = einstein_tensor(r_munu, r, gl)

    # Calculate Energy density
    energy_density_tensor = energy_density(e, gu)

    return energy_density_tensor