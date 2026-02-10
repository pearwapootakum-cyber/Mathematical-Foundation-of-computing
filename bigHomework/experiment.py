import pandas as pd

from solvers import gaussian_elimination, jacobi, gauss_seidel
from matrix_generators import (
    random_matrix,
    diagonal_dominant_matrix,
    hilbert_matrix,
    generate_b
)
from errors import residual_error, solution_error


def experiment_A():
    results = []

    for n in range(3, 51):
        A = random_matrix(n)
        b, x_test = generate_b(A)

        x = gaussian_elimination(A.copy(), b.copy())

        results.append([
            n, "Gaussian", "Random",
            residual_error(A, x, b),
            solution_error(x, x_test),
            "-"
        ])

    df = pd.DataFrame(results,
        columns=["n", "method", "matrix", "residual", "solution_error", "iterations"]
    )
    df.to_csv("exp_A_random_gaussian.csv", index=False)


def experiment_B():
    results = []

    for n in range(3, 51):
        A = hilbert_matrix(n)
        b, x_test = generate_b(A)

        x_g = gaussian_elimination(A.copy(), b.copy())
        results.append([
            n, "Gaussian", "Hilbert",
            residual_error(A, x_g, b),
            solution_error(x_g, x_test),
            "-"
        ])

        x_s, it_s = gauss_seidel(A, b)
        results.append([
            n, "Seidel", "Hilbert",
            residual_error(A, x_s, b),
            solution_error(x_s, x_test),
            it_s
        ])

    df = pd.DataFrame(results,
        columns=["n", "method", "matrix", "residual", "solution_error", "iterations"]
    )
    df.to_csv("exp_B_hilbert.csv", index=False)


def experiment_C():
    results = []

    for n in range(3, 51):
        A = diagonal_dominant_matrix(n)
        b, x_test = generate_b(A)

        x_g = gaussian_elimination(A.copy(), b.copy())
        results.append([
            n, "Gaussian", "DiagDominant",
            residual_error(A, x_g, b),
            solution_error(x_g, x_test),
            "-"
        ])

        x_j, it_j = jacobi(A, b)
        results.append([
            n, "Jacobi", "DiagDominant",
            residual_error(A, x_j, b),
            solution_error(x_j, x_test),
            it_j
        ])

        x_s, it_s = gauss_seidel(A, b)
        results.append([
            n, "Seidel", "DiagDominant",
            residual_error(A, x_s, b),
            solution_error(x_s, x_test),
            it_s
        ])

    df = pd.DataFrame(results,
        columns=["n", "method", "matrix", "residual", "solution_error", "iterations"]
    )
    df.to_csv("exp_C_diagonal_dominant.csv", index=False)


if __name__ == "__main__":
    experiment_A()
    experiment_B()
    experiment_C()
