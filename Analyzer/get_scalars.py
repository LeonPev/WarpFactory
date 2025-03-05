
def three_plus_one_decomposer(metric):
    pass  # TODO: Implement

def change_tensor_index(metric, index):
    pass  # TODO: Implement

def cov_div(metric_tensor, c4_inv, u_up_cell, u_down_cell, i, j, factors, try_gpu):
    pass  # TODO: Implement

def c4_inv(metric_tensor):
    pass  # TODO: Implement

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

    # TODO: Implement remaining calculations for theta, omega, and scalars

    return 0, 0, 0