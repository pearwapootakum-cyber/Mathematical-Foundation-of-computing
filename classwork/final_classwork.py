import numpy as np

np.random.seed(0)

true_c = np.array([2, -1, 3, 0.5, -2])

def test_plane(x):
    return true_c @ x

n = 1000
m = 5

a, b = -1, 1

x_vals = np.random.uniform(a, b, size=(m, n))
y_vals_exact = test_plane(x_vals)

noise = np.random.normal(0, 0.5, size=y_vals_exact.shape)
y = y_vals_exact + noise

X = np.stack(x_vals, axis=1)

c = np.ones(m)

max_iters = 5000
alpha = 0.0005   
eps = 1e-6

print("True coefficients:", true_c)
print()

for i in range(max_iters):
    grad = X.T @ (X @ c - y)
    step = alpha * grad
    c -= step

    loss = np.linalg.norm(X @ c - y) ** 2

    if i % 200 == 0:
        print(f"{i}: loss={loss:.2f}, c={c}")

    if np.linalg.norm(step) < eps:
        break

print("\nFinal estimated coefficients:")
print(c)