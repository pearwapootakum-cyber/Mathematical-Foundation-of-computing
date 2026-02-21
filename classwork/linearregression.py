import numpy as np

x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 5, 4, 5], dtype=float)

n = len(x)

c0 = 0
c1 = 0

alpha = 0.01   
iterations = 20

print("Iter |   c0     |   c1")
print("---------------------------")

for i in range(iterations):
    y_pred = c0 + c1 * x
    
    error = y - y_pred
    
    grad_c0 = (-2/n) * np.sum(error)
    grad_c1 = (-2/n) * np.sum(x * error)
    
    # update
    c0 = c0 - alpha * grad_c0
    c1 = c1 - alpha * grad_c1
    
    print(f"{i:4d} | {c0:8.4f} | {c1:8.4f}")

print("\nFinal coefficients:")
print("c0 =", c0)
print("c1 =", c1)