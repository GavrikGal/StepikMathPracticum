import numpy as np


Z = np.array([1, 2, 0, 0, 4, 0])

NonZerros = np.nonzero(np.array(Z))


print(NonZerros)