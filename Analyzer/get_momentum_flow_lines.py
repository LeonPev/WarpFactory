
import numpy as np
from Solver.utils.trilinear_interp import trilinear_interp

def get_momentum_flow_lines(energy_tensor, start_points, step_size, max_steps, scale_factor):
    # Check that the energy_tensor is contravariant
    if energy_tensor["index"] != "contravariant":
        raise ValueError("Energy tensor for momentum flowlines should be contravariant.")

    # Load in the momentum data
    x_mom = np.squeeze(energy_tensor["tensor"][0, 1]) * scale_factor
    y_mom = np.squeeze(energy_tensor["tensor"][0, 2]) * scale_factor
    z_mom = np.squeeze(energy_tensor["tensor"][0, 3]) * scale_factor

    # Reshape the starting points X, Y, and Z
    start_pts_x = np.reshape(start_points[0], (1, np.size(start_points[0])))
    start_pts_y = np.reshape(start_points[1], (1, np.size(start_points[1])))
    start_pts_z = np.reshape(start_points[2], (1, np.size(start_points[2])))

    # Make the paths
    paths = [None] * len(start_pts_x[0])
    for j in range(len(start_pts_x[0])):
        pos = np.zeros((max_steps, 3))
        pos[0, :] = [start_pts_x[0][j], start_pts_y[0][j], start_pts_z[0][j]]

        for i in range(max_steps):
            # Check if the particle is outside the world
            if np.any(np.isnan(pos[i, :])) or \
               (np.floor(pos[i, 0]) <= 0 or np.ceil(pos[i, 0]) >= x_mom.shape[0] -1 ) or \
               (np.floor(pos[i, 1]) <= 0 or np.ceil(pos[i, 1]) >= x_mom.shape[1] - 1) or \
               (np.floor(pos[i, 2]) <= 0 or np.ceil(pos[i, 2]) >= x_mom.shape[2] - 1):
                break

            # Interpolate the momentum
            x_momentum = trilinear_interp(x_mom, pos[i, :])
            y_momentum = trilinear_interp(y_mom, pos[i, :])
            z_momentum = trilinear_interp(z_mom, pos[i, :])

            # Propagate position
            pos[i + 1, 0] = pos[i, 0] + (x_momentum) * step_size
            pos[i + 1, 1] = pos[i, 1] + (y_momentum) * step_size
            pos[i + 1, 2] = pos[i, 2] + (z_momentum) * step_size

        paths[j] = pos[0:i, :]

    return paths