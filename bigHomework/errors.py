import numpy as np

def residual_error(A, x, b):
    return np.linalg.norm(A @ x - b)

def solution_error(x, x_test):
    return np.linalg.norm(x - x_test)
