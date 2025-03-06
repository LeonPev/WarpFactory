
import numpy as np

def set_minkowski(grid_size):
    metric_tensor = np.zeros((4, 4, *grid_size))
    metric_tensor[0, 0] = -1
    metric_tensor[1, 1] = 1
    metric_tensor[2, 2] = 1
    metric_tensor[3, 3] = 1
    return metric_tensor