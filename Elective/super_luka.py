from decimal import Decimal

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


def l2n(n):
    n = int(n/2)
    return luka_n(n)**2 - 2 * (-1)**n


def l3n(n):
    n = int(n/3)
    return luka_n(n)**3 - 3 * (-1)**n * luka_n(n)


def l4n(n):
    n = int(n/4)
    return luka_n(n)**4 - 4 * (-1)**n * luka_n(n)**2 + 2


def l5n(n):
    n = int(n/5)
    return luka_n(n)**5 - 5 * (-1)**n * luka_n(n)**3 + 5 * luka_n(n)


def l6n(n):
    n = int(n/6)
    return luka_n(n)**6 - 6 * (-1)**n * luka_n(n)**4 + 9 * luka_n(n)**2 - 2 * (-1)**n


def super_L(n):
    if n % 6 == 0:
        return l6n(n)
    if n % 5 == 0:
        return l5n(n)
    if n % 4 == 0:
        return l4n(n)
    if n % 3 == 0:
        return l3n(n)
    if n % 2 == 0:
        return l2n(n)
    return luka_n(n)



n = 180
print(f'{luka_n(n)=}')
if n % 2 == 0:
    print(f'{l2n(n)=}')
if n % 3 == 0:
    print(f'{l3n(n)=}')
if n % 4 == 0:
    print(f'{l4n(n)=}')
if n % 5 == 0:
    print(f'{l5n(n)=}')
if n % 6 == 0:
    print(f'{l6n(n)=}')

print(f'{super_L(n)=}')

