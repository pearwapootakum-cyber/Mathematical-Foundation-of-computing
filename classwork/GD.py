import numpy as np
import math

def f(x):
    return (x - 3)**2

def df(x):
    return 2 * (x - 3)


x = 10          
alpha = 0.1     
iterations = 15

print("Step |    x     |   f(x)   |  df(x)")
print("----------------------------------------")

for i in range(iterations):
    grad = df(x)
    print(f"{i:4d} | {x:8.4f} | {f(x):8.4f} | {grad:7.4f}")
    
    x = x - alpha * grad

print("\nFinal x =", x)
print("Minimum value =", f(x))