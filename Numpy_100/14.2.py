import numpy as np
import numpy.random

n, m = (map(int, input().split()))

numpy.random.seed(42)

z = np.random.rand(n, m)

means = z.mean(axis=0)
print(means.min())
print(means.max())
