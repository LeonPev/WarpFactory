
import numpy as np
import matplotlib.pyplot as plt


def verify_tensor(tensor):
    return True
def plot_tensor(tensor, alpha=0.2, sliced_planes=np.array([1, 4]), slice_locations=None):
        # Verify tensor
    if not verify_tensor(tensor):
        raise ValueError("Tensor is not verified. Please verify tensor using verify_tensor(tensor).")

    # Check that the sliced planes are different
    if sliced_planes[0] == sliced_planes[1]:
        raise ValueError("Selected planes must not be the same, select two different planes to slice along.")

    # Round sliceLocations
    slice_locations = np.round(slice_locations).astype(int)

    # Check that the sliceLocations are inside the world
    if any(slice_locations < 1) or slice_locations[0] > tensor.tensor[0, 0].shape[sliced_planes[0] - 1] or slice_locations[1] > tensor.tensor[0, 0].shape[sliced_planes[1] - 1]:
        raise ValueError('sliceLocations are outside the world.')
    # Check tensor type
    if tensor.type.lower() == "metric":
        title_character = "g"
    elif tensor.type.lower() == "stress-energy":
        title_character = "T"
    else:
        raise ValueError("Unknown tensor type. Must be 'Metric' or 'Stress-Energy'")

    # Check tensor index
    if tensor.index.lower() == "covariant":
        title_augment1 = "_"
        title_augment2 = ""
    elif tensor.index.lower() == "contravariant":
        title_augment1 = "^"
        title_augment2 = ""
    elif tensor.index.lower() == "mixedupdown":
        title_augment1 = "^"
        title_augment2 = "_"
    elif tensor.index.lower() == "mixeddownup":
        title_augment1 = "_"
        title_augment2 = "^"
    else:
        raise ValueError("Unknown tensor index. Must be one of: 'covariant', 'contravariant', 'mixedupdown', 'mixeddownup'")

    # Check that the coords are cartesian
    if tensor.coords.lower() == "cartesian":
        if tensor.index.lower() == "mixedupdown" or tensor.index.lower() == "mixeddownup":
            c1 = np.array([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4])
            c2 = np.array([1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4])
        else:
            c1 = np.array([1, 1, 1, 1, 2, 3, 4, 2, 2, 3])
            c2 = np.array([1, 2, 3, 4, 2, 3, 4, 3, 4, 4])

        idx = get_slice_data(sliced_planes, slice_locations, tensor)

        for i in range(len(c1)):
            plot_component(np.squeeze(tensor.tensor[c1[i]-1, c2[i]-1][idx]), title_character + title_augment1 + str(c1[i]) + title_augment2 + str(c2[i]), alpha)
    else:
        raise ValueError('Unknown coordinate system, must be: "cartesian"')

def get_slice_data(sliced_planes, slice_locations, tensor):
    idx = [slice(None)] * 4
    for i in range(len(sliced_planes)):
        idx[sliced_planes[i]-1] = slice_locations[i]-1
    return tuple(idx)

def plot_component(data, title, alpha):
    plt.imshow(data, alpha=alpha)
    plt.title(title)
    plt.show()

    