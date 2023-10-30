import numpy as np


A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
B = np.array([
    [11.5, 12.5, 13.5]
])

try:
    Z = A @ B
except ValueError:
    Z = "Упс! Что-то пошло не так..."

print(Z)