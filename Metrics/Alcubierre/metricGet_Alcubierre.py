
import numpy as np
from utilities import threePlusOneBuilder, setMinkowskiThreePlusOne
c = 299792458

def metricGet_Alcubierre(gridSize, worldCenter, v, R, sigma, gridScale=None):
    if gridScale is None:
        gridScale = np.array([1, 1, 1, 1])

    metric = {}
    metric['params'] = {}
    metric['params']['gridSize'] = gridSize
    metric['params']['worldCenter'] = worldCenter
    metric['params']['velocity'] = v
    metric['params']['R'] = R
    metric['params']['sigma'] = sigma
    metric['type'] = "metric"
    metric['name'] = 'Alcubierre'
    metric['scaling'] = gridScale
    metric['coords'] = "cartesian"
    metric['index'] = "covariant"
    metric['date'] = 'today' # Placeholder - need to figure out date function

    alpha, beta, gamma = setMinkowskiThreePlusOne(gridSize)
    from utilities import shapeFunction_Alcubierre

    x = np.arange(0, gridSize[1]) * gridScale[1] - worldCenter[1]
    y = np.arange(0, gridSize[2]) * gridScale[2] - worldCenter[2]
    z = np.arange(0, gridSize[3]) * gridScale[3] - worldCenter[3]
    xv, yv, zv = np.meshgrid(x, y, z, indexing='ij')

    for t in range(gridSize[0]):
        xs = (t * gridScale[0] - worldCenter[0]) * v * c
        r = np.sqrt((xv - xs)**2 + yv**2 + zv**2)
        fs = shapeFunction_Alcubierre(r, R, sigma)
        beta[0][t, :, :, :] = -v * fs # Assuming beta is a list of numpy arrays

    metric['tensor'] = threePlusOneBuilder(alpha, beta, gamma)

    return metric
    # ... (rest of the function body will go here)