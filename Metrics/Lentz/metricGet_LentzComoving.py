
import numpy as np
from utilities import threePlusOneBuilder, setMinkowskiThreePlusOne

def metricGet_LentzComoving(gridSize, worldCenter, v, scale=None, gridScale=None):
    if scale is None:
        scale = max(gridSize[1:]) / 7
    if gridScale is None:
        gridScale = np.array([1, 1, 1, 1])

    if gridSize[0] > 1:
        raise ValueError('The time grid is greater than 1, only a size of 1 can be used for Lentz')

    def getWarpFactorByRegion(xIn, yIn, sizeScale):
        x = xIn
        y = abs(yIn)
        WFX = 0
        WFY = 0

        if (x >= sizeScale and x <= 2 * sizeScale) and (x - sizeScale >= y):
            WFX = -2
            WFY = 0
        elif (x > sizeScale and x <= 2 * sizeScale) and (x - sizeScale <= y) and (-y + 3 * sizeScale >= x):
            WFX = -1
            WFY = 1
        elif (x > 0 and x <= sizeScale) and (x + sizeScale > y) and (-y + sizeScale < x):
            WFX = 0
            WFY = 1
        elif (x > 0 and x <= sizeScale) and (x + sizeScale <= y) and (-y + 3 * sizeScale >= x):
            WFX = -0.5
            WFY = 0.5
        elif (x > -sizeScale and x <= 0) and (-x + sizeScale < y) and (-y + 3 * sizeScale >= -x):
            WFX = 0.5
            WFY = 0.5
        elif (x > -sizeScale and x <= 0) and (-x + sizeScale >= y) and (-y + sizeScale < -x):
            WFX = 1
            WFY = 0
        elif (x >= -2 * sizeScale and x < -sizeScale) and (-x - sizeScale < y) and (-y + 3 * sizeScale > -x):
            WFX = 1
            WFY = -1
        elif (x >= -2 * sizeScale and x < -sizeScale) and (-x - sizeScale >= y):
            WFX = 2
            WFY = 0

        return WFX, WFY

    metric = {}
    metric['params'] = {}
    metric['params']['gridSize'] = gridSize
    metric['params']['worldCenter'] = worldCenter
    metric['params']['velocity'] = v
    metric['type'] = "metric"
    metric['name'] = "Lentz Comoving"
    metric['scaling'] = gridScale
    metric['coords'] = "cartesian"
    metric['index'] = "covariant"
    metric['date'] = 'today'  # Placeholder

    alpha, beta, gamma = setMinkowskiThreePlusOne(gridSize)

    x = np.arange(0, gridSize[1]) * gridScale[1] - worldCenter[1]
    y = np.arange(0, gridSize[2]) * gridScale[2] - worldCenter[2]
    xv, yv = np.meshgrid(x, y, indexing='ij')

    WFX, WFY = getWarpFactorByRegion(xv, yv, scale)
    beta[0][0, :, :, :] = v * (1 - WFX)
    beta[1][0, :, :, :] = v * WFY

    metric['tensor'] = threePlusOneBuilder(alpha, beta, gamma)

    return metric