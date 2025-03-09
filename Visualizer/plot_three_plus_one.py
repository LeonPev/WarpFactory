
import numpy as np
import matplotlib.pyplot as plt

def plot_three_plus_one(metric, sliced_planes=np.array([1, 4]), slice_locations=None, alpha=0.2):
    from plot_tensor import verify_tensor

    # Check that tensor is a metric
    if not metric.type.lower() == "metric":
        raise ValueError("Must provide a metric object.")

    # Verify tensor
    if not verify_tensor(metric):
        raise ValueError("Metric is not verified. Please verify metric using verify_tensor(metric).")

    # Check that the sliced planes are different
    if sliced_planes[0] == sliced_planes[1]:
        raise ValueError("Selected planes must not be the same, select two different planes to slice along.")

    # Handle default slice_locations
    if slice_locations is None:
        s = metric.tensor[0, 0].shape
        slice_locations = np.round((np.array(s) + 1) / 2).astype(int)

    # Round sliceLocations
    slice_locations = np.round(slice_locations).astype(int)

    # Check that the sliceLocations are inside the world
    if any(slice_locations < 1) or slice_locations[0] > metric.tensor[0, 0].shape[sliced_planes[0] - 1] or slice_locations[1] > metric.tensor[0, 0].shape[sliced_planes[1] - 1]:
        raise ValueError('sliceLocations are outside the world.')

    # Check that the coords are cartesian
    if metric.coords.lower() == "cartesian":
        # Decompose the metric (placeholder)
        alpha_lapse, betaDown, gammaDown = decompose_metric(metric)

        idx = get_slice_data(sliced_planes, slice_locations, metric)

        # Plot alpha
        plot_component(np.squeeze(alpha_lapse[idx]), "\\alpha", alpha)

        # Plot beta
        for i in range(3):
            plot_component(np.squeeze(betaDown[i][idx]), f"\\beta_{{i+1}}", alpha)

        # Plot gamma
        c = np.array([[1, 1], [1, 2], [1, 3], [2, 2], [2, 3], [3, 3]])
        for i in range(c.shape[0]):
            plot_component(np.squeeze(gammaDown[c[i, 0]-1, c[i, 1]-1][idx]), f"\\gamma_{{{c[i, 0]}{c[i, 1]}}}", alpha)
    else:
        raise ValueError('Unknown coordinate system, must be: "cartesian"')

def decompose_metric(metric):
    return metric.tensor[0, 0], [metric.tensor[0, 1], metric.tensor[0, 2], metric.tensor[0, 3]], metric.tensor[1:, 1:]  # Placeholder

from plot_tensor import get_slice_data, plot_component