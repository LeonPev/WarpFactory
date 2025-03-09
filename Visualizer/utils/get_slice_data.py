
import numpy as np

def get_slice_data(plane, slice_center, tensor):
    s = tensor.tensor[0, 0].shape
    index_data = [slice(None)] * 4

    index_data[plane[0]-1] = slice_center[0]-1
    index_data[plane[1]-1] = slice_center[1]-1

    return tuple(index_data)