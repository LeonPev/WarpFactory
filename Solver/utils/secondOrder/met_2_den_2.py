
import numpy as np
from .c4_inv_2 import c4_inv_2
from .ricci_t_2 import ricci_tensor_2
from .ricci_s_2 import ricci_scalar_2
from .ein_t_2 import einstein_tensor_2
from .ein_e_2 import energy_density_2

def met_2_den_2(metric_tensor, delta=np.array([1, 1, 1, 1]), units=np.array([1, 1, 1])):
    gl = metric_tensor
    gu = c4_inv_2(gl)
    r_munu = ricci_tensor_2(gu, gl, delta)
    r = ricci_scalar_2(r_munu, gu)
    e = einstein_tensor_2(r_munu, r, gl)
    energy_density = energy_density_2(e, gu, units)
    return energy_density