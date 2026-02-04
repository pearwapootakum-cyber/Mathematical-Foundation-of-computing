import math

def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1   

def relaxation(x0, alpha, eps, max_iter=50):
    print("\n===Relaxation method===")
    x = x0
    for i in range(max_iter):
        fx = f(x)
        print("iter", i+1, "x =", round(x,6), "f(x) =", round(fx,6))
        if abs(fx) < eps:
            break
        x = x + alpha * fx
    return x



def newton(x0, eps, max_iter=50):
    print("\n=== Newton Method ===")
    x = x0
    for i in range(max_iter):
        fx = f(x)
        print(f"iter {i:2d}: x = {x:.8f}, f(x) = {fx:.3e}")
        if abs(fx) < eps:
            return x
        x = x - fx / df(x)
    return x


def bisection(a, b, eps, max_iter=50):
    print("\n=== Bisection Method ===")
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")

    for i in range(1, max_iter + 1):
        c = 0.5 * (a + b)
        fc = f(c)
        print(f"iter {i:2d}: x = {c:.8f}, f(x) = {fc:.3e}")
        if abs(fc) < eps or (b - a)/2 < eps:
            return c
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return c


a, b = 1.0, 2.0
x0 = 1.5
eps = 1e-6
alpha = -0.1   

relaxation(x0, alpha, eps)
newton(x0, eps)
bisection(a, b, eps)
