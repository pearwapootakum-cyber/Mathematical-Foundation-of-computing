import numpy as np
import matplotlib.pyplot as plt

f  = lambda x: x**2 - 4
df = lambda x: 2*x

a, b   = 0, 5     
x0     = 3.0    
alpha  = 0.2      
N      = 30      



def bisection(f, a, b, N):
    err = []
    for _ in range(N):
        err.append(abs(b - a))
        c = (a + b) / 2
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
    return err


def fixed_point(f, x, alpha, N):
    err = []
    for _ in range(N):
        x_new = x - alpha*f(x)
        err.append(abs(x_new - x))
        x = x_new
    return err


def newton(f, df, x, N):
    err = []
    for _ in range(N):
        x_new = x - f(x)/df(x)
        err.append(abs(x_new - x))
        x = x_new
    return err


e_bis = bisection(f, a, b, N)
e_fp  = fixed_point(f, x0, alpha, N)
e_new = newton(f, df, x0, N)


plt.semilogy(e_bis, label="Bisection")
plt.semilogy(e_fp, label="Fixed Point")
plt.semilogy(e_new, label="Newton")

plt.xlabel("Iteration")
plt.ylabel("Error")
plt.legend()
plt.grid()
plt.show()
