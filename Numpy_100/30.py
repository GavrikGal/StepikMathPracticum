import numpy as np


A = np.array([1, 2, 3, 4, 5])
B = np.array([-5, -4, -3])


Z = np.intersect1d(A, B)


print(Z)