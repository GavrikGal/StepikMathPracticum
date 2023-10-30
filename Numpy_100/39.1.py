import numpy as np


start = int(input())
stop = int(input())
n = int(input())

Z = np.linspace(start, stop, n+1, endpoint=False)[1:].round(3)

print(Z)