import numpy as np


def random_matrix(n, low=-5, high=5):
    return np.random.uniform(low, high, (n, n))



def diagonal_dominant_matrix(n):
    A = np.random.uniform(-5, 5, (n, n))
    for i in range(n):
        A[i, i] = np.sum(np.abs(A[i])) + 1
    return A



def hilbert_matrix(n):
    H = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            H[i, j] = 1.0 / (i + j + 1)
    return H



def generate_b(A):
    x_test = np.ones(A.shape[0])
    b = A @ x_test
    return b, x_test
