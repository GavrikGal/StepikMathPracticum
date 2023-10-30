import numpy as np


Y = np.array([[1, 2],
              [2, 1]])

Y_mean = Y.mean()
Y_std = Y.std()

Z = np.around((Y - Y_mean) / Y_std, 2)

print(Z)