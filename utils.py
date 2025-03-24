import numpy as np


def inner_product(vector1: np.ndarray, vector2: np.ndarray):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be of the same length")
    return sum(vector1[i] * vector2[i] for i in range(len(vector1)))


def outer_product(vector1: np.ndarray, vector2: np.ndarray):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be of the same length")
    return [vector1[i] * vector2[i] for i in range(len(vector1))]


def scalar_product(scalar: int, vector: np.ndarray):
    return [scalar * vector[i] for i in range(len(vector))]


def vector_addition(vector1: np.ndarray, vector2: np.ndarray):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be of the same length")
    return [vector1[i] + vector2[i] for i in range(len(vector1))]


def matrix_addition(matrix1: np.ndarray, matrix2: np.ndarray):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions")
    return [vector_addition(matrix1[i], matrix2[i]) for i in range(len(matrix1))]


def matrix_scalar_product(scalar: int, matrix: np.ndarray):
    return [scalar_product(scalar, matrix[i]) for i in range(len(matrix))]


def matrix_multiplication(matrix1: np.ndarray, matrix2: np.ndarray):
    res_matrix: np.ndarray = np.ndarray(shape=(matrix1.shape[0], matrix2.shape[1]))
    print(f"res matrix dimension: {res_matrix.shape}")

    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            res_matrix[i][j] = inner_product(matrix1[i], matrix2[:, j])

    return res_matrix


matrix1 = np.array([[1, 2, 3], [3, 4, 5]])
matrix2 = np.array([[0, 1], [1, 0], [1, 1]])
print(matrix1)
print(matrix2)
print(matrix_multiplication(matrix1, matrix2))
