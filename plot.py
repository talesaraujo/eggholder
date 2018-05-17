import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

from eggholder import *

def plot():
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    X1 = X2 = np.arange(-512, 513, 1)

    X1, X2 = np.meshgrid(X1, X2)

    F = EggHolder((X1, X2))

    surface = ax.plot_surface(X1, X2, F, linewidth=0, antialiased=False)
    
    ax.set_zlim(-1000, 1000)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    fig.colorbar(surface, shrink=0.5, aspect=5)

    plt.show()


if __name__ == '__main__':
    plot()

    
