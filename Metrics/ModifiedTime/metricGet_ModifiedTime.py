
import numpy as np
from utilities import setMinkowski, shapeFunction_Alcubierre
c = 299792458

def metricGet_ModifiedTime(gridSize, worldCenter, v, R, sigma, A, gridScaling=None):
    if gridScaling is None:
        gridScaling = np.array([1, 1, 1, 1])

    metric = {}
    metric['params'] = {}
    metric['params']['gridSize'] = gridSize
    metric['params']['worldCenter'] = worldCenter
    metric['params']['velocity'] = v
    metric['params']['R'] = R
    metric['params']['sigma'] = sigma
    metric['params']['A'] = A
    metric['type'] = "metric"
    metric['frame'] = "comoving"
    metric['name'] = "Modified Time"
    metric['scaling'] = gridScaling
    metric['coords'] = "cartesian"
    metric['index'] = "covariant"
    metric['date'] = 'today'  # Placeholder

    metric['tensor'] = setMinkowski(gridSize)

    x = np.arange(0, gridSize[1]) * gridScaling[1] - worldCenter[1]
    y = np.arange(0, gridSize[2]) * gridScaling[2] - worldCenter[2]
    z = np.arange(0, gridSize[3]) * gridScaling[3] - worldCenter[3]
    xv, yv, zv = np.meshgrid(x, y, z, indexing='ij')

    for t in range(gridSize[0]):
        xs = (t * gridScaling[0] - worldCenter[0]) * v * c
        r = np.sqrt((xv - xs)**2 + yv**2 + zv**2)
        fs = shapeFunction_Alcubierre(r, R, sigma)
        metric['tensor'][0, 1][t, :, :, :] = -v * fs
        metric['tensor'][1, 0][t, :, :, :] = -v * fs
        metric['tensor'][0, 0][t, :, :, :] = -((1 - fs) + fs / A)**2 + (fs * v)**2

    return metric