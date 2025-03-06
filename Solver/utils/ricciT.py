
import numpy as np
from .take_finite_difference_1 import take_finite_difference_1
from .take_finite_difference_2 import take_finite_difference_2
from Units.Universal_Constants import c

def ricci_tensor(gu, gl, delta):
    s = gl[0, 0].shape
    R_munu = np.zeros((4, 4, *s))

    diff_1_gl = np.zeros((4, 4, 4, *s))
    diff_2_gl = np.zeros((4, 4, 4, 4, *s))

    for i in range(4):
        for j in range(i, 4):
            for k in range(4):
                diff_1_gl[i, j, k] = take_finite_difference_1(gl[i, j], k, delta)
                if k == 0:
                    diff_1_gl[i, j, k] /= c
                for n in range(k, 4):
                    diff_2_gl[i, j, k, n] = take_finite_difference_2(gl[i, j], k, n, delta)
                    if (n == 0 and k != 0) or (n != 0 and k == 0):
                        diff_2_gl[i, j, k, n] /= c
                    elif n == 0 and k == 0:
                        diff_2_gl[i, j, k, n] /= (c**2)
                    if k != n:
                        diff_2_gl[i, j, n, k] = diff_2_gl[i, j, k, n]

    # Assign symmetric values
    for k in range(4):
        diff_1_gl[1, 0, k] = diff_1_gl[0, 1, k]
        diff_1_gl[2, 0, k] = diff_1_gl[0, 2, k]
        diff_1_gl[2, 1, k] = diff_1_gl[1, 2, k]
        diff_1_gl[3, 0, k] = diff_1_gl[0, 3, k]
        diff_1_gl[3, 1, k] = diff_1_gl[1, 3, k]
        diff_1_gl[3, 2, k] = diff_1_gl[2, 3, k]
        for n in range(4):
            diff_2_gl[1, 0, k, n] = diff_2_gl[0, 1, k, n]
            diff_2_gl[2, 0, k, n] = diff_2_gl[0, 2, k, n]
            diff_2_gl[2, 1, k, n] = diff_2_gl[1, 2, k, n]
            diff_2_gl[3, 0, k, n] = diff_2_gl[0, 3, k, n]
            diff_2_gl[3, 1, k, n] = diff_2_gl[1, 3, k, n]
            diff_2_gl[3, 2, k, n] = diff_2_gl[2, 3, k, n]

    # Construct Ricci tensor
    for i in range(4):
        for j in range(i, 4):
            R_munu_temp = np.zeros(s)
            for a in range(4):
                for b in range(4):
                    R_munu_temp_2 = np.zeros(s)
                    # First term
                    R_munu_temp_2 -= (diff_2_gl[i, j, a, b] + diff_2_gl[a, b, i, j] - diff_2_gl[i, b, j, a] - diff_2_gl[j, b, i, a])
                    for r in range(4):
                        R_munu_temp_3 = np.zeros(s)
                        R_munu_temp_4 = np.zeros(s)
                        R_munu_temp_5 = np.zeros(s)
                        for d in range(4):
                            # Second term
                            R_munu_temp_3 += diff_1_gl[b, d, j] * gu[r, d]
                            R_munu_temp_4 += (diff_1_gl[j, d, b] - diff_1_gl[j, b, d]) * gu[r, d]
                            # Third term
                            R_munu_temp_5 += gl[a, b] * (diff_2_gl[i, r, j, d] + diff_2_gl[j, r, i, d] - diff_2_gl[r, i, j, d] - diff_2_gl[j, d, i, r])
                        R_munu_temp_2 += gl[a,r] * (R_munu_temp_3 + R_munu_temp_4)
                        R_munu_temp_2 += 0.5 * gu[a,r] * R_munu_temp_5
                    R_munu_temp += 0.5 * gu[a, b] * R_munu_temp_2
            R_munu[i, j] = R_munu_temp
            if i != j:
                R_munu[j, i] = R_munu_temp

    return R_munu