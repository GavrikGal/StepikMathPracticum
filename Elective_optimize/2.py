import math


def S_six(x):
    return ((3 * (3 ** 0.5)) / 2) * x ** 2


def S_five(x):
    return ((5**0.5 * (5 + 2 * 5**0.5)**0.5) / 4) * x**2


def S(x):
    return 20 * S_six(x) + 12 * S_five(x)


def S_ceil(x):
    return math.ceil(S(x))

print(S(7))
