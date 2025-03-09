



def setMinkowski(gridSize):
    # TODO: Implement setMinkowski
    tensor = np.zeros((4, 4) + tuple(gridSize))
    # Diagonal elements of Minkowski metric
    for i in range(4):
        tensor[i, i, ...] = -1 if i == 0 else 1  # -+++ signature
    return tensor

def shapeFunction_Alcubierre(r, R, sigma):
    tanh = np.tanh
    return (tanh(sigma * (r + R)) - tanh(sigma * (r - R))) / (2 * tanh(sigma * R))
import numpy as np
from datetime import datetime

def metricGet_VanDenBroeck(gridSize, worldCenter, v, R1, sigma1, R2, sigma2, A, gridScale=None):
    if gridScale is None:
        gridScale = np.array([1, 1, 1, 1])

    metric = {}
    metric['params'] = {}
    metric['params']['gridSize'] = gridSize
    metric['params']['worldCenter'] = worldCenter
    metric['params']['velocity'] = v * (1 + A)**2
    metric['params']['R1'] = R1
    metric['params']['sigma1'] = sigma1
    metric['params']['R2'] = R2
    metric['params']['sigma2'] = sigma2
    metric['params']['A'] = A

    metric['type'] = "metric"
    metric['name'] = 'Van Den Broeck'
    metric['scaling'] = gridScale
    metric['coords'] = 'cartesian'
    metric['index'] = "covariant"
    metric['date'] = datetime.now().strftime("%Y-%m-%d")

    metric['tensor'] = setMinkowski(gridSize)


    c = 1 # Speed of light
    for i in range(gridSize[1]):
        for j in range(gridSize[2]):
            for k in range(gridSize[3]):
                x = (i+1) * gridScale[1] - worldCenter[1] # Added +1 for 1-based indexing
                y = (j+1) * gridScale[2] - worldCenter[2] # Added +1 for 1-based indexing
                z = (k+1) * gridScale[3] - worldCenter[3] # Added +1 for 1-based indexing

                for t in range(gridSize[0]):
                    xs = ((t+1) * gridScale[0] - worldCenter[0]) * v * (1 + A)**2 * c  # Added +1 for 1-based indexing
                    r = np.sqrt((x - xs)**2 + y**2 + z**2)
                    B = 1 + shapeFunction_Alcubierre(r, R1, sigma1) * A
                    fs = shapeFunction_Alcubierre(r, R2, sigma2) * v

                    
                    metric['tensor'][0, 0, t, i, j, k] = -(1 - B**2 * fs**2)
                    metric['tensor'][0, 1, t, i, j, k] = -B**2 * fs
                    metric['tensor'][1, 0, t, i, j, k] = -B**2 * fs
                    metric['tensor'][1, 1, t, i, j, k] = B**2
                    metric['tensor'][2, 2, t, i, j, k] = B**2
                    metric['tensor'][3, 3, t, i, j, k] = B**2
    # Van Den Brock modification
