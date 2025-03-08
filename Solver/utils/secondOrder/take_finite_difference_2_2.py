
import numpy as np

def take_finite_difference_2_2(A, k1, k2, delta):
    s = A.shape
    B = np.zeros(s)

    if s[k1] >= 3 and s[k2] >= 3:
        if k1 == k2:
            if k1 == 0:
                B[1:-1] = (A[2:] - 2 * A[1:-1] + A[:-2]) / delta[k1]**2
                B[0] = B[1]
                B[-1] = B[-2]
            elif k1 == 1:
                B[:, 1:-1] = (A[:, 2:] - 2 * A[:, 1:-1] + A[:, :-2]) / delta[k1]**2
                B[:, 0] = B[:, 1]
                B[:, -1] = B[:, -2]
            elif k1 == 2:
                B[:, :, 1:-1] = (A[:, :, 2:] - 2 * A[:, :, 1:-1] + A[:, :, :-2]) / delta[k1]**2
                B[:, :, 0] = B[:, :, 1]
                B[:, :, -1] = B[:, :, -2]
            elif k1 == 3:
                B[:, :, :, 1:-1] = (A[:, :, :, 2:] - 2 * A[:, :, :, 1:-1] + A[:, :, :, :-2]) / delta[k1]**2
                B[:, :, :, 0] = B[:, :, :, 1]
                B[:, :, :, -1] = B[:, :, :, -2]
        else:
            kL = max(k1, k2)
            kS = min(k1, k2)

            sl = [slice(None)] * 4
            sl[kS] = slice(1, -1)
            sl[kL] = slice(1, -1)

            def f(i, kS, kL, x, y):
                return tuple(x if j == kS else y for j in range(4))

            B[tuple(sl)] = 1 / (4 * delta[kS] * delta[kL]) * (
                A[f(0, kS, kL, 0, 0)] - A[f(1, kS, kL, 0, 2)] - A[f(2, kS, kL, 2, 0)] + A[f(3, kS, kL, 2, 2)]
            )

    return B