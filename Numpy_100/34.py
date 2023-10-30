import numpy as np

start = np.datetime64(input())
stop = np.datetime64(input())

# print(start)
# print(stop)

Z = np.arange(start, stop, dtype='datetime64[D]')

print(Z)