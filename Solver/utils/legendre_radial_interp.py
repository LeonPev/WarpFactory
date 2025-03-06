
import numpy as np

def legendre_radial_interp(input_array, r):
    r_scale = 1

    x0 = int(np.floor(r / r_scale - 1))
    x1 = int(np.floor(r / r_scale))
    x2 = int(np.ceil(r / r_scale))
    x3 = int(np.ceil(r / r_scale + 1))

    y0 = input_array[max(x0, 0)]
    y1 = input_array[max(x1, 0)]
    y2 = input_array[max(x2, 0)]
    y3 = input_array[max(x3, 0)]

    x = r

    x0 *= r_scale
    x1 *= r_scale
    x2 *= r_scale
    x3 *= r_scale

    output_value = (
        y0 * (x - x1) * (x - x2) * (x - x3) / ((x0 - x1) * (x0 - x2) * (x0 - x3)) +
        y1 * (x - x0) * (x - x2) * (x - x3) / ((x1 - x0) * (x1 - x2) * (x1 - x3)) +
        y2 * (x - x0) * (x - x1) * (x - x3) / ((x2 - x0) * (x2 - x1) * (x2 - x3)) +
        y3 * (x - x0) * (x - x1) * (x - x2) / ((x3 - x0) * (x3 - x1) * (x3 - x2))
    )

    return output_value