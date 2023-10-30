import numpy as np

n, m = (map(int, input().split()))

Z = np.zeros((n, m))

Z[0] = 1
Z[-1] = 1
Z[:, 0] = 1
Z[:, -1] = 1

Z2 = np.ones((n, m))
Z2[1:-1, 1:-1] = 0

Z1 = np.pad(Z, 0)

print(Z1)
