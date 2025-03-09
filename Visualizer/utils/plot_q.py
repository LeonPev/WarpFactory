
import matplotlib.pyplot as plt
import numpy as np

def plot_q(*args):
    if len(args) >= 2 and len(np.squeeze(args[0])) > 3 and len(np.squeeze(args[1])) > 3:
        plt.plot(np.squeeze(args[0]), np.squeeze(args[1]), *args[2:])
    else:
        plt.plot(np.squeeze(args[0]), *args[1:])
    plt.show()