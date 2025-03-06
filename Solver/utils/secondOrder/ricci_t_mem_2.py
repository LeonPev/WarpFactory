
import numpy as np
from Units.Universal_Constants import c
from .take_finite_difference_1_2 import take_finite_difference_1_2
from .take_finite_difference_2_2 import take_finite_difference_2_2

def ricci_tensor_mem_2(gu, gl, delta):
    s = gl[0, 0].shape
    R_munu = np.zeros((4, 4, *s))

    diff_1_gl = np.zeros((4, 4, 4, *s))

    for i in range(4):
        for j in range(i, 4):
            for k in range(4):
                diff_1_gl[i, j, k] = take_finite_difference_1_2(gl[i, j], k, delta)
                if k == 0:
                    diff_1_gl[i, j, k] /= c

    # Assign symmetric values
    for k in range(4):
        diff_1_gl[1, 0, k] = diff_1_gl[0, 1, k]
        diff_1_gl[2, 0, k] = diff_1_gl[0, 2, k]
        diff_1_gl[2, 1, k] = diff_1_gl[1, 2, k]
        diff_1_gl[3, 0, k] = diff_1_gl[0, 3, k]
        diff_1_gl[3, 1, k] = diff_1_gl[1, 3, k]
        diff_1_gl[3, 2, k] = diff_1_gl[2, 3, k]

    for i in range(4):
        for j in range(i, 4):
            for a in range(4):
                for b in range(4):
                    term1 = take_finite_difference_2_2(gl[i, j], a, b, delta)
                    term2 = take_finite_difference_2_2(gl[a, b], i, j, delta)
                    term3 = take_finite_difference_2_2(gl[i, b], j, a, delta)
                    term4 = take_finite_difference_2_2(gl[j, b], i, a, delta)
                    R_munu[i, j] -= 0.5 * (term1 + term2 - term3 - term4) * gu[a, b]
                    for c in range(4):
                        for d in range(4):
                            R_munu[i, j] += 0.5 * (0.5 * diff_1_gl[a, c, i] * diff_1_gl[b, d, j] + diff_1_gl[i, c, a] * diff_1_gl[j, d, b] - diff_1_gl[i, c, a] * diff_1_gl[j, b, d]) * gu[a, b] * gu[c, d]
                            R_munu[i, j] -= 0.25 * (diff_1_gl[j, c, i] + diff_1_gl[i, c, j] - diff_1_gl[i, j, c]) * (2 * diff_1_gl[b, d, a] - diff_1_gl[a, b, d]) * gu[a, b] * gu[c, d]

            if i != j:
                R_munu[j, i] = R_munu[i, j]

    return R_munu