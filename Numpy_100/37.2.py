import numpy as np


n, m = map(int, input().split())
k = int(input())

Z = np.array([np.arange(k, k+n)] * m, dtype=float)
Z = Z.transpose()

print(Z)

arr = np.arange(k, k+n).reshape(n, 1)

print(arr)