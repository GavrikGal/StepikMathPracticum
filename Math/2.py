import numpy as np


m, n = map(int, input().split())


def check_can_cover(m: int, n: int):
    square = m * n - 2

    a0 = np.tile([0., 1.], int(np.ceil(m / 2)))
    a1 = np.tile([1., 0.], int(np.ceil(m / 2)))

    Z = np.tile([a0, a1], (int(np.ceil(n / 2)), 1))
    Z = Z[:n, :m]

    left_top = Z[0, -1]
    right_bottom = Z[-1, 0]

    if (square > 0) and (left_top != right_bottom):
        print('Замостить можно')
    else:
        print('Замостить нельзя')


check_can_cover(m, n)

