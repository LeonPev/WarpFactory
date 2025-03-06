
from Metrics.threePlusOneDecomposer import three_plus_one_decomposer
from .do_frame_transfer import change_tensor_index
from Solver.utils.covDiv import cov_div
from .c4Inv import c4_inv



import numpy as np

def get_scalars(metric):
    # Convert metric tensor to array (assuming metric.tensor is a nested list)
    array_metric_tensor = np.array(metric["tensor"])

    alpha, _, _, beta_up, _ = three_plus_one_decomposer(metric)

    s = metric["tensor"][0][0].shape
    u_up = np.zeros(s + (4,))  # Add a dimension for the 4-velocity components
    u_down = np.zeros(s + (4,))

    # Iterate through all points to create u_up and u_down
    for t in range(s[0]):
        for i in range(s[1]):
            for j in range(s[2]):
                for k in range(s[3]):
                    u_up[t, i, j, k, :] = (1 / alpha[t, i, j, k]) * np.array([1, -beta_up[t, i, j, k, 0], -beta_up[t, i, j, k, 1], -beta_up[t, i, j, k, 2]])
                    u_down[t, i, j, k, :] = np.dot(array_metric_tensor[t, i, j, k, :, :], u_up[t, i, j, k, :])

    del_u = [[0 for _ in range(4)] for _ in range(4)]
    metric = change_tensor_index(metric, "covariant")

    for i in range(4):
        for j in range(4):
            del_u[i][j] = cov_div(metric["tensor"], c4_inv(metric["tensor"]), [u_up[:, :, :, :, i]], [u_down[:, :, :, :, j]], i, j, [1, 1, 1, 1], 0)

    p_mix = [[0 for _ in range(4)] for _ in range(4)]
    p = [[0 for _ in range(4)] for _ in range(4)]

    for i in range(4):
        for j in range(4):
            k_delta = 1 if i == j else 0
            p_mix[i][j] = k_delta + u_up[:, :, :, :, i] * u_down[:, :, :, :, j]
            p[i][j] = metric["tensor"][i][j] + u_down[:, :, :, :, i] * u_down[:, :, :, :, j]

    theta = {"index": "covariant", "type": "tensor", "tensor": [[0 for _ in range(4)] for _ in range(4)]}
    omega = {"index": "covariant", "type": "tensor", "tensor": [[0 for _ in range(4)] for _ in range(4)]}

        # Calculate theta and omega tensors
    for i in range(4):
        for j in range(4):
            theta["tensor"][i][j] = 0.5 * (del_u[i][j] + del_u[j][i] - np.einsum('mn...,mi...,nj...->ij...', c4_inv(metric["tensor"]), p_mix[i], p_mix[j]))
            omega["tensor"][i][j] = 0.5 * (del_u[i][j] - del_u[j][i])

    # Calculate scalars
    expansion_scalar = np.trace(theta["tensor"])
    shear_scalar = 0.5 * np.einsum('ij...,ij...', theta["tensor"], theta["tensor"]) - (1/3) * expansion_scalar**2
    vorticity_scalar = 0.5 * np.einsum('ij...,ij...', omega["tensor"], omega["tensor"])

    return expansion_scalar, shear_scalar, vorticity_scalar