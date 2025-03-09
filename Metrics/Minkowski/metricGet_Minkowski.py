
import numpy as np

def metricGet_Minkowski(gridSize, gridScaling=None):
    if gridScaling is None:
        gridScaling = np.array([1, 1, 1, 1])

    metric = {}
    metric['type'] = "metric"
    metric['name'] = "Minkowski"
    metric['scaling'] = gridScaling
    metric['coords'] = "cartesian"
    metric['index'] = "covariant"
    metric['date'] = 'today'  # Placeholder

    metric['tensor'] = np.zeros((4, 4) + tuple(gridSize))
    metric['tensor'][0, 0] = -np.ones(gridSize)
    metric['tensor'][1, 1] = np.ones(gridSize)
    metric['tensor'][2, 2] = np.ones(gridSize)
    metric['tensor'][3, 3] = np.ones(gridSize)

    return metric