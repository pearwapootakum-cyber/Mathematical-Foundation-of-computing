A = [
    [4, -1, 0],
    [-1, 4, -1],
    [0, -1, 4]
]

b = [5, -1, 7]

x_prev = [1.0, 2.0, 3.0]
x = x_prev.copy()

if __name__ == "__main__":
    eps = 0.01
    max_iter_num = 200

    n = len(b)
    it = 1
    
    def diff_norm(x, x_prev):
        s = 0.0
        for i in range(len(x)):
            s += (x[i] - x_prev[i])**2
        return s**0.5

    while (it == 1 or diff_norm(x, x_prev) > eps) and it <= max_iter_num:
        x_prev = x.copy()
        for i in range(n):
            x[i] = b[i]
            for j in range(n):
                if j != i:
                    x[i] -= A[i][j] * x_prev[j]
            x[i] /= A[i][i]

        print(f"{it}: {x}")
        it += 1
