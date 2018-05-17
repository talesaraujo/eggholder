import numpy as np

def EggHolder(x):
    """ 
    Args:
        x = tuple representing which holds the two values, (x1, x2)
        of this function.

    Returns:
        The current value of 'EggHolder' funcion for x
    """
    x1, x2 = x

    return -(x2+47)*np.sin(np.sqrt(np.abs(x2+(x1/2)+47)))-x1*np.sin(np.sqrt(np.abs(x1-(x2+47))))
    