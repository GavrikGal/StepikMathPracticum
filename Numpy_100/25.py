import numpy as np

Z = np.arange(11)

np.putmask(Z, (Z>3) & (Z<9), Z * -1)


print(Z)