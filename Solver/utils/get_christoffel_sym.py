
import numpy as np

def get_christoffel_sym(gu, diff_1_gl, i, k, l):
    gamma = 0
    for m in range(4):
        gamma += 0.5 * gu[i, m] * (diff_1_gl[m, k, l] + diff_1_gl[m, l, k] - diff_1_gl[k, l, m])
    return gamma