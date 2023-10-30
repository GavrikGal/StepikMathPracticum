import numpy as np


n, m = (map(int, input().split()))

# Z = np.ones((n, m))
# Z[::2, ::2] = 0
# Z[1::2, 1::2] = 0

a0 = np.tile([0., 1.], int(np.ceil(m / 2)))
a1 = np.tile([1., 0.], int(np.ceil(m / 2)))

Z = np.tile([a0, a1], (int(np.ceil(n / 2)), 1))
Z = Z[:n, :m]



print(Z)