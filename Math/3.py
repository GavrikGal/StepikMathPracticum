import numpy as np


N = int(input())


def g(N):
    y = [0, 1]
    x = N
    while True:
        y = []
        for i in range(x+1):
            n = x - i
            y.append(sum([int(j) for j in str(i)]) + sum([int(j) for j in str(n)]))

        if (min(y) == max(y)) and (max(y) == N):
            break
        x += 9
    print(x)

g(N)