
import numpy as np

def verifyTensor(tensor, value):
    return True

def getTrace(tensor, metric):
    """Calculates the trace of a tensor."""
    if not verifyTensor(metric, 1):
        raise ValueError("Metric is not verified. Please verify metric using verifyTensor(metric).")

    Trace = np.zeros(metric.tensor[0, 0].shape)

    if tensor.index == metric.index:
        metric.tensor = np.linalg.inv(metric.tensor)

    for a in range(4):
        for b in range(4):
            Trace += metric.tensor[a, b] * tensor.tensor[a, b]

    return Trace