import numpy as np


def gaussian_elimination(A, b):
    A = A.astype(float)
    b = b.astype(float)
    n = len(b)

  
    for k in range(n):
        for i in range(k + 1, n):
            factor = A[i, k] / A[k, k]
            A[i, k:] -= factor * A[k, k:]
            b[i] -= factor * b[k]

   
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

    return x



def jacobi(A, b, eps=1e-6, max_iter=1000):
    n = len(b)
    x = np.zeros(n)
    x_new = np.zeros(n)

    for iteration in range(max_iter):
        for i in range(n):
            s = 0.0
            for j in range(n):
                if i != j:
                    s += A[i, j] * x[j]
            x_new[i] = (b[i] - s) / A[i, i]

        if np.linalg.norm(x_new - x) < eps:
            return x_new, iteration + 1

        x = x_new.copy()

    return x, max_iter



def gauss_seidel(A, b, eps=1e-6, max_iter=1000):
    n = len(b)
    x = np.zeros(n)

    for iteration in range(max_iter):
        x_old = x.copy()

        for i in range(n):
            s1 = np.dot(A[i, :i], x[:i])
            s2 = np.dot(A[i, i+1:], x_old[i+1:])
            x[i] = (b[i] - s1 - s2) / A[i, i]

        if np.linalg.norm(x - x_old) < eps:
            return x, iteration + 1

    return x, max_iter
