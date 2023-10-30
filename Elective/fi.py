from decimal import *
from functools import lru_cache

getcontext().prec = 50

@lru_cache(maxsize=None)
def luka_r(L0, L1, n):
    list_ = [L0, L1]
    if n < 2:
        return list_[n]
    else:
        return luka(L1, L1+L0, n-1)

def luka(L0, L1, n):
    list_ = [L0, L1]
    if n < 2:
        return list_[n]
    else:
        while n > 1:
            L0, L1 = L1, L1+L0
            n -= 1
        return L1

def fi(L0, L1, n):
    for _ in range(n-1):
        L0, L1 = L1, L1 + L0
    return L1 / L0

L0 = Decimal(0)
L1 = Decimal(1)
# print(fi(L0, L1, 11))

def luka_n(n):
    L0 = 2
    L1 = 1
    list_ = [L0, L1]
    if n < 2:
        return list_[n]
    else:
        while n > 1:
            L0, L1 = L1, L1+L0
            n -= 1
        return L1



print(luka_n(4))