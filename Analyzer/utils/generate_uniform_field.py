
import numpy as np

def get_even_points_on_sphere(radius, num_points, try_gpu=False):
    golden_ratio = (1 + 5**0.5) / 2
    i = np.arange(0, num_points)
    theta = 2 * np.pi * i / golden_ratio
    phi = np.arccos(1 - 2 * (i + 0.5) / num_points)
    x = radius * np.cos(theta) * np.sin(phi)
    y = radius * np.sin(theta) * np.sin(phi)
    z = radius * np.cos(phi)

    if try_gpu:
        # TODO: Implement GPU handling
        pass

    return np.array([x, y, z])

def generate_uniform_field(field_type, num_angular_vec, num_time_vec, try_gpu=False):
    if field_type.lower() not in ["nulllike", "timelike"]:
        raise ValueError("Vector field type not generated, use either: \"nulllike\", \"timelike\"")

    if field_type.lower() == "timelike":
        bb = np.linspace(0, 1, num_time_vec)
        vec_field = np.ones((4, num_angular_vec, num_time_vec))
        for jj in range(num_time_vec):
            vec_field[0, :, jj] = 1
            vec_field[1:, :, jj] = get_even_points_on_sphere(1 - bb[jj], num_angular_vec, try_gpu)
            vec_field[..., jj] /= np.linalg.norm(vec_field[..., jj], axis=0)

    elif field_type.lower() == "nulllike":
        vec_field = np.ones((4, num_angular_vec))
        vec_field[1:] = get_even_points_on_sphere(1, num_angular_vec, try_gpu)
        vec_field /= np.linalg.norm(vec_field, axis=0)

    if try_gpu:
        # TODO: Implement GPU handling
        pass

    return vec_field