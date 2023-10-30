import numpy as np


n, m = map(int, input().split())
k = int(input())

Z = np.zeros((n, m))
arr = np.arange(k, k+m)
Z1 = Z + arr

Z = np.array([np.arange(k, k+m, 1)] * n, dtype=float)

print(Z)