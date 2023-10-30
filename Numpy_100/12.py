import numpy as np
import numpy.random

n, m, l = (map(int, input().split()))

numpy.random.seed(42)

Z = np.random.rand(n, m, l)

print(Z)