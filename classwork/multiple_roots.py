def f(x):
    return x**4 + 3*x**3 + x**2 - 2*x - 0.5


def bisection(f, a, b, eps=1e-6, max_iter=100):
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        return None 

    for _ in range(max_iter):
        m = (a + b) / 2
        fm = f(m)

        if abs(fm) < eps or (b - a) / 2 < eps:
            return m

        if fa * fm < 0:
            b = m
            fb = fm
        else:
            a = m
            fa = fm

    return (a + b) / 2


def find_roots(f, start, end, step=0.01):
    roots = []
    x = start

    while x < end:
        a = x
        b = x + step

        if f(a) * f(b) < 0:
            root = bisection(f, a, b)
            if root is not None:
                
                if not any(abs(root - r) < 1e-4 for r in roots):
                    roots.append(root)

        x += step

    return roots


roots = find_roots(f, -3, 2)

print("Roots found:")
for r in roots:
    print(f"{r:.6f}")
