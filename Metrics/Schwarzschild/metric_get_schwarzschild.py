
import numpy as np
from ..setMinkowski import set_minkowski

def metric_get_schwarzschild(grid_size, world_center, rs, grid_scaling=np.array([1, 1, 1, 1])):
    if grid_size[0] > 1:
        raise ValueError('The time grid is greater than 1, only a size of 1 can be used for the Schwarzschild solution')

    metric = {
        "params": {"gridSize": grid_size, "worldCenter": world_center, "rs": rs},
        "type": "metric",
        "frame": "comoving",
        "name": "Schwarzschild",
        "scaling": grid_scaling,
        "coords": "cartesian",
        "index": "covariant",
        "date": "2024-04-26"  # TODO: Replace with actual date
    }

    # Set Minkowski terms
    metric["tensor"] = set_minkowski(grid_size)

    epsilon = 1e-10
    t = 0  # Only 1 time slice
    for i in range(grid_size[1]):
        for j in range(grid_size[2]):
            for k in range(grid_size[3]):
                x = (i + 0.5) * grid_scaling[1] - world_center[1]
                y = (j + 0.5) * grid_scaling[2] - world_center[2]
                z = (k + 0.5) * grid_scaling[3] - world_center[3]

                r = np.sqrt(x**2 + y**2 + z**2) + epsilon

                # Diagonal terms
                metric["tensor"][0, 0, i, j, k] = -(1 - rs / r)
                metric["tensor"][1, 1, i, j, k] = (x**2 / (1 - rs / r) + y**2 + z**2) / r**2
                metric["tensor"][2, 2, i, j, k] = (x**2 + y**2 / (1 - rs / r) + z**2) / r**2
                metric["tensor"][3, 3, i, j, k] = (x**2 + y**2 + z**2 / (1 - rs / r)) / r**2

                # Cross terms
                cross_term = rs / (r**3 - r**2 * rs)
                metric["tensor"][1, 2, i, j, k] = cross_term * x * y
                metric["tensor"][2, 1, i, j, k] = metric["tensor"][1, 2, i, j, k]
                metric["tensor"][1, 3, i, j, k] = cross_term * x * z
                metric["tensor"][3, 1, i, j, k] = metric["tensor"][1, 3, i, j, k]
                metric["tensor"][2, 3, i, j, k] = cross_term * y * z
                metric["tensor"][3, 2, i, j, k] = metric["tensor"][2, 3, i, j, k]

    return metric