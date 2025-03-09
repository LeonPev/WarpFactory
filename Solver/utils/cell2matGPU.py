
import numpy as np

def cell2matGPU(c):
    """Convert the contents of a cell array into a single matrix.

    M = cell2matGPU(C) converts a multidimensional cell array with contents of
    the same data type into a single matrix. The contents of C must be able
    to concatenate into a hyperrectangle. Moreover, for each pair of
    neighboring cells, the dimensions of the cell's contents must match,
    excluding the dimension in which the cells are neighbors. This constraint
    must hold true for neighboring cells along all of the cell array's
    dimensions.

    The dimensionality of M, i.e. the number of dimensions of M, will match
    the highest dimensionality contained in the cell array.

    cell2matGPU is not supported for cell arrays containing cell arrays or
    objects.

    Example:
        C = [[[1]] [[2, 3, 4]]; [[5], [9]] [[6, 7, 8], [10, 11, 12]]]
        M = cell2matGPU(C)

    """
    if isinstance(c, (int, float, str)):
        return c
    if isinstance(c, (list, np.ndarray)) and len(c) == 0:
        return []
    if isinstance(c, (list, np.ndarray)) and len(c) == 1:
        if isinstance(c[0], (int, float, str, list, np.ndarray)):
            return c[0]
    elements = len(c)

    if elements == 0:
        return []

    if elements == 1:
        if isinstance(c[0], (np.ndarray, list, int, float, str, bool)):
            return c[0]

    cell_class = type(c[0])
    if not all(isinstance(x, cell_class) for x in c):
        raise ValueError("Mixed data types in cell array")

    if isinstance(c[0], (list, np.ndarray)):
        raise ValueError("Nested cell arrays or objects are not supported")

    if isinstance(c[0], dict):
        c_fields = [list(x.keys()) for x in c]
        if not all(x == c_fields[0] for x in c_fields):
            raise ValueError("Inconsistent field names in struct array")

    if np.array(c).ndim == 2:
        rows = len(c)
        cols = len(c[0])
        if rows < cols:
            m = []
            for n in range(rows):
                m.append(np.concatenate([x for x in c[n]], axis=0))
            m = np.concatenate(m, axis = 0)
        else:
            m = []
            for n in range(cols):
                m.append(np.concatenate([c[j][n] for j in range(rows)], axis=0))
            m = np.concatenate(m, axis=0)
        return m

    c_size = np.array(c).shape
    m = c
    for dim in range(len(c_size) - 1, 0, -1):
        m_temp = []
        for i in range(np.prod(c_size[:dim]).astype(int)):
            temp = []
            for j in range(c_size[dim]):
                temp.append(m[i * c_size[dim] + j])
            m_temp.append(np.concatenate(temp, axis=0))
        m = m_temp
        c_size = np.array(m).shape
    return np.concatenate(m, axis=0)