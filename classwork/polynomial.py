import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x) + 0.5 * x**2   
a = -2
b = 2
n = 3

x_points = np.linspace(a, b, n + 1)
y_points = f(x_points)

v = np.zeros((n + 1, n + 1))

for i in range(n + 1):
    for j in range(n + 1):
        v[i, j] = x_points[i] ** j

c = np.linalg.solve(v, y_points)

print("Polynomial coefficients:")
for i in range(len(c)):
    print(f"c{i} = {c[i]}")


def p(x):
    s = 0
    for j in range(len(c)):
        s += c[j] * x**j
    return s

x_plot = np.linspace(a, b, 500)

plt.figure()
plt.plot(x_plot, p(x_plot), label="Interpolating polynomial")
plt.scatter(x_points, y_points, color="black", zorder=5, label="Interpolation points")
plt.plot(x_plot, f(x_plot), color="red", label="f(x) (original)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Polynomial Interpolation using SLE")
plt.legend()
plt.grid(True)
plt.show()
