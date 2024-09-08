import numpy as np
from numpy import ndarray

def inv(A: ndarray) -> ndarray:
    return np.linalg.inv(A)

def det(A: ndarray) -> ndarray:
    return np.linalg.det(A)