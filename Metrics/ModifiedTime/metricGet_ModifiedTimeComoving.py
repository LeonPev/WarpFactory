
import numpy as np
from utilities import setMinkowski, shapeFunction_Alcubierre

def metricGet_ModifiedTimeComoving(gridSize, worldCenter, v, R, sigma, A, gridScaling=None):
    if gridScaling is None:
        gridScaling = np.array([1, 1, 1, 1])

    if gridSize[0] > 1:
        raise ValueError('The time grid is greater than 1, only a size of 1 can be used in comoving')

    metric = {}
    metric['params'] = {}
    metric['params']['gridSize'] = gridSize
    metric['params']['worldCenter'] = worldCenter
    metric['params']['velocity'] = v
    metric['params']['R'] = R
    metric['params']['sigma'] = sigma
    metric['params']['A'] = A
    metric['type'] = "metric"
    metric['name'] = "Modified Time Comoving"
    metric['scaling'] = gridScaling
    metric['coords'] = "cartesian"
    metric['index'] = "covariant"
    metric['date'] = 'today'  # Placeholder

    metric['tensor'] = setMinkowski(gridSize)

    x = np.arange(0, gridSize[1]) * gridScaling[1] - worldCenter[1]
    y = np.arange(0, gridSize[2]) * gridScaling[2] - worldCenter[2]
    z = np.arange(0, gridSize[3]) * gridScaling[3] - worldCenter[3]
    xv, yv, zv = np.meshgrid(x, y, z, indexing='ij')

    r = np.sqrt(xv**2 + yv**2 + zv**2)
    fs = shapeFunction_Alcubierre(r, R, sigma)
    metric['tensor'][0, 1][0, :, :, :] = v * (1 - fs)
    metric['tensor'][1, 0][0, :, :, :] = v * (1 - fs)
    metric['tensor'][0, 0][0, :, :, :] = -((1 - fs) + fs / A)**2 + (fs * v)**2

    return metric