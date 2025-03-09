
import numpy as np
from utilities import threePlusOneBuilder, setMinkowskiThreePlusOne, shapeFunction_Alcubierre

def metricGet_AlcubierreComoving(gridSize, worldCenter, v, R, sigma, gridScale=None):
    if gridScale is None:
        gridScale = np.array([1, 1, 1, 1])

    if gridSize[0] > 1:
        raise ValueError('The time grid is greater than 1, only a size of 1 can be used in comoving')

    metric = {}
    metric['params'] = {}
    metric['params']['gridSize'] = gridSize
    metric['params']['worldCenter'] = worldCenter
    metric['params']['velocity'] = v
    metric['params']['R'] = R
    metric['params']['sigma'] = sigma
    metric['type'] = "metric"
    metric['name'] = 'Alcubierre Comoving'
    metric['scaling'] = gridScale
    metric['coords'] = "cartesian"
    metric['index'] = "covariant"
    metric['date'] = 'today' # Placeholder

    alpha, beta, gamma = setMinkowskiThreePlusOne(gridSize)

    x = np.arange(0, gridSize[1]) * gridScale[1] - worldCenter[1]
    y = np.arange(0, gridSize[2]) * gridScale[2] - worldCenter[2]
    z = np.arange(0, gridSize[3]) * gridScale[3] - worldCenter[3]
    xv, yv, zv = np.meshgrid(x, y, z, indexing='ij')

    r = np.sqrt(xv**2 + yv**2 + zv**2)
    fs = shapeFunction_Alcubierre(r, R, sigma)
    beta[0][0, :, :, :] = v * (1 - fs) # Assuming beta is a list of numpy arrays and t=0

    metric['tensor'] = threePlusOneBuilder(alpha, beta, gamma)

    return metric
    # ... (rest of the function will go here)