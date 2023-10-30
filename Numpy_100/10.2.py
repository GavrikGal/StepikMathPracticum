import numpy as np


Z = np.array([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9],
             [0, 0, 9]])

res1 = Z[Z > 3].tolist()

res = Z[np.nonzero(Z > 3)].tolist()

print(res1)
print(res)
