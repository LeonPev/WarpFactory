
import numpy as np

def get_eulerian_transformation_matrix(g, coords):
    if len(g.shape) == 2:
        # For single point metrics
        factor0 = g[3, 3]
        factor1 = -g[2, 3]**2 + g[2, 2] * factor0
        factor2 = 2 * g[1, 2] * g[1, 3] * g[2, 3] - factor0 * g[1, 2]**2 - g[2, 2] * g[1, 3]**2 + g[1, 1] * factor1
        factor3 = -2 * factor0 * g[0, 1] * g[0, 2] * g[1, 2] + 2 * g[0, 2] * g[0, 3] * g[1, 2] * g[1, 3] + \
                  2 * g[0, 1] * g[0, 2] * g[1, 3] * g[2, 3] + 2 * g[0, 1] * g[0, 3] * g[1, 2] * g[2, 3] - \
                  g[0, 1]**2 * g[2, 3]**2 - g[0, 2]**2 * g[1, 3]**2 - g[0, 3]**2 * g[1, 2]**2 + \
                  g[2, 2] * (-2 * g[0, 1] * g[0, 3] * g[1, 3] + factor0 * g[0, 1]**2) + \
                  g[1, 1] * (-2 * g[0, 2] * g[0, 3] * g[2, 3] + factor0 * g[0, 2]**2 + g[2, 2] * g[0, 3]**2) - g[0, 0] * factor2

        m = np.zeros((4, 4))
        m[0, 0] = (factor2 / factor3)**0.5
        m[1, 0] = (g[0, 1] * g[2, 3]**2 + g[0, 2] * g[1, 2] * factor0 - g[0, 2] * g[1, 3] * g[2, 3] - \
                  g[0, 3] * g[1, 2] * g[2, 3] + g[0, 3] * g[1, 3] * g[2, 2] - g[0, 1] * g[2, 2] * factor0) / (factor2 * factor3)**0.5
        m[2, 0] = (g[0, 2] * g[1, 3]**2 - g[0, 3] * g[1, 2] * g[1, 3] + g[0, 1] * g[1, 2] * factor0 - \
                  g[0, 1] * g[1, 3] * g[2, 3] - g[0, 2] * g[1, 1] * factor0 + g[0, 3] * g[1, 1] * g[2, 3]) / (factor2 * factor3)**0.5
        m[3, 0] = (g[0, 3] * g[1, 2]**2 - g[0, 2] * g[1, 2] * g[1, 3] - g[0, 1] * g[1, 2] * g[2, 3] + \
                  g[0, 1] * g[1, 3] * g[2, 2] + g[0, 2] * g[1, 1] * g[2, 3] - g[0, 3] * g[1, 1] * g[2, 2]) / (factor2 * factor3)**0.5
        m[1, 1] = (factor1 / factor2)**0.5
        m[2, 1] = (g[1, 3] * g[2, 3] - g[1, 2] * factor0) / (factor1 * factor2)**0.5
        m[3, 1] = (g[1, 2] * g[2, 3] - g[1, 3] * g[2, 2]) / (factor1 * factor2)**0.5
        m[2, 2] = (factor0 / factor1)**0.5
        m[3, 2] = -g[2, 3] / (factor0 * factor1)**0.5
        m[3, 3] = (1 / factor0)**0.5

    elif len(g.shape) == 6:
        # For spacetime array metrics
        factor0 = g[..., 3, 3]
        factor1 = -g[..., 2, 3]**2 + g[..., 2, 2] * factor0
        factor2 = 2 * g[..., 1, 2] * g[..., 1, 3] * g[..., 2, 3] - factor0 * g[..., 1, 2]**2 - \
                  g[..., 2, 2] * g[..., 1, 3]**2 + g[..., 1, 1] * factor1
        factor3 = -2 * factor0 * g[..., 0, 1] * g[..., 0, 2] * g[..., 1, 2] + \
                  2 * g[..., 0, 2] * g[..., 0, 3] * g[..., 1, 2] * g[..., 1, 3] + \
                  2 * g[..., 0, 1] * g[..., 0, 2] * g[..., 1, 3] * g[..., 2, 3] + \
                  2 * g[..., 0, 1] * g[..., 0, 3] * g[..., 1, 2] * g[..., 2, 3] - \
                  g[..., 0, 1]**2 * g[..., 2, 3]**2 - g[..., 0, 2]**2 * g[..., 1, 3]**2 - \
                  g[..., 0, 3]**2 * g[..., 1, 2]**2 + g[..., 2, 2] * \
                  (-2 * g[..., 0, 1] * g[..., 0, 3] * g[..., 1, 3] + factor0 * g[..., 0, 1]**2) + \
                  g[..., 1, 1] * (-2 * g[..., 0, 2] * g[..., 0, 3] * g[..., 2, 3] + factor0 * g[..., 0, 2]**2 + \
                  g[..., 2, 2] * g[..., 0, 3]**2) - g[..., 0, 0] * factor2

        m = np.zeros(g.shape[:-2] + (4, 4))
        m[..., 0, 0] = (factor2 / factor3)**0.5
        m[..., 1, 0] = (g[..., 0, 1] * g[..., 2, 3]**2 + g[..., 0, 2] * g[..., 1, 2] * factor0 - \
                  g[..., 0, 2] * g[..., 1, 3] * g[..., 2, 3] - g[..., 0, 3] * g[..., 1, 2] * g[..., 2, 3] + \
                  g[..., 0, 3] * g[..., 1, 3] * g[..., 2, 2] - g[..., 0, 1] * g[..., 2, 2] * factor0) / (factor2 * factor3)**0.5
        # ... (Other elements of M)

    else:
        raise ValueError("Unrecognized matrix size")

    if np.any(np.isinf(m)):
        raise ValueError("Eulerian Transformation is Infinite - Numerical Precision Insufficient")

    if not np.all(np.isreal(m)):
        raise ValueError("Eulerian Transformation is imaginary - Numerical Precision Insufficient")

    return m