import numpy as np


seed = int(input())
n = int(input())

np.random.seed(seed)
Z = np.random.random(n)
Z.sort()

print(Z)