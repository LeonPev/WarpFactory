import numpy as np

def verifyTensor(tensor, value):
    return True

def getInnerProduct(vecA, vecB, Metric):
    """Calculates the inner product of two vector fields."""
    if not verifyTensor(Metric, 1):
        raise ValueError("Metric is not verified. Please verify metric using verifyTensor(metric).")

    s = Metric.tensor[0, 0].shape
    innerprod = np.zeros(s)

    if vecA.index != vecB.index:
        for mu in range(4):
            for nu in range(4):
                innerprod += vecA.field[mu] * vecB.field[nu]

    elif vecA.index == vecB.index:
        if vecA.index == Metric.index:
            Metric.tensor = np.linalg.inv(Metric.tensor)  # flip index

        for mu in range(4):
            for nu in range(4):
                innerprod += vecA.field[mu] * vecB.field[nu] * Metric.tensor[mu, nu]

    return innerprod
