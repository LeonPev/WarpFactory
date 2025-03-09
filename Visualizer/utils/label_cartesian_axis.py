
import numpy as np

def label_cartesian_axis(plane):
    labels = ["t", "x", "y", "z"]
    shown_planes = np.sort(np.setdiff1d(np.arange(1, 5), plane))
    return labels[int(shown_planes[0])-1], labels[int(shown_planes[1])-1]