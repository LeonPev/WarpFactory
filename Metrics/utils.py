
import numpy as np

def setMinkowski(gridSize):
    metric = {}
    metric['tensor'] = np.zeros((4, 4, gridSize[0], gridSize[1], gridSize[2], gridSize[3]))

    metric['tensor'][0, 0, :, :, :, :] = -1
    metric['tensor'][1, 1, :, :, :, :] = 1
    metric['tensor'][2, 2, :, :, :, :] = 1
    metric['tensor'][3, 3, :, :, :, :] = 1
    return metric