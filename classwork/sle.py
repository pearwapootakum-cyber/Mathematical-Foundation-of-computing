import math

A = [
    [1, 1, 1],
    [3, 2, 1],
    [2, -1, 4]
]

b = [6, 10, 12]

def gaussian_elimination(A, b):
    n = len(A)

    # Forward elimination with partial pivoting
    for i in range(n - 1):
       
        max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
        if A[max_row][i] == 0:
            raise ValueError("Matrix is singular!")

        if max_row != i:
            A[i], A[max_row] = A[max_row], A[i]
            b[i], b[max_row] = b[max_row], b[i]
            print(f"Swapped rows {i} and {max_row}")

        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            print(f"Eliminate A[{j}][{i}], factor = {factor:.2f}")

            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

            print(f"A = {A}")
            print(f"b = {b}")
            print("-" * 40)

    
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        s = sum(A[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (b[i] - s) / A[i][i]
        print(f"x[{i}] = {x[i]:.2f}")

    return x


solution = gaussian_elimination(A, b)
print("\nSolution:", solution)
