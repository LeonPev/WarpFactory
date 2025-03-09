
import numpy as np
from datetime import datetime
from scipy.integrate import cumtrapz


def metricGet_WarpShellComoving(gridSize, worldCenter, m, R1, R2, Rbuff=0, sigma=0, smoothFactor=1, vWarp=0, doWarp=0, gridScaling=None):
    if gridScaling is None:
        gridScaling = np.array([1, 1, 1, 1])

    Metric = {}
    Metric['type'] = "metric"
    Metric['name'] = "Comoving Warp Shell"
    Metric['scaling'] = gridScaling
    Metric['coords'] = "cartesian"
    Metric['index'] = "covariant"
    Metric['date'] = datetime.now().strftime("%Y-%m-%d")
    Metric['params'] = {}

    # Placeholder for TOV function (needs to be implemented)
    def TOVconstDensity(R2, M, rho, rsample):
        pass  # TODO: Implement TOV solver


    worldSize = np.sqrt((gridSize[1] * gridScaling[1] - worldCenter[1])**2 + (gridSize[2] * gridScaling[2] - worldCenter[2])**2 + (gridSize[3] * gridScaling[3] - worldCenter[3])**2)
    rSampleRes = 10**5
    rsample = np.linspace(0, worldSize * 1.2, rSampleRes)

    rho = np.zeros_like(rsample) + m / (4/3 * np.pi * (R2**3 - R1**3)) * (np.logical_and(rsample > R1, rsample < R2))
    Metric['params']['rho'] = rho

    maxR_index = np.argmin(np.diff(rho > 0))
    maxR = rsample[maxR_index]

    M = cumtrapz(4 * np.pi * rho * rsample**2, rsample)

    P = TOVconstDensity(R2, M, rho, rsample)
    Metric['params']['P'] = P
    
    from scipy.ndimage import gaussian_filter1d

    def smooth(data, factor):
        """Simple smoothing function using a Gaussian filter."""
        return gaussian_filter1d(data, factor)

    rho_smooth = smooth(rho, smoothFactor)
    Metric['params']['rhosmooth'] = rho_smooth

    P_smooth = smooth(P, smoothFactor)
    Metric['params']['Psmooth'] = P_smooth

    M = cumtrapz(4 * np.pi * rho_smooth * rsample**2, rsample)
    M[M < 0] = np.max(M)
    Metric['params']['M'] = M
    Metric['params']['rVec'] = rsample

    # setMinkowski function (from previous files)
    def setMinkowski(gridSize):
        tensor = np.zeros((4, 4) + tuple(gridSize))
        for i in range(4):
            tensor[i, i, ...] = -1 if i == 0 else 1
        return tensor

    Metric['tensor'] = setMinkowski(gridSize)

    # shapeFunction_Alcubierre function (from previous files)
    def shapeFunction_Alcubierre(r, R, sigma):
        tanh = np.tanh
        return (tanh(sigma * (r + R)) - tanh(sigma * (r - R))) / (2 * tanh(sigma * R))

    t = 0
    for i in range(gridSize[1]):
        for j in range(gridSize[2]):
            for k in range(gridSize[3]):
                x = (i + 1) * gridScaling[1] - worldCenter[1]
                y = (j + 1) * gridScaling[2] - worldCenter[2]
                z = (k + 1) * gridScaling[3] - worldCenter[3]

                r = np.sqrt(x**2 + y**2 + z**2)

                # Find nearest rsample index
                idx = np.abs(rsample - r).argmin()

                rho_val = rho_smooth[idx]
                P_val = P_smooth[idx]
                M_val = M[idx]

                
                # Comoving Shell calculations
                alpha = 1.0 - 2.0 * M_val / r  # Example lapse function calculation
                beta = np.array([vWarp, 0, 0])  # Example shift vector calculation
                gamma = np.diag([1.0, 1.0, 1.0])  # Example 3-metric calculation

                # Implement actual calculations for alpha, beta, and gamma based on rho_val, P_val, M_val, etc.
                # ... (Now implemented with placeholders)

                # Assign to Metric tensor
                Metric['tensor'][0, 0, t, i, j, k] = -alpha**2
                Metric['tensor'][0, 1:, t, i, j, k] = alpha * beta
                Metric['tensor'][1:, 0, t, i, j, k] = alpha * beta.reshape(3, 1)  # Reshape beta for correct broadcasting
                Metric['tensor'][1:, 1:, t, i, j, k] = gamma


    return Metric
    return Metric