
from .take_finite_difference_1 import take_finite_difference_1
from .get_christoffel_sym import get_christoffel_sym
import numpy as np

def cov_div(gl, gu, vec_u, vec_d, idx_div, idx_vec, delta, stair_sel):
    diff_1_gl = np.zeros((4, 4, 4, *gl[0, 0].shape))
    s = gl[0, 0].shape
    for i in range(4):
        for j in range(4):
            phiphi_flag = (i == 1 and j == 1 and s[1] == 1)
            for k in range(4):
                diff_1_gl[i, j, k] = take_finite_difference_1(gl[i, j], k, delta, phiphi_flag)

    if stair_sel == 0:
        cd_vec = take_finite_difference_1(vec_d[idx_vec], idx_div, delta)
        for i in range(4):
            gamma = get_christoffel_sym(gu, diff_1_gl, i, idx_vec, idx_div)
            cd_vec -= gamma * vec_d[i]
    elif stair_sel == 1:
        cd_vec = take_finite_difference_1(vec_u[idx_vec], idx_div, delta)
        for i in range(4):
            gamma = get_christoffel_sym(gu, diff_1_gl, idx_vec, idx_div, i)
            cd_vec += gamma * vec_u[i]
    else:
        raise ValueError("Invalid variance selected")

    return cd_vec