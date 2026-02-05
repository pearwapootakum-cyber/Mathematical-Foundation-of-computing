import math

def hilbert_matrix(n):
    return [[1.0 / (i + j + 1) for j in range(n)] for i in range(n)]

def mat_vec_mul(A, x):
    return [sum(A[i][j] * x[j] for j in range(len(x))) for i in range(len(A))]

def gaussian_elimination(A, b):
    n = len(A)

    # Forward elimination
    for i in range(n):
        for j in range(i+1, n):
            if A[i][i] == 0:
                raise ValueError("Zero pivot encountered!")
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

    # Back substitution
    x = [0.0] * n
    for i in range(n-1, -1, -1):
        s = sum(A[i][j] * x[j] for j in range(i+1, n))
        x[i] = (b[i] - s) / A[i][i]

    return x

def max_error(x, exact):
    return max(abs(x[i] - exact[i]) for i in range(len(x)))

sizes = [5, 10, 20, 50, 100]

for n in sizes:
    H = hilbert_matrix(n)
    x_exact = [1.0] * n
    b = mat_vec_mul(H, x_exact)

    H_copy = [row[:] for row in H]
    b_copy = b[:]

    try:
        x_num = gaussian_elimination(H_copy, b_copy)
        err = max_error(x_num, x_exact)
        print(f"n = {n:3d} | max error = {err:.2e}")
    except Exception as e:
        print(f"n = {n:3d} | FAILED: {e}")
