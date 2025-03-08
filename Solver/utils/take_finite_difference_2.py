
import numpy as np

def take_finite_difference_2(A, k1, k2, delta, phiphi_flag=False):
    s = A.shape
    B = np.zeros(s)

    if s[k1] >= 5 and s[k2] >= 5:
        if k1 == k2:
            if k1 == 0:
                B[2:-2] = (-(A[4:] + A[:-4]) + 16 * (A[3:-1] + A[1:-3]) - 30 * A[2:-2]) / (12 * delta[k1]**2)
                B[:2] = B[2]
                B[-2:] = B[-3]
            elif k1 == 1:
                B[:, 2:-2] = (-(A[:, 4:] + A[:, :-4]) + 16 * (A[:, 3:-1] + A[:, 1:-3]) - 30 * A[:, 2:-2]) / (12 * delta[k1]**2)
                B[:, :2] = B[:, 2]
                B[:, -2:] = B[:, -3]
            elif k1 == 2:
                B[:, :, 2:-2] = (-(A[:, :, 4:] + A[:, :, :-4]) + 16 * (A[:, :, 3:-1] + A[:, :, 1:-3]) - 30 * A[:, :, 2:-2]) / (12 * delta[k1]**2)
                if phiphi_flag:
                    B[:, :, :2] = -2
                    B[:, :, -2:] = 2
                else:
                    B[:, :, :2] = B[:, :, 2]
                    B[:, :, -2:] = B[:, :, -3]
            elif k1 == 3:
                B[:, :, :, 2:-2] = (-(A[:, :, :, 4:] + A[:, :, :, :-4]) + 16 * (A[:, :, :, 3:-1] + A[:, :, :, 1:-3]) - 30 * A[:, :, :, 2:-2]) / (12 * delta[k1]**2)
                B[:, :, :, :2] = B[:, :, :, 2]
                B[:, :, :, -2:] = B[:, :, :, -3]
        else:
            kL = max(k1, k2)
            kS = min(k1, k2)

            sl = [slice(None)] * 4
            sl[kS] = slice(2, -2)
            sl[kL] = slice(2, -2)

            def f(i, kS, kL, x, y):
                return [x if j == kS else y for j in range(4)]

            B[tuple(sl)] = 1 / (12**2 * delta[kS] * delta[kL]) * (
                -(-(A[tuple(f(0, kS, kL, 4, 4))] - A[tuple(f(1, kS, kL, 0, 4))]) + 8 * (A[tuple(f(2, kS, kL, 3, 4))] - A[tuple(f(3, kS, kL, 1, 4))])) +
                (-(A[tuple(f(4, kS, kL, 4, 0))] - A[tuple(f(5, kS, kL, 0, 0))]) + 8 * (A[tuple(f(6, kS, kL, 3, 0))] - A[tuple(f(7, kS, kL, 1, 0))])) +
                8 * (-(A[tuple(f(8, kS, kL, 4, 3))] - A[tuple(f(9, kS, kL, 0, 3))]) + 8 * (A[tuple(f(10, kS, kL, 3, 3))] - A[tuple(f(11, kS, kL, 1, 3))])) -
                8 * (-(A[tuple(f(12, kS, kL, 4, 1))] - A[tuple(f(13, kS, kL, 0, 1))]) + 8 * (A[tuple(f(14, kS, kL, 3, 1))] - A[tuple(f(15, kS, kL, 1, 1))]))
            )

    return B