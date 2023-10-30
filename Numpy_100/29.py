import numpy as np


A = np.array([-3.1, -5.9, 0, 2.2, 9.8])

Z1 = np.where(A > 0, np.ceil(A), np.floor(A))

Z = np.copysign(np.ceil(np.absolute(A)), A)

print(Z)