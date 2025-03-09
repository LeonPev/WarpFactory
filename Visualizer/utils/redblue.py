
import numpy as np
import matplotlib.colors

def redblue(value, gradient_num=1024):
    min_val = np.min(value)
    max_val = np.max(value)

    if not (min_val <= 0 and max_val >= 0):
        if min_val > 0 and max_val > 0:
            return matplotlib.colors.LinearSegmentedColormap.from_list("red", [(1, 1, 1), (1, 0, 0)], N=gradient_num)
        if min_val < 0 and max_val < 0:
            return matplotlib.colors.LinearSegmentedColormap.from_list("blue", [(0, 0, 1), (1, 1, 1)], N=gradient_num)

    if min_val == 0 and max_val == 0:
        return matplotlib.colors.ListedColormap([(1, 1, 1)])

    center_val = abs(max_val) / (abs(max_val) + abs(min_val))
    cmap1 = matplotlib.colors.LinearSegmentedColormap.from_list("blue", [(0, 0, 1), (1, 1, 1)], N=int(round((1 - center_val) * gradient_num)))
    cmap2 = matplotlib.colors.LinearSegmentedColormap.from_list("red", [(1, 1, 1), (1, 0, 0)], N=int(round(center_val * gradient_num)))

    return matplotlib.colors.LinearSegmentedColormap.from_list("redblue", [cmap1(0.0), cmap1(1.0), cmap2(1.0)])