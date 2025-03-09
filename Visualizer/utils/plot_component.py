
import matplotlib.pyplot as plt
from .redblue import redblue

def plot_component(array, title_text, x_label_text, y_label_text, alpha):
    plt.figure()
    plt.imshow(array, alpha=alpha, cmap=redblue(array), aspect='auto', origin='lower', extent=[1, array.shape[1], 1, array.shape[0]])
    plt.title(title_text)
    plt.xlabel(x_label_text)
    plt.ylabel(y_label_text)
    plt.show()