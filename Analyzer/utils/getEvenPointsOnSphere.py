
import numpy as np

def getEvenPointsOnSphere(R, numberOfPoints, useGPU=False):
    """Distributes points evenly on a sphere."""
    goldenRatio = (1 + 5**0.5) / 2
    Vector = np.zeros((3, numberOfPoints))

    for i in range(numberOfPoints):
        theta = 2 * np.pi * i / goldenRatio
        phi = np.arccos(1 - 2 * (i + 0.5) / numberOfPoints)

        Vector[0, i] = R * np.cos(theta) * np.sin(phi)
        Vector[1, i] = R * np.sin(theta) * np.sin(phi)
        Vector[2, i] = R * np.cos(phi)

    return Vector