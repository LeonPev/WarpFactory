
import matplotlib.pyplot as plt
import numpy as np
from .redblue import redblue

def surf_q(*args):
    if len(args) >= 3 and len(np.squeeze(args[0])) > 3 and len(np.squeeze(args[1])) > 3 and len(np.squeeze(args[2])) > 3 and isinstance(args[1], np.ndarray) and isinstance(args[2], np.ndarray):
        plt.figure()
        plt.imshow(np.squeeze(args[2]).T, cmap=redblue(np.squeeze(args[2])), aspect='auto', origin='lower', extent=[1, np.squeeze(args[2]).T.shape[1], 1, np.squeeze(args[2]).T.shape[0]])
    else:
        plt.figure()
        plt.imshow(np.squeeze(args[0]).T, cmap=redblue(np.squeeze(args[0])), aspect='auto', origin='lower', extent=[1, np.squeeze(args[0]).T.shape[1], 1, np.squeeze(args[0]).T.shape[0]])
    plt.show()