import numpy as np


Z = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

Z = np.pad(Z, 1, mode='constant', constant_values=0)

print(Z)
