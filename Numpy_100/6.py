import numpy as np


n = int(input())
x = int(input())

Z1 = np.zeros(n)
Z1[x] = 1

Z = np.eye(1, n, x).ravel()

print(Z)
