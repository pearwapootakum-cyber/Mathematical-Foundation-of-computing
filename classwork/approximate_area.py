def inside_unit_circle(x, y):
    return x*x + y*y <= 1


def approximate_area(square_size):
    area = 0.0

    x = -1.0
    while x < 1.0:
        y = -1.0
        while y < 1.0:

            cx = x + square_size / 2
            cy = y + square_size / 2

            if inside_unit_circle(cx, cy):
                area += square_size * square_size

            y += square_size
        x += square_size

    return area



sizes = [0.5, 0.25, 0.1, 0.05]

for s in sizes:
    area = approximate_area(s)
    print("square size =", s, "approximate area =", area)

print("true area =", 3.141592653589793)
