
import numpy as np

def take_finite_difference_2(A, k1, k2, delta, phiphi_flag=False):
    s = A.shape
    B = np.zeros(s)

    if s[k1] >= 5 and s[k2] >= 5:
        if k1 == k2:
            if k1 == 0:
                B[2:-2] = (-(A[4:] + A[:-4]) + 16 * (A[3:-1] + A[1:-3]) - 30 * A[2:-2]) / (12 * delta**2)
                B[:2] = B[2]
                B[-2:] = B[-3]
            elif k1 == 1:
                B[:, 2:-2] = (-(A[:, 4:] + A[:, :-4]) + 16 * (A[:, 3:-1] + A[:, 1:-3]) - 30 * A[:, 2:-2]) / (12 * delta**2)
                B[:, :2] = B[:, 2]
                B[:, -2:] = B[:, -3]
            elif k1 == 2:
                B[:, :, 2:-2] = (-(A[:, :, 4:] + A[:, :, :-4]) + 16 * (A[:, :, 3:-1] + A[:, :, 1:-3]) - 30 * A[:, :, 2:-2]) / (12 * delta**2)
                if phiphi_flag:
                    B[:, :, :2] = -2
                    B[:, :, -2:] = 2
                else:
                    B[:, :, :2] = B[:, :, 2]
                    B[:, :, -2:] = B[:, :, -3]
            elif k1 == 3:
                B[:, :, :, 2:-2] = (-(A[:, :, :, 4:] + A[:, :, :, :-4]) + 16 * (A[:, :, :, 3:-1] + A[:, :, :, 1:-3]) - 30 * A[:, :, :, 2:-2]) / (12 * delta**2)
                B[:, :, :, :2] = B[:, :, :, 2]
                B[:, :, :, -2:] = B[:, :, :, -3]
        else:
            kL = max(k1, k2)
            kS = min(k1, k2)

            x2 = slice(4, None)
            x1 = slice(3, -1)
            x0 = slice(2, -2)
            x_1 = slice(1, -3)
            x_2 = slice(0, -4)

            y2 = slice(4, None)
            y1 = slice(3, -1)
            y0 = slice(2, -2)
            y_1 = slice(1, -3)
            y_2 = slice(0, -4)
            
            sl = [slice(None)] * 4

            if kS == 0:
                sl[kS] = x0
                if kL == 1:
                    sl[kL] = y0
                    B[tuple(sl)] = 1 / (12**2 * delta**2) * (
                        -(-(A[tuple([x2 if i == kS else y2 for i in range(4)])]  - A[tuple([x_2 if i == kS else y2 for i in range(4)])] ) + 8 * (A[tuple([x1 if i == kS else y2 for i in range(4)])]  - A[tuple([x_1 if i == kS else y2 for i in range(4)])])) +
                        (-(A[tuple([x2 if i == kS else y_2 for i in range(4)])] - A[tuple([x_2 if i == kS else y_2 for i in range(4)])]) + 8 * (A[tuple([x1 if i == kS else y_2 for i in range(4)])] - A[tuple([x_1 if i == kS else y_2 for i in range(4)])])) +
                        8 * (-(A[tuple([x2 if i == kS else y1 for i in range(4)])]  - A[tuple([x_2 if i == kS else y1 for i in range(4)])] ) + 8 * (A[tuple([x1 if i == kS else y1 for i in range(4)])]  - A[tuple([x_1 if i == kS else y1 for i in range(4)])])) -
                        8 * (-(A[tuple([x2 if i == kS else y_1 for i in range(4)])] - A[tuple([x_2 if i == kS else y_1 for i in range(4)])]) + 8 * (A[tuple([x1 if i == kS else y_1 for i in range(4)])] - A[tuple([x_1 if i == kS else y_1 for i in range(4)])]))
                    )
                # ... (rest of the cases for kL)

    return B