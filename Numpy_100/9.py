import numpy as np


n = int(input())
m, k = map(int, input().split())


elems = np.arange(n)

elems_shaped = list(zip(*[iter(elems)] * k))
Z1 = np.array(elems_shaped)

Z = np.reshape(elems, (m, k))

print(Z)