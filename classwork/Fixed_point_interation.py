import math

def fixed_point_iteration(x0, max_iter=10):
    x = x0
    print(f"x0 = {x}")
    
    for k in range(1, max_iter + 1):
        x = math.sqrt(x + 2)
        print(f"x{k} = {x}")


x0 = 3
fixed_point_iteration(x0)