import numpy as np


args = input().split()

if not args[-1].isnumeric():
    dtype = args.pop(-1)
else:
    dtype = 'float'

shape = tuple(map(int, args))

Z = np.zeros(shape, dtype=dtype)

print(Z)