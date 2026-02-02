def f(x):
    return x**3 - x - 2

a = 1
b = 2

for i in range(1, 101):
    c = (a + b) / 2.0

    print(f"Iteration {i}: c = {c}")

    if f(a) * f(c) < 0:
        b = c
    else:
        a = c