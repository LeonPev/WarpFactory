
import numpy as np
from Metrics import utils

def metricGet_Schwarzschild(gridSize, worldCenter, rs, gridScaling=None):
    if gridScaling is None:
        gridScaling = np.array([1, 1, 1, 1])

    if gridSize[0] > 1:
        raise ValueError('The time grid is greater than 1, only a size of 1 can be used for the Schwarzschild solution')

    metric = utils.setMinkowski(gridSize)

    epsilon = 1e-10
    t = 0  # Python indexing starts from 0

    x = np.arange(gridSize[1]) * gridScaling[1] - worldCenter[1]
    y = np.arange(gridSize[2]) * gridScaling[2] - worldCenter[2]
    z = np.arange(gridSize[3]) * gridScaling[3] - worldCenter[3]

    r = np.sqrt(x[:, None, None]**2 + y[None, :, None]**2 + z[None, None, :]**2) + epsilon

    metric['tensor'][0, 0, t, :, :, :] = -(1 - rs / r)
    metric['tensor'][1, 1, t, :, :, :] = (x[:, None, None]**2 / (1 - rs / r) + y[None, :, None]**2 + z[None, None, :]**2) / r**2
    metric['tensor'][2, 2, t, :, :, :] = (x[:, None, None]**2 + y[None, :, None]**2 / (1 - rs / r) + z[None, None, :]**2) / r**2
    metric['tensor'][3, 3, t, :, :, :] = (x[:, None, None]**2 + y[None, :, None]**2 + z[None, None, :]**2 / (1 - rs / r)) / r**2

    metric['tensor'][1, 2, t, :, :, :] = rs / (r**3 - r**2 * rs) * x[:, None, None] * y[None, :, None]
    metric['tensor'][2, 1, t, :, :, :] = metric['tensor'][1, 2, t, :, :, :]

    metric['tensor'][1, 3, t, :, :, :] = rs / (r**3 - r**2 * rs) * x[:, None, None] * z[None, None, :]
    metric['tensor'][3, 1, t, :, :, :] = metric['tensor'][1, 3, t, :, :, :]

    metric['tensor'][2, 3, t, :, :, :] = rs / (r**3 - r**2 * rs) * y[None, :, None] * z[None, None, :]
    metric['tensor'][3, 2, t, :, :, :] = metric['tensor'][2, 3, t, :, :, :]

    metric['type'] = "metric"
    metric['frame'] = "comoving"
    metric['name'] = "Schwarzschild"
    metric['scaling'] = gridScaling
    metric['coords'] = "cartesian"
    metric['index'] = "covariant"
    # metric['date'] = date  # Add date if needed

    return metric