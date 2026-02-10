import pandas as pd
import matplotlib.pyplot as plt

def plot_errors(filename):
    df = pd.read_csv(filename)

    for method in df["method"].unique():
        data = df[df["method"] == method]
        plt.plot(data["n"], data["solution_error"], label=method)

    plt.xlabel("Matrix size n")
    plt.ylabel("Solution error")
    plt.legend()
    plt.title(filename)
    plt.show()


if __name__ == "__main__":
    plot_errors("exp_A_random_gaussian.csv")
    plot_errors("exp_B_hilbert.csv")
    plot_errors("exp_C_diagonal_dominant.csv")
