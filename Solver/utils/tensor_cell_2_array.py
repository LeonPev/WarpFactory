
import numpy as np

def tensor_cell_2_array(tensor, try_gpu=False):
    array_tensor = np.array(tensor.tensor)
    return array_tensor