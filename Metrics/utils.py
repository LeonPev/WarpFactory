
import numpy as np

def setMinkowski(gridSize):
    metric = {}
    metric['tensor'] = np.zeros((4, 4, gridSize[0], gridSize[1], gridSize[2], gridSize[3]))

    metric['tensor'][0, 0, :, :, :, :] = -1
    metric['tensor'][1, 1, :, :, :, :] = 1
    metric['tensor'][2, 2, :, :, :, :] = 1
    metric['tensor'][3, 3, :, :, :, :] = 1
    return metric

def c3Inv(gamma):
    gamma_up = np.zeros_like(gamma)
    for i in range(gamma.shape[2]):
        for j in range(gamma.shape[3]):
            for k in range(gamma.shape[4]):
                for l in range(gamma.shape[5]):
                    gamma_up[:, :, i, j, k, l] = np.linalg.inv(gamma[:, :, i, j, k, l])
    return gamma_up