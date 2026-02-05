import math

def hilbert_matrix(n):
    return [[1.0 / (i + j + 1) for j in range(n)] for i in range(n)]

def gaussian_elimination(A, b):
    n = len(b)

    # Forward elimination
    for k in range(n - 1):
        for i in range(k + 1, n):
            factor = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= factor * A[k][j]
            b[i] -= factor * b[k]

    # Back substitution
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        s = sum(A[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (b[i] - s) / A[i][i]

    return x

def mat_vec_mul(A, x):
    return [sum(A[i][j] * x[j] for j in range(len(x))) for i in range(len(A))]

def max_error(x, x_true):
    return max(abs(x[i] - x_true[i]) for i in range(len(x)))


sizes = [5, 10, 20, 50, 100]

print("Hilbert Matrix Experiment (Gaussian Elimination)\n")

for n in sizes:
    H = hilbert_matrix(n)
    x_true = [1.0] * n
    b = mat_vec_mul(H, x_true)

    A = [row[:] for row in H]
    b_copy = b[:]

    x_num = gaussian_elimination(A, b_copy)
    err = max_error(x_num, x_true)

    print(f"n = {n:3d} | max error = {err:.3e}")
